from telegram import Update

from telegram.ext import Application, CommandHandler,MessageHandler,filters,ContextTypes

# Define the start function
async def start(update: Update, context) -> None:
    await update.message.reply_text("Welcome, I'm a robot!")

async def  help_command(update:Update, context)-> None:
    await update.message.reply_text("/help:راهنما/start:راه اندازی")

async def  about(update:Update, context)-> None:
    await update.message.reply_text("2")

async def us(update,context):
    msg=update.message.text
    await update.message.reply_text(f"hello {msg}")

# Create an Application instance
application = Application.builder().token('8354226566:AAHJ5HR86OuA4KIxs2nyhBMIHWNiAqC-aNo').build()

# Add handlers to the application
application.add_handler(CommandHandler('start', start))

application.add_handler(CommandHandler('help', help_command))

application.add_handler(CommandHandler('about', about))

application.add_handler(MessageHandler(filters.TEXT &~filters.COMMAND,us))


# Start polling
application.run_polling()

