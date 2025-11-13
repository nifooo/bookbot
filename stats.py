def get_book_text(path):
    with open(path) as f:
        text_book = f.read()
    
    counts = {}
    for ch in text_book.lower():
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1
    return print(counts)
    # words = text_book.split()
    # num_words = len(words)
    # return print(f"Found {num_words} total words.")