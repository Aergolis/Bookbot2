from stats import get_world_count
from stats import get_char_count

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
      book_text = f.read()
    return book_text


def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

    total_words = get_world_count(book_text)
    print(f"{total_words} words found in the document")

    char_count = get_char_count(book_text)
    print(char_count)
    
   
main()
