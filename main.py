def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    words = count_words(text)
    print (f"your file has {words} words in it")
    letters = count_letters(text)
    letter_report(letters)
    print ("--- end of report ---")

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

def sort_on(dict):
    return dict["num"]

def letter_report(letters):
    list_letters = []
    for char in letters:
        if char.isalpha():
            new_dict = {"char": char, "num": letters[char]}
            list_letters.append(new_dict)
    list_letters.sort(reverse=True, key=sort_on)
    for item in list_letters:
        print (f"there are {item['num']} instances of the letter {item['char']}")

main()