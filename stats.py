from typing import Dict


def get_number_of_words(text: str) -> int:
    text_list = text.split()
    return len(text_list)


def get_number_of_characters(text: str) -> Dict[str, int]:
    text_list = text.lower().split()
    char_dict = {}
    for word in text_list:
        for char in word:
            if char not in char_dict:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
    return char_dict


def print_report(file: str, num_words: int, char_dict: Dict[str, int]) -> str:
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {file}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {num_words} total words\n"
    report += "--------- Character Count -------\n"
    for key, value in char_dict.items():
        report += f"{key}: {value}\n"

    report += "============= END ===============\n"
    return report
