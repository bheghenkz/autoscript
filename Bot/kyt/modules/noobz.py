from kyt import *

def noobz_user_list():
    try:
        out = subprocess.check_output("noobzvpns --info-all-user", shell=True).decode("utf-8", errors="ignore")
        return [line.split()[1] for line in out.splitlines() if line.startswith("+ ")]
    except Exception:
        return []

def noobz_list_text():
    users = noobz_user_list()
    return "\n".join(f"{i}) {u}" for i, u in enumerate(users, 1))

def noobz_pick_user(text):
    text = text.strip()
    if text.isdigit():
        users = noobz_user_list()
        idx = int(text) - 1
        if 0 <= idx < len(users):
            return users[idx]
        return ""
    return text


@bot.on(events.CallbackQuery(data=b'noobz'))
async def nob(event):
	async def nob_(event):
		inline = [
[Button.inline(" CREATE NOOBZ ","create-noobz"),
Button.inline(" SHOW USER ","cek-noobz")],
[Button.inline(" DELETE USER ","delete-noobz"),
Button.inline(" UNLOCK USER ","unblock-noobz")],
[Button.inline(" LOCK USER ","lock-noobz"),
Button.inline("‹ BACK ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		noob = f' cat /etc/xray/noob | grep "###" | wc -l'
		noobz = subprocess.check_output(noob, shell=True).decode("ascii")
		msg = f"""
🧿───────────────────🧿
   **PANEL MENU NOOBZVPNS**
🧿───────────────────🧿
` Service:` `NOOBZVPNS`
` Total  :` `{noobz.strip()}` __account__
` Host   :` `{DOMAIN}`
` ISP    :` `{z["isp"]}`
` Country:` `{z["country"]}`
** @Smile_Bots_bot**
🧿───────────────────🧿
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await nob_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
@bot.on(events.CallbackQuery(data=b'create-noobz'))
async def create_noobz(event):
	async def create_noobz_(event):
		async with bot.conversation(chat) as user:
			await event.edit(f"""
**✨ 𝙽𝚊𝚖𝚊 𝚋𝚎𝚛𝚞𝚙𝚊 𝚌𝚊𝚖𝚙𝚞𝚛𝚊𝚗, 
 𝙷𝚞𝚛𝚞𝚏 𝚔𝚊𝚙𝚒𝚝𝚊𝚕, 𝚍𝚊𝚗 𝙰𝚗𝚐𝚔𝚊**
**✨ No Space**
**✨ No double Name**
**✨ Bot : @Smile_Bots_bot**

**✨ KETIK NAMA AKUN  :**
/cancel Kembali Ke Menu
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			async with bot.conversation(chat) as pw:
				await event.respond(f"""
**✨ KETIK PASWORD AKUN :**
""")
				pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw = (await pw).raw_text
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**✨ KETIK EXP AKUN (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			async with bot.conversation(chat) as pw2:
				await event.respond(f"""
**✨ KETIK LIMIT IP LOGIN :**
""")
				pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw2 = (await pw2).raw_text
			cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" "{pw2}" | addnoobz | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**🧿───────────────────🧿**
`•TCP•`
**🧿───────────────────🧿**
**» Host:** `{DOMAIN}`
**» Username:** `{user}`
**» Password:** `{pw}`
**» limit ip:** `{pw2}`
**🧿───────────────────🧿**
**» TCP_STD PORT     :** `8080`
**» TCP_SSL PORT    :** `8443`
**◇━━━━━━━━━━━━━━━━━◇**
**⟨ Payload WS  ⟩**
`GET / HTTP/1.1[crlf]Host: [s_host][crlf]Upgrade: websocket[crlf]Connection: Upgrade[crlf]User-Agent: [ua][crlf][crlf]`
**🧿───────────────────🧿**
**» Expired Until:** `{exp}` Days
**» 🛂@Smile_Bots_bot**
**🧿───────────────────🧿**
""")
			await event.respond(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_noobz_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'delete-noobz'))
async def delete_noobz(event):
    async def delete_noobz_(event):
            async with bot.conversation(chat) as user:
                    cmd2 = "grep -E '^### ' /etc/xray/noob | cut -d ' ' -f 2-3 | nl -s ') '"
                    z = subprocess.check_output(cmd2, shell=True).decode("utf-8", errors="ignore")
                    await event.edit(f"""**✨ LIST DELETE USER**
{z}
**✨ KETIK NOMOR / NAMA AKUN :**
/cancel Kembali KeMENU
""")
                    user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                    user = (await user).raw_text.strip()

            if user == "/cancel":
                    await event.respond("**» CANCEL**", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
                    return

            if user.isdigit():
                    user = subprocess.check_output(
                        f'grep -E "^### " /etc/xray/noob | cut -d " " -f 2 | sed -n "{user}p"',
                        shell=True
                    ).decode("utf-8", errors="ignore").strip()

            if not user:
                    await event.respond("**» USER TIDAK DITEMUKAN**", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
                    return

            cmd = (
                f'noobzvpns --remove-user "{user}" >/dev/null 2>&1 || true; '
                f'sed -i "/^### {user} /d" /etc/xray/noob 2>/dev/null || true; '
                f'sed -i \'/^,"{user}"$/d\' /etc/noobzvpns/users.json 2>/dev/null || true; '
                f'sed -i \'/"{user}"/d\' /etc/noobzvpns/users.json 2>/dev/null || true; '
                f'systemctl restart noobzvpns >/dev/null 2>&1 || true'
            )
            subprocess.run(cmd, shell=True)
            await event.respond(f"**» DELETE NOOBZ SUCCESS**\nUser: `{user}`", buttons=[[Button.inline("‹ Main Menu ›","menu")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
            await delete_noobz_(event)
    else:
            await event.answer("Akses Ditolak",alert=True)


@bot.on(events.CallbackQuery(data=b'lock-noobz'))
async def lock_noobz(event):
    async def lock_noobz_(event):
            async with bot.conversation(chat) as user:
                    z = noobz_list_text()
                    await event.edit(f"""
**✨ LIST LOCK USER**
{z}
**✨ KETIK NOMOR / NAMA AKUN :**
/cancel Kembali KeMENU
""")
                    user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                    user = noobz_pick_user((await user).raw_text)

            if user == "/cancel":
                    await event.respond("**» CANCEL**", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
                    return

            if not user:
                    await event.respond("**» USER TIDAK DITEMUKAN**", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
                    return

            subprocess.run(f'noobzvpns --block-user "{user}" >/dev/null 2>&1 || true', shell=True)
            await event.respond(f"**» SUCCES LOCK ACCOUNT**\nUser: `{user}`", buttons=[[Button.inline("‹ Main Menu ›","menu")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
            await lock_noobz_(event)
    else:
            await event.answer("Akses Ditolak",alert=True)


@bot.on(events.CallbackQuery(data=b'unblock-noobz'))
async def unblock_noobz(event):
    async def unblock_noobz_(event):
            async with bot.conversation(chat) as user:
                    z = noobz_list_text()
                    await event.edit(f"""
**✨ LIST UNLOCK USER**
{z}
**✨ KETIK NOMOR / NAMA AKUN :**
/cancel Kembali KeMENU
""")
                    user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                    user = noobz_pick_user((await user).raw_text)

            if user == "/cancel":
                    await event.respond("**» CANCEL**", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
                    return

            if not user:
                    await event.respond("**» USER TIDAK DITEMUKAN**", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
                    return

            subprocess.run(f'noobzvpns --unblock-user "{user}" >/dev/null 2>&1 || true', shell=True)
            await event.respond(f"**» SUCCES UNLOCK ACCOUNT**\nUser: `{user}`", buttons=[[Button.inline("‹ Main Menu ›","menu")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
            await unblock_noobz_(event)
    else:
            await event.answer("Akses Ditolak",alert=True)


@bot.on(events.CallbackQuery(data=b'cek-noobz'))
async def login_noobz(event):
	async def login_noobz_(event):
		
		cmd = 'cek-noobz'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.edit(f"""
** NOOBZ USER ONLINE**
{z}
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_noobz_(event)
	else:
		await event.answer("Access Denied",alert=True)
