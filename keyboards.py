from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


#Главное меню
main_menu = InlineKeyboardMarkup()
main_menu.row(InlineKeyboardButton(text='Онлайн-ведение', callback_data='online'))
main_menu.row(InlineKeyboardButton(text='Подготовка к соревнованиям', callback_data='prepearing'))
main_menu.row(InlineKeyboardButton(text='Обо мне', callback_data='about_me'))
main_menu.insert(InlineKeyboardButton(text='Мой телеграм', url='https://t.me/alexandr01_87'))

#Возврат в главное меню
back_to_mm = InlineKeyboardMarkup()
back_to_mm.row(InlineKeyboardButton(text='< Назад в главное меню', callback_data='back_to_mm'))

#Кнопки для Онлайн-ведения
back_or_pay = InlineKeyboardMarkup()
back_or_pay.row(InlineKeyboardButton(text='Записаться на тренировки >', url='https://t.me/alexandr01_87'))
back_or_pay.row(InlineKeyboardButton(text='< Назад в главное меню', callback_data='back_to_mm'))
