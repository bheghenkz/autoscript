from kyt import *

@bot.on(events.CallbackQuery(data=b'create-ssh'))
async def create_ssh(event):
	async def create_ssh_(event):
		async with bot.conversation(chat) as user:
			await event.edit(f"""
**BUAT USERNAME TANPA SPASI**
/cancel Untuk Kembali
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
**KETIK PASWORD AKUN :**
""")
				pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw = (await pw).raw_text
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**KETIK EXP AKUN (Day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			async with bot.conversation(chat) as pw2:
				await event.respond(f"""
**KETIK LIMIT IP LOGIN :**
""")
				pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw2 = (await pw2).raw_text
			cmd = f'printf "%s\n" "1" "{user}" "{pw}" "{exp}" "{pw2}" | timeout 15s env HOME=/root TERM=xterm BOT_MODE=1 bash /usr/local/sbin/m-sshovpn || true'
			subprocess.check_output(cmd, shell=True)
			await event.respond("‹ Main Menu ›", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'delete-ssh'))
async def delete_ssh(event):
	async def delete_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/ssh | grep '^###' | cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**LIST ALL USER**
{z}
**KETIK NOMOR :**
/cancel Untuk Kembali
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "4" "{user}" | timeout 15s env HOME=/root TERM=xterm BOT_MODE=1 bash /usr/local/sbin/m-sshovpn || true'
			subprocess.check_output(cmd, shell=True)
			await event.respond("‹ Main Menu ›", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'limit-ssh'))
async def limit_ssh(event):
	async def limit_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/ssh | grep '^###' | cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**CHANGE LIMIT USER**
{z}
**KETIK NOMOR :**
/cancel Untuk Kembali
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**Ketik Limit IP Login Baru :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			cmd = f'printf "%s\n" "7" "{user}" "{exp}" | timeout 15s env HOME=/root TERM=xterm BOT_MODE=1 bash /usr/local/sbin/m-sshovpn || true'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES Delete**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limit_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'trial-ssh'))
async def trial_ssh(event):
	async def trial_ssh_(event):
		async with bot.conversation(chat) as exp:
			await event.edit(f"""
**Masukan Menit (Hanya angka) :**
/cancel Untuk Kembali
""")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		per = "/cancel"
		if exp == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" {2} "{exp}" | timeout 15s env HOME=/root TERM=xterm BOT_MODE=1 bash /usr/local/sbin/m-sshovpn || true'
			subprocess.check_output(cmd, shell=True)
			await event.respond("‹ Main Menu ›", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'cek-ssh'))
async def login_ssh(event):
	async def login_ssh_(event):
		cmd = 'bot-cek-login-ssh'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.edit(f"""
** SSH USER ONLINE**
{z}
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)


@bot.on(events.CallbackQuery(data=b'renew-ssh'))
async def renew_ssh(event):
	async def renew_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/ssh | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**LIST RENEW USER**
{z}
**MASUKAN NOMOR :**
/cancel Untuk Kembali
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			async with bot.conversation(chat) as exp:
				await event.respond(f"""
**KETIK EXPIRED BARU (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			cmd = f'printf "%s\n" "3" "{user}" "{exp}" | timeout 15s env HOME=/root TERM=xterm BOT_MODE=1 bash /usr/local/sbin/m-sshovpn || true'
			subprocess.check_output(cmd, shell=True)
			await event.respond("‹ Main Menu ›", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renew_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'login-ssh'))
async def login_ssh(event):
	async def login_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/sshx/listlock | grep '^###' | cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**LIST MULTI LOGIN USER**
{z}
**KETIK NOMOR :**
/cancel Untuk Kembali
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "9" "{user}" | timeout 15s env HOME=/root TERM=xterm BOT_MODE=1 bash /usr/local/sbin/m-sshovpn || true'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES UNLOCK**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await login_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'akun-ssh'))
async def akun_ssh(event):
	async def akun_ssh_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/ssh | grep '^###' | cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**CEK CONFIG USER**
{z}
**KETIK NOMOR :**
/cancel Untuk Kembali
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "6" "{user}" | timeout 15s env HOME=/root TERM=xterm BOT_MODE=1 bash /usr/local/sbin/m-sshovpn || true'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES CEK AKUN**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await akun_ssh_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

@bot.on(events.CallbackQuery(data=b'ssh'))
async def ssh(event):
	async def ssh_(event):
		inline = [
[Button.inline(" Trial ","trial-ssh"),
Button.inline(" Create ","create-ssh"),
Button.inline(" Login ","cek-ssh")],
[Button.inline(" Delete ","delete-ssh"),
Button.inline(" Unlock ","login-ssh"),
Button.inline(" Limit ","limit-ssh")],
[Button.inline(" Renew","renew-ssh"),
Button.inline(" Akun ","akun-ssh"),
Button.inline("‹ BACK ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		sh = f' cat /etc/xray/ssh | grep "###" | wc -l'
		ssh = subprocess.check_output(sh, shell=True).decode("ascii")
		msg = f"""
🧿───────────────────🧿
            **PANEL MENU SSH**
🧿───────────────────🧿
` Total   :` `{ssh.strip()}` __account__
` Host    :` `{DOMAIN}`
` ISP     :` `{z["isp"]}`
` Country :` `{z["country"]}`
🧿───────────────────🧿
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await ssh_(event)
	else:
		await event.answer("Access Denied",alert=True)
