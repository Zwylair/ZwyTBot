import aiogram
import splitter.splitter as sp


def setup(dp: aiogram.Dispatcher, bot: aiogram.Bot):
    sp.bot = bot

    dp.register_message_handler(sp.splitter_command, commands=['splitter'])
    dp.register_message_handler(sp.process_image_message, state=sp.AnswersForm, content_types=aiogram.types.ContentTypes.PHOTO)
