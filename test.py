from telegram import Message, Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters
async def start(update: Update, context) -> None:
    await update.message.reply_text(f"hello")
async def help_command(update: Update, context):
    await update.message.reply_text("This is a help message./start:run ,/help:get help")
async def about(update: Update, context):
    await update.message.reply_text("This bot is created to help users manage tasks efficiently.")
application =Application.builder().token("8141360652:AAGSw6ObZP-qzshZzvTIeltlHZ4guskEMKc").build()
async def us(update: Update, context):
    msg=update.message.text
    await update.message.reply_text(f"hello {msg}✌")
application.add_handler(CommandHandler("start", start))
application.add_handler(CommandHandler("help", help_command))
application.add_handler(CommandHandler("about", about))
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, us))
application.run_polling()      
    