import os

FFMPEG_DIR = f'{os.getcwd()}\\ffmpeg'
TOKEN = os.getenv('zwytbot_token')
SQL_DB_FL = 'sql.db'
OWNER_ID = 880708503

os.environ['PATH'] += f';{FFMPEG_DIR}'
