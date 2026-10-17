from datetime import datetime

def count_words(text):
    return len(text.split())

name = input("What's your name? ")
sentence = input("Type any sentence: ")

print(f"\nHello, {name}! Today is {datetime.now():%A, %B %d, %Y}.")
print(f"Your sentence has {count_words(sentence)} words.")