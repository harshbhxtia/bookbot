from stats import get_number_of_characters, get_number_of_words, print_report
import sys


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    num_words = get_number_of_words(file_contents)
    num_chars = get_number_of_characters(file_contents)
    string = print_report(file_path, num_words, char_dict=num_chars)
    print(string)


main()
