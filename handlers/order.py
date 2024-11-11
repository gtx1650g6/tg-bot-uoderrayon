#     __  __           _         _              ____       _             _      _   
#    |  \/  | __ _  __| | ___   | |__  _   _   |  _ \ __ _| |_ _ __ ___ | | ___| |_ 
#    | |\/| |/ _` |/ _` |/ _ \  | '_ \| | | |  | |_) / _` | __| '__/ _ \| |/ _ \ __|
#    | |  | | (_| | (_| |  __/  | |_) | |_| |  |  __/ (_| | |_| | | (_) | |  __/ |_ 
#    |_|  |_|\__,_|\__,_|\___|  |_.__/ \__, |  |_|   \__,_|\__|_|  \___/|_|\___|\__|
#                                      |___/                                       

from aiogram import Router, types
import config
import keyboards


router = Router()

@router.message(lambda message: message.text.lower() == '📁 подать заявку "шаг в будущее"')
async def order_button_handler(message: types.Message):
    
    if config.isActiveFuture == False:
        await message.reply('<b>Проведение конкурса было завершено. ⚠️\nОжидайте следующей волны подачи заявок!</b>', 
                             parse_mode='HTML')
        return
    
    await message.reply('<b>Для подачи заявки, кандидату необходимо выполнить следующее:</b>\n\n· Зайти на <a href="https://drive.google.com/drive/my-drive?hl=ru">гугл диск</a>\n· Войти под своим гугл аккаунтом\n· Нажать на значок плюсика или кнопку загрузить файл\n· Добавить свой файл .doc / .docx (Научно-исследовательскую работу)\n· Нажать "Настроить доступ" / "Поделиться"\n· Поменять "Доступ ограничен" на "Все, у кого есть ссылка"\n\n<b>Данную ссылку предоставить по кнопке ниже</b> ⬇️', 
                         parse_mode='HTML',
                         reply_markup=keyboards.order_keyboard)
    print(f"{message.from_user.full_name}: call order")
