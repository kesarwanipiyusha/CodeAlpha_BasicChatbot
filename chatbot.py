
# Basic Chatbot - CodeAlpha Internship

def chatbot():

    print("==============================")
    print("       MY CHATBOT")
    print("==============================")
    print("Hello! I am your chatbot.")
    print("You can talk to me.")
    print("Type 'bye' to exit.")

    while True:

        user_input = input("\nYou: ").lower().strip()

        if user_input == "hello":
            print("Bot: Hi! How can I help you?")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user_input == "what is your name":
            print("Bot: I am your Python chatbot!")

        elif user_input == "thank you":
            print("Bot: You're welcome!")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()
