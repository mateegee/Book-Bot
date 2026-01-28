from stats import get_book_text, count_words

def main():
    frankenstein = get_book_text("books/frankenstein.txt")
    word_count = count_words(frankenstein)
    print(f"Found {word_count} total words")

main()