import asyncio
import datetime

from . import *

@bot.on(Lion_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def pong(Lion):
    if Lion.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(Lion, "`·.·★ ℘ıŋɠ ★·.·´")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"╰•★★  ℘ơŋɠ ★★•╯\n\n    ⚘  `{ms}`\n    ⚘  __**Oɯɳҽɾ**__ **:**  {Lion_mention}"
    )


CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your ʟɨօռ-Ӽ"
).add_warning(
  "✅ Harmless Module"
).add()

# Lion
