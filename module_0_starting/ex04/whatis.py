from sys import argv


def is_even(arg: int) -> bool:
    return arg % 2 == 0


argc = len(argv)
if argc == 1:
    exit()

try:
    assert argc == 2, "more than one argument is provided."
    assert argv[1].isdigit(), "argument is not an integer."
    print("I'm Even.") if is_even(int(argv[1])) else print("I'm Odd.")
except AssertionError as e:
    print(f"AssertionError: {e}")
