from PIL import Image
import discord
import requests
import io
import random
from discord import app_commands
from commands import wasabi, chat, ayataka
from env import discord_api_key

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await tree.sync()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await tree.process_commands(message)


@tree.command(name="wasabi", description="wasabiコマンドです。")
async def wasabi_command(interaction:  discord.interactions.Interaction):
    await wasabi.wasabi_command(interaction)


@tree.command(name="chat", description="わさびに質問できるコマンドです。")
async def chat_command(interaction: discord.Interaction, text: str):
    await chat.chat_command(interaction, text)


@tree.command(name="ayataka", description="ayatakaコマンドです。")
async def ayataka_command(interaction:  discord.interactions.Interaction):
    await ayataka.ayataka_command(interaction)
API_URL = "https://api-inference.huggingface.co/models/Linaqruf/anything-v3.0"
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content


def generate_and_save_image(query_text, save_path):
    image_bytes = query({
        "inputs": query_text,
    })
    image = Image.open(io.BytesIO(image_bytes))
    image.save(save_path, overwrite=True)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!wsmoe":
        number = random.randint(0, 3000000)
        query_text = f"A girl with moe green hair who personified wasabi{number}"
        save_path = "image/images.jpg"
        generate_and_save_image(query_text, save_path)
        with open(save_path, "rb") as f:
            image_data = f.read()
        await message.channel.send(file=discord.File(io.BytesIO(image_data), filename="image.jpg"))

    if message.content == "!wsmoe-sm":
        number = random.randint(0, 3000000)
        query_text = f"A girl with green hair who personified wasabi  Noterotic 　{number}"
        save_path = "image/images-sm.jpg"
        generate_and_save_image(query_text, save_path)
        with open(save_path, "rb") as f:
            image_data = f.read()
        await message.channel.send(file=discord.File(io.BytesIO(image_data), filename="image.jpg"))
    if message.content == "!wsmoe-r18":
        number = random.randint(0, 3000000)
        query_text = f"A girl with moe green hair who personified wasabi flat chest {number}"
        save_path = "image/images-r18.jpg"
        generate_and_save_image(query_text, save_path)
        with open(save_path, "rb") as f:
            image_data = f.read()
        await message.channel.send(file=discord.File(io.BytesIO(image_data), filename="image.jpg"))
client.run(discord_api_key)
