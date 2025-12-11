from telegram import Update

from telegram.ext import Application, CommandHandler

# Define the start function
async def start(update: Update, context) -> None:
    await update.message.reply_text("Welcome, I'm at your service!")

# Create an Application instance
application = Application.builder().token('8475936738:AAEyiXki4JAJDGOrVy7LjR2Akw6tFEMkiC8').build()

# Add handlers to the application
application.add_handler(CommandHandler('start', start))

# Start polling
application.run_polling()

