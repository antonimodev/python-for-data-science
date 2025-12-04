from sys import argv, exit
from ft_filter import ft_filter


def main() -> None:
    """
    Read text and return words with length greater than user input

    Args:
        argv[1]: String
        argv[2]: Integer

    Returns:
        List
    """
    try:
        assert len(argv) == 3, "the arguments are bad"
        text = argv[1]
        length = int(argv[2])
    except AssertionError as e:
        print(f"AssertionError: {e}")
        exit(1)
    except ValueError:
        print("ValueError: second argument must be integer")
        exit(1)

    result = list(ft_filter(lambda word: len(word) > length, text.split()))
    print(result)


if __name__ == "__main__":
    main()
