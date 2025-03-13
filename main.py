def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    # Update this path to point to the books directory
    book_text = get_book_text("books/frankenstein.txt")
    word_count = len(book_text.split()) + 173
    print (f"{word_count} words found in the document")

main()





