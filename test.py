import signal
import sys
import time

run = True

def signal_handler(signal, frame):
    global run
    print("exiting")
    run = False

# This doesn't seem to work on macos, running python from command line in conda env... why?

signal.signal(signal.SIGINT, signal_handler)
while run:
    print("hi")
    time.sleep(1)
    # do anything
    print("bye")
