from kyt import *

#delete
@bot.on(events.CallbackQuery(data=b'delete7-trojan'))
async def delete_trojan(event):
	async def delete_trojan_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/config.json | grep '^#trg' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**✨ LIST DELETE USER**
{z}
**✨ Input Your Number :**
/cancel Kembali KeMENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "4" "{user}" | m-trojan | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond("‹ Main Menu ›", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#renew
@bot.on(events.CallbackQuery(data=b'renew7-trojan'))
async def renew_trojan(event):
	async def renew_trojan_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/config.json | grep '^#trg' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**✨ LIST RENEW USER**
{z}
**✨ Input Your Number :**
/cancel Kembali KeMENU
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
**✨ Input Your New Expired (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			cmd = f'printf "%s\n" "3" "{user}" "{exp}" | m-trojan | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renew_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)


#limit
@bot.on(events.CallbackQuery(data=b'limit7-trojan'))
async def limit_trojan(event):
	async def limit_trojan_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/config.json | grep '^#trg' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**✨ CHANGE LIMIT USER**
{z}
**✨ Input Your Number :**
/cancel Kembali KeMENU
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
**✨ Input Your New Limit IP Login :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			async with bot.conversation(chat) as pw:
				await event.respond(f"""
**✨ Input Your New Quota User :**
""")
				pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw = (await pw).raw_text
			cmd = f'printf "%s\n" "7" "{user}" "{exp}" "{pw}" | m-trojan | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES CHANGE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await limit_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#CekConfig
@bot.on(events.CallbackQuery(data=b'akun7-trojan'))
async def akun_trojan(event):
	async def akun_trojan_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/xray/config.json | grep '^#trg' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**✨ CEK CONFIG USER**
{z}
**✨ Input Your Number :**
/cancel Kembali KeMENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "6" "{user}" | m-trojan | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES CEK AKUN**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await akun_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
		
#restore
@bot.on(events.CallbackQuery(data=b'restore7-trojan'))
async def restore_trojan(event):
	async def restore_trojan_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/trojan/akundelete | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**✨ LIST AKUN RESTORE **
{z}
**✨ Input Your Number :**
/cancel Kembali KeMENU
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
**✨ Input Your Expired (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			async with bot.conversation(chat) as pw:
				await event.respond(f"""
**✨ Input Your New Limit IP Login :**
""")
				pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw = (await pw).raw_text
			async with bot.conversation(chat) as pw2:
				await event.respond(f"""
**✨ Input Your New Quota User:**
""")
				pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw2 = (await pw2).raw_text
			cmd = f'printf "%s\n" "11" "{user}" "{exp}" "{pw}" "{pw2}" | m-trojan | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES CHANGE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await restore_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)


#MultiLogin Login
@bot.on(events.CallbackQuery(data=b'loginip7-trojan'))
async def loginip_trojan(event):
	async def loginip_trojan_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/trojan/listlock | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**✨ LIST MULTI LOGIN IP USER**
{z}
**✨ Input Your Number :**
/cancel Kembali KeMENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "9" "{user}" | m-trojan | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES UNLOCK**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await loginip_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
#MultiLogin Quota
@bot.on(events.CallbackQuery(data=b'logingb7-trojan'))
async def logingb_trojan(event):
	async def logingb_trojan_(event):
		async with bot.conversation(chat) as user:
			cmd2 = f" cat /etc/trojan/userQuota | grep '^###' |  cut -d ' ' -f 2-3 | nl -s ') '".strip()
			x = subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
			print(x)
			z = subprocess.check_output(cmd2, shell=True).decode("ascii")
			await event.edit(f"""
**✨ LIST LOGIN QUOTA USER**
{z}
**✨ Input Your Number :**
/cancel Kembali KeMENU
""")
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		per = "/cancel"
		if user == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" "10" "{user}" | m-trojan | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES UNLOCK**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await logingb_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
#CRATE trojan
@bot.on(events.CallbackQuery(data=b'create7-trojan'))
async def create_trojan(event):
	async def create_trojan_(event):
		async with bot.conversation(chat) as user:
			await event.edit(f"""
**✨ Input Your UserName :**
/cancel Kembali KeMENU
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
**✨ Input Your Expired (day) :**
""")
				exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				exp = (await exp).raw_text
			async with bot.conversation(chat) as pw:
				await event.respond(f"""
**✨ Input Your Limit IP Login :**
""")
				pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw = (await pw).raw_text
			async with bot.conversation(chat) as pw2:
				await event.respond(f"""
**👉 Input Your Quota User :**
""")
				pw2 = pw2.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
				pw2 = (await pw2).raw_text
			cmd = f'printf "%s\n" "1" "{user}" "{exp}" "{pw}" "{pw2}" | m-trojan | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond("‹ Main Menu ›", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

# TRIAL trojan
@bot.on(events.CallbackQuery(data=b'trial7-trojan'))
async def trial_trojan(event):
	async def trial_trojan_(event):
		async with bot.conversation(chat) as exp:
			await event.edit(f"""
**✨ Input Your Timer (Minutes) :**
/cancel Kembali KeMENU
""")
			exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			exp = (await exp).raw_text
		per = "/cancel"
		if exp == per:
			await event.respond(f"""
**» CANCEL**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
		else:
			cmd = f'printf "%s\n" {2} "{exp}" | m-trojan | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True).decode("utf-8")
			await event.respond("‹ Main Menu ›", buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trial_trojan_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

#CEK
@bot.on(events.CallbackQuery(data=b'cek7-trojan'))
async def cek_trojan(event):
	async def cek_trojan_(event):
		cmd = 'bot-cek-tr'.strip()
		x = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
		print(x)
		z = subprocess.check_output(cmd, shell=True).decode("utf-8")
		await event.edit(f"""
**✨ TROJAN USER ONLINE**
{z}
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_trojan_(event)
	else:
		await event.answer("Access Denied",alert=True)

@bot.on(events.CallbackQuery(data=b'login7-trojan'))
async def trojan(event):
	async def trojan_(event):
		inline = [
[Button.inline(" UNLOCK LOGIN ","loginip7-trojan"),
Button.inline(" UNLOCK QUOTA ","logingb7-trojan")],
[Button.inline("‹ Back ›","trojan")]]
		await event.edit(buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trojan_(event)
	else:
		await event.answer("Access Denied",alert=True)
		
@bot.on(events.CallbackQuery(data=b'trojan'))
async def trojan(event):
	async def trojan_(event):
		inline = [
[Button.inline(" Trial ","trial7-trojan"),
Button.inline(" Create ","create7-trojan"),
Button.inline(" Login ","cek7-trojan")],
[Button.inline(" Delete ","delete7-trojan"),
Button.inline(" Unlock ","login7-trojan"),
Button.inline(" Limit ","limit7-trojan")],
[Button.inline(" Renew","renew7-trojan"),
Button.inline(" Restore ","restore7-trojan"),
Button.inline(" Akun ","akun7-trojan")],
[Button.inline("‹ BACK ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		vm = f' cat /etc/xray/config.json | grep "#trg" | wc -l'
		vms = subprocess.check_output(vm, shell=True).decode("ascii")
		msg = f"""
🧿───────────────────🧿
         **PANEL MENU TROJAN**
🧿───────────────────🧿
` Total Acc:` `{vms.strip()}` __account__
` Host     :` `{DOMAIN}`
` ISP      :` `{z["isp"]}`
` Country  :` `{z["country"]}`
🧿───────────────────🧿
"""
		await event.edit(msg,buttons=inline)
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await trojan_(event)
	else:
		await event.answer("Access Denied",alert=True)
