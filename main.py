from stats import get_world_count
from stats import get_char_count
from stats import dict_into_list
from stats import sort_on

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
      book_text = f.read()
    return book_text


def main():
    book_text = get_book_text("books/frankenstein.txt")
    total_words = get_world_count(book_text)
    char_count = get_char_count(book_text)
    char_into_list = dict_into_list(char_count)
    char_count_sorted = sorted(char_into_list, key=sort_on, reverse=True)




    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {"books/frankenstein.txt"}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for item in char_count_sorted:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
