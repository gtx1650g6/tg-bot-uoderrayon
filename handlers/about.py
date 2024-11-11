#     __  __           _         _              ____       _             _      _   
#    |  \/  | __ _  __| | ___   | |__  _   _   |  _ \ __ _| |_ _ __ ___ | | ___| |_ 
#    | |\/| |/ _` |/ _` |/ _ \  | '_ \| | | |  | |_) / _` | __| '__/ _ \| |/ _ \ __|
#    | |  | | (_| | (_| |  __/  | |_) | |_| |  |  __/ (_| | |_| | | (_) | |  __/ |_ 
#    |_|  |_|\__,_|\__,_|\___|  |_.__/ \__, |  |_|   \__,_|\__|_|  \___/|_|\___|\__|
#                                      |___/                                       

from aiogram import Router, types

router = Router()

@router.message(lambda message: message.text.lower() == 'ℹ️ о боте')
async def about_button_handler(message: types.Message):
    await message.reply(f'Бот разработал: <b>Велибеков Нариман Сабирович</b>\nУченик 11 "А" класса - "Белиджинской гимназии №1"\nСпециально для <b>УО МР "Дербентский район"</b>\n\n<b>Контакты:</b>\n📍 Адрес: Республика Дагестан, г.Дербент, ул.Буйнакского, 10.\n📧 Электронная почта: derbentruo@mail.ru\n✈️ Телеграм канал: <a href="https://t.me/uoderbrayon">Ссылка</a>', 
                         parse_mode='HTML')
    print(f"{message.from_user.full_name}: call about")