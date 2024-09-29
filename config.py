import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

# Filled variables
SESSION_NAME = "MyBotSession"  # You can change this to any name you prefer

SESSION2 = "BQFToMkAKe5Ozfqc7R_Y8p0zQb6ShWVVhZkxtahYFE73F-UisrR-mMGoj5_aUNgTWkW-ueDdlyRLUJ2qBEjWm1OiNwES9t31CaAl-z4Tu6SzeSxRZeeAw4fu3X6mu8J74RKAJtFrCi_rh3zwwYR_z78DzzFlZmZC4G3COgg-3frD8y6JSSwD5Gq-zEPh0nUEVAzt-eoa7uaPi5QR78D_bQd6ok8EhqY3DQHcmIab23Zaf8GWGtv-Td4j1fvmMheM2iw5YasULrV3jXxzfiYVGbkhxj2FwjL0Ju272FonaOnHaP2ZE7nPBRP19XdO9HvmBSmSUdg6Jka7lC_3CtY_-JFB-A0tIQAAAABiNGsPAA"

SESSION3 = None
SESSION4 = None
SESSION5 = None

BOT_TOKEN = "6327930809:AAEWwQaVMw_a0pxotKkM8C2BmBFaF3jLW6M"
BOT_NAME = "Iᴛᴀᴄʜɪ ᴍᴜsɪᴄ ʙᴏᴛ"  # Updated bot name

API_ID = 22257865
API_HASH = "97fc23c20e06f411abbf36cad8e118ce"
MONGO_DB_URL = "mongodb+srv://Cloner:Cloner@cluster0.cgc6t.mongodb.net/?retryWrites=true&w=majority"
OWNER_NAME = "itachi uchiha"
OWNER_USERNAME = "itachi_ztx"
ALIVE_NAME = "Zaid"
BOT_USERNAME = "@Itachising_bot"  # Updated bot username
OWNER_ID = 1647602447  # Updated owner ID
ASSISTANT_NAME = "Zaid2_Assistant"
GROUP_SUPPORT = "TheSupportChat"
UPDATES_CHANNEL = "TheUpdatesChannel"
HEROKU_APP_NAME = None  # Fill in if you have it
HEROKU_API_KEY = None  # Fill in if you have it
SUDO_USERS = [1647602447]  # Only your user ID as the Sudo user
COMMAND_PREFIXES = ["/", "!", "."]  # List of command prefixes
ALIVE_IMG = "https://telegra.ph/file/fc9d87ffd1c6f828eb7fc.png"
START_PIC = "https://telegra.ph/file/a414e2cdfeaa7d4414b89.png"
DURATION_LIMIT = 60  # Duration in minutes
UPSTREAM_REPO = "https://github.com/ITZ-ZAID/Zaid-Vc-Player"
PLAY_IMG = "https://telegra.ph/file/10b1f781170b1e1867f68.png"
QUE_IMG = "https://telegra.ph/file/b95c13eef1ebd14dbb458.png"
CMD_IMG = "https://telegra.ph/file/66518ed54301654f0b126.png"
VIDEO_IMG = "https://telegra.ph/file/6213d2673486beca02967.png"
SKIP_IMG = "https://telegra.ph/file/f02efde766160d3ff52d6.png"
NEXT_IMG = "https://telegra.ph/file/f02efde766160d3ff52d6.png"
HEROKU_MODE = None  # Fill in if you have it
