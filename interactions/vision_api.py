import subprocess
import cv2
import numpy as np
import time
import os

def get_screen():

    process = subprocess.Popen(
        "adb exec-out screencap -p", 
        shell=True, 
        stdout=subprocess.PIPE
    )
    
    screenshot_bytes, _ = process.communicate()
    
    image_array = np.frombuffer(screenshot_bytes, np.uint8)
    print(image_array)

    image = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
    
    return image

def save(image, label="unknown"):
    folder = "assets/screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = int(time.time())
    filename = f"{folder}/{label}_{timestamp}.png"
    
    cv2.imwrite(filename, image)
    print(f"💾 Saved evidence: {filename}")

def cut(x0, x1, y0, y1, image_arr):
    cut_image = image_arr[y0:y1, x0:x1];
    return cut_image
