class script(object):
    START_TXT = """<b>ʜᴇʏ {}, <i>{}</i>
    
ɪ ᴀᴍ ᴘᴏᴡᴇʀғᴜʟ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴀꜱ ᴀᴜᴛᴏ ғɪʟᴛᴇʀ ᴡɪᴛʜ ʟɪɴᴋ sʜᴏʀᴛᴇɴᴇʀ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ... ɪᴛ'ꜱ ᴇᴀꜱʏ ᴛᴏ ᴜꜱᴇ ᴊᴜsᴛ ᴀᴅᴅ ᴍᴇ ᴀꜱ ᴀᴅᴍɪɴ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴛʜᴇʀᴇ ᴍᴏᴠɪᴇꜱ ᴡɪᴛʜ ʏᴏᴜʀ ʟɪɴᴋ ꜱʜᴏʀᴛᴇɴᴇʀ... ♻️</b>"""
   
    MY_ABOUT_TXT = """<b>➣ ᴍʏ ɴᴀᴍᴇ ⋟</b> {}
<b>★ ᴄʀᴇᴀᴛᴏʀ ⋟</b> <a href=https://telegram.me/ps_updates>𝙏𝙃𝙀 𝙋𝙎 𝘽𝙊𝙏𝙎</a>
<b>★ ʟɪʙʀᴀʀʏ ⋟</b> <a href=https://pyrogram.org>𝘱𝘺𝘳𝘰𝘨𝘳𝘢𝘮</a>
<b>★ ʟᴀɴɢᴜᴀɢᴇ ⋟</b> <a href=https://www.python.org>𝘱𝘺𝘵𝘩𝘰𝘯 3</a>
<b>★ ᴅᴀᴛᴀʙᴀsᴇ ⋟</b> <a href=https://www.mongodb.com>𝘮𝘰𝘯𝘨𝘰 𝘥𝘣</a>
<b>★ ʙᴏᴛ sᴇʀᴠᴇʀ ⋟</b>  𝘩𝘦𝘳𝘰𝘬𝘶
<b>★ ʙᴜɪʟᴅ sᴛᴀᴛs ⋟</b>  𝘷2.0.1 ﹝ʙᴇᴛᴀ﹞"""
    

    MY_OWNER_TXT = """💵 ɪ ʀᴇǫᴜᴇsᴛᴇᴅ ᴛᴏ ʏᴏᴜ 💸

ᴘʟᴇᴀsᴇ ᴅᴏɴᴀᴛᴇ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ ꜰᴏʀ ᴋᴇᴇᴘɪɴɢ ᴛʜᴇ sᴇʀᴠɪᴄᴇ ᴀʟɪᴠᴇ & ᴋᴇᴇᴘ ʙʀɪɴɢɪɴɢ ᴍᴏʀᴇ ɴᴇᴡ ꜰᴇᴀᴛᴜʀᴇs ꜰᴏʀ ʏᴏᴜ....</b>

𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💷

<b>᚜ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅs ᚛

𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨</b>"""



    STATUS_TXT = """🗂 Total Files: <code>{}</code>
👤 Total Users: <code>{}</code>
👥 Total Chats: <code>{}</code>
✨ Used Storage: <code>{}</code>
🗳 Free Storage: <code>{}</code>
🚀 Bot Uptime: <code>{}</code>"""

    NEW_GROUP_TXT = """#NewGroup
Title - {}
ID - <code>{}</code>
Username - {}
Total - <code>{}</code>"""

    NEW_USER_TXT = """#NewUser
★ Name: {}
★ ID: <code>{}</code>"""

    NO_RESULT_TXT = """#NoResult
★ Group Name: {}
★ Group ID: <code>{}</code>
★ Name: {}

★ Message: {}"""

    REQUEST_TXT = """★ Name: {}
★ ID: <code>{}</code>

★ Message: {}"""

    NOT_FILE_TXT = """👋 Hello {},

I can't find the <b>{}</b> in my database! 🥲

👉 Google Search and check your spelling is correct.
👉 Please read the Instructions to get better results.
👉 Or not been released yet."""
    
    EARN_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴇᴀʀɴ ꜰʀᴏᴍ ᴛʜɪs ʙᴏᴛ

➥ ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴇᴀʀɴ ᴍᴏɴᴇʏ ʙʏ ᴜsɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

» sᴛᴇᴘ 1:- ғɪʀsᴛ ʏᴏᴜ ʜᴀᴠᴇ ᴛᴏ ᴀᴅᴅ ᴛʜɪs ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀᴅᴍɪɴ ᴘᴇʀᴍɪssɪᴏɴ.

» sᴛᴇᴘ 2:- ᴍᴀᴋᴇ ᴀᴄᴄᴏᴜɴᴛ ᴏɴ <a href=https://onepagelink.in/ref/infinity07>onepagelink.in</a> [ ʏᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴜsᴇ ᴏᴛʜᴇʀ sʜᴏʀᴛɴᴇʀ ᴡᴇʙsɪᴛᴇ ]

» sᴛᴇᴘ 3:- ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ʙᴇʟᴏᴡ ɢɪᴠᴇɴ ʙᴜᴛᴛᴏɴ ᴛᴏ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ sʜᴏʀᴛɴᴇʀ ᴡɪᴛʜ ᴛʜɪs ʙᴏᴛ.

➥ ᴛʜɪꜱ ʙᴏᴛ ɪs ꜰʀᴇᴇ ꜰᴏʀ ᴀʟʟ, ʏᴏᴜ ᴄᴀɴ ᴜꜱᴇ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘs ғᴏʀ ꜰʀᴇᴇ ᴏꜰ ᴄᴏꜱᴛ.</b>"""

    HOW_TXT = """<b>ʜᴏᴡ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ‼️

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄᴏɴɴᴇᴄᴛ ʏᴏᴜʀ ᴏᴡɴ sʜᴏʀᴛɴᴇʀ ᴛʜᴇɴ ᴊᴜsᴛ sᴇɴᴅ ᴛʜᴇ ɢɪᴠᴇɴ ᴅᴇᴛᴀɪʟs ɪɴ ᴄᴏʀʀᴇᴄᴛ ꜰᴏʀᴍᴀᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ

➥ ғᴏʀᴍᴀᴛ ↓↓↓

<code>/set_shortlink sʜᴏʀᴛɴᴇʀ sɪᴛᴇ sʜᴏʀᴛɴᴇʀ ᴀᴘɪ</code>

➥ ᴇxᴀᴍᴘʟᴇ ↓↓↓

<code>/set_shortlink onepagelink.in f646357aa129cfbd7eb59bcba428096ab54ca950</code>

➥ ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴄʜᴇᴄᴋ ᴡʜɪᴄʜ sʜᴏʀᴛᴇɴᴇʀ ʏᴏᴜ ʜᴀᴠᴇ ᴄᴏɴɴᴇᴄᴛᴇᴅ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛʜᴇɴ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ /get_shortlink

📝 ɴᴏᴛᴇ:- ʏᴏᴜ sʜᴏᴜʟᴅ ɴᴏᴛ ʙᴇ ᴀɴ ᴀɴᴏɴʏᴍᴏᴜs ᴀᴅᴍɪɴ ɪɴ ɢʀᴏᴜᴘ. sᴇɴᴅ ᴄᴏᴍᴍᴀɴᴅ ᴡɪᴛʜᴏᴜᴛ ʙᴇɪɴɢ ᴀɴ ᴀɴᴏɴʏᴍᴜs ᴀᴅᴍɪɴ.</b>"""

    IMDB_TEMPLATE = """✅ I Found: <code>{query}</code>

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating} / 10</a>
☀️ Languages: {languages}
📀 RunTime: {runtime} Minutes

🗣 Requested by: {message.from_user.mention}
©️ Powered by: <b>{message.chat.title}</b>"""

    FILE_CAPTION = """<i>{file_name}</i>

🚫 ᴘʟᴇᴀsᴇ ᴄʟɪᴄᴋ ᴏɴ ᴛʜᴇ ᴄʟᴏsᴇ ʙᴜᴛᴛᴏɴ ɪꜰ ʏᴏᴜ ʜᴀᴠᴇ sᴇᴇɴ ᴛʜᴇ ᴍᴏᴠɪᴇ 🚫"""

    WELCOME_TEXT = """👋 Hello {mention}, Welcome to {title} group! 💞"""

    HELP_TXT = """<b>Note - <spoiler>Try each command without any argument to see more details 😹</spoiler></b>"""
    
    ADMIN_COMMAND_TXT = """<b>Here is bot admin commands 👇

/index_channels - to check how many index channel id added
/stats - to get bot status
/delete - to delete files using query
/delete_all - to delete all indexed file
/broadcast - to send message to all bot users
/grp_broadcast - to send message to all groups
/pin_broadcast - to send message as pin to all bot users.
/pin_grp_broadcast - to send message as pin to all groups.
/restart - to restart bot
/leave - to leave your bot from particular group
/unban_grp - to enable group
/ban_grp - to disable group
/ban_user - to ban a users from bot
/unban_user - to unban a users from bot
/users - to get all users details
/chats - to get all groups
/invite_link - to generate invite link
/index - to index bot accessible channels
/add_premium - to add user in premium
/remove_premium - to remove user from premium</b>"""
    
    USER_COMMAND_TXT = """<b>Here is bot user commands 👇

/start - to check bot alive or not
/settings - to change group settings as your wish
/set_template - to set custom imdb template
/set_caption - to set custom bot files caption
/set_shortlink - group admin can set custom shortlink
/get_custom_settings - to get your group settings details
/set_welcome - to set custom new joined users welcome message for group
/set_tutorial - to set custom tutorial link in result page button
/id - to check group or channel id
/my_plan - to check your plan details
/plans - to get plan details</b>"""
    
    SOURCE_TXT ="""<b>ᴛʜɪꜱ ɪꜱ ɴᴏᴛ ᴀɴ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴘʀᴏᴊᴇᴄᴛ.</b>

ᴀʟʟ ᴛʜᴇ ꜰɪʟᴇꜱ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴀʀᴇ ꜰʀᴇᴇʟʏ ᴀᴠᴀɪʟᴀʙʟᴇ ᴏɴ ᴛʜᴇ ɪɴᴛᴇʀɴᴇᴛ ᴏʀ ᴘᴏꜱᴛᴇᴅ ʙʏ ꜱᴏᴍᴇʙᴏᴅʏ ᴇʟꜱᴇ.  ᴊᴜꜱᴛ ꜰᴏʀ ᴇᴀꜱʏ ꜱᴇᴀʀᴄʜɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɪɴᴅᴇxɪɴɢ ꜰɪʟᴇꜱ ᴡʜɪᴄʜ ᴀʀᴇ ᴀʟʀᴇᴀᴅʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ. ᴡᴇ ʀᴇꜱᴘᴇᴄᴛ ᴀʟʟ ᴛʜᴇ ᴄᴏᴘʏʀɪɢʜᴛ ʟᴀᴡꜱ ᴀɴᴅ ᴡᴏʀᴋꜱ ɪɴ ᴄᴏᴍᴘʟɪᴀɴᴄᴇ ᴡɪᴛʜ ᴅᴍᴄᴀ ᴀɴᴅ ᴇᴜᴄᴅ. ɪꜰ ᴀɴʏᴛʜɪɴɢ ɪꜱ ᴀɢᴀɪɴꜱᴛ ʟᴀᴡ ᴘʟᴇᴀꜱᴇ ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ꜱᴏ ᴛʜᴀᴛ ɪᴛ ᴄᴀɴ ʙᴇ ʀᴇᴍᴏᴠᴇᴅ ᴀꜱᴀᴘ. ɪᴛ ɪꜱ ꜰᴏʀʙɪʙʙᴇɴ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ, ꜱᴛʀᴇᴀᴍ, ʀᴇᴘʀᴏᴅᴜᴄᴇ, ᴏʀ ʙʏ ᴀɴʏ ᴍᴇᴀɴꜱ, ꜱʜᴀʀᴇ, ᴏʀ ᴄᴏɴꜱᴜᴍᴇ, ᴄᴏɴᴛᴇɴᴛ ᴡɪᴛʜᴏᴜᴛ ᴇxᴘʟɪᴄɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ ꜰʀᴏᴍ ᴛʜᴇ ᴄᴏɴᴛᴇɴᴛ ᴄʀᴇᴀᴛᴏʀ ᴏʀ ʟᴇɢᴀʟ ᴄᴏᴘʏʀɪɢʜᴛ ʜᴏʟᴅᴇʀ. ɪꜰ ʏᴏᴜ ʙᴇʟɪᴇᴠᴇ ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴠɪᴏʟᴀᴛɪɴɢ ʏᴏᴜʀ ɪɴᴛᴇʟʟᴇᴄᴛᴜᴀʟ ᴘʀᴏᴘᴇʀᴛʏ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ʀᴇꜱᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀɴɴᴇʟꜱ ꜰᴏʀ ʀᴇᴍᴏᴠᴀʟ. ᴛʜᴇ ʙᴏᴛ ᴅᴏᴇꜱ ɴᴏᴛ ᴏᴡɴ ᴀɴʏ ᴏꜰ ᴛʜᴇꜱᴇ ᴄᴏɴᴛᴇɴᴛꜱ, ɪᴛ ᴏɴʟʏ ɪɴᴅᴇx ᴛʜᴇ ꜰɪʟᴇꜱ ꜰʀᴏᴍ ᴛᴇʟᴇɢʀᴀᴍ.

<b><a href=https://telegram.me/ps_updates>~ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ ᴛʜᴇ ᴘs ʙᴏᴛs</a></b>
"""
#Premium plans 

    PAGE_TXT = """ᴡʜʏ ᴀʀᴇ ʏᴏᴜ ꜱᴏ ᴄᴜʀɪᴏᴜꜱ ⁉️"""

    PURCHASE_TXT = """ꜱᴇʟᴇᴄᴛ ʏᴏᴜʀ ᴘᴀʏᴍᴇɴᴛ ᴍᴇᴛʜᴏᴅ."""

    PREMIUM_TEXT = """<b>👋 ʜᴇʏ {},
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u>

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>60₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>180₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>250₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>400₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>ps-updates@airtel</code>
📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    CPREMIUM_TEXT = """<b>👋 ʜᴇʏ {},
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u> :

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>60₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>180₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>250₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>400₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>ps-updates@airtel</code>
📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    PLAN_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴘʀᴇᴍɪᴜᴍ ғᴇᴀᴛᴜʀᴇs</u> :

○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴅɪʀᴇᴄᴛ ғɪʟᴇs   
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ 
○ ʜɪɢʜ-sᴘᴇᴇᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ                         
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs                           
○ ᴜɴʟɪᴍɪᴛᴇᴅ ᴍᴏᴠɪᴇs & sᴇʀɪᴇs                                                                        
○ ꜰᴜʟʟ ᴀᴅᴍɪɴ sᴜᴘᴘᴏʀᴛ                              
○ ʀᴇǫᴜᴇsᴛ ᴡɪʟʟ ʙᴇ ᴄᴏᴍᴘʟᴇᴛᴇᴅ ɪɴ 1ʜ [ ɪꜰ ᴀᴠᴀɪʟᴀʙʟᴇ ]

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴀғᴛᴇʀ sᴇɴᴅɪɴɢ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴘʟᴇᴀsᴇ ɢɪᴠᴇ ᴜs sᴏᴍᴇ ᴛɪᴍᴇ ᴛᴏ ᴀᴅᴅ ʏᴏᴜ ɪɴ ᴛʜᴇ ᴘʀᴇᴍɪᴜᴍ ʟɪsᴛ.</b>"""

    FREE_TXT = """<b>👋 ʜᴇʏ {},
    
🎉 <u>ꜰʀᴇᴇ ᴛʀɪᴀʟ</u> 🎉
❗ ᴏɴʟʏ ꜰᴏʀ 5 ᴍɪɴᴜᴛᴇꜱ
 
○ ɴᴏ ɴᴇᴇᴅ ᴛᴏ ᴏᴘᴇɴ ʟɪɴᴋꜱ
○ ᴍᴜʟᴛɪ-ᴘʟᴀʏᴇʀ sᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋs
○ ᴀᴅ-ғʀᴇᴇ ᴇxᴘᴇʀɪᴇɴᴄᴇ

👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ <a href='https://t.me/DeletedFromEarth'>ᴏᴡɴᴇʀ</a> ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴛʀɪᴀʟ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    BRONZE_TXT = """<b>👋 ʜᴇʏ {},
    
🥉 <u>ʙʀᴏɴᴄᴇ ᴘʟᴀɴ</u>
⏰ 7 ᴅᴀʏꜱ
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 10₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    SILVER_TXT = """<b>👋 ʜᴇʏ {},
    
🥈 <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u>
⏰ 30 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 60₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    GOLD_TXT = """<b>👋 ʜᴇʏ {},
    
🥇 <u>ɢᴏʟᴅ ᴘʟᴀɴ</u>
⏰ 90 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 180₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    PLATINUM_TXT = """<b>👋 ʜᴇʏ {},
    
🏅 <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u>
⏰ 180 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 250₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""
    
    DIAMOND_TXT = """<b>👋 ʜᴇʏ {},

💎 <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u>
⏰ 365 ᴅᴀʏꜱ 
💸 ᴘʟᴀɴ ᴘʀɪᴄᴇ ➛ 400₹

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    OTHER_TXT = """<b>👋 ʜᴇʏ {},
    
🎁 <u>ᴏᴛʜᴇʀ ᴘʟᴀɴ</u>
⏰ ᴄᴜꜱᴛᴏᴍɪꜱᴇᴅ ᴅᴀʏꜱ
💸 ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴅᴀʏꜱ ʏᴏᴜ ᴄʜᴏᴏꜱᴇ

🏆 ɪꜰ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ɴᴇᴡ ᴘʟᴀɴ ᴀᴘᴀʀᴛ ꜰʀᴏᴍ ᴛʜᴇ ɢɪᴠᴇɴ ᴘʟᴀɴ, ᴛʜᴇɴ ʏᴏᴜ ᴄᴀɴ ᴛᴀʟᴋ ᴛᴏ ᴏᴜʀ <a href='https://t.me/DeletedFromEarth'>ᴏᴡɴᴇʀ</a> ᴅɪʀᴇᴄᴛʟʏ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜᴇ ᴄᴏɴᴛᴀᴄᴛ ʙᴜᴛᴛᴏɴ ɢɪᴠᴇɴ ʙᴇʟᴏᴡ.
    
👨‍💻 ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴏᴡɴᴇʀ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ᴏᴛʜᴇʀ ᴘʟᴀɴ.

➛ ᴜꜱᴇ /plan ᴛᴏ ꜱᴇᴇ ᴀʟʟ ᴏᴜʀ ᴘʟᴀɴꜱ ᴀᴛ ᴏɴᴄᴇ.
➛ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan</b>"""

    UPI_TXT = """<b>👋 ʜᴇʏ {},
    
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

💵 ᴜᴘɪ ɪᴅ - <code>ps-updates@airtel</code>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    QR_TXT = """<b>👋 ʜᴇʏ {},
    
⚜️ ᴘᴀʏ ᴀᴍᴍᴏᴜɴᴛ ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ʏᴏᴜʀ ᴘʟᴀɴ ᴀɴᴅ ᴇɴᴊᴏʏ ᴘʀᴇᴍɪᴜᴍ ᴍᴇᴍʙᴇʀꜱʜɪᴘ !

📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""

    PREPLANS_TXT = """<b>👋 ʜᴇʏ {},
    
🎖️ <u>ᴀᴠᴀɪʟᴀʙʟᴇ ᴘʟᴀɴs</u> :

● <code>10₹</code> ➛ <u>ʙʀᴏɴᴢᴇ ᴘʟᴀɴ</u> » <code>7 ᴅᴀʏꜱ</code>
● <code>60₹</code> ➛ <u>ꜱɪʟᴠᴇʀ ᴘʟᴀɴ</u> » <code>30 ᴅᴀʏꜱ</code>
● <code>180₹</code> ➛ <u>ɢᴏʟᴅ ᴘʟᴀɴ</u> » <code>90 ᴅᴀʏꜱ</code>
● <code>250₹</code> ➛ <u>ᴘʟᴀᴛɪɴᴜᴍ ᴘʟᴀɴ</u> » <code>180 ᴅᴀʏꜱ</code>
● <code>400₹</code> ➛ <u>ᴅɪᴀᴍᴏɴᴅ ᴘʟᴀɴ</u> » <code>365 ᴅᴀʏꜱ</code>

💵 ᴜᴘɪ ɪᴅ - <code>ps-updates@airtel</code>
📸 ǫʀ ᴄᴏᴅᴇ - <a href='https://telegra.ph/Payment-Information-01-03'>ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ ꜱᴄᴀɴ</a>

⚜️ ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴀᴄᴛɪᴠᴇ ᴘʟᴀɴ ʙʏ ᴜꜱɪɴɢ : /myplan

‼️ ᴍᴜsᴛ sᴇɴᴅ sᴄʀᴇᴇɴsʜᴏᴛ ᴀғᴛᴇʀ ᴘᴀʏᴍᴇɴᴛ.</b>"""    

