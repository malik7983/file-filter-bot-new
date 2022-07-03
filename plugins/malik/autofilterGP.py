import re, random, asyncio 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from info import PICS, MOVIE_TEXT as REQUEST_TEXT, FILTER_DEL_SECOND
import get_size, split_list, get_settings
from database.autofilter_mdb import get_filter_results

async def group_filters(client, update):
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
        if files:
            for file in files:
                file_id = file.file_id
                filesize = f"[{get_size(file.file_size)}]"
                filename = f"{file.file_name}"
                
                if settings["button"]:
                    try:
                        btn.append([InlineKeyboardButton(f"{filesize} {filename}", callback_data=f'luciferGP#{file_id}')])
                    except:
                        btn.append([InlineKeyboardButton(f"{filesize} {filename}", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}")])
                else:
                    try:
                        btn.append([InlineKeyboardButton(f"{filesize}", callback_data=f'luciferGP#{file_id}'),
                                    InlineKeyboardButton(f"{filename}", callback_data=f'luciferGP#{file_id}')])
                    except:
                        btn.append([InlineKeyboardButton(f"{filesize}", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}"),
                                    InlineKeyboardButton(f"{filename}", url=f"https://telegram.dog/{temp.Bot_Username}?start=muhammedrk-mo-tech-group-{file_id}")])
        else:
            return

        if not btn:
            return

        if len(btn) > temp.filterBtns: 
            btns = list(split_list(btn, temp.filterBtns)) 
            keyword = f"{update.chat.id}-{update.id}"
            temp.BUTTONS[keyword] = {
                "total" : len(btns),
                "buttons" : btns
            }
        else:
            buttons = btn
            buttons.append([InlineKeyboardButton("📃 Pages 1/1",callback_data="pages"),
                            InlineKeyboardButton("Close 🗑️", callback_data="close")])

            buttons.append([InlineKeyboardButton("🤖 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙿𝙼 🤖", url=f"https://telegram.dog/{temp.Bot_Username}?")])

            try:             
                if settings["photo"]:
                    try:
                        auto0_delete=await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                        await asyncio.sleep(FILTER_DEL_SECOND)
                        await auto0_delete.delete()
                    except Exception as error:
                        auto1_delete=await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=MOVIE_TEXT, reply_to_message_id=update.id)
                        auto2_delete=await client.send_photo(chat_id=update.chat.id, photo="https://telegra.ph/file/2602c9d464dc2b1a53e0f.jpg", caption=f"‼️‼️‼️‼️‼️‼️‼️ **🅻︎🅾︎🅶︎🆂︎**\n   ❌️ 🅴︎🆁︎🆁︎🅾︎🆁︎ **{error}**", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("✖️ 𝙲𝙻𝙾𝚂𝙴 ✖️", callback_data="close") ]] ))
                        auto3_delete=await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=REQUEST_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                        await asyncio.sleep(FILTER_DEL_SECOND)
                        await auto1_delete.delete()
                        await auto2_delete.delete()
                        await auto3_delete.delete()
                else:
                    try:
                        auto0_delete=await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                        await asyncio.sleep(FILTER_DEL_SECOND)
                        await auto0_delete.delete()
                    except Exception as error:
                        auto1_delete=await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT, reply_to_message_id=update.id)
                        auto2_delete=await client.send_message(chat_id=update.chat.id, text=f"‼️‼️‼️‼️‼️‼️‼️ **🅻︎🅾︎🅶︎🆂︎**\n   ❌️ 🅴︎🆁︎🆁︎🅾︎🆁︎ **{error}**", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("✖️ 𝙲𝙻𝙾𝚂𝙴 ✖️", callback_data="close") ]] ))
                        auto3_delete=await client.send_message(chat_id=update.chat.id, text=REQUEST_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                        await asyncio.sleep(FILTER_DEL_SECOND)
                        await auto1_delete.delete()
                        await auto2_delete.delete()
                        await auto3_delete.delete()
            except Exception as error:
                auto1_delete=await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT, reply_to_message_id=update.id)
                auto2_delete=await client.send_photo(chat_id=update.chat.id, photo="https://telegra.ph/file/2602c9d464dc2b1a53e0f.jpg", caption=f"""‼️‼️‼️‼️‼️‼️‼️ **🅻︎🅾︎🅶︎🆂︎**\n   ❌️ 🅴︎🆁︎🆁︎🅾︎🆁︎ **{error}**""", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("✖️ 𝙲𝙻𝙾𝚂𝙴 ✖️", callback_data="close") ]] ))
                auto3_delete=await client.send_message(chat_id=update.chat.id, text=REQUEST_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name=f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                await asyncio.sleep(FILTER_DEL_SECOND)
                await auto1_delete.delete()
                await auto2_delete.delete()
                await auto3_delete.delete()
            return

        data = temp.BUTTONS[keyword]
        buttons = data['buttons'][0].copy()
   
        buttons.append([InlineKeyboardButton(f"📃 1/{data['total']}",callback_data="pages"),
                        InlineKeyboardButton("🗑️", callback_data="close"),
                        InlineKeyboardButton("➡",callback_data=f"nextgroup_0_{keyword}")])

        buttons.append([InlineKeyboardButton("🤖 𝙲𝙷𝙴𝙲𝙺 𝙼𝚈 𝙿𝙼 🤖", url=f"https://telegram.dog/{temp.Bot_Username}")])

        try:             
            if settings["photo"]:
                try:
                    auto0_delete=await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                    await asyncio.sleep(FILTER_DEL_SECOND)
                    await auto0_delete.delete()
                except Exception as error:
                    auto1_delete=await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=MOVIE_TEXT, reply_to_message_id=update.id)
                    auto2_delete=await client.send_photo(chat_id=update.chat.id, photo="https://telegra.ph/file/2602c9d464dc2b1a53e0f.jpg", caption=f"‼️‼️‼️‼️‼️‼️‼️ **🅻︎🅾︎🅶︎🆂︎**\n   ❌️ 🅴︎🆁︎🆁︎🅾︎🆁︎ **{error}**", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("✖️ 𝙲𝙻𝙾𝚂𝙴 ✖️", callback_data="close") ]] ))
                    auto3_delete=await client.send_photo(chat_id=update.chat.id, photo=random.choice(PICS), caption=REQUEST_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                    await asyncio.sleep(FILTER_DEL_SECOND)
                    await auto1_delete.delete()
                    await auto2_delete.delete()
                    await auto3_delete.delete()
            else:
                try:
                    auto0_delete=await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                    await asyncio.sleep(FILTER_DEL_SECOND)
                    await auto0_delete.delete()
                except Exception as error:
                    auto1_delete=await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT, reply_to_message_id=update.id)
                    auto2_delete=await client.send_message(chat_id=update.chat.id, text=f"‼️‼️‼️‼️‼️‼️‼️ **🅻︎🅾︎🅶︎🆂︎**\n   ❌️ 🅴︎🆁︎🆁︎🅾︎🆁︎ **{error}**", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("✖️ 𝙲𝙻𝙾𝚂𝙴 ✖️", callback_data="close") ]] ))
                    auto3_delete=await client.send_message(chat_id=update.chat.id, text=REQUEST_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name = f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
                    await asyncio.sleep(FILTER_DEL_SECOND)
                    await auto1_delete.delete()
                    await auto2_delete.delete()
                    await auto3_delete.delete()
        except Exception as error:
            auto1_delete=await client.send_message(chat_id=update.chat.id, text=MOVIE_TEXT, reply_to_message_id=update.id)
            auto2_delete=await client.send_photo(chat_id=update.chat.id, photo="https://telegra.ph/file/2602c9d464dc2b1a53e0f.jpg", caption=f"""‼️‼️‼️‼️‼️‼️‼️ **🅻︎🅾︎🅶︎🆂︎**\n   ❌️ 🅴︎🆁︎🆁︎🅾︎🆁︎ **{error}**""", reply_to_message_id=update.id, reply_markup=InlineKeyboardMarkup( [[ InlineKeyboardButton("✖️ 𝙲𝙻𝙾𝚂𝙴 ✖️", callback_data="close") ]] ))
            auto3_delete=await client.send_message(chat_id=update.chat.id, text=REQUEST_TEXT.format(mention=update.from_user.mention, query=search, greeting=None, group_name=f"[{update.chat.title}](t.me/{update.chat.username})" or f"[{update.chat.title}](t.me/{update.from_user.username})"), reply_markup=InlineKeyboardMarkup(buttons), reply_to_message_id=update.id)
            await asyncio.sleep(FILTER_DEL_SECOND)
            await auto1_delete.delete()
            await auto2_delete.delete()
            await auto3_delete.delete()

@Client.on_message(filters.private & filters.command('pmautofilter'))
async def pmautofilter(client, message):        
    try:
        cmd=message.command[1] 
        if cmd == "on":   
            if message.chat.id in temp.PMAF_OFF:
                temp.PMAF_OFF.remove(message.chat.id)
                await message.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙽..!")  
            else:
                await message.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙽..!")                           
        elif cmd == "off": 
            if message.chat.id in temp.PMAF_OFF:
                await message.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙵𝙵..!")                                             
            else:
                temp.PMAF_OFF.append(message.chat.id)
                await message.reply_text("𝙿𝙼 𝙰𝚄𝚃𝙾𝙵𝙸𝙻𝚃𝙴𝚁 𝚃𝚄𝚁𝙽𝙴𝙳 𝙾𝙵𝙵..!")
        else:
            await message.reply_text("𝚄𝚂𝙴 𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝙵𝙾𝚁𝙼𝙰𝚃.!\n\n • /pmautofilter on\n • /pmautofilter off")    
    except:
        pass

