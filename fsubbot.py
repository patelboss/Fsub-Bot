import Config
import logging
from pyrogram import Client, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid


logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

API_ID = "14055090"
API_HASH = "a46f7b439d0afa45b7a69fc450f754e9"
BOT_TOKEN = "5632628980:AAEUq11V-CNJrP_KXJuZ_HkGp7UQo4EWCuo"


app = Client(
    ":memory:",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="ForceSubscribeBot"),
)


# Run Bot
if __name__ == "__main__":
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"Connected For Emo Network @{uname} Started Successfully!")
    idle()
    app.stop()
    print("Emo Network disconnected Bot stopped.")
