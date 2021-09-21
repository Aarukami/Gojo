   
from Gojo.tevents import register
from Gojo import telethn as tbot
TMP_DOWNLOAD_DIRECTORY = "./"
from telethon import events
import os
from PIL import Image
from datetime import datetime
from telegraph import Telegraph, upload_file, exceptions
gojo = "GOJO"
telegraph = Telegraph()
r = telegraph.create_account(short_name=gojo)
auth_url = r["auth_url"]
