import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    [r"how are you", ["I'm just a bot, but I'm doing well!", "I'm good, thanks for asking!"]],
    [r"what is your name", ["I'm a chatbot created by Om!", "You can call me ChatBot."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care!"]],
    [r"(.*)", ["I'm not sure how to respond to that, but I'm learning!"]]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm your chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("ChatBot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

# Run chatbot
if __name__ == "__main__":
    start_chat()
