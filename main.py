from stats import get_book_text

def main():
    path = "books/frankenstein.txt"
    text_book = get_book_text(path)
    words = text_book.split()
    num_words = len(words)
    print(f"Found {num_words} total words.")

main()
