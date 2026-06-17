import random
import datetime

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print(" Chatbot: Hello! How can I help you?")

    elif "What is your name" in user:
        print(" Chatbot: My name is AI Chatbot.")

    elif "Do you speak hindi?" in user:
        print("Chatbot: No")01

    elif "how are you" in user:
        print(" Chatbot: I am doing great! and how are you Thanks for asking.")
    
    elif "Who made you?" in user:
        print(" Chatbot: You have made me Ashutosh")

    elif "What is time now" in user:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f" Chatbot: Current time is {current_time}")

    elif "date" in user:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f" Chatbot: Today's date is {current_date}")

    elif "Nice to meet you" in user:
        print(" Chatbot: Thank you")

    elif "thank you" in user or "thanks" in user:
        print(" Chatbot: You're welcome!")

    elif "bye" in user:
        print(" Chatbot: Goodbye! Have a great day.")
        break

    else:
        print(" Chatbot: Sorry, I don't understand that. Please try another question.")