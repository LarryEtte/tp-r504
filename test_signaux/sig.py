#!/usr/bin/python3
import signal as sig
from time import sleep
import sys
import os

def signal_handler(s, frame):
    print("réception du signal", sig.Signals(s).name)
    if sig.Signals(s).name == "SIGINT":
        exit(0)

sig.signal(sig.SIGINT, signal_handler)
sig.signal(sig.SIGQUIT, signal_handler)

x=1
while True:
    print("pid=", os.getpid(), x)
    sleep(.5)
    x += 1
