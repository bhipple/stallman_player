#!/usr/bin/python
import subprocess
import time
import random

MIN_SLEEP_SECS = 60 * 10
MAX_SLEEP_SECS = 60 * 60

while True:
    subprocess.call("vlc --play-and-exit stallman_free_software_song.mp4", shell=True)
    
    lolwait = random.randint(MIN_SLEEP_SECS, MAX_SLEEP_SECS) / 60
    print "Fear not hackers, St. iGNUcius will return in",
    print "%.f" % lolwait + "ish minutes."
    
    time.sleep(random.randint(MIN_SLEEP_SECS, MAX_SLEEP_SECS))
    
