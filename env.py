import os
from dotenv import load_dotenv

load_dotenv()  # .env ファイルから環境変数を読み込む

openai_api_key = os.getenv("OPENAI_API_KEY")
discord_api_key = os.getenv("DISCORD_API_KEY")
ilust_api = os.getenv("ILUST_API_KEY")