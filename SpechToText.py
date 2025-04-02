import speech_recognition

recognizer = speech_recognition.Recognizer()

def listen():
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Listening...")
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            return text  # Return the recognized text

    except speech_recognition.UnknownValueError:
        print("Could not understand audio, please try again.")
        return None  # Return None if recognition fails
