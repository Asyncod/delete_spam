# -*- coding: utf-8 -*-
import re

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types, executor, filters
from loguru import logger
from sys import stderr

#### LOGGER MOMENT ####
logger.remove()
logger.add(stderr, format="<white>{time:HH:mm:ss}</white>"
                          " | <level>{level: <8}</level>"
                          " - <white>{message}</white>")

# #### NEED BASE ####
# base.create_db(data="channel")

#### PARAMETRS BOT'S ####
bot = Bot("токен", parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())


#### START HANDLER ####
@dp.message_handler(commands=["start"], state="*")
async def start_message(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="<b>🙋 Хеллоу всем нашим</b>\n\n"
                                "С этим ботом можно забыть о барабанной дроби и даунах, которые спамят своей ахуенно нужной хуйней по комментам\n\n"
                                "Добавьте этого бота в чат и он будет удалять сообщения по этим правилам:\n\n"
                                "1️⃣ Если кинута ссылка: <code>https://, http://, t.me или @</code>\n\n"
                                "2️⃣ Эти ссылки удаляются только в том случае, если человек не находится в чате")


@dp.message_handler(content_types=['text'])
async def catch_message(message: types.Message):
    if "работаешь?" in message.text.lower():
        await message.reply(text="Так точно! Ебашу на благо Отечества 🫡")

    elif "о горе" in message.text.lower():
        await message.reply(text="о горе")

    elif "да" in message.text.lower():
        await message.reply(text="пизда")

    elif "нет" in message.text.lower():
        await message.reply(text="тише малой")

    else:
        status = await bot.get_chat_member(chat_id=message.chat.id,
                                           user_id=message.from_user.id)

        ban_flag = re.search(pattern=r'(http(s?)|t.me|@)', string=message.text)
        resend_flag = not message.from_user.first_name == "Telegram"

        if status.status == "left" and ban_flag and resend_flag:
            await bot.delete_message(chat_id=message.chat.id,
                                     message_id=message.message_id)


@dp.message_handler(content_types=['new_chat_members'])
async def add_to_chat(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text="<b>HELLO CHAT!!!!!!</b>\n\n"
                                "Я пришел сюда, чтобы банить всяких гадов\n\n"
                                "Для этого выдайте мне права администратора *(для удаления сообщений)")


#### BOT'S POLLING ####
if __name__ == '__main__':
    logger.success("TG bot work")
    executor.start_polling(dp)
