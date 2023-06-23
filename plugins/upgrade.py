"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Free Plan User**
            Get All Plans For Free
	    To get Ask Admin @xdecoy 
	**VIP 1  FREE** 
	Daily  Upload  limit 50GB
	Price Rs FREE 
	
	**VIP 2 FREE**
	Daily Upload limit Unlimited 
	Price Rs  Free
        ASK Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Xdecoy")], 
        			[InlineKeyboardButton("Support 🌎",url = "https://t.me/HeavenBotSupport"),
        			InlineKeyboardButton("Join",url = "https://t.me/VipMoviez")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Free Plan User**
	           Get All Plans For Free
	    To get Ask Admin @xdecoy 
	**VIP 1  FREE** 
	Daily  Upload  limit 50GB
	Price Rs FREE 
	
	**VIP 2 FREE**
	Daily Upload limit Unlimited 
	Price Rs  Free
        ASK Admin"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("ADMIN 🛂",url = "https://t.me/Xdecoy")], 
        			[InlineKeyboardButton("Support 🌎",url = "https://t.me/HeavenBotSupport"),
        			InlineKeyboardButton("Join",url = "https://t.me/VipMoviez")],[InlineKeyboardButton("Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
