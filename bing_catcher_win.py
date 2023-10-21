#! -*- coding: utf-8 -*-

import requests
import re
import os
import sys
import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--directory', type=str, help="Folder path to save bing wallpaper")
args = parser.parse_args()

TYEAR = datetime.datetime.now().year
TYEAR = str(TYEAR) if TYEAR > 9 else "0"+str(TYEAR)
TMONTH = datetime.datetime.now().month
TMONTH = str(TMONTH) if TMONTH > 9 else "0"+str(TMONTH)
TDAY = datetime.datetime.now().day
TDAY = str(TDAY) if TDAY > 9 else "0"+str(TDAY)
BING_URL = "https://bing.com"
BING_WALLPAPER_FILENAME = TYEAR + TMONTH + TDAY + "_bing_wallpaper.jpeg"

if args.directory:
    BING_WALLPAPER_LOCAL_PATH = os.path.join(args.directory, BING_WALLPAPER_FILENAME)
    SUCCESS = "Wallpaper download success: " + BING_WALLPAPER_LOCAL_PATH
else:
   parser.print_help()
   sys.exit(1)




def bing_wallpaper_url() -> str:
    try:
        req = requests.get(BING_URL)
        if req.status_code == 200:
            for _ in req.text.split(" "):
                if re.match(r'^url\(', _):
                    bing_wallpaper_url = "https://bing.com" + str(_.split("(")[1].split(")")[0])
                    return bing_wallpaper_url
        else:
            raise SystemError("HTTPS request failed resolving wallpaper url")
        
    except Exception as e:
        print("Error: " + e)
        sys.exit(1)

def bing_wallpaper_img(url: str) -> bool:
    try:
        req = requests.get(url)
        if req.status_code == 200:
            f = open(BING_WALLPAPER_LOCAL_PATH, 'wb')
            f.write(req.content)
            f.close()
            return True
        else:
            raise SystemError("HTTPS request failed downloading wallpaper img")
            
    except Exception as e:
        print("Error: " + e)
        sys.exit(1)
        

def main():
    try:
        wu = bing_wallpaper_url()
        bing_wallpaper_img(wu)
        print(SUCCESS)
    
    except Exception as e:
        print("Error: " + e)
        sys.exit(0)


if __name__ == "__main__":
  main()
