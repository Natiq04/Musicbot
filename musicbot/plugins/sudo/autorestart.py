import os
from typing import List, Tuple

from pyrogram import Client, filters
from pyrogram.types import Message

import config
from musicbot import app
from musicbot.misc import SUDOERS, Zone, calculate_hours, datetime
from musicbot.utils.database import AutoRestart


def isinteger(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


@app.on_message(filters.command("autorestart") & SUDOERS)
async def autorestart(client: Client, message: Message):
    command = message.command
    db = AutoRestart()
    helpText = f"""**Otomatik Yeniden Başlatma**\n\n
    
**Komutlar:**\n
`/autorestart on` - Otomatik Yeniden Başlatmayı Açar.
`/autorestart off` - Otomatik Yeniden Başlatmayı Kapatır.
`/autorestart set <saat>` - Otomatik Yeniden Başlatma Saatini Ayarlar.
`/autorestart` - Otomatik Yeniden Başlatma Durumunu Gösterir.
"""
    if len(command) < 2:
        # en yakın yeniden başlatmaya kalan süreyi göster
        if not await db.get_status():
            await message.reply_text("Otomatik Yeniden Başlatma Kapalı!\n\n" + helpText)
            return
        interval = await db.get_interval()
        if interval == 0:
            await message.reply_text(
                "Otomatik Yeniden Başlatma Kapalı!\n\n**Saat Aralığı:** `0` saat\n\n"
                + helpText
            )
            return
        restart_times: List[datetime] = await calculate_hours(interval)
        now = datetime.now(Zone(+4, False, "GMT"))
        hours = [x.hour for x in restart_times]
        # bir sonra ki yeniden başlatma zamanını bul (şu anki saatten büyük olan en küçük saat)
        next_restart = None
        for x in hours:
            if x > now.hour:
                next_restart = x
                break
        if next_restart is None:
            next_restart = hours[0]
        next_restart = restart_times[hours.index(next_restart)]
        time_left = next_restart - now
        time_left = time_left.seconds
        hours, remainder = divmod(time_left, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_left = f"{hours} saat, {minutes} dakika, {seconds} saniye"
        await message.reply_text(
            f"**Otomatik Yeniden Başlatma**\n\n"
            f"**Durum:** `{await db.get_status()}`\n"
            f"**Saat Aralığı:** `{await db.get_interval()}` saat\n"
            f"**Kalan Süre:** `{time_left}`"
        )
        return

    if command[1] == "on":
        await db.set_status(True)
        await message.reply_text("Otomatik Yeniden Başlatma Açıldı!")
    elif command[1] == "off":
        await db.set_status(False)
        await message.reply_text("Otomatik Yeniden Başlatma Kapatıldı!")
    elif command[1] == "set":
        if len(command) < 3:
            await message.reply_text("Saat belirtin.")
            return
        if not isinteger(command[2]):
            await message.reply_text("Saat belirtin.")
            return
        if int(command[2]) < 1:
            await message.reply_text("Saat 1'den küçük olamaz.")
            return
        await db.set_interval(int(command[2]))
        await message.reply_text(
            f"Otomatik Yeniden Başlatma Saati `{command[2]}` olarak ayarlandı."
        )
    else:
        await message.reply_text("Geçersiz Argüman.")
