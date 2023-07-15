import discord
from env import openai_api_key
import openai

openai.api_key = openai_api_key

async def chat_command(interaction: discord.Interaction, text: str):
    prompt = text
    model_engine = "gpt-3.5-turbo"

    try:
        # ChatGPTに質問を送信して回答を取得
        completion = openai.ChatCompletion.create(
            model=model_engine,
            messages=[
                {
                    "role": "system",
                    "content": "あなたは、たしなむわさびという人です。あなたはスマホとガジェットが好きで、よく、パソコンを分解したり、スマホを修理しています。自分というのがあなたの一人称です。そのため自分を一人称にしてください。また回答の内容は、30字以内で回答してください。また、４割の確率で♨️の絵文字を最後に追加してください。温泉の絵文字を使わない場合、2割の確率で、文の最後に〜をつけてください。また、LINEなどで返信するような返し方をしてください。"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        response = completion["choices"][0]["message"]["content"]

        # 回答を送信
        await interaction.response.send_message(response)

    except Exception as e:
        error_message = f"エラーが発生しました: {str(e)}"
        await interaction.response.send_message(error_message)
