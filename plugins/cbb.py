from pyrogram import Client 
from bot import Bot
from config import OWNER_ID, ABOUT_TXT, HELP_TXT, START_MSG
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from database.database import add_user, del_user, full_userbase, present_user

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "help":
        await query.message.edit_text(
            text=HELP_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                        InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data='close')
                    ]
                ]
            )
        )
    elif data == "about":
        await query.message.edit_text(
            text=ABOUT_TXT.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton('ʜᴏᴍᴇ', callback_data='start'),
                     InlineKeyboardButton('ᴄʟᴏꜱᴇ', callback_data='close')]
                ]
            )
        )
    elif data == "start":
        await query.message.edit_text(
            text=START_MSG.format(first=query.from_user.first_name),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("Help", callback_data='help'),
                 InlineKeyboardButton("About", callback_data='about')],
                [InlineKeyboardButton('Backup Channel', url='https://t.me/AIO_Backup'),
                 InlineKeyboardButton('Developer', url='https://t.me/Soutick_09')],
                [InlineKeyboardButton("Close", callback_data='close')]
            ])
        )
    elif data == "premium":
        await query.message.edit_text(
            text=f"Premium Benefits & Perks\nDirect Channel Links, No Ad Links\nSpecial Access In Events\n\nPricing Rates\n1 Day - ₹10 Only\n7 Days - ₹70\n1 Month - ₹150 (50% Discount)\n3 Months - ₹250 (72% Discount) [Popular]\n\nWant To Buy?\nPay Using UPI »»» <code>soutick@fam</code>\nSend Screenshot to @Soutick_09\n\nWe Have Limited Seats For Premium Users",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Owner", url="https://t.me/Soutick_09"),
                        InlineKeyboardButton("Main Channel", url="https://t.me/AIO_Backup")
                    ],
                    [
                        InlineKeyboardButton("🔒 Close", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
