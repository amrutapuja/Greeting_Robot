import ollama

def getResponse(promptIn):
    response = ollama.chat(model='samantha-mistral', messages=[
        {
            'role': 'user',
            'content': promptIn,
        },
    ])
    return response['message']['content']


