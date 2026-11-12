import telebot


botik = telebot.TeleBot('8939347233:AAFmsFP56KkOlxrJfqZKHTBiyZ2ADU6RNYw')

@botik.message_handler(commands=['start'])
def send_message(message):
    botik.send_message(message.chat.id, f'Hello, {message.from_user.username}! Выбери преподавателя:')
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text = 'Hi', callback_data = 'hi')
    keyboard.add(callback_button)
    botik.send_message(message.chat.id, "Z", reply_markup = keyboard)

@botik.message_handler(commands=['csf'])
def send_message_and_photo(message):
    with open('photo_2026-02-20_12-17-14.jpg', 'rb') as photo:
        botik.send_photo(message.chat.id, photo, caption='Слава ВГУ! Слава ФКН!')


botik.infinity_polling()