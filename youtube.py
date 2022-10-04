from pytube import Playlist, YouTube, exceptions
from colorama import Fore, init
from time import sleep
import sys
import time
import platform

init(autoreset=True)
z = """
  ______   _____   _____   __     __  _____    _______    ____  
 |___  /  / ____| |  __ \  \ \   / / |  __ \  |__   __|  / __ \ 
    / /  | |      | |__) |  \ \_/ /  | |__) |    | |    | |  | |
   / /   | |      |  _  /    \   /   |  ___/     | |    | |  | |
  / /__  | |____  | | \ \     | |    | |         | |    | |__| |
 /_____|  \_____| |_|  \_\ _  |_|    |_|         |_|     \____/ 
"""

# Greetings Because I love colors
name = platform.uname()[1]
print(Fore.BLUE + z)
time.sleep(1)
api_status = f"Hi {name} ... Welcome to the ZCRYPTO Youtube downloader .\n"
for char in api_status:
    sleep(0.010)
    sys.stdout.write(Fore.RED + char)
    sys.stdout.flush()
    sleep(0.010)
time.sleep(2)
print(f"{Fore.BLUE} - - - - - - - - - - - - - - - - - - - - - - - - - - -")
while True:
    question = input("Is your download a single Video or playlist?\n"
                     f"Type s for single video or p "
                     f" for Playlist ..\n")
    if question == "s":
        yt = YouTube(input(f"Video Link?\n"))
        name = yt.title
        link = yt.watch_url
        try:
            video = yt.streams.get_highest_resolution()
            print(f'{Fore.LIGHTGREEN_EX}Downloading video: {Fore.LIGHTBLUE_EX}{link}')
            video.download(output_path="Downloaded Videos")
            finish_download = f"Download is Finished !.\n"
            for char in finish_download:
                sleep(0.010)
                sys.stdout.write(Fore.LIGHTCYAN_EX + char)
                sys.stdout.flush()
                sleep(0.010)
            time.sleep(2)
            print(f"{Fore.BLUE} - - - - - - - - - - - - - - - - - - - - - - - - - - -")
        except exceptions:
            print(f'{Fore.LIGHTRED_EX}Video {link} is unavaialable, skipping.')

    elif question == "p":
        yt = Playlist(input(f"Playlist Link?\n"))
        number = 0
        for video in yt.videos:

            try:
                ha = video.streams.get_highest_resolution()
                print(f'{Fore.LIGHTGREEN_EX}Downloading video: {Fore.LIGHTBLUE_EX}{video.title}')
                strnumber = str(number)
                ha.download(output_path="Downloaded Videos", filename_prefix=strnumber + " ---")
                finish_download = f"Downloading {video.title} is Finished !.\n"
                for char in finish_download:
                    sleep(0.010)
                    sys.stdout.write(Fore.LIGHTCYAN_EX + char)
                    sys.stdout.flush()
                    sleep(0.010)
                time.sleep(2)
                number += 1
            except exceptions:
                print(
                    f'{Fore.LIGHTRED_EX}Playlist {Fore.LIGHTGREEN_EX}{Fore.LIGHTRED_EX}is unavaialable or Wrong link.')
    else:
        print(f"{Fore.LIGHTRED_EX}NO operations ")
