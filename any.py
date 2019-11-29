# from gtts import gTTS
# import os    
# text=input("enter in french")
# tts = gTTS(text=text, lang='fr')
# tts.save("pcvoice.mp3")
# # to start the file from python
# os.system("start pcvoice.mp3")
# =========file operations =============
# f=open("ab.txt","rt")

# contents=f.read()
# print("Previous ",contents)
# contents=contents.replace("good","verygood")
# f.close()

# f=open("ab.txt","wt")
# f.write(contents)
# print("\n\n NaWW!!!! ",contents)
# f.close

# =======automating google translate=========
# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options

# chrome_options=Options()
# chrome_options.add_argument("--start-maximized")
# browser=webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options)

# text=input("enter")

# browser.get('https://translate.google.com/')
# browser.find_element_by_id("sugg-item-fr").click()
# browser.find_element_by_id("source").send_keys(text)

# time.sleep(1200000)

# ====automating github login=====

# browser.get('https://github.com/')
# browser.find_element_by_link_text("Sign in").click()
# browser.find_element_by_id("login_field").send_keys("abhik-b")
# browser.find_element_by_id("password").send_keys("wannaB.13")
# browser.find_element_by_name("commit").click()
# browser.find_element_by_link_text("New").click()

# time.sleep(1200000)
# =====automating using py autogui=========
import pyautogui,time
time.sleep(1)
# pyautogui.click()
# distance=400

# while distance>0:
#     pyautogui.dragRel(distance,0,duration=0.2)
#     distance-=50
#     pyautogui.dragRel(0,distance,duration=0.2)
#     pyautogui.dragRel(-distance,0,duration=0.2)
#     distance=distance-50
#     pyautogui.dragRel(0,-distance,duration=0.2)

# =====automating calcu ==================================

# pyautogui.click(pyautogui.locateCenterOnScreen('1key.png'))
# pyautogui.click(pyautogui.locateCenterOnScreen('plus.png'))
# pyautogui.click(pyautogui.locateCenterOnScreen('1key.png'))
# pyautogui.click(pyautogui.locateCenterOnScreen('equalkey.png'))
pyautogui.FAILSAFE=True
# print(pyautogui.size())
# for i in range(10):
#     pyautogui.moveTo(500,500,duration=0.25)
#     pyautogui.moveTo(700,500,duration=0.25)
#     pyautogui.moveTo(700,700,duration=0.25)
#     pyautogui.moveTo(500,700,duration=0.25)

# pyautogui.moveRel(100,0,duration=0.25)
print(pyautogui.position())
# pyautogui.moveTo(637,1080,duration=0.25)
# pyautogui.moveTo(637,1060,duration=0.25)
# pyautogui.click(637,1060,clicks=1)
# pyautogui.moveTo(965,930,duration=0.25)
# pyautogui.click(965,930,clicks=1)
# pyautogui.click(1624,111,clicks=1)