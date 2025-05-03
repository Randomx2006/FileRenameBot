import logging
import os
import pyrogram

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config:
    DOWNLOAD_LOCATION = "./downloads"
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7591552604:AAHrwJwmVGwxbNTDphs-ku9wTisamrUuk0U")
    APP_ID = int(os.environ.get("APP_ID","25132804"))
    API_HASH = os.environ.get("API_HASH", "843d95d64eba173d7ef49ed4bb1440a8")
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "7686184938").split(","))

if __name__ == "__main__":
    if not os.path.isdir(Config.DOWNLOAD_LOCATION):
        os.makedirs(Config.DOWNLOAD_LOCATION)
    
    plugins = dict(root="plugins")
    
    app = pyrogram.Client(
        "RenameBot",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins
    )
    
    app.run()
