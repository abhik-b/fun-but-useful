# from gtts import gTTS
# import os    
# text=input("enter in french")
# tts = gTTS(text=text, lang='fr')
# tts.save("pcvoice.mp3")
# # to start the file from python
# os.system("start pcvoice.mp3")

f=open("ab.txt","rt")

contents=f.read()
print("Previous ",contents)
contents=contents.replace("good","verygood")
f.close()

f=open("ab.txt","wt")
f.write(contents)
print("\n\n NaWW!!!! ",contents)
f.close

