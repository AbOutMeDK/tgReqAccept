# © 𝘼𝙗𝙊𝙪𝙩𝙈𝙚_𝘿𝙆 🌿

import os
import logging
from os import environ
from logging.handlers import RotatingFileHandler
from time import time

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your Telegram ID Not Mandatory for pending request accepting 
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

#Port
PORT = os.environ.get("PORT", "8080")

#no need to change
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Pyrogram V2 string session
SESSION = environ.get("SESSION")

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
