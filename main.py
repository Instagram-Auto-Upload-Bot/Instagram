#google sheet key: 13V9PNOB6ZfVIdO-G3XNnrgfQqB88P4OpObxQqomrf3k
from logging import shutdown
import gspread
import shutil
from gspread_formatting import *
import pprint
from gspread_formatting.functions import get_user_entered_format
from oauth2client.service_account import ServiceAccountCredentials
from instabot import Bot

shutil.rmtree("./config")

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Post responses").sheet1

data = sheet.get_all_records()

forma = get_user_entered_format(sheet, cols="G")

row = sheet.row_values(2)

print(row)
print(forma)

bot = Bot()

bot.login(username="info.wtsmcsecret@gmail.com", password="ahPT~y?{@g:W8bBS")
