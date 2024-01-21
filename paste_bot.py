from pbwrap import Pastebin

# Telegram Bot Token
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
# Pastebin API Key
PASTEBIN_API_KEY = 'YOUR_PASTEBIN_API_KEY'

# Initialize Telegram Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Initialize Pastebin client
pastebin = Pastebin(api_dev_key=PASTEBIN_API_KEY)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Send me any code, and I'll paste it to Pastebin for you.")

@bot.message_handler(func=lambda message: True)
def paste_to_pastebin(message):
    chat_id = message.chat.id
    code_to_paste = message.text

    try:
        # Create a new paste on Pastebin
        paste_url = pastebin.create_paste(code_to_paste)
        bot.send_message(chat_id, f"Your code has been pasted to Pastebin! Here is the link:\n{paste_url}")

    except Exception as e:
        bot.send_message(chat_id, f"An error occurred: {str(e)}")

# Start the bot
if __name__ == "__main__":
    bot.polling()
