def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
        return book_contents

def count_words(book):
    words = book.split()
    return len(words)

def character_count(book):
    characters = {}
    for character in book:
        c = character.lower()
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters