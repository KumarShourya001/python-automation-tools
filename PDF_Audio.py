import os 
import pyttsx3 as pts
from pypdf import PdfReader
print(os.getcwd())
path_pdf=input("Give path of PDF")
cng = os.chdir(path_pdf)
file = os.listdir()
lst=[]
for i in file:
    if i.endswith(".pdf"):
        lst.append(i)

print(lst)
lst0=lst[1]

reader =PdfReader(lst0)
page =reader.pages[0]
my_text =page.extract_text()
print()
engine=pts.init()
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate',125)

volume = engine.getProperty('volume')
voice = engine.getProperty('voice')
print(volume)
engine.setProperty('volume',1.0)
print(voice)
engine.setProperty('voice',voice[1])
for part in my_text.splitlines():
    if part.strip():
        engine.say(part)
        engine.runAndWait()
engine.stop()
engine.save_to_file(my_text,'test.mp3')
engine.runAndWait()
