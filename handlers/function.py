import os
import yt_dlp
from aiogram.types import FSInputFile

async def download_and_send_media(bot, chat_id, url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        media_file = FSInputFile(filename)

        try:
            await bot.send_video(chat_id, media_file, caption="Вот твое видео!")
        except Exception:
            await bot.send_document(chat_id, media_file, caption="Вот твой файл!")

        os.remove(filename)

    except Exception as e:
        await bot.send_message(chat_id, f"Ошибка при скачивании: {e}")
