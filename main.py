#google sheet key: 13V9PNOB6ZfVIdO-G3XNnrgfQqB88P4OpObxQqomrf3k
import gspread
import gspread_formatting.functions as gsfm
import json


from syncer import sync
from oauth2client.service_account import ServiceAccountCredentials
from instabot import Bot

#try:
#    shutil.rmtree("./config")
#except:
#    print("No need to delete config.")



def startup():
    cookie_json = open(
        "config\info.wtsmcsecret@gmail.com_uuid_and_cookie.json", "r+")
    json_object = json.load(cookie_json)
    json_object["cookie"]["ds_user"] = "info.wtsmcsecret@gmail.com"
    json_object["cookie"]["urlgen"] = "https://www.instagram.com/"
    cookie_json.close()

    cookie_json = open(
        "config\info.wtsmcsecret@gmail.com_uuid_and_cookie.json", "w+")
    json.dump(json_object, cookie_json)
    cookie_json.close()

    ig_json = open("ig_creds.json", "r")
    json_object = json.load(ig_json)
    global ig_creds
    class ig_creds: pass
    ig_creds.username = json_object["username"]
    ig_creds.password = json_object["password"]
    ig_json.close()


print(ig_creds.username)

def body():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
    client = gspread.authorize(creds)

    sheet = client.open("Post responses").sheet1

    forma = gsfm.get_user_entered_format(sheet, "G3").backgroundColorStyle.rgbColor
    row = sheet.row_values(2)

    print(row)
    print(forma)

    bot = Bot()

    bot.login(username="info.wtsmcsecret@gmail.com", password="ahPT~y?{@g:W8bBS")


def main():
    startup()
    body()

main()
