kana_list = [
    "a",
    "i",
    "e",
    "o",
    "u",
    "ka",
    "ki",
    "ku",
    "ke",
    "ko",
    "sa",
    "shi",
    "su",
    "se",
    "so",
    "ta",
    "chi",
    "tsu",
    "te",
    "to",
    "na",
    "ni",
    "nu",
    "ne",
    "no",
    "ha",
    "hi",
    "fu",
    "he",
    "ho",
]

# Every 3 seconds print a random element from the list

# Until user types in q in terminal

import random
import time


def main():
    while True:
        random_kana = random.choice(kana_list)
        print(random_kana)
        time.sleep(2)


if __name__ == "__main__":
    main()
