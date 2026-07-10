"""
Basic Rule-Based Chatbot
A simple chatbot that replies to user input like "hello", "how are you",
and "bye", along with a few extra common phrases.

Key concepts used: if-elif, functions, loops, input/output.
"""

from datetime import datetime
import string


def normal_input(user_input):
    """Return a format of chatbot by handling uppercase and punctuations."""
    
    text = user_input.lower().strip()

    for ch in string.punctuation:
        if ch != "'":
            text = text.replace(ch, "")

    words = text.split()
    return words, text;


def get_response(user_input):
    """Return a predefined reply based on the user's message."""

    words, text = normal_input(user_input)

    feel = any(word in words for word in ("good", "fine", "great", "nice", "well"))

    today = datetime.now()


    if text == "":
        return "Please type something so I can respond."

    elif any(word in words for word in ("hello", "hi", "hey", "greetings")):
        return "Hi there! How can I help you today?"

    elif any(word in text for word in ("how are you", "how're you")):
        return "I'm doing great, thanks for asking! How about you?"

    elif any(word in text for word in ("who are you", "who're you", "your name")):
        return "I'm a simple rule-based Chatbot, built in Python!"

    elif (any(word in words for word in ("help", "capabilities", "feature", "features", "function", "functions")) or 
          all(word in words for word in ("what", "you", "do"))):
        return ("I can respond to greetings, questions about myself, time, day and date, "
                "and a few other simple phrases. Try saying 'hello' or 'bye'!")

    elif "thank" in words or "thanks" in words:
        return "You're welcome!"

    elif any(word in words for word in ("made", "built", "created")) and "you" in words and "who" in words:
        return "I was built as a simple Python project to demonstrate rule-based chatbot conversation logic."

    elif (feel and ("not" in words or "don't" in words)) or (any(word in words for word in ("sad", "bad")) and "not" not in words):
        return "I'm sorry to hear that. I hope things get better soon."
    
    elif feel or any(word in text for word in ("going well", "not so bad", "not bad")):
        return "Glad to hear that!"


    # Time, Day, Date is handled here using 6 different cases.

    elif all(word in words for word in ("time", "day", "date")):
        return ("The current time is " + today.strftime("%I:%M %p") + ". "
                "Today is " + today.strftime("%A") + ", " + today.strftime("%B %d, %Y") + ".")

    elif all(word in words for word in ("time", "date")):
        return ("The current time is " + today.strftime("%I:%M %p") + ". "
                "And the date is " + today.strftime("%B %d, %Y")) + "."

    elif all(word in words for word in ("day", "date")):
        return "Today is " + today.strftime("%A") + ", " + today.strftime("%B %d, %Y") + "."

    elif "time" in words:
        return "The current time is " + today.strftime("%I:%M %p") + "."

    elif "date" in words:
        return "Today's date is " + today.strftime("%B %d, %Y") + "."

    elif "day" in words:
        return "Today is " + today.strftime("%A") + "."


    elif any(word in text for word in ("see you", "see ya")) or any(word in words for word in ("bye","goodbye", "exit", "quit")):
        return "Goodbye! Have a great day!\n"

    else:
        return "I'm sorry, I didn't quite understand that. Could you try rephrasing, or type 'help' to see what I can do?";


def is_exit_command(user_input):
    """Check whether the user's input signals they want to end the chat."""

    words, text = normal_input(user_input)
    exit_words = ("bye", "goodbye", "exit", "quit")

    return any(word in text for word in ("see you", "see ya")) or any(word in words for word in exit_words);


def main():
    """Run the chatbot loop until the user says bye/exit/quit."""

    print("\n")
    print("=" * 60)
    print("\t\tSimple Rule-Based Chatbot\n")
    print("  Type 'help' to see what I can do.")
    print("  Type 'bye', 'exit', or 'quit' to end the chat.")
    print("=" * 60)
    print("\n")

    while True:
        user_input = input("\nYou: ")
        response = get_response(user_input)
        print("Bot:", response)

        if is_exit_command(user_input):
            break;

if __name__ == "__main__":
    main();
