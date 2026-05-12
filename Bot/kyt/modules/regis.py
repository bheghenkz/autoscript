from kyt import *
import subprocess
import time

# // RNEW IP
@bot.on(events.CallbackQuery(data=b'renewip'))
async def renewipp(event):
    async def renewipp_(event):
        async with bot.conversation(chat) as user:
            pko = f' curl -sS https://raw.githubusercontent.com/bheghenkz/premium/main/ip | grep -E "^###" | cut -d " " -f 2-6 | column -t | sort | uniq'
            userlist = subprocess.check_output(pko, shell=True).decode("ascii")
            await event.edit(f"""
**✨ LIST USER** 
{userlist} 
**✨ INPUT IP :** 
/cancel Kembali
""")
            user= user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        per = "/cancel"
        if user == per:
              await event.respond(f"""**» CANCEL**""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
        else:
              async with bot.conversation(chat) as exp:
                  await event.respond(f"""**✨ KETIK EXP AKUN (day) :**""")
                  exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                  exp = (await exp).raw_text
                  cmd = f'printf "%s\n" "3" "{user}" "{exp}" | add-ip-new | sleep 8 | exit'
              subprocess.check_output(cmd,shell=True).decode("utf-8")
              await event.respond(f"""**» SUCCES RENEW****» DONE**""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
        

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await renewipp_(event)
    else:
        await event.answer("Akses Ditolak",alert=True)


# // DELETE IP
@bot.on(events.CallbackQuery(data=b'deleteip'))
async def deleteipp(event):
    async def deleteipp_(event):
        async with bot.conversation(chat) as pw:
            po = f' curl -sS https://raw.githubusercontent.com/bheghenkz/premium/main/ip | grep -E "^###" | cut -d " " -f 2-6 | column -t | sort | uniq'
            usersc = subprocess.check_output(po, shell=True).decode("ascii")
            await event.edit(f"""
**✨ LIST USER** 
{usersc} 
**✨ INPUT IP :** 
/cancel Kembali
""")
            pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            pw = (await pw).raw_text
        cmd = f'printf "%s\n" "2" "{pw}"| add-ip-new | sleep 8 | exit'
        per ="/cancel"
        if pw == per:
            await event.respond(f"""**» CANCEL**""",buttons=[[Button.inline("‹ BACK ›","deleteip")]])
        else:
            subprocess.check_output(cmd,shell=True).decode("utf-8")
            await event.respond(f"""**» SUCCES DELETE IP**""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])

    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await deleteipp_(event)
    else:
        await event.answer("Akses Ditolak",alert=True)


# // ADD IP
@bot.on(events.CallbackQuery(data=b'resgissc'))
async def registersc(event):
    async def registersc(event):
        async with bot.conversation(chat) as user:
            await event.respond(f"""**✨ KETIK IP  :**""")
            user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
            user = (await user).raw_text
        per = "/cancel"
        if user == per:
            await event.respond(f"""**» CANCEL**""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
        else:
            async with bot.conversation(chat) as pw:
                await event.respond(f"""**✨ KETIK USER :**""")
                pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                pw = (await pw).raw_text
            async with bot.conversation(chat) as exp:
                await event.respond(f"""**✨ KETIK EXP AKUN (day) :**""")
                exp = exp.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
                exp = (await exp).raw_text
                cmd = f'printf "%s\n" "1" "{user}" "{pw}" "{exp}" | add-ip-new | sleep 8 | exit'
            subprocess.check_output(cmd,shell=True).decode("utf-8")
            await event.respond(f"""**» SUCCES CREATE****» DONE**""",buttons=[[Button.inline("‹ Main Menu ›","menu")]])
    chat = event.chat_id
    sender = await event.get_sender()
    a = valid(str(sender.id))
    if a == "true":
        await registersc(event)
    else:
        await event.answer("Akses Ditolak",alert=True)

#BATAS
@bot.on(events.CallbackQuery(data=b'regis'))
async def menu(event):
    inline = [[Button.inline(" ADD IP ","resgissc"),Button.inline(" DELETE IP ","deleteip")],[Button.inline(" RENEW IP ","renewip"),Button.url(" JOIN ","https://t.me/fensmilebots")],[Button.inline("‹ BACK ›","menu")]]
    sender = await event.get_sender()
    val = valid(str(sender.id))
    if val == "false":
        try:
            await event.answer("Akses Ditolak", alert=True)
        except:
            await event.reply("Akses Ditolak")
    elif val == "true":
        sh = f' curl -sS https://raw.githubusercontent.com/bheghenkz/premium/main/ip | grep -E "^###" | cut -d " " -f 2-6 | column -t | sort | uniq | wc -l'
        usersc = subprocess.check_output(sh, shell=True).decode("ascii")
        asu=(int(usersc )-1)
        sdss = f" cat /etc/os-release | grep -w PRETTY_NAME | head -n1 | sed 's/=//g' | sed 's/PRETTY_NAME//g'"
        namaos = subprocess.check_output(sdss, shell=True).decode("ascii")
        ipvps = f" curl -4 -s ifconfig.me/ip"
        ipsaya = subprocess.check_output(ipvps, shell=True).decode("ascii")
        msg = f"""
🧿───────────────────🧿
   **REGISTRASI IP AUTO SCRIPT**
🧿───────────────────🧿
Hi {sender.first_name}
`Total Online  :` `{int(usersc)-1}`
`Autoscript By :` @Smile_Bots_bot
🧿───────────────────🧿

"""
        x = await event.edit(msg,buttons=inline)
        if not x:
            await event.reply(msg,buttons=inline)


