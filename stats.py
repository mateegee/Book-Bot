import sys

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

def sort_on(items):
    return items["num"]

def character_sorting(character_count_dict):
    sorted_list = []
    for key, value in character_count_dict.items():
        if key.isalpha() == False:
            pass
        else:
            sorted_list.append({"char": key, "num": value})
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def book_report():
    book_location = sys.argv[1]
    frankenstein = get_book_text(book_location)
    word_count = count_words(frankenstein)
    characters = character_count(frankenstein)
    sorted_characters = character_sorting(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_characters:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("============= END ===============")

    