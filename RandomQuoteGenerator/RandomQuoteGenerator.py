import random

with open("quotes.txt", "r", encoding="utf-8") as file:
    quotes = file.readlines()
    print()

while True: #infinite loop
    input("Press Enter to generate a random quote ")
    random_quote = random.choice(quotes)
    print()
    print(random_quote.strip())
    print()
