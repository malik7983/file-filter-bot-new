#malik
import os
import logging
import random
import asyncio
from Script import script, ADDG
from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, PHTT, LOG_CHANNEL, PICS, BATCH_FILE_CAPTION, CUSTOM_FILE_CAPTION, PROTECT_CONTENT
from utils import get_settings, get_size, is_subscribed, save_group_settings, temp
from database.connections_mdb import active_connection
import re
import json
import base64
@Client.on_message(filters.command("star") & filters.incoming & ~filters.edited)
async def star(client, message):
    if message.chat.type in ['group', 'supergroup']:

        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton('❇️ Add Me To Your Groups ❇️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('🖥 CHANNEL 🖥', url='https://t.me/+ZeZNvt43B4o3ZmJl'),
            InlineKeyboardButton('❗️Bot Owner❗️', callback_data='owner'),
            InlineKeyboardButton('🖥 UPDATES 🖥', url='https://t.me/m_house786')
            ],[
            InlineKeyboardButton('♻️ Help ♻️', callback_data='help'),
            InlineKeyboardButton('🌷Join my group', url='https://t.me/+gXuMKXOWm1UyOTdl'),
            InlineKeyboardButton('♻️ About ♻️', callback_data='about')
            ],[
            InlineKeyboardButton('Search', switch_inline_query_current_chat=''),
            InlineKeyboardButton('❤️ Donation ❤️', callback_data='dinette'),
            ],[
            InlineKeyboardButton('🚀 Download YouTube video 🛰', callback_data='videos')
            ],[
            InlineKeyboardButton('🔗 Url Shortner 🔗', callback_data='urlshortn')
            ],[
            InlineKeyboardButton('✅ Subscribe my YouTube channel  ✅', url='https://youtube.com/channel/UCPaHDqWf3D3w2nxb8p3sr4A')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return
