import sys
from stats import word_count
from stats import character_count  

def get_book_text(filepath):
    with open(filepath) as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    raw_text = (get_book_text(sys.argv[1]))
    print(f"{word_count(raw_text)} words found in the document")
    for i in range(0, len(character_count(raw_text))):
            char = list(character_count(raw_text).keys())[i]
            if char.isalpha():
                print(f"{char}: {character_count(raw_text)[char]}")


main()

