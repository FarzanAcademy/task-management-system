from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

async def start(update: Update, context) -> None:
    await update.message.reply_text("Hello I'm your New friend!")

async def help_command(update: Update, context) -> None:
    await update.message.reply_text("Okay i'm here for help say me what you want")

async def about(update: Update, context) -> None:
    await update.message.reply_text("i'm a special robot for game")

async def us(update,context):
    msg = update.message.text
    await update.message.reply_text(f"hello {msg}")

application=Application.builder().token("8441928463:AAGsaNIgmmbuHl7YGGGtkm0Zty8Ydx-PF3Q").build()


application.add_handler (CommandHandler('start',start))
application.add_handler (CommandHandler('help',help_command))
application.add_handler (CommandHandler('about',about))
application.add_handler (MessageHandler(filters.TEXT & ~filters.COMMAND, us))
application.run_polling()
