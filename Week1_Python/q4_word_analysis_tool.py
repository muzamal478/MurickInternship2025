# Word Analysis Tool
# Analyzes a sentence for characters, words, vowels, consonants, and letter frequency
from collections import Counter

def analyze_text(text):
    # Total characters
    chars = len(text)
    
    # Word count
    words = text.split()
    word_count = len(words)
    
    # Vowels and consonants count
    vowels = sum(1 for c in text.lower() if c in 'aeiou')
    consonants = sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')
    
    # Longest word
    longest = max(words, key=len, default="")
    
    # Letter frequency (case-insensitive)
    letter_freq = Counter(c.lower() for c in text if c.isalpha())
    
    # Print results
    print(f"Total Characters: {chars}")
    print(f"Word Count: {word_count}")
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Longest Word: {longest}")
    print("Letter Frequency:", dict(letter_freq))

# Get input and run analysis
text = input("Enter sentence: ")
analyze_text(text)