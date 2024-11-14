import asyncio
import os
from datetime import datetime, timedelta, timezone, tzinfo
from typing import List

from pyrogram import filters, Client
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
    CallbackQuery,
)

from config import LOGGER_ID
from musicbot import app
from musicbot.utils.database import (
    get_active_chats,
    remove_active_chat,
    remove_active_video_chat,
)
from musicbot.utils.database import AutoRestart
from musicbot.misc import HAPP, SUDOERS, Zone, calculate_hours, is_heroku


db = AutoRestart()

dateFormat = "%d-%m--%H:%M"


async def notify_restart(interval: int):
    served_chats = await get_active_chats()
    USERNAME = (await app.get_me()).username
    for x in served_chats:
        try:
            await app.send_message(
                x,
                "**__#AUTORESTART__**\n\n{} kendini {} saate bir yeniden başlatmaya ayarlandığı için kendini yeniden başlattı. __Sorunlar için özür dilerim.\n**10 - 15 saniye içerisinde bot aktif olacaktır.**".format(
                    USERNAME, interval
                ),
            )
            await remove_active_chat(x)
            await remove_active_video_chat(x)
        except Exception:
            pass


async def controller():
    restartCommand = (
        f"kill -9 {os.getpid()} && python3 -m musicbot"
        if os.name != "nt"
        else f"taskkill /F /PID {os.getpid()} && python3 -m musicbot"
    )
    status = await db.get_status()
    if status == False:
        return
    interval = await db.get_interval()
    if interval == 0:
        return
    hours: List[datetime] = await calculate_hours(interval)
    now = datetime.now(Zone(+4, False, "GMT"))
    if status == True:
        if now.hour in [x.hour for x in hours]:
            if now.minute == 0 and now.second < 15:
                await notify_restart(interval)
                if is_heroku():
                    if HAPP is not None:
                        HAPP.restart()
                    else:
                        await app.send_message(
                            LOGGER_ID,
                            "Heroku App Restart Failed!..",
                        )
                        os.system(restartCommand)
                else:
                    os.system(restartCommand)
    else:
        pass


async def loop_auto_restart():
    while True:
        await controller()
        await asyncio.sleep(1)
