#malik
import os
from info import PHT
from plugins.malik.extra import GHHMT
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
               text=(GHHMT.format(total_users)),
               reply_markup=InlineKeyboardMarkup(
                                      [[
                                        InlineKeyboardButton('💢 Request to admin 💢', url="https://t.me/m_admins"),
                                        InlineKeyboardButton('💢 Request to admin 💢', url="https://t.me/m_admins")
                                                                         
                                      ]]
               ),
               parse_mode='html'
)




STTS = """★<b>🗂𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
👨‍👩‍👧‍👧 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
🤿 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
⏳ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
⌛️ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱</b> """


GHHMT = """<b>Thanks For {}.User... 💖 

Thanks For Your Support...

𝖩𝗎𝗌𝗍 𝖠𝖽𝖽 𝖮𝗎𝗋 𝖡𝗈𝗍 𝖳𝗈 𝖸𝗈𝗎𝗋 𝖦𝗋𝗈𝗎𝗉 𝖠𝗌 𝖠𝖽𝗆𝗂𝗇, 𝖨𝗍 𝖶𝗂𝗅𝗅 𝖯𝗋𝗈𝗏𝗂𝖽𝖾 𝖬𝗈𝗏𝗂𝖾𝗌 𝖳𝗁𝖾𝗋𝖾... 😎


     ♋️ 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀 ♋️

✪ AutoFilter, Manual Filter
✪ IMDb HD Posters
✪ IMDb Real Details
✪ Two Buttons Mode
✪ Force Subscribe
✪ Extra Features: download songs, download you tube video, URL Shortner,  

⚙ More Features Adding Soon</b> 😎"""

