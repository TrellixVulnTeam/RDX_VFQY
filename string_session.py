print(
    "ㅤ\nㅤ\n\n\n\nㅤ\n┈┈┏━╮╭━┓┈╭━━━━━━╮\n┈┈┃┏┗┛┓┃╭┫ⓞⓘⓝⓚ ┃\n┈┈╰┓▋▋┏╯╯╰━━━━━━╯\n┈╭━┻╮╲┗━━━━╮╭╮┈\n┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n┈┈┈┈┈┗┻┛┗┻┛┈┈"
)
print("\n\n\n\n\nHello sir!!, I'm Here To Help u to Generate Telethon String Session")
print("\n\nBygByrd UserBot")

print("\n\nProperly Fill APP_ID ,HASH and Number.\n")

from telethon.sync import TelegramClient
from telethon.sessions import StringSession
APP_ID = int(input("Enter APP ID here: "))
API_HASH = input("Enter API HASH here: ")
with TelegramClient(StringSession(), APP_ID, API_HASH) as hehe:
	dcsession = hehe.session.save()
	BBYRD = hehe.send_message(
	    "me",
	    f"`{dcsession}`\n\n**Apki BygByrd ki String Session yaha hai sir ji Sir😁😎😎\nClick on above Code to Copy it\n\nFor Support Join** @BygBrd_userbot_Support"
	)

print("\n\n############################\n")
print(
    "check your Telegram Saved Messages For Ur New String String Session 😂😂 or see below. ")

print("\n############################\n")


print(f"{dcsession}")

Print(" ")
