#     __  __           _         _              ____       _             _      _   
#    |  \/  | __ _  __| | ___   | |__  _   _   |  _ \ __ _| |_ _ __ ___ | | ___| |_ 
#    | |\/| |/ _` |/ _` |/ _ \  | '_ \| | | |  | |_) / _` | __| '__/ _ \| |/ _ \ __|
#    | |  | | (_| | (_| |  __/  | |_) | |_| |  |  __/ (_| | |_| | | (_) | |  __/ |_ 
#    |_|  |_|\__,_|\__,_|\___|  |_.__/ \__, |  |_|   \__,_|\__|_|  \___/|_|\___|\__|
#                                      |___/                                       

from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards import start_keyboard
from database import executor
from datetime import datetime

router = Router()

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    print(f"{message.from_user.full_name}: call start")

    await message.answer(f'Приветствуем вас, <b>{message.from_user.full_name}</b> !\nЭто бот Управления Образования МР "Дербентский район".',
                         parse_mode='HTML',
                         reply_markup=start_keyboard)
    
    executor.User.add(message.from_user.id, message.from_user.username, datetime.now().isoformat())