#google sheet key: 13V9PNOB6ZfVIdO-G3XNnrgfQqB88P4OpObxQqomrf3k
import gspread
from gspread.utils import A1_ADDR_ROW_COL_RE
import gspread_formatting as gsfm
from  photo import photo_gen, ratio
import json

from oauth2client.service_account import ServiceAccountCredentials
from instabot import Bot


class ig_creds:
    username = ""
    password = ""

#Setup
#Add things to the cookies json
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

#Read credentials from IG json
ig_json = open("ig_creds.json", "r")
json_object = json.load(ig_json)

ig_creds.username = json_object["username"]
ig_creds.password = json_object["password"]
ig_json.close()


#Google sheet init
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
client = gspread.authorize(creds)

#IG bot init
bot = Bot()

#Main
sheet = client.open("Post responses").sheet1

a = 2

class p:
    ratio = ""
    tcolour = ""
    bgcolour = ""
    string = ""
    forma = ""


while True:
    try:
        p.ratio = sheet.acell(f"I{a}").value.split(" ")[0]
        p.string = sheet.acell(f"E{a}").value
        p.caption = sheet.acell(f"F{a}").value if sheet.acell(f"F{a}").value == None else ""
        p.bgcolour = sheet.acell(f"G{a}").value.split("(")[-1][:-1]
        p.tcolour = sheet.acell(f"H{a}").value.split("(")[-1][:-1]
        p.forma = gsfm.functions.get_user_entered_format(sheet, f"K{a}").backgroundColorStyle.rgbColor

        print(p.forma)


        if p.forma.alpha == 1.0:
            pass
        elif p.forma.red == 1.0:
            pass
        elif p.forma.green == 1.0:
            photo_gen(ratio=ratio.ratios[p.ratio], tcolour=p.tcolour, bgcolour=p.bgcolour, string=p.string)



    except AttributeError:
        print("out")
        break
    
    
    a += 1
    print(a)

print(p.forma)
#bot.login(username="info.wtsmcsecret@gmail.com", password="ahPT~y?{@g:W8bBS")

#bot.upload_photo(photo="output.jpg", caption="Test.")
