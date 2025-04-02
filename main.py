from ollama_request import getResponse
from SpechToText import listen
from textToSpech import textToSpeech


def audioToTextInput():
    prompt_in = listen()
    if prompt_in:
        print("Input: " + prompt_in)
        return prompt_in
    else:
        print("No valid input received from speech recognition.")
        return None

def getOllamaResponse():
    prompt_in = audioToTextInput()  # Get the input from audioToTextInput
    if prompt_in:  # Check if the input is valid
        prompt_out = getResponse(prompt_in)
        print(prompt_out)
        textToSpeech(prompt_out)
        print('done')
    else:
        print("No response generated due to invalid input.")




if __name__ == "__main__":
    getOllamaResponse()
