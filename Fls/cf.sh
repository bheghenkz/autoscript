#!/bin/bash
set -euo pipefail

clear
apt install -y jq curl dnsutils >/dev/null 2>&1 || true

DOMAIN="smilebots.my.id"
CF_ID="zukatsuzuka@gmail.com"
CF_KEY="1c849f6fb12f757697d39521351b6ab16e3f9"

IP=$(curl -4 -s ifconfig.me/ip)

echo -e "\033[96;1m============================\033[0m"
echo -e "\033[93;1m      MASUKAN SUBDOMAIN"
echo -e "\033[96;1m============================\033[0m"
echo -e "\033[91;1mContoh:\033[0m \033[93msmile01\033[0m"
echo ""

while true; do
  read -rp "SUBDOMAIN : " domen
  domen=$(echo "$domen" | tr '[:upper:]' '[:lower:]' | tr -cd 'a-z0-9-')

  if [[ "$domen" =~ ^[a-z0-9]([a-z0-9-]{1,30}[a-z0-9])?$ ]]; then
    break
  fi

  echo "[ERROR] Subdomain hanya boleh huruf kecil, angka, dan strip. Minimal 3 karakter."
done

dns="${domen}.${DOMAIN}"

echo "Checking Cloudflare zone..."

ZONE=$(curl -sLX GET "https://api.cloudflare.com/client/v4/zones?name=${DOMAIN}&status=active" \
  -H "X-Auth-Email: ${CF_ID}" \
  -H "X-Auth-Key: ${CF_KEY}" \
  -H "Content-Type: application/json" | jq -r '.result[0].id // empty')

if [[ -z "$ZONE" || "$ZONE" == "null" ]]; then
  echo "[ERROR] Zone ${DOMAIN} tidak ditemukan / CF KEY salah."
  exit 1
fi

echo "Checking existing record ${dns}..."

RECORD=$(curl -sLX GET "https://api.cloudflare.com/client/v4/zones/${ZONE}/dns_records?name=${dns}" \
  -H "X-Auth-Email: ${CF_ID}" \
  -H "X-Auth-Key: ${CF_KEY}" \
  -H "Content-Type: application/json" | jq -r '.result[0].id // empty')

if [[ -n "$RECORD" && "$RECORD" != "null" ]]; then
  echo "[ERROR] Subdomain ${dns} sudah dipakai. Pilih nama lain."
  exit 1
fi

echo "Creating DNS A record:"
echo "Domain : ${dns}"
echo "IP     : ${IP}"

CREATE=$(curl -sLX POST "https://api.cloudflare.com/client/v4/zones/${ZONE}/dns_records" \
  -H "X-Auth-Email: ${CF_ID}" \
  -H "X-Auth-Key: ${CF_KEY}" \
  -H "Content-Type: application/json" \
  --data "{\"type\":\"A\",\"name\":\"${dns}\",\"content\":\"${IP}\",\"ttl\":120,\"proxied\":false}")

SUCCESS=$(echo "$CREATE" | jq -r '.success')

if [[ "$SUCCESS" != "true" ]]; then
  echo "[ERROR] Gagal membuat DNS record."
  echo "$CREATE" | jq .
  exit 1
fi

echo "Waiting DNS propagation..."

for i in {1..30}; do
  RESOLVE=$(dig +short "$dns" A | tail -n1 || true)
  if [[ "$RESOLVE" == "$IP" ]]; then
    echo "DNS OK: ${dns} -> ${IP}"
    break
  fi
  echo "Waiting DNS... ${i}/30 current=${RESOLVE:-none}"
  sleep 4
done

RESOLVE=$(dig +short "$dns" A | tail -n1 || true)
if [[ "$RESOLVE" != "$IP" ]]; then
  echo "[ERROR] DNS belum mengarah ke VPS. Stop installer agar SSL tidak kosong."
  exit 1
fi

mkdir -p /etc/xray /etc/v2ray /var/lib/kyt

echo "$dns" > /root/domain
echo "$dns" > /root/scdomain
echo "$dns" > /etc/xray/domain
echo "$dns" > /etc/v2ray/domain
echo "$dns" > /etc/xray/scdomain
echo "IP=$dns" > /var/lib/kyt/ipvps.conf

echo "SUCCESS: ${dns}"
