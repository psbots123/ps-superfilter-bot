import logging
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid, ChatAdminRequired, UsernameInvalid, UsernameNotModified, UserIsBlocked
from info import ADMINS, LOG_CHANNEL, INDEX_EXTENSIONS
from database.ia_filterdb import save_file
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils import temp, get_readable_time
import re, time

lock = asyncio.Lock()

@Client.on_callback_query(filters.regex(r'^index'))
async def index_files(bot, query):
    _, ident, chat, lst_msg_id, skip = query.data.split("#")
    if ident == 'yes':
        msg = query.message
        await msg.edit("ꜱᴛᴀʀᴛɪɴɢ ɪɴᴅᴇxɪɴɢ...")
        try:
            chat = int(chat)
        except:
            chat = chat
        await index_files_to_db(int(lst_msg_id), chat, msg, bot, int(skip))
    elif ident == 'cancel':
        temp.CANCEL = True
        await query.message.edit("ᴛʀʏɪɴɢ ᴛᴏ ᴄᴀɴᴄᴇʟ ɪɴᴅᴇxɪɴɢ...")


@Client.on_message(filters.command('index') & filters.private & filters.incoming & filters.user(ADMINS))
async def send_for_index(bot, message):
    if lock.locked():
        return await message.reply('ᴡᴀɪᴛ ᴜɴᴛɪʟ ᴘʀᴇᴠɪᴏᴜꜱ ᴘʀᴏᴄᴇꜱꜱ ᴄᴏᴍᴘʟᴇᴛᴇ.')
    i = await message.reply("ꜰᴏʀᴡᴀʀᴅ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ꜱᴇɴᴅ ʟᴀꜱᴛ ᴍᴇꜱꜱᴀɢᴇ ʟɪɴᴋ.")
    msg = await bot.listen(chat_id=message.chat.id, user_id=message.from_user.id)
    await i.delete()
    if msg.text and msg.text.startswith("https://t.me"):
        try:
            msg_link = msg.text.split("/")
            last_msg_id = int(msg_link[-1])
            chat_id = msg_link[-2]
            if chat_id.isnumeric():
                chat_id = int(("-100" + chat_id))
        except:
            await message.reply("ɪɴᴠᴀʟɪᴅ ᴍᴇꜱꜱᴀɢᴇ ʟɪɴᴋ")
            return
    elif msg.forward_from_chat and msg.forward_from_chat.type == enums.ChatType.CHANNEL:
        last_msg_id = msg.forward_from_message_id
        chat_id = msg.forward_from_chat.username or msg.forward_from_chat.id
    else:
        await message.reply('ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ꜰᴏʀᴡᴀʀᴅᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ᴏʀ ʟɪɴᴋ.')
        return
    try:
        chat = await bot.get_chat(chat_id)
    except Exception as e:
        return await message.reply(f'Errors - {e}')

    if chat.type != enums.ChatType.CHANNEL:
        return await message.reply("ɪ ᴄᴀɴ ɪɴᴅᴇx ᴏɴʟʏ ᴄʜᴀɴɴᴇʟꜱ.")

    s = await message.reply("ꜱᴇɴᴅ ꜱᴋɪᴘ ᴍᴇꜱꜱᴀɢᴇ ɴᴜᴍʙᴇʀ.")
    msg = await bot.listen(chat_id=message.chat.id, user_id=message.from_user.id)
    await s.delete()
    try:
        skip = int(msg.text)
    except:
        return await message.reply("ɴᴜᴍʙᴇʀ ɪꜱ ɪɴᴠᴀʟɪᴅ.")

    buttons = [[
        InlineKeyboardButton('YES', callback_data=f'index#yes#{chat_id}#{last_msg_id}#{skip}')
    ],[
        InlineKeyboardButton('CLOSE', callback_data='close_data'),
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(f'ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɪɴᴅᴇx {chat.title} channel?\nᴛᴏᴛᴀʟ ᴍᴇꜱꜱᴀɢᴇꜱ : <code>{last_msg_id}</code>', reply_markup=reply_markup)


async def index_files_to_db(lst_msg_id, chat, msg, bot, skip):
    start_time = time.time()
    total_files = 0
    duplicate = 0
    errors = 0
    deleted = 0
    no_media = 0
    unsupported = 0
    current = skip
    
    async with lock:
        try:
            async for message in bot.iter_messages(chat, lst_msg_id, skip):
                time_taken = get_readable_time(time.time()-start_time)
                if temp.CANCEL:
                    temp.CANCEL = False
                    await msg.edit(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄᴀɴᴄᴇʟʟᴇᴅ!\nᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ {time_taken}\n\nꜱᴀᴠᴇᴅ <code>{total_files}</code> ꜰɪʟᴇꜱ ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ!\nᴅᴜᴘʟɪᴄᴀᴛᴇ ꜰɪʟᴇꜱ ꜱᴋɪᴘᴘᴇᴅ : <code>{duplicate}</code>\nᴅᴇʟᴇᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ : <code>{deleted}</code>\nɴᴏɴ-ᴍᴇᴅɪᴀ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ : <code>{no_media + unsupported}</code>\nᴜɴꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ : <code>{unsupported}</code>\nᴇʀʀᴏʀꜱ ᴏᴄᴄᴜʀʀᴇᴅ : <code>{errors}</code>")
                    return
                current += 1
                if current % 30 == 0:
                    btn = [[
                        InlineKeyboardButton('CANCEL', callback_data=f'index#cancel#{chat}#{lst_msg_id}#{skip}')
                    ]]
                    await msg.edit_text(text=f"ᴛᴏᴛᴀʟ ᴍᴇꜱꜱᴀɢᴇꜱ ʀᴇᴄᴇɪᴠᴇᴅ : <code>{current}</code>\nᴛᴏᴛᴀʟ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴀᴠᴇᴅ : <code>{total_files}</code>\nᴅᴜᴘʟɪᴄᴀᴛᴇ ꜰɪʟᴇꜱ ꜱᴋɪᴘᴘᴇᴅ : <code>{duplicate}</code>\nᴅᴇʟᴇᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ : <code>{deleted}</code>\nɴᴏɴ-ᴍᴇᴅɪᴀ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ : <code>{no_media + unsupported}</code>\nᴜɴꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ : <code>{unsupported}</code>\nᴇʀʀᴏʀꜱ ᴏᴄᴄᴜʀʀᴇᴅ : <code>{errors}</code>", reply_markup=InlineKeyboardMarkup(btn))
                if message.empty:
                    deleted += 1
                    continue
                elif not message.media:
                    no_media += 1
                    continue
                elif message.media not in [enums.MessageMediaType.VIDEO, enums.MessageMediaType.DOCUMENT]:
                    unsupported += 1
                    continue
                media = getattr(message, message.media.value, None)
                if not media:
                    unsupported += 1
                    continue
                elif not (str(media.file_name).lower()).endswith(tuple(INDEX_EXTENSIONS)):
                    unsupported += 1
                    continue
                media.caption = message.caption
                sts = await save_file(media)
                if sts == 'suc':
                    total_files += 1
                elif sts == 'dup':
                    duplicate += 1
                elif sts == 'err':
                    errors += 1
        except Exception as e:
            await msg.reply(f'ɪɴᴅᴇx ᴄᴀɴᴄᴇʟᴇᴅ ᴅᴜᴇ ᴛᴏ ᴇʀʀᴏʀ - {e}')
        else:
            await msg.edit(f"ꜱᴜᴄᴄᴇꜱꜰᴜʟʟʏ ꜱᴀᴠᴇᴅ <code>{total_files}</code> ᴛᴏ ᴅᴀᴛᴀʙᴀꜱᴇ!\nᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ {time_taken}\nᴅᴜᴘʟɪᴄᴀᴛᴇ ꜰɪʟᴇꜱ ꜱᴋɪᴘᴘᴇᴅ : <code>{duplicate}</code>\nᴅᴇʟᴇᴛᴇᴅ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ : <code>{deleted}</code>\nɴᴏɴ-ᴍᴇᴅɪᴀ ᴍᴇꜱꜱᴀɢᴇꜱ ꜱᴋɪᴘᴘᴇᴅ : <code>{no_media + unsupported}</code>\nᴜɴꜱᴜᴘᴘᴏʀᴛᴇᴅ ᴍᴇᴅɪᴀ : <code>{unsupported}</code>\nᴇʀʀᴏʀꜱ ᴏᴄᴄᴜʀʀᴇᴅ : <code>{errors}</code>")
