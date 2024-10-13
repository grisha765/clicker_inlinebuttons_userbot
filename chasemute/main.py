from pyrogram import Client, filters
import os

api_id = int(os.getenv('API_ID'))
api_hash = os.getenv('API_HASH')
usermain = os.getenv('USER_MAIN')
userchase = os.getenv('USER_CHASE')
sessions_path = os.getenv('SESSIONS_PATH')

if not os.path.exists(sessions_path):
    os.makedirs(sessions_path)

bot = Client(f"{sessions_path}/{usermain.strip('@')}", api_id=api_id, api_hash=api_hash)

@bot.on_edited_message(filters.group)
@bot.on_message(filters.group)
async def handle_messages(client, message):
    if message.from_user.username == "gmanka3_anarchy_bot":
        lines = message.text.split("\n")
        votes_for_mute = []
        votes_against_mute = []
        collect_votes_for = False
        collect_votes_against = False
        for item in lines:
            if item == 'votes for mute:':
                collect_votes_for = True
                continue
            elif item == 'votes against mute:':
                collect_votes_for = False
                collect_votes_against = True
                continue

            if collect_votes_for and item != '':
                votes_for_mute.append(item)
            elif collect_votes_against and item != '':
                votes_against_mute.append(item)
        buttons_callback_data = []
        buttons = message.reply_markup.inline_keyboard
        for row in buttons:
            for button in row:
                callback_data = button.callback_data
                buttons_callback_data.append(callback_data)

        if userchase in votes_for_mute:
            await client.request_callback_answer(
                chat_id=message.chat.id,
                message_id=message.id,
                callback_data=buttons_callback_data[0]
            )
            return

        if userchase in votes_against_mute:
            await client.request_callback_answer(
                chat_id=message.chat.id,
                message_id=message.id,
                callback_data=buttons_callback_data[1]
            )
            return
bot.run()
