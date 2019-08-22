import speech_recognition as sr 
from textblob import TextBlob


r=sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything \n\n")
    audio=r.listen(source)
    

    try:
        text=r.recognize_google(audio)
        print("you said   {}".format(text))
        wrd=TextBlob(text)
        z=wrd.translate(from_lang='en', to='fr')
        print("\n French :   ",z)
        
    except:
        print("sorry man samajh nei aya")

    