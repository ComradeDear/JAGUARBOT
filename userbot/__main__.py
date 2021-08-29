import glob
import os
import sys
from pathlib import Path

import telethon.utils
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest

from Lion import LOGS, bot, tbot
from Lion.config import Config
from Lion.utils import load_module
from Lion.version import __Lion__ as Lionver
hl = Config.HANDLER
LION_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"

# let's get the bot ready
async def Lion_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        LOGS.error(f"LION_SESSION - {str(e)}")
        sys.exit()


# Lion starter...
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Config.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Config.APP_ID, api_hash=Config.API_HASH
            ).start(bot_token=Config.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("🔰 Starting Lion-X 🔰")
            bot.loop.run_until_complete(Lion_bot(Config.BOT_USERNAME))
            LOGS.info("🔥 Lion-X Startup Completed 🔥")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

# imports plugins...
path = "Lion/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

# let the party begin...
LOGS.info("Starting Bot Mode !")
tbot.start()
LOGS.info("⚡ Your Lion-X Is Now Working ⚡")
LOGS.info(
    "Head to @LionXUpdates for Updates. Also join chat group to get help regarding to Lion-X."
)

# that's life...
async def Lion_is_on():
    try:
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                LION_PIC,
                caption=f"#START \n\nDeployed Hêllẞø† Successfully\n\n**Hêllẞø† - {Lionver}**\n\nType `{hl}ping` or `{hl}alive` to check! \n\nJoin [Hêllẞø† Channel](t.me/LionXUpdates) for Updates & [Hêllẞø† Chat](t.me/LionXSupport) for any query regarding Hêllẞø†",
            )
    except Exception as e:
        LOGS.info(str(e))

# Join Lion-X Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@LionXUpdates"))
    except BaseException:
        pass


bot.loop.create_task(Lion_is_on())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()

# Lion
