from telegram import Update,ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler
async def start(update: Update, context) -> None:
    reply_markup=ReplyKeyboardMarkup('/start')
    if "name"in context.user_data:
        name=context.user_data["name"]
    await update.message.reply_text(f"hello{name}")
async def set(update,context):
    await update.message.reply_text("enter your name:")
async def get(update,context):
    user_name=update.message.text
    context.user_data["name"]=user_name
applicaton=Application.builder().token("8525901841:AAGzfS1dkUnhx2ukGWZJy5BDuGvmAuk5xds").build()
applicaton.add_handler(CommandHandler("start", start))
applicaton.run_polling()