import telebot
import os
import logging
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))
telebot.logger.setLevel(logging.DEBUG)


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("ABSENSI", callback_data="absensi"),
    InlineKeyboardButton("PERSONAL", callback_data="personal"),
    InlineKeyboardButton("CUTI", callback_data="cuti"),
    InlineKeyboardButton("DINAS", callback_data="dinas"),
    InlineKeyboardButton("TUGAS", callback_data="tugas"),
    InlineKeyboardButton("IJIN", callback_data="ijin"),
    InlineKeyboardButton("TRAINING", callback_data="training"),
    InlineKeyboardButton("DEKLARASI", callback_data="deklarasi"),)
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
        if call.data == 'personal':
            getPersonalData(call.message.chat.id)
    except Exception as e:
        print(e)


@bot.message_handler(commands=['check'])
def message_handler(message):
    bot.send_message(message.chat.id, "Silahkan pilih data yang ingin anda cek :",
                     reply_markup=gen_markup())


@bot.message_handler(commands=['myid'])
def message_handler(message):
    bot.send_message(message.chat.id, f'User ID anda: {message.from_user.id}')

def getPersonalData(chatId):
    data = """*DATA PERSONAL XXX ONLINE*
    NRP        : ABC123
    Nama       : DUMMY
    Jabatan    : CEO
    Dept       : 9.9
    Tgl Lahir  : 09-09-2023
    Gol. Datah : X
    Agama      : Warrior"""
    bot.send_message(chatId, data)

bot.infinity_polling()
