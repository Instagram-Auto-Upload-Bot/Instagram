#google sheet key: 13V9PNOB6ZfVIdO-G3XNnrgfQqB88P4OpObxQqomrf3k
import gspread
from functions import IG_creds
import formats
from gspread.utils import A1_ADDR_ROW_COL_RE
import gspread_formatting as gsfm
from  photo import photo_gen, ratio
import json

from oauth2client.service_account import ServiceAccountCredentials
from instabot import Bot


#Google sheet init
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("google_creds.json", scope)
client = gspread.authorize(creds)

#IG bot/ credential class init
bot = Bot()
ig_creds = IG_creds()

bot.login(username=ig_creds.username, password=ig_creds.password)
print(bot.username)

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
        p.caption = " " if sheet.acell(
            f"F{a}").value == None else sheet.acell(f"F{a}").value
        p.bgcolour = sheet.acell(f"G{a}").value.split("(")[-1][:-1]
        p.tcolour = sheet.acell(f"H{a}").value.split("(")[-1][:-1]
        p.forma = gsfm.functions.get_user_entered_format(sheet, f"K{a}")

    
        print(p.forma.backgroundColor)
        print(formats.bg_styles.green)
        print(p.caption)

        if p.forma.backgroundColor == formats.bg_styles.black.backgroundColor:
            pass
        elif p.forma.backgroundColor == formats.bg_styles.red.backgroundColor:
            pass
        elif p.forma.backgroundColor == formats.bg_styles.green.backgroundColor:
            print("yes")
            photo_gen(ratio=ratio.ratios[p.ratio], tcolour=p.tcolour, bgcolour=p.bgcolour, string=p.string)
            gsfm.functions.format_cell_range(sheet, f"K{a}", formats.bg_styles.black)
            bot.upload_photo("output.jpg", caption=p.caption)

    except AttributeError as error:
        print("out")
        raise(error)
        break

    except Exception as error:
        raise(error)

    print(a)
    a += 1
    




