# bot.py

# A simple simulation of Karami WhatsApp bot logic
# This does NOT connect to WhatsApp yet – it's a basic demo for hackathon purposes

signs = {
    "a": "media/alphabets/a.gif.mp4",
    "b": "media/alphabets/b.gif.mp4",
    "c": "media/alphabets/c.gif.mp4",
}

def get_sign(user_input):
    letter = user_input.lower().strip()
    if letter in signs:
        return f"Here is the NSL sign for '{letter.upper()}': {signs[letter]}"
    else:
        return "Sorry, I don't have that sign yet. Try A, B, or C."

# Simulated conversation
if __name__ == "__main__":
    print("👋 Welcome to Karami (NSL Bot for Parents)")
    while True:
        user_input = input("Type a letter (A–C) to learn the sign, or 'exit' to quit: ")
        if user_input.lower() == "exit":
            print("👋 Goodbye! Keep signing.")
            break
        print(get_sign(user_input))

