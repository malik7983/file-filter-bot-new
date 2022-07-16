#malik
import os
from plugins.malik.extraa import GHHMT
from Script import script
from database.users_chats_db import db
from database.ia_filterdb import Media
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils import temp, get_size

@Client.on_message(filters.command("star") & filters.incoming & ~filters.edited)
async def star(client, message):
    if len(message.command):
        buttons = [[
            InlineKeyboardButton('❇️ Add Me To Your Groups ❇️', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            text=(GHHMT),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return

@Client.on_message(filters.command('malik') & filters.incoming)
async def get_ststs(bot, message):
    rju = await message.reply('Fetching stats..')
    total_users = await db.total_users_count()
    totl_chats = await db.total_chat_count()
    files = await Media.count_documents()
    size = await db.get_db_size()
    free = 536870912 - size
    size = get_size(size)
    free = get_size(free)
    await rju.edit(
               msg=(GHHMT.format(files, total_users, totl_chats, size, free)),
               reply_markup=InlineKeyboardMarkup(
                                      [[
                                        InlineKeyboardButton('💢 Request to admin 💢', url="https://t.me/m_admins"),
                                                                         
                                      ]]
               ),
               parse_mode='html'
)
