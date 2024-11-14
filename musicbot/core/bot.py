from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Bot başlayır...")
        super().__init__(
            name="musicbot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            in_memory=True,
            parse_mode=ParseMode.HTML,
            max_concurrent_transmissions=7,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"<u><b>» {self.mention} aktivdir :</b><u>\n\nɪᴅ : <code>{self.id}</code>\nAd : {self.name}\nUsername : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot log kanalını/qrupunu görmür. Botun kanalda/qrupda olduğunu kontrol edin."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"Bot log kanalını/qrupunu görə bilmir.\n  Səbəb : {type(ex).__name__}."
            )
            exit()

        a = await self.get_chat_member(config.LOGGER_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error(
                "Botu kanalda/qrupda admin edin."
            )
            exit()
        LOGGER(__name__).info(f"{self.name} Musiqi botu aktivdir")

    async def stop(self):
        await super().stop()
