import pyttsx3
import sys
import os
import time
import datetime
import re
import json
import random

wow_phrase = [
    "Woww!",
    "Yikes!",
    "Are you okay?",
    "Cry-key!",
    "I'm concerned about this."
]

engine = pyttsx3.init()

config = {}
with open("chrome-logwatch-config.json") as c:
    config = json.load(c)

filename = "C:/Users/James/AppData/Local/BraveSoftware/Brave-Browser/User Data/chrome_debug.log"

#start monitoring for new stuff
def read_log(f, sleep=3):
    with open(f,encoding="utf8") as logfile:
        logfile.seek(0, os.SEEK_END)
        newstuff = []
        while True:
            new = logfile.readline()
            if new:
                newstuff.append(new)
            else:
                yield newstuff
                time.sleep(sleep)
                newstuff = []

for stuff in read_log(filename):
    counts = {}
    for line in stuff:
        print(datetime.datetime.now())
        for p in range(len(config["patterns"])):
            if re.search(config["patterns"][p]["match"],line,re.IGNORECASE):
                for site in config["sites"]:
                    if re.search(site,line):
                        if p in counts:
                            counts[p] += 1
                        else:
                            counts[p] = 1
    for item in counts:
        if counts[item] == 1:
            engine.say(config["patterns"][item]["say"])
            engine.runAndWait()
        elif counts[item] > 1 and counts[item] < 10:
            engine.say("A lot of " + config["patterns"][item]["say"] + ". " + str(counts[item]) + " times in 3 seconds")
            engine.runAndWait()
        elif counts[item] >= 10:
            engine.say("A lot of " + config["patterns"][item]["say"] + ". " + str(counts[item]) + " times in 3 seconds. " + wow_phrase[random.randint(0,4)])
            engine.runAndWait()
