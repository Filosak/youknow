from PIL import Image, ImageGrab
import pyautogui
import pytesseract
import keyboard
import cv2 as cv
import numpy as np
import random
import string
from time import sleep

RIGHT_WORDS = {
    "realitni kancelar": "real estate office",
    "real estate office": "realitní kancelář",
    "zahradnictvi": "gardening store",
    "gardening store": "zahradnictví",
    "pradelna": "laundry service",
    "laundry service": "prádelna",
    "sekac": "second-hand clothing store",
    "sekaé": "second-hand clothing store",
    "second-hand clothing store": "sekáč",
    "papirnictvi": "stationery shop",
    "stationery shop": "papírnictví",
    "obchod pro kutily": "DIY store",
    "diy store": "obchod pro kutily"
}

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\\tesseract.exe'


run = True

while run:
    wait_for_answer = True
    while wait_for_answer:
        try:
            img = ImageGrab.grab(bbox=(600, 255, 1350, 560))
            img_np = cv.cvtColor(np.array(img), cv.COLOR_BGR2GRAY)

            correct_answer = RIGHT_WORDS[pytesseract.image_to_string(img_np).lower().replace("\n", "")]
            wait_for_answer = False
        except Exception as e:
            print(e)

        if keyboard.is_pressed('esc'):
            break

    pyautogui.moveTo(1000, 600, random.uniform(0.2, 0.4))
    pyautogui.click()

    if (random.random() > 1):
        correct_answer = correct_answer.replace("a", "s", 1)

        keyboard.write(correct_answer, random.uniform(0.08, 0.15))

        pyautogui.moveTo(random.randint(800, 1200), random.randint(660, 680), random.uniform(0.2, 0.5))
        pyautogui.click()

        pyautogui.moveTo(random.randint(800, 1200), random.randint(830, 860), random.uniform(0.2, 0.5))
        pyautogui.click()
    else:
        keyboard.write(correct_answer, random.uniform(0.08, 0.15))

        pyautogui.moveTo(random.randint(800, 1200), random.randint(660, 680), random.uniform(0.2, 0.5))
        pyautogui.click()

    if keyboard.is_pressed('esc'):
        break

    sleep(random.uniform(2.5, 3))
