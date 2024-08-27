#Shoutout to everyone - 
'''take names of the people to whom you want to give the shoutout form the user
the pronounce list of the name along with the string containing the names
of the user and call the message.'''

#USE THE WIN32 API



from win32com.client import Dispatch

# to take names for speech from user
finallist = []
inp1 = str(input("enter the name of the employees separated by name:"))
finallist = [item.strip() for item in inp1.split(',')] #strip cuts string and split removes ','

#function for text to speech
def speak(str):
    speakengine = (Dispatch("SAPI.SpVoice"))
    speakengine.speak(str)


# to get the speech as input

for names in finallist:
    speak(f"Shout out to {names}")
    speak("THANK YOU")


