ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list[1] = "World!"
print(ft_list)

ft_temp_tuple = list(ft_tuple)
ft_temp_tuple[1] = "Spain"  # type: ignore
ft_tuple = tuple(ft_temp_tuple)
print(ft_tuple)

ft_set.remove("tutu!")
ft_set.add("Malaga")
print(ft_set)

ft_dict["Hello"] = "42Malaga"
print(ft_dict)
