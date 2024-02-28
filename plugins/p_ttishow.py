import random, os, sys
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors.exceptions.bad_request_400 import MessageTooLong, PeerIdInvalid
from info import ADMINS, LOG_CHANNEL, PICS, SUPPORT_LINK, UPDATES_LINK
from database.users_chats_db import db
from database.ia_filterdb import Media
from utils import get_size, temp, get_settings
from Script import script
from pyrogram.errors import ChatAdminRequired


@Client.on_chat_member_updated(filters.group)
async def welcome(bot, message):
    if message.new_chat_member and not message.old_chat_member:
        if message.new_chat_member.user.id == temp.ME:
            buttons = [[
                InlineKeyboardButton('ᴜᴘᴅᴀᴛᴇ', url=UPDATES_LINK),
                InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ', url=SUPPORT_LINK)
            ]]
            reply_markup=InlineKeyboardMarkup(buttons)
            user = message.from_user.mention if message.from_user else "ᴅᴇᴀʀ"
            await bot.send_photo(chat_id=message.chat.id, photo=random.choice(PICS), caption=f"👋 ʜᴇʟʟᴏ {user},\n\nᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ᴛᴏ ᴛʜᴇ <b>'{message.chat.title}'</b> ɢʀᴏᴜᴘ, ᴅᴏɴ'ᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ ᴍᴀᴋᴇ ᴍᴇ ᴀᴅᴍɪɴ. ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ ᴀꜱᴋ ᴛʜᴇ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.  😘</b>", reply_markup=reply_markup)
            return
        settings = await get_settings(message.chat.id)
        if settings["welcome"]:
            WELCOME = settings['welcome_text']
            welcome_msg = WELCOME.format(
                mention = message.new_chat_member.user.mention,
                title = message.chat.title
            )
            await bot.send_message(chat_id=message.chat.id, text=welcome_msg)


@Client.on_message(filters.command('restart') & filters.user(ADMINS))
async def restart_bot(bot, message):
    msg = await message.reply("ʀᴇꜱᴛᴀʀᴛɪɴɢ...")
    with open('restart.txt', 'w+') as file:
        file.write(f"{msg.chat.id}\n{msg.id}")
    os.execl(sys.executable, sys.executable, "bot.py")

@Client.on_message(filters.command('leave') & filters.user(ADMINS))
async def leave_a_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "ɴᴏ ʀᴇᴀꜱᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ."
    try:
        chat = int(chat)
    except:
        chat = chat
    try:
        buttons = [[
            InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url=SUPPORT_LINK)
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat,
            text=f'ʜᴇʟʟᴏ ꜰʀɪᴇɴᴅꜱ,\nᴍʏ ᴏᴡɴᴇʀ ʜᴀꜱ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ɢʀᴏᴜᴘ ꜱᴏ ɪ ᴀᴍ ɢᴏɪɴɢ! ɪꜰ ʏᴏᴜ ɴᴇᴇᴅ ᴍᴇ ᴀᴅᴅ/ᴡᴏʀᴋ ᴀɢᴀɪɴ ʜᴇʀᴇ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.\nReason - <code>{reason}</code>',
            reply_markup=reply_markup,
        )
        await bot.leave_chat(chat)
        await message.reply(f"<b>✅️ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʙᴏᴛ ʟᴇꜰᴛ ꜰʀᴏᴍ ᴛʜɪꜱ ɢʀᴏᴜᴘ - `{chat}`</b>")
    except Exception as e:
        await message.reply(f'Error - {e}')

@Client.on_message(filters.command('ban_grp') & filters.user(ADMINS))
async def disable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "ɴᴏ ʀᴇᴀꜱᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ."
    try:
        chat_ = int(chat)
    except:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ᴠᴀʟɪᴅ ᴄʜᴀᴛ ɪᴅ')
    cha_t = await db.get_chat(int(chat_))
    if not cha_t:
        return await message.reply("ᴄʜᴀᴛ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ")
    if cha_t['is_disabled']:
        return await message.reply(f"ᴛʜɪꜱ ᴄʜᴀᴛ ɪꜱ ᴀʟʀᴇᴀᴅʏ ᴅɪꜱᴀʙʟᴇᴅ.\nReason - <code>{cha_t['reason']}</code>")
    await db.disable_chat(int(chat_), reason)
    temp.BANNED_CHATS.append(int(chat_))
    await message.reply('ᴄʜᴀᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴅɪꜱᴀʙʟᴇᴅ')
    try:
        buttons = [[
            InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ', url=SUPPORT_LINK)
        ]]
        reply_markup=InlineKeyboardMarkup(buttons)
        await bot.send_message(
            chat_id=chat_, 
            text=f'ʜᴇʟʟᴏ ꜰʀɪᴇɴᴅꜱ,\nᴍʏ ᴏᴡɴᴇʀ ʜᴀꜱ ᴛᴏʟᴅ ᴍᴇ ᴛᴏ ʟᴇᴀᴠᴇ ꜰʀᴏᴍ ɢʀᴏᴜᴘ ꜱᴏ ɪ ᴀᴍ ɢᴏɪɴɢ! ɪꜰ ʏᴏᴜ ɴᴇᴇᴅ ᴍᴇ ᴀᴅᴅ/ᴡᴏʀᴋ ᴀɢᴀɪɴ ʜᴇʀᴇ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ ᴄᴏɴᴛᴀᴄᴛ ᴍʏ ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ.\nReason - <code>{reason}</code>',
            reply_markup=reply_markup)
        await bot.leave_chat(chat_)
    except Exception as e:
        await message.reply(f"Error - {e}")

@Client.on_message(filters.command('unban_grp') & filters.user(ADMINS))
async def re_enable_chat(bot, message):
    if len(message.command) == 1:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ')
    chat = message.command[1]
    try:
        chat_ = int(chat)
    except:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ᴠᴀʟɪᴅ ᴄʜᴀᴛ ɪᴅ')
    sts = await db.get_chat(int(chat))
    if not sts:
        return await message.reply("ᴄʜᴀᴛ ɴᴏᴛ ꜰᴏᴜɴᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ")
    if not sts.get('is_disabled'):
        return await message.reply('ᴛʜɪꜱ ᴄʜᴀᴛ ɪꜱ ɴᴏᴛ ʏᴇᴛ ᴅɪꜱᴀʙʟᴇᴅ.')
    await db.re_enable_chat(int(chat_))
    temp.BANNED_CHATS.remove(int(chat_))
    await message.reply("ᴄʜᴀᴛ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʀᴇ-ᴇɴᴀʙʟᴇᴅ")

@Client.on_message(filters.command('invite_link') & filters.user(ADMINS))
async def gen_invite_link(bot, message):
    if len(message.command) == 1:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ᴄʜᴀᴛ ɪᴅ')
    chat = message.command[1]
    try:
        chat = int(chat)
    except:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ᴠᴀʟɪᴅ ᴄʜᴀᴛ ɪᴅ')
    try:
        link = await bot.create_chat_invite_link(chat)
    except Exception as e:
        return await message.reply(f'Error - {e}')
    await message.reply(f'ʜᴇʀᴇ ɪꜱ ʏᴏᴜʀ ɪɴᴠɪᴛᴇ ʟɪɴᴋ : {link.invite_link}')

@Client.on_message(filters.command('ban_user') & filters.user(ADMINS))
async def ban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ᴜꜱᴇʀ ɪᴅ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ')
    r = message.text.split(None)
    if len(r) > 2:
        reason = message.text.split(None, 2)[2]
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
        reason = "ɴᴏ ʀᴇᴀꜱᴏɴ ᴘʀᴏᴠɪᴅᴇᴅ."
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        if k.id in ADMINS:
            return await message.reply('You are not an ADMINS')
        jar = await db.get_ban_status(k.id)
        if jar['is_banned']:
            return await message.reply(f"{k.mention} is ɪꜱ ᴀʟʀᴇᴀᴅʏ ʙᴀɴɴᴇᴅ.\nReason - <code>{jar['ban_reason']}</code>")
        await db.ban_user(k.id, reason)
        temp.BANNED_USERS.append(k.id)
        await message.reply(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ʙᴀɴɴᴇᴅ {k.mention}")
   
@Client.on_message(filters.command('unban_user') & filters.user(ADMINS))
async def unban_a_user(bot, message):
    if len(message.command) == 1:
        return await message.reply('ɢɪᴠᴇ ᴍᴇ ᴀ ᴜꜱᴇʀ ɪᴅ ᴏʀ ᴜꜱᴇʀɴᴀᴍᴇ')
    r = message.text.split(None)
    if len(r) > 2:
        chat = message.text.split(None, 2)[1]
    else:
        chat = message.command[1]
    try:
        chat = int(chat)
    except:
        pass
    try:
        k = await bot.get_users(chat)
    except Exception as e:
        return await message.reply(f'Error - {e}')
    else:
        jar = await db.get_ban_status(k.id)
        if not jar['is_banned']:
            return await message.reply(f"{k.mention} ɪꜱ ɴᴏᴛ ʏᴇᴛ ʙᴀɴɴᴇᴅ.")
        await db.remove_ban(k.id)
        temp.BANNED_USERS.remove(k.id)
        await message.reply(f"ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ᴜɴʙᴀɴɴᴇᴅ {k.mention}")
    
@Client.on_message(filters.command('users') & filters.user(ADMINS))
async def list_users(bot, message):
    raju = await message.reply('ɢᴇᴛᴛɪɴɢ ʟɪꜱᴛ ᴏꜰ ᴜꜱᴇʀꜱ')
    users = await db.get_all_users()
    out = "ᴜꜱᴇʀꜱ ꜱᴀᴠᴇᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ ᴀʀᴇ :\n\n"
    async for user in users:
        out += f"**ɴᴀᴍᴇ:** <a href=tg://user?id={user['id']}>{user['name']}</a>\n**ɪᴅ:** `{user['id']}`"
        if user['ban_status']['is_banned']:
            out += ' (ʙᴀɴɴᴇᴅ ᴜꜱᴇʀ)'
        if user['verify_status']['is_verified']:
            out += ' (ᴠᴇʀɪꜰɪᴇᴅ ᴜꜱᴇʀ)'
        out += '\n\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('users.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('users.txt', caption="List of users")
        await raju.delete()
        os.remove('users.txt')

@Client.on_message(filters.command('chats') & filters.user(ADMINS))
async def list_chats(bot, message):
    raju = await message.reply('ɢᴇᴛᴛɪɴɢ ʟɪꜱᴛ ᴏꜰ ᴄʜᴀᴛꜱ')
    chats = await db.get_all_chats()
    out = "ᴄʜᴀᴛꜱ ꜱᴀᴠᴇᴅ ɪɴ ᴅᴀᴛᴀʙᴀꜱᴇ ᴀʀᴇ :\n\n"
    async for chat in chats:
        out += f"**ᴛɪᴛʟᴇ:** {chat['title']}\n**ɪᴅ:** `{chat['id']}`"
        if chat['chat_status']['is_disabled']:
            out += ' (ᴅɪꜱᴀʙʟᴇᴅ ᴄʜᴀᴛ)'
        out += '\n\n'
    try:
        await raju.edit_text(out)
    except MessageTooLong:
        with open('chats.txt', 'w+') as outfile:
            outfile.write(out)
        await message.reply_document('chats.txt', caption="List of chats")
        await raju.delete()
        os.remove('chats.txt')
