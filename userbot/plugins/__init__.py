import datetime
from Lion import *
from Lion.config import Config
from Lion.helpers import *
from Lion.utils import *
from Lion.random_strings import *
from Lion.version import __Lion__
from telethon import version


LION_USER = bot.me.first_name
ForGo10God = bot.uid
Lion_mention = f"[{LION_USER}](tg://user?id={ForGo10God})"
Lion_logo = "./Lion/resources/pics/Lion_logo.jpg"
cjb = "./Lion/resources/pics/cjb.jpg"
restlo = "./Lion/resources/pics/rest.jpeg"
shuru = "./Lion/resources/pics/shuru.jpg"
hl = Config.HANDLER
shl = Config.SUDO_HANDLER
Lion_ver = __Lion__
tel_ver = version.__version__

async def get_user_id(ids):
    if str(ids).isdigit():
        userid = int(ids)
    else:
        userid = (await bot.get_entity(ids)).id
    return userid

sudos = Config.SUDO_USERS
if sudos:
    is_sudo = "True"
else:
    is_sudo = "False"

abus = Config.ABUSE
if abus == "ON":
    abuse_m = "Enabled"
else:
    abuse_m ="Disabled"

START_TIME = datetime.datetime.now()
uptime = f"{str(datetime.datetime.now() - START_TIME).split('.')[0]}"
my_channel = Config.MY_CHANNEL or "Lionxupdates"
my_group = Config.MY_GROUP or "Lionxsupport"
if "@" in my_channel:
    my_channel = my_channel.replace("@", "")
if "@" in my_group:
    my_group = my_group.replace("@", "")

chnl_link = "https://t.me/Lionxupdates"
Lion_channel = f"[†hê ʟɨօռ-Ӽ]({chnl_link})"
grp_link = "https://t.me/Lionxsupport"
Lion_grp = f"[ʟɨօռ-Ӽ Group]({grp_link})"

WELCOME_FORMAT = """**Use these fomats in your welcome note to make them attractive.**
  {mention} :  To mention the user
  {title} : To get chat name in message
  {count} : To get group members
  {first} : To use user first name
  {last} : To use user last name
  {fullname} : To use user full name
  {userid} : To use userid
  {username} : To use user username
  {my_first} : To use my first name
  {my_fullname} : To use my full name
  {my_last} : To use my last name
  {my_mention} : To mention myself
  {my_username} : To use my username
"""
# will add more soon

# Lion
