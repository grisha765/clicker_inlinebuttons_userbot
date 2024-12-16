from config.config import Config
from pyrogram import Client, filters

from modes.chasemute import chasemute_func
from modes.antimute import antimute_func

from config import logging_config
logging = logging_config.setup_logging(__name__)

app = Client(f"{Config.sessions_path}/{Config.usermain.strip('@')}", api_id=Config.tg_id, api_hash=Config.tg_hash)

@app.on_message(filters.group)
@app.on_edited_message(filters.group)
async def handle_messages(client, message):
    mode = Config.mode
    if mode == 'chasemute':
        if not Config.userchase:
            logging.error('Env userchase is not set')
            return
        await chasemute_func(client, message)
    if mode == 'antimute':
        if not Config.usernames:
            logging.error('Env usernames is not set')
            return
        await antimute_func(client, message)
    else:
        logging.error('Env mode is not set')
        return

async def start_bot():
    logging.info("Launching the bot...")
    await app.start()

async def stop_bot():
    logging.info("Stopping the bot...")
    await app.stop()

if __name__ == "__main__":
    raise RuntimeError("This module should be run only via main.py")
