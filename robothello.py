from telegram import Update

from telegram.ext import Application, CommandHandler

# Define the start function
async def start(update: Update, context) -> None:
    await update.message.reply_text("Welcome, I'm a robot!")

# Create an Application instance
application = Application.builder().token('8375163716:AAEQkkJ-bMOcjgOZBwWnI89eDRf36BIVwH8').build()

# Add handlers to the application
application.add_handler(CommandHandler('start', start))

# Start polling
application.run_polling()

