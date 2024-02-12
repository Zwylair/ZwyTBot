import asyncio
import logging
import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import splitter
import voice_message_creator
import settings
import backgrounds

#

backgrounds.start_keeping()

logger = logging.getLogger(__name__)
logging.basicConfig(format='[%(asctime)s | %(levelname)s | %(name)s]: %(message)s')
logger.setLevel(logging.INFO)

bot = aiogram.Bot(settings.TOKEN)
storage = MemoryStorage()
dp = aiogram.Dispatcher(bot, storage=storage)
end_handler_states = [
    splitter.splitter.AnswersForm,
    voice_message_creator.v_msg_creator.AnswersForm
]


@dp.message_handler(state='*', commands=['cancel'])
async def cancel_handler(message: aiogram.types.Message, state: aiogram.dispatcher.FSMContext):
    current_state = await state.get_state()

    if current_state is None:  # User is not in any state, ignoring
        return

    await state.finish()
    await message.reply('Отменено 🔙')


@dp.message_handler(state=end_handler_states, commands=['end'])
async def end_handler(message: aiogram.types.Message, state: aiogram.dispatcher.FSMContext):
    await state.finish()
    await message.reply('Окей, если я еще понадоблюсь, я буду тут 😊')


async def main():
    me = await bot.me

    voice_message_creator.setup(dp, bot)
    splitter.setup(dp, bot)

    await dp.skip_updates()
    logger.info(f"I'm up! @{me.username} [{me.id}] at your service, Sir!")
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
