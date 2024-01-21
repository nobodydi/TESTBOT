# Telegram Bot for Pasting Code to Pastebin

This is a simple Telegram bot that allows users to send code, and the bot pastes it to Pastebin, providing the user with the Pastebin link.

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

## Deploy to Heroku

You can deploy this Telegram bot to Heroku. Follow the steps below:

1. **Create a Heroku Account:**
   If you don't have a Heroku account, [sign up](https://signup.heroku.com/) for free.

2. **Fork this Repository:**
   Fork this repository to your GitHub account.

3. **Create a New Heroku App:**
   - Go to the [Heroku Dashboard](https://dashboard.heroku.com/).
   - Click on the "New" button and choose "Create new app."
   - Set a unique app name and choose your region.

4. **Configure Environment Variables:**
   - In the Heroku app dashboard, navigate to the "Settings" tab.
   - Click on "Reveal Config Vars" and add the following:
     - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
     - `PASTEBIN_API_KEY`: Your Pastebin API key.

5. **Deploy the App:**
   - Connect your GitHub repository to your Heroku app.
   - Manually deploy the app from the "Deploy" tab.

6. **Run the Bot:**
   - Once deployed, go to the "Resources" tab in your Heroku app dashboard.
   - Make sure the worker dyno is turned on.

7. **Enjoy!**
   Your Telegram bot should be up and running on Heroku.

**Note:** Remember to keep your API tokens confidential. Do not expose them in public repositories.
