import os

FFMPEG_DIR = f'{os.getcwd()}\\ffmpeg'
TOKEN = os.getenv('tiktok_telegram_bot_token')
SQL_DB_FL = 'sql.db'
OWNER_ID = 880708503

os.environ['PATH'] += FFMPEG_DIR
