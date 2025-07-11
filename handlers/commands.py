from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
import handlers.function as hf

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        "Привет! Отправь мне ссылку из TikTok, YouTube или Instagram — и я скачаю видео для тебя."
    )

@router.message(lambda message: any(domain in message.text.lower() for domain in ["tiktok.com", "youtube.com", "instagram.com"]))
async def video_request(message: Message):
    url = message.text.strip()
    await message.answer("Скачиваю видео, подожди...")
    await hf.download_and_send_media(message.bot, message.chat.id, url)
