import random
import discord
import requests
import io
from PIL import Image

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


async def wsmoe_command(interaction: discord.Interaction):
    number = random.randint(0, 3000000)
    query_text = f"A girl with moe green hair who personified wasabi {number}"
    save_path = "image/images.jpg"
    await interaction.response.defer()
    generate_and_save_image(query_text, save_path)
    file = discord.File(save_path)
    await interaction.followup.send(file=file)

async def wsmoe_r18_command(interaction: discord.Interaction):
    number = random.randint(0, 3000000)
    query_text = f"A girl with moe green hair who personified wasabi nsfw {number}"
    await interaction.response.defer()
    save_path = "image/images_R18.jpg"
    generate_and_save_image(query_text, save_path)
    file = discord.File(save_path)
    await interaction.followup.send(file=file)


async def wsmoe_text_command(interaction: discord.Interaction, text: str):
    number = random.randint(0, 3000000)
    query_text = f"A girl with moe green hair who personified wasabi {text} {number}"
    await interaction.response.defer()
    save_path = "image/images_custom.jpg"
    generate_and_save_image(query_text, save_path)
    file = discord.File(save_path)
    await interaction.followup.send(file=file)
