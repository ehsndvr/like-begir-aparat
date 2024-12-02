import requests
import time
import re
import os
import termcolor

ARMYSEC_TEXT = r"""
 ▄▄▄       ██▀███   ███▄ ▄███▓▓██   ██▓  ██████ ▓█████  ▄████▄
▒████▄    ▓██ ▒ ██▒▓██▒▀█▀ ██▒ ▒██  ██▒▒██    ▒ ▓█   ▀ ▒██▀ ▀█
▒██  ▀█▄  ▓██ ░▄█ ▒▓██    ▓██░  ▒██ ██░░ ▓██▄   ▒███   ▒▓█    ▄
░██▄▄▄▄██ ▒██▀▀█▄  ▒██    ▒██   ░ ▐██▓░  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒
 ▓█   ▓██▒░██▓ ▒██▒▒██▒   ░██▒  ░ ██▒▓░▒██████▒▒░▒████▒▒ ▓███▀ ░
 ▒▒   ▓▒█░░ ▒▓ ░▒▓░░ ▒░   ░  ░   ██▒▒▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░
  ▒   ▒▒ ░  ░▒ ░ ▒░░  ░      ░ ▓██ ░▒░ ░ ░▒  ░ ░ ░ ░  ░  ░  ▒
  ░   ▒     ░░   ░ ░      ░    ▒ ▒ ░░  ░  ░  ░     ░   ░
      ░  ░   ░            ░    ░ ░           ░     ░  ░░ ░
                               ░ ░                     ░
"""
WELCOME_TEXT = """
[---]        LikeBegir-Aparat                 [---]
[---]        Created by : \033[31mArmySEC (ehsndvr)   \033[34m[---]
[---]        \033[34mVersion : \033[31m1.0.0\033[37m                  \033[34m[---]



"""
print(termcolor.colored(ARMYSEC_TEXT, "red"))
print(termcolor.colored(WELCOME_TEXT, "blue").center(
    os.get_terminal_size().columns))
def ChangeIP():
    try:
        os.system("service tor reload")
    except:
        return RestartTor()

def RestartTor():
    os.system("service tor start")
    return ChangeIP()

def SendLike(VideoTag , SleepTime):
    try:
        while True:
            time.sleep(SleepTime)
            Link = "https://www.aparat.com/api/fa/v1/video/video/show/videohash/{}?pr=1&mf=1&referer=direct".format(VideoTag)
            ChangeIP()
            Proxies = {"https":"socks5://127.0.0.1:9050" , "http":"socks5://127.0.0.1:9050"}
            FirstUrl = requests.get(Link , proxies = Proxies).json()
            if FirstUrl['included'][2]['attributes']['status'] == "unlike":
                Response = requests.get(FirstUrl['included'][2]['attributes']['link'] , proxies = Proxies).json()
                print("[+] LikeCount: {}".format(Response["data"]["attributes"]["cnt"]))
    except:
        SendLike(VideoTag , SleepTime)
def InputData():
    AparatLink = input("[+] input your aparat video link >> ")
    if re.search(r"(https|http):\/\/www\.aparat\.com\/v\/[a-zA-Z0-9]+\/" , AparatLink , re.MULTILINE):
        VideoTag = (AparatLink.split('/'))[4]
        if re.search(r"[a-zA-Z0-9]+" , VideoTag , re.MULTILINE):
            intSleepTime = input("[+] time to change Ip in Sec [type=60] >> ")
            os.system("service tor start")
            SendLike(VideoTag , int(intSleepTime))
        else:
            InputData()
    else:
        InputData()
    
InputData()

