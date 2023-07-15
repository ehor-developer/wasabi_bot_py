import discord
from discord import app_commands
from commands import wasabi, chat, ayataka, voice, wsmoe
from env import discord_api_key
#初期設定
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    await tree.sync()
    await client.change_presence(activity = discord.Activity(name="辛いわさび", type=discord.ActivityType.playing))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await tree.process_commands(message)

#コマンド一覧

@tree.command(name="wasabi", description="ランダムな会話をします")
async def wasabi_command(interaction:  discord.interactions.Interaction):
    await wasabi.wasabi_command(interaction)


@tree.command(name="voice", description="ランダムな音声を通話で再生します！")
async def wasabi_command(interaction:  discord.interactions.Interaction):
    await voice.wasabi_command(interaction)


@tree.command(name="chat", description="わさびに質問できるコマンドです。")
async def chat_command(interaction: discord.Interaction, text: str):
    await chat.chat_command(interaction, text)


@tree.command(name="ayataka", description="今日の綾鷹を送信します。")
async def ayataka_command(interaction:  discord.interactions.Interaction):
    await ayataka.ayataka_command(interaction)

@tree.command(name="wsmoe", description="通常の萌え画像を送信します。")
async def wsmoe_command(interaction:  discord.interactions.Interaction):
    await wsmoe.wsmoe_command(interaction)

@tree.command(name="wsmoe-r18", description="萌え画像（R18モード）を送信します。")
async def wsmoe_r18_command(interaction:  discord.interactions.Interaction):
    await wsmoe.wsmoe_r18_command(interaction)

@tree.command(name="wsmoe-text", description="自由なプロンプトの画像を送信します。")
async def wsmoe_text_command_command(interaction: discord.Interaction, text: str):
    await wsmoe.wsmoe_text_command(interaction, text)


client.run(discord_api_key)
