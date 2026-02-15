import subprocess
import time

def touch(x, y):
    process = subprocess.Popen(
        f"adb shell input tap {x} {y}", 
        shell=True, 
        stdout=subprocess.PIPE
    )
    process.communicate()

def drag(x0, y0, x1, y1, duration=100):
    process = subprocess.Popen(
        f"adb shell input swipe {x0} {y0} {x1} {y1} {duration}", 
        shell=True, 
        stdout=subprocess.PIPE
    )
    process.communicate()

def input_text(text):
    process = subprocess.Popen(
        f"adb shell input text {text}", 
        shell=True, 
        stdout=subprocess.PIPE
    )
    process.communicate()