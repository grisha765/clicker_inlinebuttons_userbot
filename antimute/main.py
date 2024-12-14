from pyrogram import Client, filters
import os

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
usernames = os.getenv('USERNAMES', '').split()
sessions_path = os.getenv('SESSIONS_PATH')

if not usernames:
    raise ValueError('Переменная окружения USERNAMES является обязательной.')

if not os.path.exists(sessions_path):
    os.makedirs(sessions_path)

bot = Client(f"{sessions_path}/{usernames[0].strip('@')}", api_id=api_id, api_hash=api_hash)

@bot.on_message(filters.chat("gmankachat"))
async def handle_messages(client, message):
    if message.from_user.username == "g_anarchy_bot":
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
