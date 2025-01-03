import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 23586960
API_HASH = "3211ab72737c484d82149623822ccc5e"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7822506982:AAHpXle-jtYYagYwLatf0XdtjBOwV19yRQQ"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://sonupersonalmails:sonupersonalmails@cluster0.l0aoo.mongodb.net/"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002320075111

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7176363449

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/tanishimusic"
SUPPORT_GROUP = "https://t.me/tanishimusicgroup"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BQFn6JAAJFMCfbSslpq6hazto4hrZx7HUATmwDEoc2AVH18CdOxGecPMq-0_2KYfrkTQn5u4plKpyT1g8s1TwuRv_UJ-flX_m00DPKzSDnd2jb2Z6VLod4GYpH1_A9495shHT4K-ovfYIEv9hkcOa-vrzRDDX1B2UeSAbkmCuCQ0d3E5JOFM-JaWK7A_bbPNeqjEdHXHNsYK5YkLSpqxl4_BDvi-uDNPdf2QCRuERHAtmY8-5OeDEIlsHaOq7VmBr_SitxsxAiTaql3fpjWvrQEZv6Y9JeWFNT4BJRFRqaKp-8244NFD96LOAM1UKTNhMr5sjoKF-POySFzzO1SBL2kQlUSIKgAAAAGrvp25AA"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"

PING_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"
STATS_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"
STREAM_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/195009cd51e00071e1d42-fc060c626ea583f58e.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
