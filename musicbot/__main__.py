import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from musicbot import LOGGER, app, userbot
from musicbot.core.call import Anony
from musicbot.misc import sudo
from musicbot.plugins import ALL_MODULES
from musicbot.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("musicbot.plugins" + all_module)
    LOGGER("musicbot.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Anony.start()
    try:
        await Anony.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("musicbot").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Anony.decorators()
    LOGGER("musicbot").info(" __  __               __  __         _    ___      _   ")
    LOGGER("musicbot").info(" \ \/ /___ ______ _ _|  \/  |_  _ __(_)__| _ ) ___| |_ ")
    LOGGER("musicbot").info("  >  </ -_)_ / -_) '_| |\/| | || (_-< / _| _ \/ _ \  _|")
    LOGGER("musicbot").info(" /_/\_\___/__\___|_| |_|  |_|\_,_/__/_\__|___/\___/\__|")
    LOGGER("musicbot").info("                                                       ")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("musicbot").info("MusicBot Stopped.")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
