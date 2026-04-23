import random

def chatbot():
    print("Hi! I'm your chatbot")
    print("Type 'game' to play, or 'bye' to exit")

    while True:
        user = input("You: ").lower()

        if user == "bye":
            print("Bot: Goodbye!")
            break

        elif "hello" in user or "hi" in user:
            print("Bot: Hello there!")

        elif "name" in user:
            print("Bot: I'm your simple chatbot!")

        elif user == "game":
            play_game()

        else:
            print("Bot: I don't understand ")

def play_game():
    print("Bot: Let's play Guess the Number!")
    number = random.randint(1, 5)

    guess = int(input("Guess a number (1-5): "))

    if guess == number:
        print("Bot: Wow! You got it right ")
    else:
        print("Bot: Nope! The number was", number)


chatbot()