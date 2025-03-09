from curses.ascii import isalpha

import sys
from stats import get_word_count
from stats import get_char_count
from stats import chars_dict_to_sorted_list

def get_book_test(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        args = sys.argv
    book_path = args[1]
    file_contents = get_book_test(book_path)
    num_words = get_word_count(file_contents)
    print(f"{num_words} words found in the document")
    char_count = get_char_count(file_contents)
    chars_sorted_list = chars_dict_to_sorted_list(char_count)
    print(print_report(book_path, num_words, chars_sorted_list))

def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")



main()
