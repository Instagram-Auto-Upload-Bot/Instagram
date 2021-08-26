import json

class IG_creds:


    def __init__(self):
        self.username = ""
        self.password = ""
    
        #Setup
        #Add things to the cookies 
        try:
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
        
        except:
            pass

        finally:
            #Read credentials from IG json
            ig_json = open("ig_creds.json", "r")
            json_object = json.load(ig_json)

            self.username = json_object["username"]
            self.password = json_object["password"]
            ig_json.close()
