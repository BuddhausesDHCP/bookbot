import sys
from stats import get_num_words, count_characters, filter_dict


def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    total_characters = count_characters(text)
    character_list = filter_dict(total_characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in character_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
        
