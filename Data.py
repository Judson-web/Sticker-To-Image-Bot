# (c) @Judson-web

from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hᴇʏ {}

Wᴇʟᴄᴏᴍᴇ ᴛᴏ <a href="t.me/M_StickerToolsBot">Sᴛɪᴄᴋᴇʀ Tᴏ Iᴍᴀɢᴇ Bᴏᴛ</a

Yᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ᴛᴏ ᴄᴏɴᴠᴇʀᴛ
1) Sᴛɪᴄᴋᴇʀ ᴛᴏ Iᴍᴀɢᴇ
2) Iᴍᴀɢᴇ ᴛᴏ Sᴛɪᴄᴋᴇʀ

Sᴇɴᴅ Mᴜʟᴛɪᴘʟᴇ ɪᴍᴀɢᴇs ᴏʀ sᴛɪᴄᴋᴇʀs ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴡᴏʀᴋ ᴛʜᴇ sᴀᴍᴇ

Bʏ <a href="https://t.me/storytym">sᴛᴍ</a>
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/STMbOTsUPPORTgROUP")],
        [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("ʙᴏᴛ ᴇᴅɪᴛᴏʀ", url="https://t.me/VAMPIRE_KING_NO_1")
        ],
        [
            InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help"),
            InlineKeyboardButton("ᴀʙᴏᴜᴛ", callback_data="about")
        ],
        [InlineKeyboardButton("ᴍᴏᴠɪᴇ ɢʀᴏᴜᴘ", url="https://t.me/storytym")],
        [InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ", url="https://t.me/STMbOTsUPPORTgROUP")],
    ]

    # Help Message
    HELP = """
Wᴀɴᴛ Hᴇʟᴘ ?!?!?!?!

1) Sᴇɴᴅ Sᴛɪᴄᴋᴇʀ ᴛᴏ ɢᴇᴛ Iᴍᴀɢᴇ
2) Sᴇɴᴅ Iᴍᴀɢᴇ ᴛᴏ ɢᴇᴛ Sᴛɪᴄᴋᴇʀ

Nᴏᴛᴇ : Yᴏᴜ ᴄᴀɴ sᴇɴᴅ ᴀɴʏ ᴀᴍᴏᴜɴᴛ ᴏғ ɪᴍᴀɢᴇs ᴏʀ sᴛɪᴄᴋᴇʀs ᴏʀ ʙᴏᴛʜ ᴛᴏɢᴇᴛʜᴇʀ ᴀᴛ ᴏɴᴄᴇ ᴀɴᴅ ɪᴛ ᴡɪʟʟ ᴡᴏʀᴋ ᴡɪᴛʜ sᴀᴍᴇ sᴘᴇᴇᴅ ᴀɴᴅ ᴀᴄᴄᴜʀᴀᴄʏ.

Mᴏʀᴇ ғᴇᴀᴛᴜʀᴇs ᴄᴏᴍɪɴɢ sᴏᴏɴ!
    """

    # About Message
    ABOUT = """
 Aʙᴏᴜᴛ Tʜɪs Bᴏᴛ
 
✯ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ : [Cʟɪᴄᴋ Hᴇʀᴇ](https://t.me/NOKIERUNNOIPPKITTUM)

✯ Fʀᴀᴍᴇᴡᴏʀᴋ: [Pʏʀᴏɢʀᴀᴍ](docs.pyrogram.org)

✯ Lᴀɴɢᴜᴀɢᴇ : [Pʏᴛʜᴏɴ](www.python.org)

✯ Dᴇᴠᴇʟᴏᴘᴇʀ : [Tᴇʀʀᴏʀ Mɪᴄᴋᴇʏ](https://t.me/VAMPIRE_KING_NO_1)
    """
