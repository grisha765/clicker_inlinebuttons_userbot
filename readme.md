# clicker_inlinebuttons_userbot
A clicker bot for automatically pressing inline buttons in Telegram bots.

## Deploy to Podman

### AntiMute

1. Navigate to the directory:
    ```bash
    cd antimute/
    ```

2. Build the project:
    ```bash
    podman build -t antimute:latest -f dockerfile .
    ```

   This command builds a Podman image from the `dockerfile` within the `antimute` directory. It packages all necessary components for the AntiMute bot to run.

3. Run the project:
    ```bash
    podman run --rm -it \
    -v $HOME/sessions/:/app/sessions/:z \
    -e API_ID="tg_api_id" \
    -e API_HASH="tg_api_hash" \
    -e USERNAMES="@user1 @user2 @user3" \
    antimute:latest
    ```

   - `-v $HOME/sessions/:/app/sessions/:z`: Mounts a local directory to store session files, ensuring the bot can persist login sessions between runs.
   - `API_ID` and `API_HASH`: These are required for authenticating with the Telegram API. You must replace `tg_api_id` and `tg_api_hash` with your own values from [my.telegram.org](https://my.telegram.org).
   - `USERNAMES`: List the Telegram usernames that should not be muted. The bot monitors messages and ensures these users are protected from being muted in relevant chats.

### ChaseMute

1. Navigate to the directory:
    ```bash
    cd chasemute/
    ```

2. Build the project:
    ```bash
    podman build -t chasemute:latest -f dockerfile .
    ```

   This step builds the Podman image for the ChaseMute bot using the Dockerfile in the `chasemute` directory, ensuring the project is ready to run.

3. Run the project:
    ```bash
    podman run --rm -it \
    -v $HOME/sessions/:/app/sessions/:z \
    -e API_ID="tg_api_id" \
    -e API_HASH="tg_api_hash" \
    -e USER_MAIN="@user1" \
    -e USER_CHASE="@user2" \
    chasemute:latest
    ```

   - `API_ID` and `API_HASH`: Used to authenticate the bot with Telegram.
   - `USER_MAIN`: The main username of the user that the bot should track and mute or protect as necessary.
   - `USER_CHASE`: The secondary username that the bot should monitor for specific interactions (votes to mute or protect).

   The bot listens for votes in Telegram groups and acts on behalf of the specified users to either mute or protect them during "mute votes" initiated by other bots (e.g., [anarchy_bot](https://github.com/gmankab/anarchy_bot)).

#### Designed for use with [anarchy_bot](https://github.com/gmankab/anarchy_bot)
