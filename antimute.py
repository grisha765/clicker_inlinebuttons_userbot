from pyrogram import Client, filters
from argparse import ArgumentParser
import asyncio
parser = ArgumentParser(description='User-Бот для автоматического голосания против мута самого себя для гманкабота.')
parser.add_argument('-u', '--username', nargs='+', type=str, help='Твой username через "@", можно несколько.')
args = parser.parse_args()
if not args.username:
    parser.error('Аргумент username является обязательным. (-u @USERNAME или --username @USERNAME), --help для дополнительной информации.')

api_id = int(id)
api_hash = str(hash)
usernames = args.username

bot = Client(usernames[0], api_id=api_id, api_hash=api_hash)

@bot.on_message(filters.chat("gmankachat"))
async def handle_messages(client, message):
    if message.from_user.username == "gmanka3_anarchy_bot":
        lines = message.text.split("\n")
        mute_target = lines[0].split(' ')[1].rstrip('?')
        buttons_callback_data = []
        buttons = message.reply_markup.inline_keyboard
        for row in buttons:
            for button in row:
                callback_data = button.callback_data
                buttons_callback_data.append(callback_data)
        if any(user in mute_target for user in usernames):
            await client.request_callback_answer(
                chat_id=message.chat.id,
                message_id=message.id,
                callback_data=buttons_callback_data[1]
            )
            return
bot.run()
