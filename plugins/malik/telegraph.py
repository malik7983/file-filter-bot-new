import os
import shutil
from pyrogram import Client, filters
from telegraph import upload_file
from plugins.malik.extra import get_file_id, f_onw_fliter, TMP_DOWNLOAD_DIRECTORY


@Client.on_message(
    filters.command(["telegraph", "tel"]) &
    f_onw_fliter
)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply_text("ππ΄πΏπ»π ππΎ π° πΏπ·πΎππΎ πΎπ ππΈπ³π΄πΎ ππ½π³π΄π π»πΌπ±.")
        return
    file_info = get_file_id(replied)
    if not file_info:
        await message.reply_text("Not supported!")
        return
    _t = os.path.join(
        TMP_DOWNLOAD_DIRECTORY,
        str(replied.message_id)
    )
    if not os.path.isdir(_t):
        os.makedirs(_t)
    _t += "/"
    download_location = await replied.download(
        _t
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply_text(message, text=document)
    else:
        await message.reply(
            f"Link :- <code>https://telegra.ph{response[0]}</code>",
            disable_web_page_preview=True
        )
    finally:
        shutil.rmtree(
            _t,
            ignore_errors=True
        )
