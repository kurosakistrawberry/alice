import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 21511354
API_HASH = "2f1042857f43cb02512bb2a3f46da9a3"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "8355791623:AAG3K74XvbBqVNwCPRix_N_nmENEdj_iSy4"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://thesimpposium:123098456765@simpposium@orihime.fqgoo6u.mongodb.net/?retryWrites=true&w=majority&appName=Orihime"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 120))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002318392631

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7891690909

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("orihime00gc")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-AA7r3K5PNGYBoNIeWWDA8L_iump_rBRnGJClOp4FRXEA_wO9JLjJ75X9")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/KurosakiEternity"
SUPPORT_GROUP = "https://t.me/+8VQeol08IElhNjRl"

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
STRING1 = "BQFIPLoArgvh5iCggnP9LtuF_g9QtiSyBNJCoxVEM9BTpFq4_prg00Y0ZOaIL8JOL9nOrFQcnaGOe2WTwQnqOdxPpBY9EbeN6Z8PsL0CnV9TyAWBX4Gr4xSNQfYleOXXYKRCGuFzcrPV5Ha7QQOA8BPsOeGZTabWwEonIrynvUaHb2mGOL_zN8rzmJyE99xK6LD422s9hlcgziaQSk_z3gRPWM6QAdO_xU4XuA6IqsOptdrBp654v52x9mmDUjiXIaPmVuphIi2RomH-eWojDN38yoPhR7E8Ba9Adqx497BF4YDEOYGo77RrQjjv6J4PEId9x0ML4Dw36Nm7cXE8TZpZQ4NkUgAAAAHWYaWdAA"
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


START_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"

PING_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"

PLAYLIST_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"
STATS_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"
TELEGRAM_AUDIO_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"
TELEGRAM_VIDEO_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"
STREAM_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/51f021dd9574d6b02c125-58b20c849c9a85bf64.jpg"


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


