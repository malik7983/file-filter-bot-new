import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from import get_size, split_list, get_settings

async def group_filters(movielist):
    if re.findall("((^\/|^,|^!|^\.|^[\U0001F600-\U000E007F]).*)", update.text):
        return
    if 2 < len(update.text) < 100:    
        btn = []
        search = update.text
        settings = await get_settings(update.chat.id)
        MOVIE_TEXT = settings["template"]
        files = await get_filter_results(query=search)
        if not files:
            if settings["spellmode"]:
                try:
                    reply = search.replace(" ", '+')  
                    buttons = [[ InlineKeyboardButton("🔍 𝚂𝙴𝙰𝚁𝙲𝙷 𝚃𝙾 𝙶𝙾𝙾𝙶𝙻𝙴 🔎", url=f"https://www.google.com/search?q={reply}") ],[ InlineKeyboardButton("× 𝙲𝙻𝙾𝚂𝙴 ×", callback_data="close") ]]
                    spell = await update.reply_text(text=settings["spelltext"].format(query=search, first_name=update.from_user.first_name, last_name=update.from_user.last_name, title=update.chat.title, mention=update.from_user.mention), disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup(buttons))           
                    await asyncio.sleep(60)
                    await spell.delete()
                except:
                    pass
            return
