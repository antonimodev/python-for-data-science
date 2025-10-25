from sys import argv
from string import punctuation


def get_text_info(text: str) -> dict:
    """
    Receive text and process all char attributes within the text.

    The dictionary contains:
        - Total chars: total number of characters.
        - Upper: number of uppercase letters.
        - Lower: number of lowercase letters.
        - Punctuation marks: number of punctuation marks.
        - Spaces: number of spaces.
        - Digits: number of digits.

    Params: str.

    Returns: Dictionary with all attributes.
    """
    text_attributes = {
        "Total chars": 0,
        "Upper": 0,
        "Lower": 0,
        "Punctuation marks": 0,
        "Spaces": 0,
        "Digits": 0
    }

    for char in text:
        text_attributes["Total chars"] += 1

        if char.isupper():
            text_attributes["Upper"] += 1
        elif char.islower():
            text_attributes["Lower"] += 1
        elif char in punctuation:
            text_attributes["Punctuation marks"] += 1
        elif char.isspace():
            text_attributes["Spaces"] += 1
        elif char.isdigit():
            text_attributes["Digits"] += 1

    return text_attributes


def main():
    try:
        assert len(argv) <= 2, "more than one argument is provided."
    except AssertionError as e:
        print(f"AssertionError: {e}")

    text_attributes = {}

    if len(argv) == 2:
        text_attributes = get_text_info(argv[1])
    elif len(argv) == 1:
        text_attributes = get_text_info(input("What is the text to count?\n"))

    print(f"The text contains {text_attributes['Total chars']} characters:")
    print(f"{text_attributes['Upper']} upper letters")
    print(f"{text_attributes['Lower']} lower letters")
    print(f"{text_attributes['Punctuation marks']} punctuation marks")
    print(f"{text_attributes['Spaces']} spaces")
    print(f"{text_attributes['Digits']} digits")


if __name__ == "__main__":
    main()
