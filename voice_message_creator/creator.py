import io

import aiogram
from aiogram.dispatcher.filters.state import State, StatesGroup

bot: aiogram.Bot


class AnswersForm(StatesGroup):
    sound_msg = State()


async def voice_creator(message: aiogram.types.Message):
    await AnswersForm.sound_msg.set()
    await message.reply('Отправь мне звук в виде файла с подписью (необязательно), а я отправлю его в виде голосового (/cancel)')


async def voice_handler(message: aiogram.types.Message, state: aiogram.dispatcher.FSMContext):
    io_bytes = await message.audio.download(destination_file=io.BytesIO())
    i_f = aiogram.types.InputFile(io_bytes)

    await message.reply_voice(i_f, message.text)
    await message.reply('Вы можете отправить еще звуков, или закончить с помощью /end')
