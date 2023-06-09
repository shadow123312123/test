from aiogram import Bot, Dispatcher, types

import logging
import os
import socket

bot = Bot("5908045764:AAGnjldKs7s0zNcNUwL3yAI6d5OcPoUvukY")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer('')


@dp.message_handler(content_types=['text'])
async def handle_coin_price(message: types.Message):
    try:
        if "ip" in message:
            await message.reply(socket.gethostbyname(socket.gethostname()))

    except ValueError:
        await message.reply(text="Not found")
