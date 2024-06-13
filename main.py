def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    words = count_words(text)
    print (words)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    total_words = text.split()
    return len(total_words)

main()