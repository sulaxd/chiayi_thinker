import speech_recognition
import requests as re
import json
import xml.etree.ElementTree as ET


r = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    audio = r.listen(source)
result = r.recognize_google(audio, language='zh-TW')
payload= {"userid":"9a11abc7-8490-41ad-9aaf-7e702becd27d","info":result}
url = 'http://www.tuling123.com/api/product_exper/chat.jhtml'
session = re.Session()
tmp=session.post(url,data=payload)

tree = ET.fromstring(tmp.text)

from subprocess import call 
import os
os.system('say -r 200 "%s"' % tree[4].text)



print(tree[4].text)
