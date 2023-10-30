from aiogram import Bot, Dispatcher;
import asyncio
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime , date , timedelta, time
dp= Dispatcher()
class Expence:
   def __init__(self,name:str,price:int|str, mockdate=None):
       self.name= name.strip()
       self.price= int(price.strip())
       self.createdAt= mockdate if mockdate else datetime.now()

expences= [
    Expence('asdf', '10000', datetime.today()-timedelta(days=2))
]

@dp.message(Command("start"))
async def command_start_handler(message:Message):
    await message.answer("Greetings^^")
@dp.message(Command("new"))
async def command_new_handler(message:Message):
    name, price = (message.text.replace("/new","").split("-"))
    expences.append(Expence(name,price))
    await message.answer(f"your spending is:\n" + ';\n'.join ([f'{expence.name}-{expence.price}' for expence in expences]))


@dp.message(Command("all"))
async def command_all_handler(message:Message):
    
    await message.answer(f"Your overall spends:\n" + 
                         ';\n'.join ([f'{expence.name}-{expence.price}' for expence in expences])
                           +f"\nall: {sum([expence.price for expence in expences])}")
   
@dp.message (Command("daily"))
async def command_daily_handler(message:Message):
    await message.answer(f"Your daily spends:{sum([expence.price for expence in filter(lambda expence: datetime.combine(date.today()-timedelta(days=1), time.min)  < expence.createdAt, expences)])}")

@dp.message (Command("clear"))
async def command_clear_handler(message:Message):
    expences.clear()
    await message.answer("your data has been erased.")
    

async def main():
    bot= Bot("6935608022:AAGm6fOmDBn0lDp8aBYPi_l9bwre3ceAA-8")
    await dp.start_polling(bot)

asyncio.run(main())