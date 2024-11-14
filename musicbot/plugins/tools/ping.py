from datetime import datetime

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from config import BANNED_USERS, PING_IMG_URL
from musicbot import app
from musicbot.core.call import Anony
from musicbot.utils import bot_sys_stats
from musicbot.utils.decorators.language import language
from musicbot.utils.inline import supp_markup


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Anony.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=supp_markup(_),
    )


@app.on_message(filters.command(["donate"]) & ~BANNED_USERS)
async def donate(client, message: Message):
    await message.reply_text(
        "🇷🇺 Свяжитесь с владельцем, чтобы поддержать нашего бота\n\n🇺🇸 Contact the owner to support our bot.\n🇹🇷 Botumuzu desteklemek için sahibiyle iletişime geçin\n@XezerBots",
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            InlineKeyboardButton("⚯͛ | Фамиль", url="https://t.me/xGuliyev")
        ),
    )
