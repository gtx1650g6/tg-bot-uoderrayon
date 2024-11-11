#     __  __           _         _              ____       _             _      _   
#    |  \/  | __ _  __| | ___   | |__  _   _   |  _ \ __ _| |_ _ __ ___ | | ___| |_ 
#    | |\/| |/ _` |/ _` |/ _ \  | '_ \| | | |  | |_) / _` | __| '__/ _ \| |/ _ \ __|
#    | |  | | (_| | (_| |  __/  | |_) | |_| |  |  __/ (_| | |_| | | (_) | |  __/ |_ 
#    |_|  |_|\__,_|\__,_|\___|  |_.__/ \__, |  |_|   \__,_|\__|_|  \___/|_|\___|\__|
#                                      |___/                                       

from aiogram import Bot, Dispatcher
import asyncio
import config
import handlers.user
import handlers.website
import handlers.order
import handlers.about

token = config.token

bot = Bot(token=token)
dp = Dispatcher()

async def main():
    
    dp.include_routers(handlers.user.router,
                       handlers.website.router,
                       handlers.order.router,
                       handlers.about.router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print(".: bot started :.")
        asyncio.run(main())
    except KeyboardInterrupt:
        print(".: bot stopped :.")