from kyt import *

@bot.on(events.CallbackQuery(data=b'trojan-go'))
async def nob(event):
	async def nob_(event):
		inline = [
[Button.inline(" CREATE TROJAN-GO ","create-trgo"),
Button.inline(" CHECK USER ","cek-trgo")],
[Button.inline(" DELETE USER ","delete-trgo"),
Button.inline(" RENEW USER ","renew-trgo")],
[Button.inline("‹ BACK ›","menu")]]
		z = requests.get(f"http://ip-api.com/json/?fields=country,region,city,timezone,isp").json()
		tgo = f' cat /etc/trojan-go/trgo | grep "###" | wc -l'
		trgo = subprocess.check_output(tgo, shell=True).decode("ascii")
		msg = f"""
🧿───────────────────🧿
**PANEL MENU TROJAN-GO**
🧿───────────────────🧿
` Service  :` `TROJAN-GO`
` Total Acc:` `{trgo.strip()}` __account__
` Host     :` `{DOMAIN}`
` ISP      :` `{z["isp"]}`
` Country  :` `{z["country"]}`
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
		
@bot.on(events.CallbackQuery(data=b'create-trgo'))
async def create_trgo(event):
	async def create_trgo_(event):
		async with bot.conversation(chat) as user:
			await event.edit(f"""
**✨ 𝙽𝚊𝚖𝚊 𝚋𝚎𝚛𝚞𝚙𝚊 𝚌𝚊𝚖𝚙𝚞𝚛𝚊𝚗, 
 𝙷𝚞𝚛𝚞𝚏 𝚔𝚊𝚙𝚒𝚝𝚊𝚕, 𝚍𝚊𝚗 𝙰𝚗𝚐𝚔𝚊**
**✨ No Space**
**✨ No double Name**
**✨ Bot : @tunnelstores13**

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
			cmd = f'printf "%s\n" "1" "{user}" "{exp}" | m-trgo | sleep 2 | exit'
			subprocess.check_output(cmd, shell=True)
			await event.respond(f"""
**» SUCCES CREATE**
**» DONE**
""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await create_trgo_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)

		
@bot.on(events.CallbackQuery(data=b'delete-trgo'))
async def delete_trgo(event):
	async def delete_trgo_(event):
		await event.edit(f"""
Fitur akan segera hadir:)
""",buttons=[[Button.inline(" Back ","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await delete_trgo_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'renew-trgo'))
async def renew_trgo(event):
	async def renew_trgo_(event):
		await event.edit(f"""
Fitur akan segera hadir:)
""",buttons=[[Button.inline(" Back ","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await renew_trgo_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
		
@bot.on(events.CallbackQuery(data=b'cek-trgo'))
async def cek_trgo(event):
	async def cek_trgo_(event):
		await event.edit(f"""
Fitur akan segera hadir:)
""",buttons=[[Button.inline(" Back ","menu")]])
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await cek_trgo_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)
