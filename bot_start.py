import asyncio
import bot_client
from db.connection import init_db
import discord
from dotenv import load_dotenv
from os import getenv


intents = discord.Intents.default()
intents.message_content = True
discordbot = bot_client.Bot(command_prefix='}', intents=intents, help_command=None, cog_counter=0)

load_dotenv()
if not (TOKEN := getenv("DISCORD_BOT_TOKEN")):
    print('Token is empty.')
    exit(1)

async def confirmation():
    print('Created Discord Bot Instance.')

async def main() -> None:
    # Run other async tasks
    # USE ASYNC TASK GROUPS TO DO MULTIPLE TASKS AT A SINGLE TIME FOR EASY PARALLEL PROCESSING
    # https://docs.python.org/3/library/asyncio-task.html#task-groups
    await confirmation()
    await init_db()
    # Start the bot
    try:
        async with discordbot:
            await discordbot.start(TOKEN)
    except Exception as e:
        print(f'Could not start bot {e}')
        exit(1)

asyncio.run(main())

# Examples
# https://github.com/Rapptz/discord.py/tree/master/docs
# https://github.com/Rapptz/discord.py/tree/master/examples

# COG EXAMPLE
# https://github.com/Rapptz/discord.py/blob/master/docs/ext/commands/cogs.rst