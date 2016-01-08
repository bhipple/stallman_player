#!/usr/bin/python
import subprocess
import time
import random

MIN_SLEEP_SECS = 60 * 10
MAX_SLEEP_SECS = 60 * 60

while True:
    subprocess.call("vlc --play-and-exit stallman_free_software_song.mp4", shell=True)

    print "Fear not hackers, St. iGNUcius will return soon."
    time.sleep(random.randint(MIN_SLEEP_SECS, MAX_SLEEP_SECS))
