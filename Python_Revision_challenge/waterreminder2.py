import time  #for time analysis
from win32com.client import Dispatch #for speech


message = ("hi Ganesh It's beeen 45 minuits since you drinked water i suggest you to take a sip right now")
def speak(message):
    speakengine = (Dispatch("SAPI.SpVoice"))
    speakengine.speak(message)


sec = 1
while True:
   time.sleep(sec)
   speak(message)




