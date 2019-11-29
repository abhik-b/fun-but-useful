import speech_recognition as sr 
from textblob import TextBlob
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

r=sr.Recognizer()

chrome_options=Options()
chrome_options.add_argument("--start-maximized")
browser=webdriver.Chrome(executable_path='./chromedriver.exe',chrome_options=chrome_options)

with sr.Microphone() as source:
    print("Speak Anything \n\n")
    audio=r.listen(source)
    

    try:
        text=r.recognize_google(audio)
        print("you said   {}".format(text))
        wrd=TextBlob(text)
        z=wrd.translate(from_lang='en', to='fr')
        print("\n French :   ",z)
        browser.get('https://translate.google.com/')
        browser.find_element_by_id("sugg-item-fr").click()
        browser.find_element_by_id("source").send_keys(str(z))
        
    except:
        print("sorry man samajh nei aya")

time.sleep(120000)