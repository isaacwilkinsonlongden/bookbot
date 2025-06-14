import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import get_num_words, get_num_char, sort_char

def main():
    text = sys.argv[1]
    book_string = get_book_text(text)
    num_words = get_num_words(book_string)
    num_char = get_num_char(book_string)
    sorted_num_char = sort_char(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {text}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_num_char:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")        

def get_book_text(path):
    with open(path) as f:
        return f.read()        

main()            
