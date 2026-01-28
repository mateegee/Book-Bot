def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_contents = f.read()
        return book_contents

def count_words(book):
    words = book.split()
    return len(words)
