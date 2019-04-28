# Disconnected
A discord bot coded in python with random features.
Made by: Antonio32A

## Features ##
- Gives offline or invisible people a role and removes the role when they go online.
- Gives people which have a role 1 another role 2 when they start typing and then removes the role 2 after 10 seconds.

## Selfhosting ##
### Windows ###
1. Download the ZIP file and extract it.
2. Open CMD and navigate to the extracted files using `cd path/to/extracted/files`
3. Install the latest version of python [here](https://www.python.org/).
4. Install the modules by executing this command in the CMD:
    ```
    py -3 -m pip install -r requirements.txt
    ```
5. Edit the config in `example_data.json` and then rename the file to `data.json`.
6. Start the bot by executing this command in the CMD:
    ```
    py main.py
    ```
### Ubuntu/Debian/Mint ###
1. Clone the repository (`git clone https://github.com/Antonio32A/Disconnected.git`) or download the ZIP file and extract it.
2. Navigate to the files using `cd path/to/extracted/files`
3. Install the latest version of python by executing these commands in the terminal:
    ```
    sudo apt-get update
    sudo apt-get install python3
    ```
4. Install the modules by executing this command in the terminal:
    ```
    python3 -m pip install -r requirements.txt
    ```
5. Edit the config in `example_data.json` and then rename the file to `data.json`.
6. Start the bot by executing this command in the terminal:
    ```
    python3 main.py
    ```

### Config variables ###
- `token` - Discord bot token.
- `invisible_role_id` - ID of the role which is given when the member goes offline/invisible and taken when the member goes online.
- `guild_id` - ID of the server where the bot gives or takes roles.
- `typing_role_id` - ID of the role which is given when the user has the `typer_role`.
- `typer_role_id` - ID of the role which allows a user to get the `typing_role` when they start typing.
