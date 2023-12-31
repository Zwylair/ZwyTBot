import io
import os

import aiogram
from aiogram.dispatcher.filters.state import State, StatesGroup
import pydub

#

bot: aiogram.Bot


class AnswersForm(StatesGroup):
    sound_msg = State()


async def voice_creator(message: aiogram.types.Message):
    await AnswersForm.sound_msg.set()
    await message.reply('Отправь мне звук с подписью (необязательно), а я отправлю его в виде голосового (/cancel)')


async def voice_handler(message: aiogram.types.Message, state: aiogram.dispatcher.FSMContext):
    status_msg = await message.reply('Обработка, подождите пожалуйста 🕒')
    await bot.send_message(message.chat.id, '⏳')

    audio_io = await message.audio.download(destination_file=io.BytesIO())
    opus_io = io.BytesIO()

    await status_msg.edit_text('Форматирование аудио 🎧')

    audio = pydub.AudioSegment.from_file(audio_io)

    await status_msg.edit_text('Экспорт 📤')

    audio.export(opus_io, format='ogg', codec='libopus', bitrate='80k')
    opus_io.seek(0)

    i_f = aiogram.types.InputFile(opus_io, filename='voice.opus')

    for i in os.listdir():
        if i.startswith('ffcache'):
            os.remove(i)

    await message.reply_voice(i_f, message.text)
    await status_msg.edit_text('Готово ✅')
    await message.reply('Вы можете отправить еще звуков, или закончить с помощью /end')
