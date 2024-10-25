from gtts import gTTS
from playsound import playsound

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    # for windows
    playsound("response.mp3")  # This will play the mp3 file
    #for linux
    # os.system("mpg321 response.mp3")  # This command will play the generated mp3
