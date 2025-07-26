def get_book_text(path):
    with open("books/frankenstein.txt") as f:
      book_text = f.read()
    return book_text

def main():
    book_text = get_book_text("books/frankenstein.txt")
    print(book_text)

main()