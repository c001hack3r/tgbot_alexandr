import config, description as dn, keyboards as kb
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

    #Ответ на кнопку СТАРТ
@dp.message_handler(commands=['start', 'help'])
async def start_msg(message: types.Message):
    await bot.send_message('720076833', f'⚡️Новая активность:\n\
Time: {message.date}\n\
User id: {message.from_user.id}\n\
Name: {message.from_user.first_name} {message.from_user.last_name}\n\
Username: @{message.from_user.username}')
    await message.answer(dn.start_msg, parse_mode='markdown', reply_markup=kb.main_menu)

    #Ответ на кнопку Обо мне
@dp.callback_query_handler(text='about_me')
async def about_me_info(callback: types.CallbackQuery):
    await bot.send_photo(callback.from_user.id, 'AgACAgIAAxkBAANZY9-PqOc2xX3bRBiZHMersfcjuCMAAkHHMRvvwAFL3-7GEkdAmBUBAAMCAANzAAMuBA')
    await callback.message.answer(dn.about_me, parse_mode='markdown', reply_markup=kb.back_to_mm)
    await callback.answer()


    #Ответ на кнопку онлайн ведение
@dp.callback_query_handler(text='online')
async def online_info(callback: types.CallbackQuery):
    # await bot.send_photo(callback.from_user.id, 'AgACAgIAAxkBAANZY9-PqOc2xX3bRBiZHMersfcjuCMAAkHHMRvvwAFL3-7GEkdAmBUBAAMCAANzAAMuBA')
    await callback.message.edit_text(dn.online, parse_mode='markdown', reply_markup=kb.back_or_pay)
    await callback.answer()

    #Ответ на кнопку Подготовка к соревнованиям
@dp.callback_query_handler(text='prepearing')
async def prepearing_info(callback: types.CallbackQuery):
    await bot.send_video(callback.from_user.id, 'BAACAgIAAxkBAAN0Y9-a0gABGf8l3cqc0wUXHA7lc1e8AAJaLAAC78ABSwQs2syjPcUZLgQ')
    await callback.message.answer(dn.prepearing, parse_mode='markdown', reply_markup=kb.back_to_mm)
    await callback.answer()


    #Ответ на нажатие кнопки Назад в главное меню
@dp.callback_query_handler(text='back_to_mm')
async def back_to_mm_info(callback: types.CallbackQuery):
    await callback.message.edit_text(dn.start_msg, parse_mode='markdown', reply_markup=kb.main_menu)
    await callback.answer()

# Получем file_id видео и фото
# @dp.message_handler(content_types=["video"])
# async def video_cmd(message):
#     id_video = message.video.file_id
#     await bot.send_message('720076833', id_video)
# @dp.message_handler(content_types=['photo'])
# async def photo_cmd(message):
#     id_photo = message.photo[0]['file_id']
#     await bot.send_message('720076833', id_photo)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
