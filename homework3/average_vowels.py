# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.


def counting_vowels_and_consonants(sentence):
    num = 0
    v = 0
    c = 0
    while num < len(sentence):
        if sentence[num] == ("a" or "e" or "i" or "o" or "u"):
            v += 1
        elif [num] == "b" or "c" or "d" or "f" or "g" or "h" or "j" or "k" or "l" or "m" or "n" or "p" or"q" or "r" or "s" or "t" or "v" or "w" or "x" or "y" or "z":
            c += 1
        num += 1
    return (v, c)
    

# --- 2. Average Vowels sh---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    s = 0
    for value in paragraph: 
        if value == ("." or "!"):
            s += 1
    return s, (counting_vowels_and_consonants(paragraph))[0]/s, (counting_vowels_and_consonants(paragraph))[1]/s

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

print(f"The average number of vowels per sentence of the paragraph is {average_vowels_and_consonants(paragraph)[1]} and the average number of consonants per sentence of the paragraph is {average_vowels_and_consonants(paragraph)[2]}")

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

