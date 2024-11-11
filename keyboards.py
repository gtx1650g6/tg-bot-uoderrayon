#     __  __           _         _              ____       _             _      _   
#    |  \/  | __ _  __| | ___   | |__  _   _   |  _ \ __ _| |_ _ __ ___ | | ___| |_ 
#    | |\/| |/ _` |/ _` |/ _ \  | '_ \| | | |  | |_) / _` | __| '__/ _ \| |/ _ \ __|
#    | |  | | (_| | (_| |  __/  | |_) | |_| |  |  __/ (_| | |_| | | (_) | |  __/ |_ 
#    |_|  |_|\__,_|\__,_|\___|  |_.__/ \__, |  |_|   \__,_|\__|_|  \___/|_|\___|\__|
#                                      |___/                                       

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📁 Подать заявку "Шаг в будущее"'), KeyboardButton(text='📎 Посетить наш сайт')],
        [KeyboardButton(text='ℹ️ О боте')]
    ],
    resize_keyboard=True
)

order_keyboard  = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='✅ Подать заявку', url='https://docs.google.com/forms/d/e/1FAIpQLSdRh0Qf5o7fuvzSvd90zkdsrJPgppEj-TD3VRJ60GnNciamxA/viewform?usp=sf_link')
        ]
    ]
)