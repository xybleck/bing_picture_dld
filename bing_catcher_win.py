#! -*- coding: utf-8 -*-

import requests
import re
import os
import datetime

TYEAR = datetime.datetime.now().year
TYEAR = str(TYEAR) if TYEAR > 9 else "0"+str(TYEAR)
TMONTH = datetime.datetime.now().month
TMONTH = str(TMONTH) if TMONTH > 9 else "0"+str(TMONTH)
TDAY = datetime.datetime.now().day
TDAY = str(TDAY) if TDAY > 9 else "0"+str(TDAY)
BING_URL = "https://bing.com"
BING_WALLPAPER_FILENAME = TYEAR + TMONTH + TDAY + "_bing_wallpaper.jpeg"
BING_WALLPAPER_LOCAL_PATH = os.path.join('C:\\Users\\j_del\\Pictures\\BingWallpaper', BING_WALLPAPER_FILENAME)


def main():
  r = requests.get(BING_URL)
  if r.status_code == 200:
    for _ in r.text.split(" "):
      if re.match(r'^url\(', _):
        bing_wallpaper_url = "https://bing.com" + str(_.split("(")[1].split(")")[0])
        r = requests.get(bing_wallpaper_url)
        if r.status_code == 200:
          f = open(BING_WALLPAPER_LOCAL_PATH, 'wb')
          f.write(r.content)
          f.close()


if __name__ == "__main__":
  main()
