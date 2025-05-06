import ollama

def getResponse(promptIn):
    response = ollama.chat(model='llama3', messages=[
        {
            'role': 'user',
            'content': promptIn,
        },
    ])
    return response['message']['content']


