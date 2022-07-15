#malik
import asyncio
from Script import script, ADDG
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
     return 
