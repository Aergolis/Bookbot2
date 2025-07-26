import sys

from stats import get_word_count
from stats import get_char_count
from stats import dict_into_list
from stats import sort_on


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path, 'r', encoding='utf-8') as file:
        book_text = file.read()


    

    total_words = get_word_count(book_text)
    char_count = get_char_count(book_text)
    char_into_list = dict_into_list(char_count)
    char_count_sorted = sorted(char_into_list, key=sort_on, reverse=True)




    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in char_count_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
