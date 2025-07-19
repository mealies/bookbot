from stats import count_words, count_characters, sort_characters
import sys

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        book = f.read()
    return book

def print_report(word_count, sorted_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for letter in sorted_list:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")




def main():

    if len(sys.argv) < 2:
        print("Please provide a filepath to a book")
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    num_words = count_words(book)
    num_chars = count_characters(book)
    sorted_list = sort_characters(num_chars)
    #print(f"{num_words} words found in the document")
    print_report(num_words, sorted_list)


main()