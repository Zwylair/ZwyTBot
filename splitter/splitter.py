import io
from PIL import Image
import aiogram
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import funcs

bot: aiogram.Bot


class AnswersForm(StatesGroup):
    image_message = State()


async def process_image_message(message: aiogram.types.Message, state: FSMContext):
    photo = await message.photo[-1].get_file()
    photo_file = io.BytesIO()
    await photo.download(destination_file=photo_file)
    image = Image.open(photo_file)

    if image.width % 2 != 0:
        image = image.resize((image.width - 1, image.height), Image.HAMMING)

    # x_start, y_end, x_end, y_start
    image_p1 = image.crop((0, 0, int(image.width / 2), image.height))
    image_p2 = image.crop((int(image.width / 2), 0, image.width, image.height))

    image_p1 = funcs.media_to_tg_file(image_p1)
    image_p2 = funcs.media_to_tg_file(image_p2)
    files = [aiogram.types.InputMediaPhoto(image_p1), aiogram.types.InputMediaPhoto(image_p2)]

    msg = await message.reply_media_group(files)
    await msg[0].reply('Вы можете загрузить еще фото, либо закончить (/end)')


async def splitter_command(message: aiogram.types.Message):
    if message.chat.type != 'private':
        return

    await AnswersForm.image_message.set()
    await message.reply('Отправьте мне изображение, которое хотите ровно разделить на две части (отмена: /cancel)')
