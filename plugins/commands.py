import os
import logging
import random, string
import asyncio
import time
import datetime
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait, ButtonDataInvalid
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id, delete_files
from database.users_chats_db import db
from info import PM_DELETE, PRE_IMG, INDEX_CHANNELS, ADMINS, IS_VERIFY, VERIFY_TUTORIAL, VERIFY_EXPIRE, TUTORIAL, SHORTLINK_API, SHORTLINK_URL, AUTH_CHANNEL, DELETE_TIME, SUPPORT_LINK, UPDATES_LINK, LOG_CHANNEL, PICS, PROTECT_CONTENT, IS_STREAM, IS_FSUB, PAYMENT_QR, REQST_CHANNEL, SUPPORT_CHAT_ID
from utils import get_settings, get_size, is_subscribed, is_check_admin, get_shortlink, get_verify_status, update_verify_status, save_group_settings, temp, get_readable_time, get_wish, get_seconds
import re
import json
import base64
import sys
from shortzy import Shortzy
from telegraph import upload_file

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    botid = client.me.id
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        if not await db.get_chat(message.chat.id):
            total = await client.get_chat_members_count(message.chat.id)
            username = f'@{message.chat.username}' if message.chat.username else 'Private'
            await client.send_message(LOG_CHANNEL, script.NEW_GROUP_TXT.format(message.chat.title, message.chat.id, username, total))       
            await db.add_chat(message.chat.id, message.chat.title)
        wish = get_wish()
        btn = [[
            InlineKeyboardButton('⚡️ ᴜᴘᴅᴀᴛᴇs ⚡️', url=UPDATES_LINK),
            InlineKeyboardButton('💡 ꜱᴜᴘᴘᴏʀᴛ 💡', url=SUPPORT_LINK)
        ]]
        await message.reply(text=f"<b>ʜᴇʏ {message.from_user.mention}, <i>{wish}</i>\nʜᴏᴡ ᴄᴀɴ ɪ ʜᴇʟᴘ ʏᴏᴜ??</b>", reply_markup=InlineKeyboardMarkup(btn))
        return 
        
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.NEW_USER_TXT.format(message.from_user.mention, message.from_user.id))

    verify_status = await get_verify_status(message.from_user.id)
    if verify_status['is_verified'] and VERIFY_EXPIRE < (time.time() - verify_status['verified_time']):
        await update_verify_status(message.from_user.id, is_verified=False)
    
    if (len(message.command) != 2) or (len(message.command) == 2 and message.command[1] == 'start'):
        buttons = [[
            InlineKeyboardButton("+ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ +", url=f'http://t.me/{temp.U_NAME}?startgroup=start')
        ],[
            InlineKeyboardButton('👨‍💻 ᴏᴡɴᴇʀ', callback_data='my_owner')
        ],[   
            InlineKeyboardButton('✨ ᴜᴘᴅᴀᴛᴇs ✨', url=UPDATES_LINK),
            InlineKeyboardButton('💡 ꜱᴜᴘᴘᴏʀᴛ 💡', url=SUPPORT_LINK)
        ],[
            InlineKeyboardButton('💠 ʜᴇʟᴘ 💠', callback_data='help'),
            InlineKeyboardButton('♻️  ᴀʙᴏᴜᴛ  ♻️', callback_data='my_about'),
        ],[
            InlineKeyboardButton('💰 ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ʙᴏᴛ 💰', callback_data='earn')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, get_wish()),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return

    mc = message.command[1]

    if mc.startswith('verify'):
        _, token = mc.split("_", 1)
        verify_status = await get_verify_status(message.from_user.id)
        if verify_status['verify_token'] != token:
            return await message.reply("ʏᴏᴜʀ ᴠᴇʀɪꜰʏ ᴛᴏᴋᴇɴ ɪꜱ ɪɴᴠᴀʟɪᴅ.")
        await update_verify_status(message.from_user.id, is_verified=True, verified_time=time.time())
        if verify_status["link"] == "":
            reply_markup = None
        else:
            btn = [[
                InlineKeyboardButton("📂 ɢᴇᴛ ꜰɪʟᴇ 📂", url=f'https://t.me/{temp.U_NAME}?start={verify_status["link"]}')
            ]]
            reply_markup = InlineKeyboardMarkup(btn)
        await message.reply(f"✅ ʏᴏᴜ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴠᴇʀɪꜰɪᴇᴅ ᴜɴᴛɪʟ : {get_readable_time(VERIFY_EXPIRE)}", reply_markup=reply_markup, protect_content=True)
        return
    
    verify_status = await get_verify_status(message.from_user.id)
    if not await db.has_premium_access(message.from_user.id):
        if IS_VERIFY and not verify_status['is_verified']:
            token = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
            await update_verify_status(message.from_user.id, verify_token=token, link="" if mc == 'inline_verify' else mc)
            link = await get_shortlink(SHORTLINK_URL, SHORTLINK_API, f'https://t.me/{temp.U_NAME}?start=verify_{token}')
            btn = [[
                InlineKeyboardButton("🧿 ᴠᴇʀɪꜰʏ 🧿", url=link)
            ],[
                InlineKeyboardButton('🗳 ᴛᴜᴛᴏʀɪᴀʟ 🗳', url=VERIFY_TUTORIAL)
            ]]
            await message.reply("ʏᴏᴜ ɴᴏᴛ ᴠᴇʀɪꜰɪᴇᴅ ᴛᴏᴅᴀʏ! ᴋɪɴᴅʟʏ ᴠᴇʀɪꜰʏ ɴᴏᴡ. 🔐", reply_markup=InlineKeyboardMarkup(btn), protect_content=True)
            return
    else:
        pass

    settings = await get_settings(int(mc.split("_", 2)[1]))
    if settings.get('is_fsub', IS_FSUB):
        btn = await is_subscribed(client, message, settings['fsub'])
        if btn:
            btn.append(
                [InlineKeyboardButton("🔁 ᴛʀʏ ᴀɢᴀɪɴ 🔁", callback_data=f"checksub#{mc}")]
            )
            reply_markup = InlineKeyboardMarkup(btn)
            await message.reply_photo(
                photo=random.choice(PICS),
                caption=f"👋 ʜᴇʟʟᴏ {message.from_user.mention},\n\nᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ᴍʏ 'ᴜᴘᴅᴀᴛᴇꜱ ᴄʜᴀɴɴᴇʟ' ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ. 😇",
                reply_markup=reply_markup,
                parse_mode=enums.ParseMode.HTML
            )
            return 
        
    if mc.startswith('all'):
        _, grp_id, key = mc.split("_", 2)
        files = temp.FILES.get(key)
        if not files:
            return await message.reply('⚠️ ɴᴏ ꜱᴜᴄʜ ᴀʟʟ ꜰɪʟᴇꜱ ᴇxɪꜱᴛ!')
        settings = await get_settings(int(grp_id))
        filesarr = []
        for file in files:
            CAPTION = settings['caption']
            f_caption = CAPTION.format(
                file_name = file.file_name,
                file_size = get_size(file.file_size),
                file_caption=file.caption
            )   
            if settings.get('is_stream', IS_STREAM):
                btn = [[
                    InlineKeyboardButton("✛ ᴡᴀᴛᴄʜ & ᴅᴏᴡɴʟᴏᴀᴅ ✛", callback_data=f"stream#{file.file_id}")
                ],[
                    InlineKeyboardButton('⁉️ ᴄʟᴏsᴇ ⁉️', callback_data='close_data')
                ]]
            else:
                btn = [[
                    InlineKeyboardButton('⁉️ ᴄʟᴏsᴇ ⁉️', callback_data='close_data')
                ]]
            msg = await client.send_cached_media(
                chat_id=message.from_user.id,
                file_id=file.file_id,
                caption=f_caption,
                protect_content=settings['file_secure'],
                reply_markup=InlineKeyboardMarkup(btn)
            )
            filesarr.append(msg)
        k = await client.send_message(chat_id = message.from_user.id, text=f"<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nᴛʜɪꜱ ᴍᴏᴠɪᴇ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ<b><u>{get_readable_time(PM_DELETE)}</u> 🫥 <i></b>(ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ)</i>.\n\n<b><i>ᴘʟᴇᴀꜱᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ꜰɪʟᴇ ᴛᴏ ꜱᴏᴍᴇᴡʜᴇʀᴇ ᴇʟꜱᴇ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇʀᴇ</i></b>")
        await asyncio.sleep(PM_DELETE)
        for x in filesarr:
            await x.delete()
        await k.edit_text("<b>ʏᴏᴜʀ ᴀʟʟ ᴠɪᴅᴇᴏꜱ/ꜰɪʟᴇꜱ ᴀʀᴇ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !\nᴋɪɴᴅʟʏ ꜱᴇᴀʀᴄʜ ᴀɢᴀɪɴ</b>")   
        return

    type_, grp_id, file_id = mc.split("_", 2)
    files_ = await get_file_details(file_id)
    if not files_:
        return await message.reply('⚠️ ɴᴏ ꜱᴜᴄʜ ᴀʟʟ ꜰɪʟᴇꜱ ᴇxɪꜱᴛ!')
    files = files_[0]
    settings = await get_settings(int(grp_id))
    if type_ != 'shortlink' and settings['shortlink']:
        if not await db.has_premium_access(message.from_user.id):
            link = await get_shortlink(settings['url'], settings['api'], f"https://t.me/{temp.U_NAME}?start=shortlink_{grp_id}_{file_id}")
            btn = [[
                InlineKeyboardButton("📂 ɢᴇᴛ ꜰɪʟᴇ 📂", url=link)
            ],[
                InlineKeyboardButton("📍 ʜᴏᴡ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋ 📍", url=settings['tutorial'])
            ]]
            await message.reply(f"[{get_size(files.file_size)}] {files.file_name}\n\nʏᴏᴜʀ ꜰɪʟᴇ ɪꜱ ʀᴇᴀᴅʏ, ᴘʟᴇᴀꜱᴇ ɢᴇᴛ ᴜꜱɪɴɢ ᴛʜɪꜱ ʟɪɴᴋ. 👍", reply_markup=InlineKeyboardMarkup(btn), protect_content=True)
            return
    else:
        pass
        
    CAPTION = settings['caption']
    f_caption = CAPTION.format(
        file_name = files.file_name,
        file_size = get_size(files.file_size),
        file_caption=files.caption
    )
    if settings.get('is_stream', IS_STREAM):
        btn = [[
            InlineKeyboardButton("✛ ᴡᴀᴛᴄʜ & ᴅᴏᴡɴʟᴏᴀᴅ ✛", callback_data=f"stream#{file_id}")
        ],[
            InlineKeyboardButton('⁉️ ᴄʟᴏsᴇ ⁉️', callback_data='close_data')
        ]]
    else:
        btn = [[
            InlineKeyboardButton('⁉️ ᴄʟᴏsᴇ ⁉️', callback_data='close_data')
        ]]
    msg = await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        protect_content=settings['file_secure'],
        reply_markup=InlineKeyboardMarkup(btn)
    )
    k = await client.send_message(chat_id = message.from_user.id, text=f"<b><u>❗️❗️❗️IMPORTANT❗️️❗️❗️</u></b>\n\nᴛʜɪꜱ ᴍᴏᴠɪᴇ ꜰɪʟᴇ/ᴠɪᴅᴇᴏ ᴡɪʟʟ ʙᴇ ᴅᴇʟᴇᴛᴇᴅ ɪɴ<b><u>{get_readable_time(PM_DELETE)}</u> 🫥 <i></b>(ᴅᴜᴇ ᴛᴏ ᴄᴏᴘʏʀɪɢʜᴛ ɪꜱꜱᴜᴇꜱ)</i>.\n\n<b><i>ᴘʟᴇᴀꜱᴇ ꜰᴏʀᴡᴀʀᴅ ᴛʜɪꜱ ꜰɪʟᴇ ᴛᴏ ꜱᴏᴍᴇᴡʜᴇʀᴇ ᴇʟꜱᴇ ᴀɴᴅ ꜱᴛᴀʀᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ᴛʜᴇʀᴇ</i></b>")
    await asyncio.sleep(PM_DELETE)
    await msg.delete()
    await k.edit_text("<b>ʏᴏᴜʀ ᴀʟʟ ᴠɪᴅᴇᴏꜱ/ꜰɪʟᴇꜱ ᴀʀᴇ ᴅᴇʟᴇᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ !\nᴋɪɴᴅʟʏ ꜱᴇᴀʀᴄʜ ᴀɢᴀɪɴ</b>")

@Client.on_message(filters.command('index_channels') & filters.user(ADMINS))
async def channels_info(bot, message):
    """Send basic information of index channels"""
    ids = INDEX_CHANNELS
    if not ids:
        return await message.reply("ɴᴏᴛ ꜱᴇᴛ INDEX_CHANNELS")

    text = '**ɪɴᴅᴇxᴇᴅ ᴄʜᴀɴɴᴇʟꜱ :**\n\n'
    for id in ids:
        chat = await bot.get_chat(id)
        text += f'{chat.title}\n'
    text += f'\n**Total:** {len(ids)}'
    await message.reply(text)

@Client.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot, message):
    msg = await message.reply('ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ...')
    files = await Media.count_documents()
    users = await db.total_users_count()
    chats = await db.total_chat_count()
    u_size = get_size(await db.get_db_size())
    f_size = get_size(536870912 - await db.get_db_size())
    uptime = get_readable_time(time.time() - temp.START_TIME)
    await msg.edit(script.STATUS_TXT.format(files, users, chats, u_size, f_size, uptime))    
    
@Client.on_message(filters.command('settings'))
async def settings(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.")
    grp_id = message.chat.id
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('ʏᴏᴜ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.')
    settings = await get_settings(grp_id)
    if settings is not None:
        buttons = [[
            InlineKeyboardButton('ᴀᴜᴛᴏ ꜰɪʟᴛᴇʀ', callback_data=f'setgs#auto_filter#{settings["auto_filter"]}#{grp_id}'),
            InlineKeyboardButton('ᴇɴᴀʙʟᴇᴅ' if settings["auto_filter"] else 'ᴅɪꜱᴀʙʟᴇᴅ', callback_data=f'setgs#auto_filter#{settings["auto_filter"]}#{grp_id}')
        ],[
            InlineKeyboardButton('ꜰɪʟᴇ ꜱᴇᴄᴜʀᴇ', callback_data=f'setgs#file_secure#{settings["file_secure"]}#{grp_id}'),
            InlineKeyboardButton('ᴇɴᴀʙʟᴇᴅ' if settings["file_secure"] else 'ᴅɪꜱᴀʙʟᴇᴅ', callback_data=f'setgs#file_secure#{settings["file_secure"]}#{grp_id}')
        ],[
            InlineKeyboardButton('ɪᴍᴅʙ ᴘᴏꜱᴛᴇʀ', callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}'),
            InlineKeyboardButton('ᴇɴᴀʙʟᴇᴅ' if settings["imdb"] else 'ᴅɪꜱᴀʙʟᴇᴅ', callback_data=f'setgs#imdb#{settings["imdb"]}#{grp_id}')
        ],[
            InlineKeyboardButton('ꜱᴘᴇʟʟɪɴɢ ᴄʜᴇᴄᴋ', callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}'),
            InlineKeyboardButton('ᴇɴᴀʙʟᴇᴅ' if settings["spell_check"] else 'ᴅɪꜱᴀʙʟᴇᴅ', callback_data=f'setgs#spell_check#{settings["spell_check"]}#{grp_id}')
        ],[
            InlineKeyboardButton('ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ', callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{grp_id}'),
            InlineKeyboardButton(f'{get_readable_time(DELETE_TIME)}' if settings["auto_delete"] else '📴 ᴏꜰꜰ', callback_data=f'setgs#auto_delete#{settings["auto_delete"]}#{grp_id}')
        ],[
            InlineKeyboardButton('ꜱᴇᴛ ᴡᴇʟᴄᴏᴍᴇ', callback_data=f'setgs#welcome#{settings["welcome"]}#{grp_id}',),
            InlineKeyboardButton('ᴇɴᴀʙʟᴇᴅ' if settings["welcome"] else 'ᴅɪꜱᴀʙʟᴇᴅ', callback_data=f'setgs#welcome#{settings["welcome"]}#{grp_id}'),
        ],[
            InlineKeyboardButton('ꜱʜᴏʀᴛʟɪɴᴋ', callback_data=f'setgs#shortlink#{settings["shortlink"]}#{grp_id}'),
            InlineKeyboardButton('ᴇɴᴀʙʟᴇᴅ' if settings["shortlink"] else 'ᴅɪꜱᴀʙʟᴇᴅ', callback_data=f'setgs#shortlink#{settings["shortlink"]}#{grp_id}'),
        ],[
            InlineKeyboardButton('ʀᴇꜱᴜʟᴛ ᴘᴀɢᴇ', callback_data=f'setgs#links#{settings["links"]}#{str(grp_id)}'),
            InlineKeyboardButton('⛓ ʟɪɴᴋ' if settings["links"] else '✨ ʙᴜᴛᴛᴏɴ', callback_data=f'setgs#links#{settings["links"]}#{str(grp_id)}')
        ],[
            InlineKeyboardButton('ꜰᴏʀᴄᴇ ꜱᴜʙ', callback_data=f'setgs#is_fsub#{settings.get("is_fsub", IS_FSUB)}#{str(grp_id)}'),
            InlineKeyboardButton('✨ ᴏɴ' if settings.get("is_fsub", IS_FSUB) else '📴 ᴏꜰꜰ', callback_data=f'setgs#is_fsub#{settings.get("is_fsub", IS_FSUB)}#{str(grp_id)}')
        ],[
            InlineKeyboardButton('ɪꜱ ꜱᴛʀᴇᴀᴍ', callback_data=f'setgs#is_stream#{settings.get("is_stream", IS_STREAM)}#{str(grp_id)}'),
            InlineKeyboardButton('✨ ᴏɴ' if settings.get("is_stream", IS_STREAM) else '📴 ᴏꜰꜰ', callback_data=f'setgs#is_stream#{settings.get("is_stream", IS_STREAM)}#{str(grp_id)}')
        ],[
            InlineKeyboardButton('❌ ᴄʟᴏꜱᴇ ❌', callback_data='close_data')
        ]]
        await message.reply_text(
            text=f"ᴄʜᴀɴɢᴇ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢꜱ ꜰᴏʀ <b>'{message.chat.title}'</b> ᴀꜱ ʏᴏᴜ ᴘʟᴇᴀꜱᴇ. ⚙",
            reply_markup=InlineKeyboardMarkup(buttons),
            parse_mode=enums.ParseMode.HTML
        )
    else:
        await message.reply_text('ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ!')

@Client.on_message(filters.command('set_template'))
async def save_template(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b> ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.")      
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('ʏᴏᴜ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.')
    try:
        template = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ!")   
    await save_group_settings(grp_id, 'template', template)
    await message.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴛᴇᴍᴘʟᴀᴛᴇ ꜰᴏʀ {title} to\n\n{template}")  
    
@Client.on_message(filters.command('set_caption'))
async def save_caption(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.")      
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('ʏᴏᴜ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.')
    try:
        caption = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ !") 
    await save_group_settings(grp_id, 'caption', caption)
    await message.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴄᴀᴘᴛɪᴏɴ ꜰᴏʀ {title} to\n\n{caption}")
        
@Client.on_message(filters.command('set_shortlink'))
async def save_shortlink(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.")    
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('ʏᴏᴜ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.')
    try:
        _, url, api = message.text.split(" ", 2)
    except:
        return await message.reply_text("<b>ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ:-\n\nɢɪᴠᴇ ᴍᴇ ᴀ ꜱʜᴏʀᴛʟɪɴᴋ & ᴀᴘɪ ᴀʟᴏɴɢ ᴡɪᴛʜ ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅ...\n\nEx:- <code>/shortlink api.shareus.io 3jYRIxHEl9b0AgGd5cauMww08mO2</code>")   
    try:
        await get_shortlink(url, api, f'https://t.me/{temp.U_NAME}')
    except:
        return await message.reply_text("ʏᴏᴜʀ ꜱʜᴏʀᴛʟɪɴᴋ ᴀᴘɪ ᴏʀ ᴜʀʟ ɪɴᴠᴀʟɪᴅ, ᴘʟᴇᴀꜱᴇ ᴄʜᴇᴄᴋ ᴀɢᴀɪɴ !")   
    await save_group_settings(grp_id, 'url', url)
    await save_group_settings(grp_id, 'api', api)
    await message.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ꜱʜᴏʀᴛʟɪɴᴋ ꜰᴏʀ {title} to\n\nᴜʀʟ - {url}\nᴀᴘɪ - {api}")
    
@Client.on_message(filters.command('get_custom_settings'))
async def get_custom_settings(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.")
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('ʏᴏᴜ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ...')    
    settings = await get_settings(grp_id)
    text = f"""ᴄᴜꜱᴛᴏᴍ ꜱᴇᴛᴛɪɴɢꜱ ꜰᴏʀ : {title}

ꜱʜᴏʀᴛʟɪɴᴋ ᴜʀʟ : {settings["url"]}
ꜱʜᴏʀᴛʟɪɴᴋ ᴀᴘɪ : {settings["api"]}

ɪᴍᴅʙ ᴛᴇᴍᴘʟᴀᴛᴇ : {settings['template']}

ꜰɪʟᴇ ᴄᴀᴘᴛɪᴏɴ : {settings['caption']}

ᴡᴇʟᴄᴏᴍᴇ ᴛᴇxᴛ : {settings['welcome_text']}

ᴛᴜᴛᴏʀɪᴀʟ ʟɪɴᴋ : {settings['tutorial']}

ꜰᴏʀᴄᴇ ᴄʜᴀɴɴᴇʟꜱ : {str(settings['fsub'])[1:-1] if settings['fsub'] else 'ɴᴏᴛ ꜱᴇᴛ'}"""

    btn = [[
        InlineKeyboardButton(text="ᴄʟᴏꜱᴇ", callback_data="close_data")
    ]]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(btn), disable_web_page_preview=True)

@Client.on_message(filters.command('set_welcome'))
async def save_welcome(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.")      
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('ʏᴏᴜ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.')
    try:
        welcome = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ !")    
    await save_group_settings(grp_id, 'welcome_text', welcome)
    await message.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴡᴇʟᴄᴏᴍᴇ ꜰᴏʀ {title} ᴛᴏ\n\n{welcome}")
    
@Client.on_message((filters.command(["request", "Request"]) | filters.regex("#request") | filters.regex("#Request")) & filters.group)
async def requests(bot, message):
    if REQST_CHANNEL is None or SUPPORT_CHAT_ID is None: return # Must add REQST_CHANNEL and SUPPORT_CHAT_ID to use this feature
    if message.reply_to_message and SUPPORT_CHAT_ID == message.chat.id:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        success = True
        content = message.reply_to_message.text
        try:
            if REQST_CHANNEL is not None:
                btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.reply_to_message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                reported_post = await bot.send_message(chat_id=REQST_CHANNEL, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n©️ 𝙏𝙃𝙀 𝙋𝙎 𝘽𝙊𝙏𝙎™</b>", reply_markup=InlineKeyboardMarkup(btn))
                success = True
            elif len(content) >= 3:
                for admin in ADMINS:
                    btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.reply_to_message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                    reported_post = await bot.send_message(chat_id=admin, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n©️ 𝙏𝙃𝙀 𝙋𝙎 𝘽𝙊𝙏𝙎™</b>", reply_markup=InlineKeyboardMarkup(btn))
                    success = True
            else:
                if len(content) < 3:
                    await message.reply_text("<b>ʏᴏᴜ ᴍᴜꜱᴛ ᴛʏᴘᴇ ᴀʙᴏᴜᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ [ᴍɪɴɪᴍᴜᴍ 3 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ]. ʀᴇǫᴜᴇꜱᴛꜱ ᴄᴀɴ'ᴛ ʙᴇ ᴇᴍᴘᴛʏ.</b>")
            if len(content) < 3:
                success = False
        except Exception as e:
            await message.reply_text(f"Error: {e}")
            pass
        
    elif SUPPORT_CHAT_ID == message.chat.id:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        success = True
        content = message.text
        keywords = ["#request", "/request", "#Request", "/Request"]
        for keyword in keywords:
            if keyword in content:
                content = content.replace(keyword, "")
        try:
            if REQST_CHANNEL is not None and len(content) >= 3:
                btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                reported_post = await bot.send_message(chat_id=REQST_CHANNEL, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n©️ 𝙏𝙃𝙀 𝙋𝙎 𝘽𝙊𝙏𝙎™</b>", reply_markup=InlineKeyboardMarkup(btn))
                success = True
            elif len(content) >= 3:
                for admin in ADMINS:
                    btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                    reported_post = await bot.send_message(chat_id=admin, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n©️ 𝙏𝙃𝙀 𝙋𝙎 𝘽𝙊𝙏𝙎™</b>", reply_markup=InlineKeyboardMarkup(btn))
                    success = True
            else:
                if len(content) < 3:
                    await message.reply_text("<b>ʏᴏᴜ ᴍᴜꜱᴛ ᴛʏᴘᴇ ᴀʙᴏᴜᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ [ᴍɪɴɪᴍᴜᴍ 3 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ]. ʀᴇǫᴜᴇꜱᴛꜱ ᴄᴀɴ'ᴛ ʙᴇ ᴇᴍᴘᴛʏ.</b>")
            if len(content) < 3:
                success = False
        except Exception as e:
            await message.reply_text(f"Error: {e}")
            pass
     
    elif SUPPORT_CHAT_ID == message.chat.id:
        chat_id = message.chat.id
        reporter = str(message.from_user.id)
        mention = message.from_user.mention
        success = True
        content = message.text
        keywords = ["#request", "/request", "#Request", "/Request"]
        for keyword in keywords:
            if keyword in content:
                content = content.replace(keyword, "")
        try:
            if REQST_CHANNEL is not None and len(content) >= 3:
                btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                reported_post = await bot.send_message(chat_id=REQST_CHANNEL, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n©️ 𝙏𝙃𝙀 𝙋𝙎 𝘽𝙊𝙏𝙎™</b>", reply_markup=InlineKeyboardMarkup(btn))
                success = True
            elif len(content) >= 3:
                for admin in ADMINS:
                    btn = [[
                        InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{message.link}"),
                        InlineKeyboardButton('ꜱʜᴏᴡ ᴏᴘᴛɪᴏɴꜱ', callback_data=f'show_option#{reporter}')
                      ]]
                    reported_post = await bot.send_message(chat_id=admin, text=f"<b>📝 ʀᴇǫᴜᴇꜱᴛ : <u>{content}</u>\n\n📚 ʀᴇᴘᴏʀᴛᴇᴅ ʙʏ : {mention}\n📖 ʀᴇᴘᴏʀᴛᴇʀ ɪᴅ : {reporter}\n\n©️ 𝙏𝙃𝙀 𝙋𝙎 𝘽𝙊𝙏𝙎™</b>", reply_markup=InlineKeyboardMarkup(btn))
                    success = True
            else:
                if len(content) < 3:
                    await message.reply_text("<b>ʏᴏᴜ ᴍᴜꜱᴛ ᴛʏᴘᴇ ᴀʙᴏᴜᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ [ᴍɪɴɪᴍᴜᴍ 3 ᴄʜᴀʀᴀᴄᴛᴇʀꜱ]. ʀᴇǫᴜᴇꜱᴛꜱ ᴄᴀɴ'ᴛ ʙᴇ ᴇᴍᴘᴛʏ.</b>")
            if len(content) < 3:
                success = False
        except Exception as e:
            await message.reply_text(f"Error: {e}")
            pass

    else:
        success = False
    
    if success:
        '''if isinstance(REQST_CHANNEL, (int, str)):
            channels = [REQST_CHANNEL]
        elif isinstance(REQST_CHANNEL, list):
            channels = REQST_CHANNEL
        for channel in channels:
            chat = await bot.get_chat(channel)
        #chat = int(chat)'''
        link = await bot.create_chat_invite_link(int(REQST_CHANNEL))
        btn = [[
                InlineKeyboardButton('ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ', url=link.invite_link),
                InlineKeyboardButton('ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ', url=f"{reported_post.link}")
              ]]
        await message.reply_text("<b>ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛ ʜᴀꜱ ʙᴇᴇɴ ᴀᴅᴅᴇᴅ! ᴘʟᴇᴀꜱᴇ ᴡᴀɪᴛ ꜰᴏʀ ꜱᴏᴍᴇ ᴛɪᴍᴇ.\n\nᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ꜰɪʀꜱᴛ & ᴠɪᴇᴡ ʀᴇǫᴜᴇꜱᴛ.</b>", reply_markup=InlineKeyboardMarkup(btn))
        
        
@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete_file(bot, message):
    try:
        query = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ!\nᴜꜱᴀɢᴇ : /delete query")
    msg = await message.reply_text('ꜱᴇᴀʀᴄʜɪɴɢ...')
    total, files = await delete_files(query)
    if int(total) == 0:
        return await msg.edit('ɴᴏᴛ ʜᴀᴠᴇ ꜰɪʟᴇꜱ ɪɴ ʏᴏᴜʀ Qᴜᴇʀʏ')
    btn = [[
        InlineKeyboardButton("ʏᴇꜱ", callback_data=f"delete_{query}")
    ],[
        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close_data")
    ]]
    await msg.edit(f"ᴛᴏᴛᴀʟ {total} ꜰɪʟᴇꜱ ꜰᴏᴜɴᴅ ɪɴ ʏᴏᴜʀ Qᴜᴇʀʏ {query}.\n\nᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ?", reply_markup=InlineKeyboardMarkup(btn))
 
@Client.on_message(filters.command('delete_all') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    btn = [[
        InlineKeyboardButton(text="ʏᴇꜱ", callback_data="delete_all")
    ],[
        InlineKeyboardButton(text="ᴄʟᴏꜱᴇ", callback_data="close_data")
    ]]
    files = await Media.count_documents()
    if int(files) == 0:
        return await message.reply_text('ɴᴏᴛ ʜᴀᴠᴇ ꜰɪʟᴇꜱ ᴛᴏ ᴅᴇʟᴇᴛᴇ')
    await message.reply_text(f'ᴛᴏᴛᴀʟ {files} ꜰɪʟᴇꜱ ʜᴀᴠᴇ.\nᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ?', reply_markup=InlineKeyboardMarkup(btn))

@Client.on_message(filters.command('set_tutorial'))
async def set_tutorial(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.")       
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('ʏᴏᴜ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ')
    try:
        tutorial = message.text.split(" ", 1)[1]
    except:
        return await message.reply_text("ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ !")   
    await save_group_settings(grp_id, 'tutorial', tutorial)
    await message.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴄʜᴀɴɢᴇᴅ ᴛᴜᴛᴏʀɪᴀʟ ꜰᴏʀ {title} ᴛᴏ\n\n{tutorial}")

@Client.on_message(filters.command('set_fsub'))
async def set_fsub(client, message):
    userid = message.from_user.id if message.from_user else None
    if not userid:
        return await message.reply("<b>ʏᴏᴜ ᴀʀᴇ ᴀɴᴏɴʏᴍᴏᴜꜱ ᴀᴅᴍɪɴ ʏᴏᴜ ᴄᴀɴ'ᴛ ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ !</b>")
    chat_type = message.chat.type
    if chat_type not in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        return await message.reply_text("ᴜꜱᴇ ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅ ɪɴ ɢʀᴏᴜᴘ.")      
    grp_id = message.chat.id
    title = message.chat.title
    if not await is_check_admin(client, grp_id, message.from_user.id):
        return await message.reply_text('ʏᴏᴜ ɴᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.')
    vp = message.text.split(" ", 1)[1]
    if vp.lower() in ["Off", "off", "False", "false", "Turn Off", "turn off"]:
        await save_group_settings(grp_id, 'is_fsub', False)
        return await message.reply_text("ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴛᴜʀɴᴇᴅ ᴏꜰꜰ !")
    elif vp.lower() in ["On", "on", "True", "true", "Turn On", "turn on"]:
        await save_group_settings(grp_id, 'is_fsub', True)
        return await message.reply_text("ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴛᴜʀɴᴇᴅ ᴏɴ !")
    try:
        ids = message.text.split(" ", 1)[1]
        fsub_ids = list(map(int, ids.split()))
    except IndexError:
        return await message.reply_text("ᴄᴏᴍᴍᴀɴᴅ ɪɴᴄᴏᴍᴘʟᴇᴛᴇ!\n\nᴄᴀɴ ᴍᴜʟᴛɪᴘʟᴇ ᴄʜᴀɴɴᴇʟ ᴀᴅᴅ ꜱᴇᴘᴀʀᴀᴛᴇ ʙʏ ꜱᴘᴀᴄᴇꜱ. ʟɪᴋᴇ: /set_fsub id1 id2 id3")
    except ValueError:
        return await message.reply_text('ᴍᴀᴋᴇ ꜱᴜʀᴇ ɪᴅꜱ ɪꜱ ɪɴᴛᴇɢᴇʀ.')        
    channels = "Channels:\n"
    for id in fsub_ids:
        try:
            chat = await client.get_chat(id)
        except Exception as e:
            return await message.reply_text(f"{id} ɪꜱ ɪɴᴠᴀʟɪᴅ!\nᴍᴀᴋᴇ ꜱᴜʀᴇ ᴛʜɪꜱ ʙᴏᴛ ᴀᴅᴍɪɴ ɪɴ ᴛʜᴀᴛ ᴄʜᴀɴɴᴇʟ.\n\nᴇʀʀᴏʀ - {e}")
        if chat.type != enums.ChatType.CHANNEL:
            return await message.reply_text(f"{id} ɪꜱ ɴᴏᴛ ᴄʜᴀɴɴᴇʟ.")
        channels += f'{chat.title}\n'
    await save_group_settings(grp_id, 'fsub', fsub_ids)
    await message.reply_text(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ꜱᴇᴛ ꜰᴏʀᴄᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ {title} ᴛᴏ\n\n{channels}")

@Client.on_message(filters.command('telegraph'))
async def telegraph(bot, message):
    reply_to_message = message.reply_to_message
    if not reply_to_message:
        return await message.reply('ʀᴇᴘʟʏ ᴛᴏ ᴀɴʏ ᴘʜᴏᴛᴏ ᴏʀ ᴠɪᴅᴇᴏ.')
    file = reply_to_message.photo or reply_to_message.video or None
    if file is None:
        return await message.reply('ɪɴᴠᴀʟɪᴅ ᴍᴇᴅɪᴀ.')
    if file.file_size >= 5242880:
        await message.reply_text(text="ꜱᴇɴᴅ ʟᴇꜱꜱ ᴛʜᴀɴ 5ᴍʙ")   
        return
    text = await message.reply_text(text="ᴘʀᴏᴄᴇssɪɴɢ....")   
    media = await reply_to_message.download()  
    try:
        response = upload_file(media)
    except Exception as e:
        await text.edit_text(text=f"Error - {e}")
        return    
    try:
        os.remove(media)
    except:
        pass
    await text.edit_text(f"<b>❤️ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴘʜ ʟɪɴᴋ ᴄᴏᴍᴘʟᴇᴛᴇᴅ 👇</b>\n\n<code>https://telegra.ph/{response[0]}</code></b>")

@Client.on_message(filters.command('ping'))
async def ping(client, message):
    start_time = time.monotonic()
    msg = await message.reply("👀")
    end_time = time.monotonic()
    await msg.edit(f'{round((end_time - start_time) * 1000)} ms')
    
"""@Client.on_message(filters.command("add_premium"))
async def give_premium_cmd_handler(client, message):
    if message.from_user.id not in ADMINS:
        return
    if len(message.command) == 3:
        user_id = int(message.command[1])  # Convert the user_id to integer
        time = message.command[2]        
        seconds = await get_seconds(time)
        if seconds > 0:
            expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            user_data = {"id": user_id, "expiry_time": expiry_time} 
            await db.update_user(user_data)  # Use the update_user method to update or insert user data
            await message.reply_text("ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ ᴀᴅᴅᴇᴅ ᴛᴏ ᴛʜᴇ ᴜꜱᴇʀ.")
            
            await client.send_message(
                chat_id=user_id,
                text=f"<b>ᴘʀᴇᴍɪᴜᴍ ᴀᴅᴅᴇᴅ ᴛᴏ ʏᴏᴜʀ ᴀᴄᴄᴏᴜɴᴛ ꜰᴏʀ {time} ᴇɴᴊᴏʏ 😀\n</b>",                
            )
        else:
            await message.reply_text("Invalid time format. Please use '1day for days', '1hour for hours', or '1min for minutes', or '1month for months' or '1year for year'")
    else:
        await message.reply_text("<b>Usage: /add_premium user_id time \n\nExample /add_premium 1252789 10day \n\n(e.g. for time units '1day for days', '1hour for hours', or '1min for minutes', or '1month for months' or '1year for year')</b>")
        
@Client.on_message(filters.command("remove_premium"))
async def remove_premium_cmd_handler(client, message):
    if message.from_user.id not in ADMINS:
        return
    if len(message.command) == 2:
        user_id = int(message.command[1])  # Convert the user_id to integer
      #  time = message.command[2]
        time = "1s"
        seconds = await get_seconds(time)
        if seconds > 0:
            expiry_time = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
            user_data = {"id": user_id, "expiry_time": expiry_time}  # Using "id" instead of "user_id"
            await db.update_user(user_data)  # Use the update_user method to update or insert user data
            await message.reply_text("ᴘʀᴇᴍɪᴜᴍ ᴀᴄᴄᴇꜱꜱ ʀᴇᴍᴏᴠᴇᴅ ᴛᴏ ᴛʜᴇ ᴜꜱᴇʀ.")
            await client.send_message(
                chat_id=user_id,
                text=f"<b>ᴘʀᴇᴍɪᴜᴍ ʀᴇᴍᴏᴠᴇᴅ ʙʏ ᴀᴅᴍɪɴꜱ \n\nᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ɪꜰ ᴛʜɪꜱ ɪꜱ ᴍɪꜱᴛᴀᴋᴇ \n\n 👮 ᴀᴅᴍɪɴ : <a href='https://telegram.me/pssupport_Robot'>ᴘs - sᴜᴘᴘᴏʀᴛ​</a>\n</b>",                
            )
        else:
            await message.reply_text("ɪɴᴠᴀʟɪᴅ ᴛɪᴍᴇ ꜰᴏʀᴍᴀᴛ.'")
    else:
        await message.reply_text("Usage: /remove_premium user_id")
        
@Client.on_message(filters.command("plans"))
async def plans_cmd_handler(client, message):                
    btn = [            
        [InlineKeyboardButton("ꜱᴇɴᴅ ᴘᴀʏᴍᴇɴᴛ ʀᴇᴄᴇɪᴘᴛ 🧾", user_id=admin)]
        for admin in ADMINS
        ]
    btn.append(
    	[InlineKeyboardButton("⚠️ ᴄʟᴏsᴇ / ᴅᴇʟᴇᴛᴇ ⚠️", callback_data="close_data")]
    	)
    reply_markup = InlineKeyboardMarkup(btn)
    await message.reply_photo(
        photo=PAYMENT_QR,
        caption="**Pʀᴇᴍɪᴜᴍ Fᴇᴀᴛᴜʀᴇs 🎁\n\n☆ No Need To Verify\n☆ Ad Free Experience\n☆ Unlimited Movie And Series",
        reply_markup=reply_markup
    )
        
@Client.on_message(filters.command("my_plan"))
async def check_plans_cmd(client, message):
    user_id  = message.from_user.id
    if await db.has_premium_access(user_id):         
        remaining_time = await db.check_remaining_uasge(user_id)             
        expiry_time = remaining_time + datetime.datetime.now()
        
        await message.reply_photo(PRE_IMG,f"**Your plans details are :\n\nRemaining Time : {remaining_time}\n\nExpirytime : {expiry_time}**")
    else:
        btn = [ 
            [InlineKeyboardButton("ɢᴇᴛ ғʀᴇᴇ ᴛʀᴀɪʟ ғᴏʀ 𝟻 ᴍɪɴᴜᴛᴇꜱ ☺️", callback_data="get_trail")],
            [InlineKeyboardButton("ʙᴜʏ sᴜʙsᴄʀɪᴘᴛɪᴏɴ : ʀᴇᴍᴏᴠᴇ ᴀᴅs", callback_data="buy_premium")],
            [InlineKeyboardButton("⚠️ ᴄʟᴏsᴇ / ᴅᴇʟᴇᴛᴇ ⚠️", callback_data="close_data")]
        ]
        reply_markup = InlineKeyboardMarkup(btn)
        m=await message.reply_sticker("CAACAgIAAxkBAAIBTGVjQbHuhOiboQsDm35brLGyLQ28AAJ-GgACglXYSXgCrotQHjibHgQ")         
        await message.reply_photo(PRE_IMG,f"**😢 You Don't Have Any Premium Subscription.\n\n Check Out Our Premium /plans**",reply_markup=reply_markup)
        await asyncio.sleep(2)
        await m.delete()"""
