######################## Packages ###################################################
import time  #for time analysis
from win32com.client import Dispatch #for speech

################################### Speech function ####################################################
def speak(messaage):
    speakengine = (Dispatch("SAPI.SpVoice"))
    speakengine.speak(messaage)

'''
speak(message)
speak("hello my name is ganesh")
'''
#########################Time Analysis part #######################################

speak("may i know your name please")
name = input("may i know your name please?:\n")

speak(f"welcome {name} enter the time in minutes you want to set for water drinking reminder ")
startmsg = float(input(f" welcome {name} enter the time in minutes you want to set for water drinking reminder:\n"))

min_to_sec = int(startmsg * 60)

msg2  = speak(f"you have set the reminder for:{min_to_sec} seconds.")

message = (f"Its been {min_to_sec} seconds since you have drinked the water take a sip right now ")


while True:
   time.sleep(min_to_sec)
   speak(message)



'''formattedtime = time.strftime("%H")
print(formattedtime)'''
