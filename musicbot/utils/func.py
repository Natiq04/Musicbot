import asyncio
import traceback
from typing import Tuple

from pyrogram import Client, filters
from pyrogram.enums import MessageEntityType
from pyrogram.types import Message
from datetime import datetime
from BasicMusic import app

from BasicMusic.utils.database.memorydatabase import memberCountSettings
from config import LOG_GROUP_ID, BOT_TOKEN

MEMBER_PIECES = {}


async def checkMemberPieces(app: Client, chat_id: int):
    if chat_id not in MEMBER_PIECES:
        try:
            count = await app.get_chat_members_count(chat_id)
            MEMBER_PIECES[chat_id] = {"count": count, "date": datetime.now()}
        except Exception as e:
            traceback.print_exc()
            return
    else:
        member = MEMBER_PIECES[chat_id]
        if (datetime.now() - member["date"]).seconds > 60 * 15:
            try:
                count = await app.get_chat_members_count(chat_id)
                MEMBER_PIECES[chat_id] = {"count": count, "date": datetime.now()}
            except Exception as e:
                traceback.print_exc()
                return
        else:
            count = member["count"]

    settings = await memberCountSettings.get()
    # print(f"Member Pieces Status: {status}")
    if settings.status is True:
        if chat_id in settings.chats:
            return
        if chat_id == LOG_GROUP_ID:
            return
        if count < settings.pieces:
            try:
                try:
                    await app.send_message(
                        chat_id,
                        f"**{app.me.first_name} botunda üye sayı sınırı açıktır.**\n\n__Üzgünüm en az {settings.pieces} üyeye sahip olan gruplarda çalışabilirim.__",
                    )
                except:
                    pass
                await app.leave_chat(chat_id)
                await app.send_message(
                    LOG_GROUP_ID,
                    f"**{app.me.first_name} botu {chat_id} ID'li gruptan ayrıldı.**\n\n__Üye sayısı: {count}__",
                )
                return False
            except Exception as e:
                print(f"Chat ID: {chat_id} - Error: {e}")
                traceback.print_exc()
                return False

        else:
            return True
    else:
        return True


def extract_user(message: Message) -> Tuple[int, str]:
    user_id = None
    user_first_name = None

    def basicbots(message: Message) -> Tuple[int, str]:
        user_id = None
        user_first_name = None

        if message.from_user:
            user_id = message.from_user.id
            user_first_name = message.from_user.first_name

        elif message.sender_chat:
            user_id = message.sender_chat.id
            user_first_name = message.sender_chat.title

        return (user_id, user_first_name)

    if len(message.command) > 1:
        if (
            len(message.entities) > 1
            and message.entities[1].type == MessageEntityType.TEXT_MENTION
        ):
            required_entity = message.entities[1]
            user_id = required_entity.user.id
            user_first_name = required_entity.user.first_name
        else:
            user_id = message.command[1]
            user_first_name = user_id

        try:
            user_id = int(user_id)
        except ValueError:
            pass

    elif message.reply_to_message:
        user_id, user_first_name = basicbots(message.reply_to_message)

    elif message:
        user_id, user_first_name = basicbots(message)

    return (user_id, user_first_name)


def isinteger(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


async def aiosend_message(chat_id: int, message_text: str, reply_markup: str = None):
    try:
        await app.send_message(chat_id, message_text, reply_markup=reply_markup)
    except Exception as e:
        print(f"Chat ID: {chat_id} - Error: {e}")
        traceback.print_exc()
        return False
    return True


def send_message(chat_id: int, message_text: str, reply_markup: str = None):
    if len(message_text) > 4096:
        message_text = message_text[:4096]
    try:
        # asyncio
        app.loop.run_until_complete(
            app.send_message(chat_id, message_text, reply_markup=reply_markup)
        )
    except Exception as e:
        print(f"Chat ID: {chat_id} - Error: {e}")
        traceback.print_exc()
        return False

# dd