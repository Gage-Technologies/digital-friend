import speech_recognition as sr


def listen_to_microphone():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening... Speak into the microphone")


        # Listen for the first phrase and extract it into audio data
        audio_data = recognizer.listen(source)

        try:

            # Use Google Web Speech API to recognize speech
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio_data)
            print(f"You said: {text}")
            return text

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")

        except sr.RequestError as e:
            print(f"Error from Google Speech Recognition service: {e}")


if __name__ == '__main__':
    listen_to_microphone()