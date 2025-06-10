import os

# Sample keyword-to-sign mapping
sign_dict = {
    "eat": "media/a.gif.mp4",
    "drink": "media/b.gif.mp4",
    "toilet": "media/c.gif.mp4"
}

def get_sign(keyword):
    keyword = keyword.lower()
    return sign_dict.get(keyword, "Sign not found. Try another word.")

# Test it locally
if __name__ == "__main__":
    while True:
        word = input("Enter a word (or 'exit' to quit): ")
        if word == "exit":
            break
        print("Response:", get_sign(word))
