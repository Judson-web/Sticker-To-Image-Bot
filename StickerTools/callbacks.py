from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
from Data import Data


# Callbacks
@Client.on_callback_query()
async def _callbacks(bot, callback_query: CallbackQuery):
    user = await bot.get_me()
    mention = user["mention"]
    if callback_query.data.lower() == "home":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.START.format(callback_query.from_user.mention, mention),
            reply_markup=InlineKeyboardMarkup(Data.buttons),
        )
    elif callback_query.data.lower() == "about":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Data.ABOUT,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
    elif callback_query.data.lower() == "help":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="**Hᴇʀᴇ's Hᴏᴡ ᴛᴏ ᴜsᴇ ᴍᴇ**\n" + Data.HELP,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
