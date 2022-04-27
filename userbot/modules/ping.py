import random
import asyncio
import time
from datetime import datetime
from speedtest import Speedtest
from userbot import CMD_HANDLER as cmd
from userbot import CMD_HELP, DEVS, StartTime, bot
from userbot.events import register
from userbot.utils import edit_or_reply, humanbytes, cilik_cmd


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "Jam", "Hari"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time
  
  
@cilik_cmd(pattern="ping$")
async def _(pang):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await pang.reply("**...**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"**Pong** - `%sms`\n"
        f"**Uptime -** `{uptime}`" % (duration)
    ) 
