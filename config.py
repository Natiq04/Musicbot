import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = 20235406
API_HASH = "968860b04772cb5b44f4ca8603bed9d3"
BOT_TOKEN = "6388818920:AAE5GYIPOzBoGeLn76HxfaiH1WHDV9jfhlQ"
MONGO_DB_URI = "mongodb+srv://abbasovnatiq828:natiq.12344321@cluster0.rmizp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
DURATION_LIMIT_MIN = 45
LOGGER_ID = -1002150762661
OWNER_ID = 7287936548
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
UPSTREAM_REPO = "https://github.com/Natiq04/Musicbot"
UPSTREAM_BRANCH = "master"
GIT_TOKEN = "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"
SUPPORT_CHANNEL = "https://t.me/GtaXatirelerKanal"
SUPPORT_CHAT = "https://t.me/silgiub"
AUTO_LEAVING_ASSISTANT = True
SPOTIFY_CLIENT_ID = "3de78b162b6f41ee860a93feee067cd1"
SPOTIFY_CLIENT_SECRET = "3a7face20ae24a078d210023c8f682b9"
PLAYLIST_FETCH_LIMIT = 75
TG_AUDIO_FILESIZE_LIMIT = 104857600
TG_VIDEO_FILESIZE_LIMIT = 104857600
BOTS_GROUP = -1002000608951
STRING1 = "AgFEDJQAFLrlDlM0mMu4pyIvCE5XoPa4yzwDDRMP3wxYG5yM1mGNFx_YfPOzezlej6ECAnVdBrAY73ref9wY9gxObGMOLqjentt8OkSLBUQ4di6ReOEtngf41VWg5HF-Ysy0S2pHj9DpLFRb4K_36H3eeT6IYf_2nkXBVvMK7l_MX8-hFmNhPN_pflRoxoSxFW26O9RDu2AL5PlxgRLwKf6OHB0ZNoKVTHaD26MuRbyOnbkrlmpX4XFJy_TSAZCwd-AVyecI6G6Y6RPOeG5NnnXikGHTOfUWILzNTQCTKMJGuC1wIdF5j5PxEll3NTJErKD-3M5bJUxIWLbmSWB3CaI0OpR0_AAAAAGd3P3lAA"
STRING2 = None
STRING3 = None
STRING4 = None
STRING5 = None

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
)
PLAYLIST_IMG_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
STATS_IMG_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
STREAM_IMG_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/09e8d4ced07b18a016ba7.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
