from stats import get_book_text, count_words, character_count
from pprint import pprint

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    word_count = count_words(frankenstein)
    characters = character_count(frankenstein)
    print(f"Found {word_count} total words")
    pprint(characters)

main()