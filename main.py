def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    words = count_words(text)
    print (f"your file has {words} words in it")
    letters = count_letters(text)
    print (letters)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    total_words = text.split()
    return len(total_words)

def count_letters(text):
    letters = {}
    for char in text:
        lowered = char.lower()
        if lowered in letters:
            letters[lowered] += 1 
        else:
            letters[lowered] = 1
    return letters

main()