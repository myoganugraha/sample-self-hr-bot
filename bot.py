import telebot
import os
import logging
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
telebot.logger.setLevel(logging.DEBUG)

availableMenu = [
    InlineKeyboardButton("ABSENSI", callback_data="absensi"),
    InlineKeyboardButton("PERSONAL", callback_data="personal"),
    InlineKeyboardButton("CUTI", callback_data="cuti"),
    InlineKeyboardButton("DINAS", callback_data="dinas"),
    InlineKeyboardButton("TUGAS", callback_data="tugas"),
    InlineKeyboardButton("IJIN", callback_data="ijin"),
    InlineKeyboardButton("TRAINING", callback_data="training"),
    InlineKeyboardButton("DEKLARASI", callback_data="deklarasi"),
]


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(availableMenu)
    return markup


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: CallbackQuery):
    try:
        bot.answer_callback_query(call.id, call.data)
        bot.edit_message_text(
            f'/check {call.data}',
            call.message.chat.id,
            call.message.message_id
        )
    except Exception as e:
        print(e)


@bot.message_handler(commands=['check'])
def message_handler(message):
    bot.send_message(message.chat.id, "Silahkan pilih data yang ingin anda cek :",
                     reply_markup=gen_markup())


bot.infinity_polling()
