import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram



if __name__ == "__main__" :
    if not os.path.isdir(Config.D:\):
        os.makedirs(Config.D:\)
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "RenameBot",
        bot_token=Config.7591552604:AAHrwJwmVGwxbNTDphs-ku9wTisamrUuk0U,
        api_id=Config.25132804,
        api_hash=Config.843d95d64eba173d7ef49ed4bb1440a8,
        plugins=plugins
    )
    Config.AUTH_USERS.add(861055237)
    app.run()
