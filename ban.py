import logging
import re
import os
import sys
import asyncio
from telethon import TelegramClient, events
import telethon.utils
from telethon.tl import functions
from telethon.tl.functions.channels import LeaveChannelRequest
from asyncio import sleep
from telethon.tl.types import ChatBannedRights, ChannelParticipantsAdmins, ChatAdminRights
from telethon.tl.functions.channels import EditBannedRequest
from datetime import datetime
from var import Var
from telethon import Button

from time import sleep
from telethon.errors.rpcerrorlist import FloodWaitError
from telethon.tl import functions
from telethon.tl.types import (
    ChannelParticipantsAdmins,
    ChannelParticipantsKicked,
    ChatBannedRights,
    UserStatusEmpty,
    UserStatusLastMonth,
    UserStatusLastWeek,
    UserStatusOffline,
    UserStatusOnline,
    UserStatusRecently,
)



RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

logging.basicConfig(level=logging.INFO)

print("Starting.....")

Ayu = TelegramClient('Ayu', Var.API_ID, Var.API_HASH).start(bot_token=Var.BOT_TOKEN)

SUDO_USERS = []
for x in Var.SUDO:
    SUDO_USERS.append(x)



@Ayu.on(events.NewMessage(pattern="^/ping"))
async def ping(e):
        start = datetime.now()
        text = "Pᴏɴɢ!"
        event = await e.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit(f"I'ᴍ Oɴ \n\n __Pᴏɴɢ__ !! `{ms}` ms")



@Ayu.on(events.NewMessage(pattern='/start'))
async def start_command(event):
    # Send a picture and start message
    await event.respond(
        "× I'ᴍ Aɴɪᴍᴇ-Tʜᴇᴍᴇ Gʀᴏᴜᴘ Cʟᴇᴀɴ Bᴏᴛ\n"
        "× I'ᴍ Vᴇʀʏ Fᴀꜱᴛ Aɴᴅ Mᴏʀᴇ Eꜰꜰɪᴄɪᴇɴᴛ I Pʀᴏᴠɪᴅᴇ Aᴡᴇꜱᴏᴍᴇ Fᴇᴀᴛᴜʀᴇꜱ!",
        buttons=[
            [Button.url("Sᴜᴘᴘᴏʀᴛ Cʜᴀɴɴᴇʟ", url="https://t.me/AloneXBots")],
            [Button.url("Sᴜᴘᴘᴏʀᴛ Aʟʟ Lɪɴᴋ", url="https://t.me/addlist/MFlGJNbdpco3NTll")],
        ],
        file='https://telegra.ph//file/9e8ce3092848a1bc5d9d6.jpg',  # Replace with your image URL
    )


                        




@Ayu.on(events.NewMessage(pattern="^/kickall"))
async def kickall(event):
        if not event.is_group:
            Reply = f"Nᴏᴏʙ !! Usᴇ Tʜɪs Cᴍᴅ Iɴ Gʀᴏᴜᴘ."
            await event.reply(Reply)
        else:
            await event.delete()
            Ven = await event.get_chat()
            Venomop = await event.client.get_me()
            admin = Ven.admin_rights
            creator = Ven.creator
            if not admin and not creator:
                return await event.reply("I Dᴏɴ'ᴛ Hᴀᴠᴇ Sᴜғғɪᴄɪᴇɴᴛ Rɪɢʜᴛs !!")
            Ayush = await Ayu.send_message(event.chat_id, "Hᴇʟʟᴏ !! I'ᴍ Aʟɪᴠᴇ")
            admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
            admins_id = [i.id for i in admins]
            all = 0
            kimk = 0
            async for user in event.client.iter_participants(event.chat_id):
                all += 1
                try:
                    if user.id not in admins_id:
                        await event.client.kick_participant(event.chat_id, user.id)
                        kimk += 1
                        await asyncio.sleep(0.1)
                except Exception as e:
                    print(str(e))
                    await asyncio.sleep(0.1)
            await Ayush.edit(f"Usᴇʀs Kɪᴄᴋᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ! \n\n Kɪᴄᴋᴇᴅ: `{kimk}` \n Tᴏᴛᴀʟ: `{all}`")


@Ayu.on(events.NewMessage(pattern="^/banall"))
async def banall(event):
    if not event.is_group:
        Reply = f"Nᴏᴏʙ !! Usᴇ Tʜɪs Cᴍᴅ Iɴ Gʀᴏᴜᴘ."
        await event.reply(Reply)
    else:
        await event.delete()
        Ven = await event.get_chat()
        Venomop = await event.client.get_me()
        admin = Ven.admin_rights
        creator = Ven.creator
        if not admin and not creator:
            return await event.reply("I Dᴏɴ'ᴛ Hᴀᴠᴇ Sᴜғғɪᴄɪᴇɴᴛ Rɪɢʜᴛs !!")
        Ayush = await Ayu.send_message(event.chat_id, "Hᴇʟʟᴏ !! I'ᴍ Aʟɪᴠᴇ")
        admins = await event.client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)
        admins_id = [i.id for i in admins]
        all = 0
        bann = 0
        async for user in event.client.iter_participants(event.chat_id):
            all += 1
            try:
                if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))
                    bann += 1
                    await asyncio.sleep(0.1)
            except Exception as e:
                print(str(e))
                await asyncio.sleep(0.1)
        await Ayush.edit(f"Usᴇʀs Bᴀɴɴᴇᴅ Sᴜᴄᴄᴇssғᴜʟʟʏ ! \n\n Bᴀɴɴᴇᴅ Usᴇʀs: {bann} \n Tᴏᴛᴀʟ Usᴇʀs: {all}")

@Ayu.on(events.NewMessage(pattern="^/unbanall"))
async def unban(event):
        if not event.is_group:
            Reply = f"Nᴏᴏʙ !! Usᴇ Tʜɪs Cᴍᴅ Iɴ Gʀᴏᴜᴘ."
            await event.reply(Reply)
        else:
            msg = await event.reply("Sᴇᴀʀᴄʜɪɴɢ Pᴀʀᴛɪᴄɪᴘᴀɴᴛ Lɪsᴛs.")
            p = 0
            async for i in event.client.iter_participants(event.chat_id, filter=ChannelParticipantsKicked, aggressive=True):
                rights = ChatBannedRights(until_date=0, view_messages=False)
                try:
                    await event.client(functions.channels.EditBannedRequest(event.chat_id, i, rights))
                except FloodWaitError as ex:
                    print(f"sleeping for {ex.seconds} seconds")
                    sleep(ex.seconds)
                except Exception as ex:
                    await msg.edit(str(ex))
                else:
                    p += 1
            await msg.edit("{}: {} unbanned".format(event.chat_id, p))


@Ayu.on(events.NewMessage(pattern="^/leave"))
async def _(e):
        venom = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(e.text) > 7:
            bc = venom[0]
            bc = int(bc)
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Sᴜᴄᴄᴇssғᴜʟʟʏ Lᴇғᴛ")
            except Exception as e:
                await event.edit(str(e))
        else:
            bc = e.chat_id
            text = "Leaving....."
            event = await e.reply(text, parse_mode=None, link_preview=None)
            try:
                await event.client(LeaveChannelRequest(bc))
                await event.edit("Sᴜᴄᴄᴇssғᴜʟʟʏ Lᴇғᴛ")
            except Exception as e:
                await event.edit(str(e))


@Ayu.on(events.NewMessage(pattern="^/restart"))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "__Rᴇsᴛᴀʀᴛɪɴɢ__ !!!"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Ayu.disconnect()
        except Exception:
            pass
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()

print("\n\n")
print("Your Ban All Bot Deployed Successfully ✅")

Ayu.run_until_disconnected()
