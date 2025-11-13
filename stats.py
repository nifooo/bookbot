def get_book_text(path):
    with open(path) as f:
        text_book = f.read()
    words = text_book.split()
    num_words = len(words)
    print(f"Found {num_words} total words.")