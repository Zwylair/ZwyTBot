import aiogram
from aiogram.types import ContentTypes
import voice_message_creator.creator as v_msg_creator


def setup(dp: aiogram.Dispatcher, bot: aiogram.Bot):
    v_msg_creator.bot = bot

    dp.register_message_handler(v_msg_creator.voice_creator, commands=['voice_msg_creator'])
    dp.register_message_handler(v_msg_creator.voice_handler, state=v_msg_creator.AnswersForm,
                                content_types=ContentTypes.AUDIO)
