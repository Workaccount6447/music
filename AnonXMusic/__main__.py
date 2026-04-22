import asyncio
import threading
import os
from flask import Flask

# ====== YOUR EXISTING IMPORTS (KEEP THEM) ======
from AnonXMusic import app  # or whatever your main bot import is
from AnonXMusic.core.call import Anony
from AnonXMusic.utils.database import get_banned_users, get_gbanned
# (keep all your existing imports here)

# ====== FLASK SETUP ======
web = Flask(__name__)

@web.route("/")
def home():
    return "AnonXMusic Bot is running!"

# ====== YOUR EXISTING INIT FUNCTION (KEEP AS IS) ======
async def init():
    # your existing startup logic
    await app.start()
    await Anony.start()

    banned_users = await get_banned_users()
    gbanned_users = await get_gbanned()

    print("Bot Started Successfully!")

    await idle()  # if you already have this

# ====== START BOT IN BACKGROUND ======
def start_bot():
    asyncio.run(init())

# ====== MAIN ENTRY POINT ======
if __name__ == "__main__":
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()

    web.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8000)),
        debug=False,
        use_reloader=False
)
