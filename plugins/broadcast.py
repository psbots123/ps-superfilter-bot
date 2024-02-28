from pyrogram import Client, filters
import datetime
import time
from database.users_chats_db import db
from info import ADMINS
from utils import broadcast_messages, groups_broadcast_messages, temp, get_readable_time
import asyncio
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lock = asyncio.Lock()

@Client.on_callback_query(filters.regex(r'^broadcast_cancel'))
async def broadcast_cancel(bot, query):
    _, ident = query.data.split("#")
    if ident == 'users':
        await query.message.edit("ᴛʀʏɪɴɢ ᴛᴏ ᴄᴀɴᴄᴇʟ ᴜꜱᴇʀꜱ ʙʀᴏᴀᴅᴄᴀꜱᴛɪɴɢ...")
        temp.USERS_CANCEL = True
    elif ident == 'groups':
        temp.GROUPS_CANCEL = True
        await query.message.edit("ᴛʀʏɪɴɢ ᴛᴏ ᴄᴀɴᴄᴇʟ ɢʀᴏᴜᴘꜱ ʙʀᴏᴀᴅᴄᴀꜱᴛɪɴɢ...")
               
@Client.on_message(filters.command(["broadcast", "pin_broadcast"]) & filters.user(ADMINS) & filters.reply)
async def users_broadcast(bot, message):
    if lock.locked():
        return await message.reply('ᴄᴜʀʀᴇɴᴛʟʏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴘʀᴏᴄᴇꜱꜱɪɴɢ, ᴡᴀɪᴛ ꜰᴏʀ ᴄᴏᴍᴘʟᴇᴛᴇ.')
    if message.command[0] == 'pin_broadcast':
        pin = True
    else:
        pin = False
    users = await db.get_all_users()
    b_msg = message.reply_to_message
    b_sts = await message.reply_text(text='ʙʀᴏᴀᴅᴄᴀꜱᴛɪɴɢ ʏᴏᴜʀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ᴜꜱᴇʀꜱ...')
    start_time = time.time()
    total_users = await db.total_users_count()
    done = 0
    failed = 0
    success = 0

    async with lock:
        async for user in users:
            time_taken = get_readable_time(time.time()-start_time)
            if temp.USERS_CANCEL:
                temp.USERS_CANCEL = False
                await b_sts.edit(f"ᴜꜱᴇʀꜱ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴀɴᴄᴇʟʟᴇᴅ!\nᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ {time_taken}\n\nᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ : <code>{total_users}</code>\nᴄᴏᴍᴘʟᴇᴛᴇᴅ : <code>{done} / {total_users}</code>\nꜱᴜᴄᴄᴇꜱꜱ : <code>{success}</code>")
                return
            sts = await broadcast_messages(int(user['id']), b_msg, pin)
            if sts == 'Success':
                success += 1
            elif sts == 'Error':
                failed += 1
            done += 1
            if not done % 20:
                btn = [[
                    InlineKeyboardButton('CANCEL', callback_data=f'broadcast_cancel#users')
                ]]
                await b_sts.edit(f"ᴜꜱᴇʀꜱ ʙʀᴏᴀᴅᴄᴀꜱᴛ ɪɴ ᴘʀᴏɢʀᴇꜱꜱ...\n\nᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{total_users}</code>\nᴄᴏᴍᴘʟᴇᴛᴇᴅ: <code>{done} / {total_users}</code>\nꜱᴜᴄᴄᴇꜱꜱ: <code>{success}</code>", reply_markup=InlineKeyboardMarkup(btn))
        await b_sts.edit(f"ᴜꜱᴇʀꜱ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ.\nᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{total_users}</code>\nᴄᴏᴍᴘʟᴇᴛᴇᴅ: <code>{done} / {total_users}</code>\nꜱᴜᴄᴄᴇꜱꜱ: <code>{success}</code>")


@Client.on_message(filters.command(["grp_broadcast", "pin_grp_broadcast"]) & filters.user(ADMINS) & filters.reply)
async def groups_broadcast(bot, message):
    if lock.locked():
        return await message.reply('ᴄᴜʀʀᴇɴᴛʟʏ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴘʀᴏᴄᴇꜱꜱɪɴɢ, ᴡᴀɪᴛ ꜰᴏʀ ᴄᴏᴍᴘʟᴇᴛᴇ.')
    if message.command[0] == 'pin_grp_broadcast':
        pin = True
    else:
        pin = False
    chats = await db.get_all_chats()
    b_msg = message.reply_to_message
    b_sts = await message.reply_text(text='ʙʀᴏᴀᴅᴄᴀꜱᴛɪɴɢ ʏᴏᴜʀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ɢʀᴏᴜᴘꜱ...')
    start_time = time.time()
    total_chats = await db.total_chat_count()
    done = 0
    failed = 0
    success = 0

    async with lock:
        async for chat in chats:
            time_taken = get_readable_time(time.time()-start_time)
            if temp.GROUPS_CANCEL:
                temp.GROUPS_CANCEL = False
                await b_sts.edit(f"ɢʀᴏᴜᴘꜱ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴀɴᴄᴇʟʟᴇᴅ!\nᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ {time_taken}\n\nᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ: <code>{total_chats}</code>\nᴄᴏᴍᴘʟᴇᴛᴇᴅ: <code>{done} / {total_chats}</code>\nꜱᴜᴄᴄᴇꜱꜱ: <code>{success}</code>\nꜰᴀɪʟᴇᴅ: <code>{failed}</code>")
                return
            sts = await groups_broadcast_messages(int(chat['id']), b_msg, pin)
            if sts == 'Success':
                success += 1
            elif sts == 'Error':
                failed += 1
            done += 1
            if not done % 20:
                btn = [[
                    InlineKeyboardButton('CANCEL', callback_data=f'broadcast_cancel#groups')
                ]]
                await b_sts.edit(f"ɢʀᴏᴜᴘꜱ ɢʀᴏᴀᴅᴄᴀꜱᴛ ɪɴ ᴘʀᴏɢʀᴇꜱꜱ...\n\nᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ: <code>{total_chats}</code>\nᴄᴏᴍᴘʟᴇᴛᴇᴅ: <code>{done} / {total_chats}</code>\nꜱᴜᴄᴄᴇꜱꜱ: <code>{success}</code>\nꜰᴀɪʟᴇᴅ: <code>{failed}</code>", reply_markup=InlineKeyboardMarkup(btn))    
        await b_sts.edit(f"ɢʀᴏᴜᴘꜱ ʙʀᴏᴀᴅᴄᴀꜱᴛ ᴄᴏᴍᴘʟᴇᴛᴇᴅ.\nᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ {time_taken}\n\nᴛᴏᴛᴀʟ ɢʀᴏᴜᴘꜱ: <code>{total_chats}</code>\nᴄᴏᴍᴘʟᴇᴛᴇᴅ: <code>{done} / {total_chats}</code>\nꜱᴜᴄᴄᴇꜱꜱ: <code>{success}</code>\nꜰᴀɪʟᴇᴅ: <code>{failed}</code>")


