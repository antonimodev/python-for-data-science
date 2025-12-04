from sys import argv, exit


def morse_translator(word: str) -> str:
    """
    Translate word string to morse using morse_dict

    Args:
        word (str): The string to translate

    Returns:
        Word translated to morse
    """
    morse_dict = {
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. ",
        " ": "/",
    }

    try:
        assert all(char.upper() in morse_dict for char in word), "the arguments are bad"
        morse = "".join(morse_dict[char.upper()] for char in word)
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)

    return morse.rstrip()


def main() -> None:
    try:
        assert len(argv) == 2, "must be one argument"
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)

    print(morse_translator(argv[1]))


if __name__ == "__main__":
    main()
