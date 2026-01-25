def all_thing_is_obj(arg: object) -> str | None:
    types = {
        list: f"List : {type(arg)}",
        tuple: f"Tuple : {type(arg)}",
        set: f"Set : {type(arg)}",
        dict: f"Dict : {type(arg)}",
        str: f"{arg} is in the kitchen : {type(arg)}",
    }
    if type(arg) in types:
        print(types[type(arg)])
    elif (type(arg)) is int:
        print(42)
        return "Type not found"
