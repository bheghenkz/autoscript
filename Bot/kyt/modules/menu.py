from kyt import *

@bot.on(events.NewMessage(pattern=r"(?:.menu|/menu)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline(" MENU SSH ","ssh"),
Button.inline(" MENU VMESS ","vmess")],
[Button.inline(" MENU VLESS ","vless"),
Button.inline(" MENU TROJAN ","trojan")],
[Button.inline(" NOOBZVPNS ","noobz"),
Button.inline(" TROJAN-GO ","trojan-go")],
[Button.inline(" VPS INFO ","info"),
Button.inline(" SETTING ","setting")],
[Button.inline(" MENU VIP ","regis")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak", alert=True)
		except:
			await event.reply("Akses Ditolak")
	elif val == "true":
		sh = f' cat /etc/xray/ssh | grep "###" | wc -l'
		ssh = subprocess.check_output(sh, shell=True).decode("ascii")
		vm = f' cat /etc/xray/config.json | grep "#vmg" | wc -l'
		vms = subprocess.check_output(vm, shell=True).decode("ascii")
		vl = f' cat /etc/xray/config.json | grep "#vlg" | wc -l'
		vls = subprocess.check_output(vl, shell=True).decode("ascii")
		tr = f' cat /etc/xray/config.json | grep "#trg" | wc -l'
		trj = subprocess.check_output(tr, shell=True).decode("ascii")
		noob = f' cat /etc/xray/noob | grep "###" | wc -l'
		noobz = subprocess.check_output(noob, shell=True).decode("ascii")
		tgo = f' cat /etc/trojan-go/trgo | grep "###" | wc -l'
		trgo = subprocess.check_output(tgo, shell=True).decode("ascii")
		sdss = f" cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
		namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
		ipvps = f" curl -4 -s ifconfig.me/ip"
		ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
		citsy = f" cat /etc/xray/city"
		city = subprocess.check_output(citsy, shell=True).decode("ascii")

		msg = f"""
🧿───────────────────🧿
      **SMILEVPN PREMIUM**
🧿───────────────────🧿
 **  Hallo {sender.first_name} **
` Ip Vps:` `{ipsaya.strip()}`
` City  :` `{city.strip()}`
🧿───────────────────🧿
                 **Total Account**
🧿───────────────────🧿
` Ssh Ovpn    :` `{ssh.strip()} Account`
` Xray Vmess  :` `{vms.strip()} Account`
` Xray Vless  :` `{vls.strip()} Account`
` Xray Trojan :` `{trj.strip()} Account`
` Noobzvpns   :` `{noobz.strip()} Account`
` Trojan-Go   :` `{trgo.strip()} Account`
🧿───────────────────🧿
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)