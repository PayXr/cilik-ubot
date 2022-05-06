# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# Recode by @greyyvbss
#
""" Modul Userbot untuk menghapus pesan yang tidak dibutuhkan (chat spam atau lainnya)."""


from asyncio import sleep

from telethon.errors import rpcbaseerrors

from CilikUbot import CMD_HANDLER as cmd
from CilikUbot import CMD_HELP, DEVS
from CilikUbot.events import register
from CilikUbot.utils import edit_delete, cilik_cmd


@cilik_cmd(pattern="purge$")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cpurge$")
async def fastpurger(purg):
    chat = await purg.get_input_chat()
    msgs = []
    itermsg = purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id)
    count = 0
    if purg.reply_to_msg_id is None:
        return await event.reply("**Reply to messages**")
    async for msg in itermsg:
        msgs.append(msg)
        count += 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []
    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "**__Fast Purge Completed!__**\n**Successfully deleted** `"
        + str(count)
        + "` **Chats**",
    )
    await sleep(2)
    await done.delete()


@cilik_cmd(pattern="purgeme")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cpurgeme")
async def purgeme(delme):
    message = delme.text
    count = int(message[9:])
    i = 1
    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i += 1
        await message.delete()
    smsg = await delme.client.send_message(
        delme.chat_id,
        "**Berhasil Menghapus** " + str(count) + " **pesan**",
    )
    await sleep(2)
    i = 1
    await smsg.delete()


@cilik_cmd(pattern="del$")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cdel$")
async def delete_it(delme):
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
        except rpcbaseerrors.BadRequestError:
            await delme.edit("**Tidak Bisa Menghapus Pesan**")


@cilik_cmd(pattern="edit")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cedit")
async def editer(edit):
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id("me")
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i += 1


@cilik_cmd(pattern="sd")
async def selfdestruct(destroy):
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()


purgechat = {}


@cilik_cmd(pattern=r"(p|purge)(from$|to$)")
async def purgfromto(prgnew):
    reply = await prgnew.get_reply_message()
    if reply:
        if prgnew.pattern_match.group(2) == "from":
            await purgfrm(prgnew)
        elif prgnew.pattern_match.group(2) == "to":
            await purgto(prgnew)
    else:
        await edit_delete(prgnew, "**Mohon Balas Ke Pesan untuk mulai menghapus**")


async def purgfrm(purgdari):
    prgstrtmsg = purgdari.reply_to_msg_id
    purgechat[purgdari.chat_id] = prgstrtmsg
    manubot = await edit_delete(
        purgdari,
        "**Pesan ini telah dipilih sebagai awal menghapus, balas pesan lain dengan** `.purgeto` **untuk menghapusnya**",
    )
    await sleep(2)
    await manubot.delete()


async def purgto(purgke):
    try:
        prgstrtmsg = purgechat[purgke.chat_id]
    except KeyError:
        manubot = await edit_delete(
            purgke,
            "**Balas pesan dengan** `.purgefrom` **terlebih dahulu lalu gunakan** `.purgeto`",
            5,
        )
        return
    try:
        chat = await purgke.get_input_chat()
        prgendmsg = purgke.reply_to_msg_id
        pmsgs = []
        message = 0
        async for msg in purgke.client.iter_messages(
            purgke.chat_id, min_id=(prgstrtmsg - 1), max_id=(prgendmsg + 1)
        ):
            pmsgs.append(msg)
            message += 1
            pmsgs.append(purgke.reply_to_msg_id)
            if len(pmsgs) == 100:
                await purgke.client.delete_messages(chat, msgs)
        if pmsgs:
            await purgke.client.delete_messages(chat, pmsgs)
            await purgke.delete()
        man = await edit_delete(
            purgke,
            f"**Fast purge complete!**\n**Berhasil Menghapus** `{message}` **Pesan**",
            5,
        )
    except Exception as er:
        await purgke.edit(f"**ERROR:** `{er}`")


CMD_HELP.update(
    {
        "Purge": f"**➢ Plugin : **`Purge`\
        \n\n **ᴄᴍᴅ :** `{cmd}purge`\
        \n └⋟ Menghapus semua pesan mulai dari pesan yang dibalas.\
        \n\n **ᴄᴍᴅ :** `{cmd}purgefrom` atau `{cmd}pfrom`\
        \n └⋟ Menandai awal dari mana harus dihapus.\
        \n\n **ᴄᴍᴅ :** `{cmd}purgeto` atau `{cmd}pto`\
        \n └⋟ Menandai akhir dari pesan yang akan dihapus.\
        \n\n **ᴄᴍᴅ :** `{cmd}purgeme` <angka>\
        \n └⋟ Menghapus jumlah pesan anda, yang mau anda hapus.\
        \n\n **ᴄᴍᴅ :** `{cmd}del`\
        \n └⋟ Menghapus pesan, balas ke pesan.\
        \n\n **ᴄᴍᴅ :** `{cmd}edit <pesan baru>`\
        \n └⋟ Ganti pesan terakhir Anda dengan <pesan baru>.\
        \n\n **ᴄᴍᴅ :** `{cmd}sd` <detik> <pesan>\
        \n └⋟ Membuat pesan yang hancur sendiri. harap pasang detik di bawah 100 untuk menghindari bot Anda akan sleep.\
    "
    }
)