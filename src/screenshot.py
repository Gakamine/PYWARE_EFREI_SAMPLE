from PIL import Image
import numpy as np
import cv2
import pyautogui
import os
import base64
import hashlib

def take_screenshot():
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite("screenshot.jpg", image)
    image=Image.open("screenshot.jpg")
    image.save("screenshot.jpg", quality=30)
    image=open("screenshot.jpg","rb")
    encoded_image = base64.b64encode(image.read()).decode()
    md5=hashlib.md5(encoded_image.encode("utf-8")).hexdigest()
    os.remove("screenshot.jpg")
    return (md5,encoded_image)