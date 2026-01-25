
import math  # .isnan() detects float NULL


def NULL_not_found(arg: object) -> int | None:
    match arg:
        case None:
            print(f"Nothing: {arg} {type(arg)}")
        case False:
            print(f"Fake: {arg} {type(arg)}")
        case 0:
            print(f"Zero: {arg} {type(arg)}")
        case x if isinstance(x, float) and math.isnan(x):
            print(f"Cheese: {arg} {type(arg)}")
        case "":
            print(f"Empty: {arg} {type(arg)}")
        case _:
            print("Type Not Found")
            return 1
    return 0
