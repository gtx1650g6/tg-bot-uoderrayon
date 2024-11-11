#     __  __           _         _              ____       _             _      _   
#    |  \/  | __ _  __| | ___   | |__  _   _   |  _ \ __ _| |_ _ __ ___ | | ___| |_ 
#    | |\/| |/ _` |/ _` |/ _ \  | '_ \| | | |  | |_) / _` | __| '__/ _ \| |/ _ \ __|
#    | |  | | (_| | (_| |  __/  | |_) | |_| |  |  __/ (_| | |_| | | (_) | |  __/ |_ 
#    |_|  |_|\__,_|\__,_|\___|  |_.__/ \__, |  |_|   \__,_|\__|_|  \___/|_|\___|\__|
#                                      |___/                                       

from aiogram import Router, types

router = Router()

@router.message(lambda message: message.text.lower() == "📎 посетить наш сайт")
async def website_button_handler(message: types.Message):
    await message.reply('<b><a href="https://derbentruo.dagestanschool.ru/">Сайт УО МР "Дербентский район".</a></b>', 
                         parse_mode='HTML')
    print(f"{message.from_user.full_name}: call website")