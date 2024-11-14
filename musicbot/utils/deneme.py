from config import LOGGER_ID
from musicbot import app
from musicbot.utils.database import get_active_chats                

async def play_logs(message):
    aktifseslisayısı = len(await get_active_chats())
    if message.chat.id != LOGGER_ID:
        try:
            await app.set_chat_title(LOGGER_ID, f"𝐑𝐀𝐆 𝐋𝐎𝐆 𝄞 - {aktifseslisayısı}")
        except:
            pass
    return