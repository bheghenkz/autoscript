from kyt import *

def menu_btn():
    return [[Button.inline("‹ Main Menu ›","menu")]]

def clean_out(s):
    s = s or ""
    s = re.sub(r"\x1b\[[0-9;]*m", "", s)
    skip = ["Press any key", "cannot remove", "No such file", "read:"]
    return "\n".join(
        line.strip() for line in s.splitlines()
        if line.strip() and not any(x.lower() in line.lower() for x in skip)
    )

def run(cmd, timeout=70):
    try:
        out = subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT, timeout=timeout
        ).decode("utf-8", errors="ignore")
    except subprocess.TimeoutExpired as e:
        out = (e.output or b"").decode("utf-8", errors="ignore")
    except subprocess.CalledProcessError as e:
        out = (e.output or b"").decode("utf-8", errors="ignore")
    except Exception as e:
        out = str(e)
    return clean_out(out)

def vmess_list():
    return run("grep -E '^#vmg ' /etc/xray/config.json | cut -d ' ' -f 2-3 | nl -s ') '", 10)

def pick_number(text):
    text = text.strip()
    if text.isdigit():
        return text
    rows = run("grep -E '^#vmg ' /etc/xray/config.json | cut -d ' ' -f 2", 10).splitlines()
    for i, name in enumerate(rows, 1):
        if name.strip() == text:
            return str(i)
    return ""

def m_vmess(inputs, timeout=70):
    data = "\\n".join(str(x) for x in inputs) + "\\n0\\n"
    cmd = f'printf "%b" "{data}" | timeout {timeout}s env HOME=/root TERM=xterm BOT_MODE=1 bash /usr/local/sbin/m-vmess || true'
    return run(cmd, timeout + 5)

async def ask_text(event, chat, sender, text):
    async with bot.conversation(chat, timeout=120, exclusive=False) as conv:
        await event.respond(text)
        msg = conv.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
        return (await msg).raw_text.strip()

async def ask_btn(event, chat, text, buttons):
    async with bot.conversation(chat, timeout=120, exclusive=False) as conv:
        await event.respond(text, buttons=buttons)
        cb = conv.wait_event(events.CallbackQuery)
        return (await cb).data.decode("ascii")

async def ok(event, text):
    await event.respond((text or "**DONE**")[:3900], buttons=menu_btn())

async def get_sender_ok(event):
    sender = await event.get_sender()
    if valid(str(sender.id)) != "true":
        await event.answer("Access Denied", alert=True)
        return None
    return sender

@bot.on(events.CallbackQuery(data=b'create-vmess'))
@bot.on(events.CallbackQuery(data=b'create7-vmess'))
async def create_vmess(event):
    sender = await get_sender_ok(event)
    if not sender: return
    chat = event.chat_id

    user = await ask_text(event, chat, sender, "**Username:**")
    if user.startswith("/"): return await ok(event, "**» CANCEL**")

    quota = await ask_text(event, chat, sender, "**Format Quota:**\n`10` = 10GB\n`0` = Unlimited\n\n**Quota Vmess:**")
    if quota.startswith("/"): return await ok(event, "**» CANCEL**")

    exp = await ask_btn(event, chat, "**Choose Expiry Day**", [
        [Button.inline(" 3 Day ","3"), Button.inline(" 7 Day ","7")],
        [Button.inline(" 30 Day ","30"), Button.inline(" 60 Day ","60")]
    ])

    limitip = await ask_btn(event, chat, "**Choose Limit IP**", [
        [Button.inline(" 1 IP ","1"), Button.inline(" 2 IP ","2")],
        [Button.inline(" 3 IP ","3"), Button.inline(" 5 IP ","5")],
        [Button.inline(" 10 IP ","10"), Button.inline(" 15 IP ","15")],
        [Button.inline(" Unlimited ","0")]
    ])

    await event.respond("`Processing Create VMESS...`")
    out = m_vmess(["1", user, exp, limitip, quota], 90)

    log = run(f"cat /etc/vmess/akun/log-create-{user}.log 2>/dev/null", 10)
    if log:
        out = log

    await ok(event, f"**✅ VMESS CREATED**\nUser: `{user}`\n\n`{out[-3500:]}`")

@bot.on(events.CallbackQuery(data=b'trial-vmess'))
@bot.on(events.CallbackQuery(data=b'trial7-vmess'))
async def trial_vmess(event):
    sender = await get_sender_ok(event)
    if not sender: return
    chat = event.chat_id

    exp = await ask_btn(event, chat, "**Choose Expiry Minutes**", [
        [Button.inline(" 10 Menit ","10"), Button.inline(" 15 Menit ","15")],
        [Button.inline(" 30 Menit ","30"), Button.inline(" 60 Menit ","60")]
    ])

    out = m_vmess(["2", exp], 70)
    await ok(event, f"**✅ TRIAL VMESS**\n`{out[-3500:]}`")

@bot.on(events.CallbackQuery(data=b'cek-vmess'))
@bot.on(events.CallbackQuery(data=b'cek7-vmess'))
async def cek_vmess(event):
    sender = await get_sender_ok(event)
    if not sender: return

    out = m_vmess(["5"], 45)
    await ok(event, f"**VMESS USER ONLINE**\n`{out[-3500:]}`")

@bot.on(events.CallbackQuery(data=b'delete-vmess'))
@bot.on(events.CallbackQuery(data=b'delete7-vmess'))
async def delete_vmess(event):
    sender = await get_sender_ok(event)
    if not sender: return
    chat = event.chat_id

    await event.edit(f"**LIST VMESS USER**\n{vmess_list()}\n\n**Input Number / Username:**\n/cancel Untuk Kembali")
    user = await ask_text(event, chat, sender, "**Input Number / Username:**")
    if user.startswith("/"): return await ok(event, "**» CANCEL**")

    num = pick_number(user)
    if not num: return await ok(event, "**User Not Found**")

    out = m_vmess(["4", num], 60)
    await ok(event, f"**✅ VMESS DELETED**\n`{out[-2500:]}`")

@bot.on(events.CallbackQuery(data=b'renew-vmess'))
@bot.on(events.CallbackQuery(data=b'renew7-vmess'))
async def renew_vmess(event):
    sender = await get_sender_ok(event)
    if not sender: return
    chat = event.chat_id

    await event.edit(f"**LIST VMESS USER**\n{vmess_list()}\n\n**Input Number / Username:**\n/cancel Untuk Kembali")
    user = await ask_text(event, chat, sender, "**Input Number / Username:**")
    if user.startswith("/"): return await ok(event, "**» CANCEL**")

    num = pick_number(user)
    if not num: return await ok(event, "**User Not Found**")

    exp = await ask_text(event, chat, sender, "**Tambah Expired Berapa Hari:**")
    if exp.startswith("/"): return await ok(event, "**» CANCEL**")

    out = m_vmess(["3", num, exp], 60)
    await ok(event, f"**✅ VMESS RENEWED**\n`{out[-2500:]}`")

@bot.on(events.CallbackQuery(data=b'limit-vmess'))
@bot.on(events.CallbackQuery(data=b'limit7-vmess'))
async def limit_vmess(event):
    sender = await get_sender_ok(event)
    if not sender: return
    chat = event.chat_id

    await event.edit(f"**LIST VMESS USER**\n{vmess_list()}\n\n**Input Number / Username:**\n/cancel Untuk Kembali")
    user = await ask_text(event, chat, sender, "**Input Number / Username:**")
    if user.startswith("/"): return await ok(event, "**» CANCEL**")

    num = pick_number(user)
    if not num: return await ok(event, "**User Not Found**")

    iplim = await ask_text(event, chat, sender, "**Limit IP Baru:**\n`0` Unlimited")
    quota = await ask_text(event, chat, sender, "**Quota GB Baru:**\n`0` Unlimited")

    out = m_vmess(["7", num, iplim, quota], 60)
    await ok(event, f"**✅ VMESS LIMIT CHANGED**\n`{out[-2500:]}`")

@bot.on(events.CallbackQuery(data=b'list-vmess'))
@bot.on(events.CallbackQuery(data=b'akun7-vmess'))
async def show_vmess(event):
    sender = await get_sender_ok(event)
    if not sender: return
    chat = event.chat_id

    await event.edit(f"**LIST VMESS USER**\n{vmess_list()}\n\n**Input Number / Username:**\n/cancel Untuk Kembali")
    user = await ask_text(event, chat, sender, "**Input Number / Username:**")
    if user.startswith("/"): return await ok(event, "**» CANCEL**")

    num = pick_number(user)
    if not num: return await ok(event, "**User Not Found**")

    out = m_vmess(["6", num], 60)
    await ok(event, f"**✅ VMESS CONFIG**\n`{out[-3500:]}`")

@bot.on(events.CallbackQuery(data=b'restore-vmess'))
@bot.on(events.CallbackQuery(data=b'restore7-vmess'))
async def restore_vmess(event):
    sender = await get_sender_ok(event)
    if not sender: return
    chat = event.chat_id

    deleted = run("grep -E '^### ' /etc/vmess/akundelete | cut -d ' ' -f 2-3 | nl -s ') ' 2>/dev/null", 10)
    await event.edit(f"**LIST RESTORE VMESS**\n{deleted}\n\n**Input Number:**\n/cancel Untuk Kembali")

    num = await ask_text(event, chat, sender, "**Input Number:**")
    if num.startswith("/"): return await ok(event, "**» CANCEL**")

    exp = await ask_text(event, chat, sender, "**Expired Days:**")
    iplim = await ask_text(event, chat, sender, "**Limit IP:**\n`0` Unlimited")
    quota = await ask_text(event, chat, sender, "**Quota GB:**\n`0` Unlimited")

    out = m_vmess(["11", num, exp, iplim, quota], 70)
    await ok(event, f"**✅ VMESS RESTORED**\n`{out[-2500:]}`")

@bot.on(events.CallbackQuery(data=b'vmess'))
async def vmess(event):
    sender = await get_sender_ok(event)
    if not sender: return

    inline = [
        [Button.inline(" [ Create Vmess ] ","create-vmess"), Button.inline(" [ Trial Vmess ] ","trial-vmess")],
        [Button.inline(" [ Delete Vmess ] ","delete-vmess"), Button.inline(" [ Renew Vmess ] ","renew-vmess")],
        [Button.inline(" [ Limit Vmess ] ","limit-vmess"), Button.inline(" [ Cek Vmess Online ] ","cek-vmess")],
        [Button.inline(" [ Restore Vmess ] ","restore-vmess"), Button.inline(" [ List Member Vmess ] ","list-vmess")],
        [Button.inline("‹ Main Menu ›","menu")]
    ]

    try:
        z = requests.get("http://ip-api.com/json/?fields=country,region,city,timezone,isp", timeout=5).json()
        isp = z.get("isp", "-")
        country = z.get("country", "-")
    except Exception:
        isp = "-"
        country = "-"

    domaintele = run("cat /etc/xray/domain", 5)
    total = run("grep -c -E '^#vmg ' /etc/xray/config.json", 5)

    msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**👑 VMESS MANAGER 👑**
━━━━━━━━━━━━━━━━━━━━━━━ 
✅ **» Service     :** `VMESS`
✅ **» Hostname/IP :** `{domaintele.strip()}`
✅ **» ISP         :** `{isp}`
✅ **» Country     :** `{country}`

✅ **» Account     :** `{total.strip()}` __account__
━━━━━━━━━━━━━━━━━━━━━━━ 
"""
    await event.edit(msg, buttons=inline)
