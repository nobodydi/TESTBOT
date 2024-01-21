# past_bot.py
import os
from pbwrap import Pastebin
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from config import TELEGRAM_BOT_TOKEN, PASTEBIN_API_KEY

# Initialize Pastebin client
pastebin = Pastebin(api_dev_key=PASTEBIN_API_KEY)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Welcome! Send me any code, and I'll paste it to Pastebin for you.")

def paste_to_pastebin(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    code_to_paste = update.message.text

    try:
        # Create a new paste on Pastebin
        paste_url = pastebin.create_paste(code_to_paste)
        update.message.reply_text(f"Your code has been pasted to Pastebin! Here is the link:\n{paste_url}")

    except Exception as e:
        update.message.reply_text(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Initialize the updater
    updater = Updater(TELEGRAM_BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))

    # Register a message handler for pasting code
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, paste_to_pastebin))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()
