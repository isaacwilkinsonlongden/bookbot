def get_num_words(book_string):
    words = book_string.split()
    return len(words)

def get_num_char(book_string):
    char_count = {}
    for char in book_string:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_char(char_count):
    sorted_dicts = []
    for char in char_count:
        sorted_dicts.append({"char": char, "num": char_count[char]})

    def sort_on(dict):
        return dict["num"]

    sorted_dicts.sort(reverse=True, key=sort_on)

    return sorted_dicts