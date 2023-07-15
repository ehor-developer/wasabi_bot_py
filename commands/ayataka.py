import discord
import random

async def ayataka_command(interaction: discord.Interaction):
    ayataka_list = ["https://pbs.twimg.com/media/FypOqRdakAALzf9?format=jpg&name=large",
                    "https://pbs.twimg.com/media/FypOgQfaUAAf-Wv?format=jpg&name=large",
                    "https://pbs.twimg.com/media/FyYa8RJaQAAah2W?format=jpg&name=medium",
                    "https://pbs.twimg.com/media/FyKS0r5aAAAps7D?format=jpg&name=large",
                    "https://pbs.twimg.com/media/FyD33IGaIAUfsEv?format=jpg&name=large"]
    ayataka = random.choice(ayataka_list)
    await interaction.response.send_message(f"今日の綾鷹！{ayataka}")
