#malik
import os
import logging
import asyncio
from Script import script, ADDG
from info import PHTT 
@Client.on_message(filters.command("star") & filters.incoming & ~filters.edited)
async def star(client, message):
    if message.chat.type in ['group', 'supergroup']:
        buttons = [
            [
                InlineKeyboardButton('❇️ Add Me To Your Groups ❇️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],
            [
                InlineKeyboardButton('♻️ Updates Channel ♻️', url='https://t.me/m_house786'),
                InlineKeyboardButton('❇️ Help ❇️', url=f"https://t.me/{temp.U_NAME}?start=help")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_video(
        video=(PHTT),
        caption=(ADDG.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME)),
        reply_markup=reply_markup)
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
