from pyrogram import Client, filters
import asyncio
from datetime import date
from config import Config
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from time import sleep
app = Client("my_account", api_id=Config.API_ID, api_hash=Config.API_HASH)
happy_birthday_days = {}

# функция
def add_dictionary(date, nikname):
    if date in happy_birthday_days:
        happy_birthday_days[date].append(nikname)
    else:
        happy_birthday_days[date] = [nikname]

def check_date():
    current_date = date.today().strftime("%m-%d")
    if current_date in happy_birthday_days:
        # TODO call def what send messages for users
        pass

@app.on_message(filters.command(['love','start', 'help']))
async def command_handler(client: Client, message: Message):
    if message.text == '/love':
        await message.reply("Привет! красавчик. я тебя люблююююю очень очень.")
    elif message.text == '/help':
        await message.reply(
            "Доступные команды:\n"
            "/start - Приветственное сообщение\n"
            "/help - Список команд\n"
            ".huck - Взлом аккаунта")
    elif message.text == '/start':
        await message.reply(
            "Приветики конфетики я личный бот Настюшки-кросотушки. я пока ничего не умею но скоро научусь. love")


@app.on_message(filters.command('huck', prefixes="."))
async def huck(client: Client, message: Message):
    # Отправляем сообщение и сохраняем объект отправленного сообщения
    reply_message = await message.reply("Инициализирую влом аккаунта.")
    await asyncio.sleep(0.3)
    perc = 0
    while perc < 100:
        try:
            text = "Взлом аккаунта в процессе ... " + str(perc)
            await reply_message.edit(text)
            perc += 2
            await asyncio.sleep(0.1)
        except FloodWait as e:
            await asyncio.sleep(e.x)
    await reply_message.edit("Успешно захвачено!")

# Асинхронная функция для запуска сервера
async def start_server():
    print('Starting server...')
    print('Server started.')

# Асинхронная функция для отправки сообщения
async def send_message():
    print('Sending message...')
    await app.send_message(chat_id='lic_nx', text="как у тебя настроение? ")
    print('Message sent.')

# Основная асинхронная функция
async def main():
    # Запуск сервера
    await start_server()

    # Отправка сообщения
    await send_message()

    # Запуск обработчиков сообщений
    # await app.idle()

# Запуск основной асинхронной функции
if __name__ == "__main__":
    app.run()
    # asyncio.run(main)
