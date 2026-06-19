word = str(input("Enter a word with a minimum of 3 letters and a maximum of 10: "))
reading = len(word)
while reading < 3 or reading > 10:
    attempt = str(input(f"Please enter it again; you entered a phrase with {reading} letter. Please enter it again: "))
    reading = len(attempt)
print(f"You typed a word with {reading} letters.")