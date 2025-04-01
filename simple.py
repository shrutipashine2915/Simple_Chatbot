# Simple Python Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Basic responses
    responses = {
        'hello': 'Hello! How can I assist you today?',
        'hi': 'Hi there! What can I do for you?',
        'how are you?': "I'm just a bunch of code, but I'm here to help you!",
        'bye': 'Goodbye! Have a great day!',
        'what is your name?': 'I am a simple Python chatbot created by you.',
        'help': 'I can respond to simple greetings and questions. Try saying hello or asking my name!'
    }

    # Check for a match in the responses dictionary
    response = responses.get(user_input, "I'm sorry, I don't understand that.")
    return response


def chat():
    print('Chatbot: Hello! I am your chatbot. Type "bye" to exit.')
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'bye':
            print('Chatbot: Goodbye! Have a great day!')
            break
        response = chatbot_response(user_input)
        print(f'Chatbot: {response}')


if __name__ == '__main__':
    chat()
