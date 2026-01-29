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

def sort_on_chars(items):
    return items["num"]

def sort_on_words(items):
    for key, value in items.items():
        return items[key]

def word_quantity(book):
    words = book.lower().split()
    word_dict = {}
    clean_words = []
    for word in words:
        word = ''.join(char for char in word if char.isalpha())  # remove punctuation
        if word:  # skip empty strings
            clean_words.append(word.lower())  # optional lowercase
    print(clean_words)

    for clean_word in clean_words:
        if clean_word not in word_dict:
            word_dict[clean_word] = 1
        else:
            word_dict[clean_word] += 1
    return word_dict

def character_sorting(character_count_dict):
    sorted_list = []
    for key, value in character_count_dict.items():
        if key.isalpha() == False:
            pass
        else:
            sorted_list.append({"char": key, "num": value})
    
    sorted_list.sort(reverse=True, key=sort_on_chars)
    return sorted_list

def word_sorting(words_dict):
    words_list = []
    for key, value in words_dict.items():
        words_list.append({key: value})
    
    words_list.sort(reverse=True, key=sort_on_words)
    return words_list

def book_report():
    book_location = sys.argv[1]
    book = get_book_text(book_location)
    word_count = count_words(book)
    characters = character_count(book)
    word_num = word_quantity(book)
    sorted_words = word_sorting(word_num)
    sorted_characters = character_sorting(characters)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_characters:
        print(f"{char_dict["char"]}: {char_dict["num"]}")
    print("---------- Word Count -----------")
    for word_dict in sorted_words:
        for key, value in word_dict.items():
            print(f"{key}: {value}")
    print("============= END ===============")

    