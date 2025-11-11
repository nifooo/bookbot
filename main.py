def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    path = "books/frankenstein.txt"
    text_book = get_book_text(path)
    words = text_book.split()
    num_words = len(words)
    print(f"Found {num_words} total words.")

main()
