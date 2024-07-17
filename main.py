""" This script going to check some pages to check updates every certain time """
import os
import time
import json
import queue
from threading import Thread
from datetime import datetime

from ojitos369.utils import printwln as pln
from test import get_last_posts

login_url = "https://i.instagram.com/accounts/login/"
user = "b7e96e72fa3042f"
passowrd = "5&a2o@@Nd6n7$1G@m@4J&Sr4%Koc*f"

insta = [
    "twicetagram",
    "nayeonyny",
    "jy_piece",
    "momo",
    "m.by__sana",
    "_zyozyo",
    "mina_sr_my",
    "dahhyunnee",
    "chaeyo.0",
    "thinkaboutzu",
]

class General:
    def load_saved_post(self):
        try:
            with open(f"{self.username}_saved.json", "r") as file:
                self.saved = file.read().split("\n")
        except:
            self.saved = {
                "insta": {},
                "yt": {},
                "tt": {},
                "fb": {},
                "x": {},
            }

    def save_post(self):
        with open(f"{self.name}_saved.json", "w") as file:
            file.write(json.dumps(self.saved, indent=4))

    def check_post(self):
        post = get_last_posts(self.username)
        if self.username not in self.saved["insta"]:
            self.saved["insta"][self.username] = []
        new_posts = False
        for p in post:
            if post not in self.saved["insta"][self.username]:
                self.saved["insta"][self.username].append(p)
                pln(f"New post from {self.username}: {p}")
                new_posts = True
        return new_posts

class Tw(General):
    def __init__(self):
        self.name = "Twice"
        self.username = "twicetagram"

def main():
    tw = Tw()
    tw.load_saved_post()
    new_post = tw.check_post()
    tw.save_post()
    print(new_post)

if __name__ == "__main__":
    main()

""" 

"""