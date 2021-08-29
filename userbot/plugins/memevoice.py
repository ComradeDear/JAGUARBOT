import re
from . import *

# Credits to @ForGo10God developer of Lion-X.
# This is my first plugin that I made when I released first Lion-X.
# Modified to work in groups with inline mode disabled.
# Added error msg if no voice is found.
# So please dont remove credit. 
# You can use it in your repo. But dont remove these lines...

@bot.on(Lion_cmd(pattern="mev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="mev(?: |$)(.*)", allow_sudo=True))
async def nope(crazy):
    Lion = crazy.pattern_match.group(1)
    if not Lion:
        if crazy.is_reply:
            (await crazy.get_reply_message()).message
        else:
            await edit_or_reply(crazy, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("TrollVoiceBot", f"{(deEmojify(Lion))}")
    if troll:
        await crazy.delete()
        hel_ = await troll[0].click(Config.LOGGER_ID)
        if hel_:
            await bot.send_file(
                crazy.chat_id,
                hel_,
                caption="",
            )
        await hel_.delete()
    else:
    	await eod(crazy, "**Error 404:**  Not Found")
    	
@bot.on(Lion_cmd(pattern="meev(?: |$)(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern="meev(?: |$)(.*)", allow_sudo=True))
async def nope(crazy):
    Lion = crazy.pattern_match.group(1)
    if not Lion:
        if crazy.is_reply:
            (await crazy.get_reply_message()).message
        else:
            await edit_or_reply(crazy, "`Sir please give some query to search and download it for you..!`"
            )
            return

    troll = await bot.inline_query("Myinstantsbot", f"{(deEmojify(Lion))}")
    if troll:
        await crazy.delete()
        hel_ = await troll[0].click(Config.LOGGER_ID)
        if hel_:
            await bot.send_file(
                crazy.chat_id,
                hel_,
                caption="",
            )
        await hel_.delete()
    else:
    	await eod(crazy, "**Error 404:**  Not Found")


CmdHelp("memevoice").add_command(
	"mev", "<query>", "Searches the given meme and sends audio if found."
).add_command(
	"meev", "<query>", "Same as {hl}mev"
).add_info(
	"Audio Memes."
).add_warning(
	"✅ Harmless Module."
).add()
