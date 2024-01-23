import discord, discord.webhook, asyncio, os
from discord.ext import commands
import plugins.discord.tokenes as tokenes
from app.log import logger
"""
bot 本体.
"""

on_conversion = False
current_channel = None
intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)

# Load cogs
async def load_extensions():
    directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cogs")
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            logger.info(f"Loading {filename[:-3]}")  
            await client.load_extension(f"{filename[:-3]}")

async def run_bot():
    logger.info("Discord bot 启动中...")
    async with client:
        try:
            await load_extensions()
            await client.start(tokenes.bot_token)
        except Exception as e:
            logger.error(f"Bot 启动失败: {e}")
