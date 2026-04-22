import threading
import os
from flask import Flask

# Flask app (Render needs this)
app = Flask(__name__)

@app.route("/")
def home():
    return "Music bot is running"

# Import your existing main logic
def start_bot():
    import main  # or whatever your main file is called

if __name__ == "__main__":
    # Run bot in background
    threading.Thread(target=start_bot).start()

    # Run web server (main process)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
