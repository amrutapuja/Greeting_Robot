import pyttsx3

def textToSpeech(text):
    text_speech = pyttsx3.init()
    voices = text_speech.getProperty('voices')
    text_speech.setProperty('voice', voices[1].id)  # Fixed this line
    text_speech.say(text)
    text_speech.runAndWait()
    # print("Done")

# textToSpeech('The histogram equation is used to describe the contrast in an image, which refers to the range of tonal values present in the image. It compares the number of pixels at each tonal value to the total number of pixels in the image. The formula for the histogram equation is as follows:')
