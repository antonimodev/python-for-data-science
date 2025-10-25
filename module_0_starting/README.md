◀️ [**Back to main repository**](https://github.com/antonimodev/python-for-data-science)

# MODULE 0 - Starting

The first module of the Python for Data Science Piscine from **Outer Core** in **42**.

It covers the language **fundamentals**: syntax, data types, functions, argument handling, data structures, list comprehensions, and creating Python packages.

# 📖 Index

- [**ex00 - First python script**](#ex00---first-python-script)
- [**ex01 - First use of package**](#ex01---first-use-of-package)
- [**ex02 - First function python**](#ex02---first-function-python)
- [**ex03 - Null not found**](#ex03---null-not-found)
- [**ex04 - The Even and the Odd**](#ex04---the-even-and-the-odd)
- [**ex05 - First standalone program python**](#ex05---first-standalone-program-python)
- [**ex06 - Filter function**](#ex06---filter-function)

<br>

## **ex00** - First python script

In this exercise I'll modify strings inside these data structures `list`, `tuple`, `set` and `dict`. The goal is to get the expected output:

```
['Hello', 'World!']
('Hello', 'Spain')
{'Hello', 'Malaga'}
{'Hello': '42Malaga'}
```

▶️ [**ex00**](https://github.com/antonimodev/python-for-data-science/tree/main/module_0_starting/ex00/Hello.py)

<br>

## **ex01** - First use of package

This exercise introduces date and time formatting using the `time` or `datetime` modules.
The script displays the current timestamp (in seconds since epoch) and the formatted current date.

```
Seconds since January 1, 1970: 1,666,355,857.3622 or 1.67e+09 in scientific notation
Oct 21 2022
```

▶️ [**ex01**](https://github.com/antonimodev/python-for-data-science/blob/main/module_0_starting/ex01/format_ft_time.py)


<br>

## **ex02** - First function python

Here I define a function `all_thing_is_obj()` that identifies and prints the type of a given object.
It returns 42 at the end and handles various Python data structures.

```
List : <class 'list'>
Tuple : <class 'tuple'>
Set : <class 'set'>
Dict : <class 'dict'>
Brian is in the kitchen : <class 'str'>
Toto is in the kitchen : <class 'str'>
Type not found
42
```

▶️ [**ex02**](https://github.com/antonimodev/python-for-data-science/tree/main/module_0_starting/ex02)

<br>

## **ex03** - NULL not found

The goal of this exercise is to detect different types of “null-like” values (`None`, `NaN`, `0`, `""`, `False`)
and print their names, values, and types.

The function returns 0 if everything goes well, or 1 if an unknown type is passed.

```
Nothing: None <class 'NoneType'>
Cheese: nan <class 'float'>
Zero: 0 <class 'int'>
Empty: <class 'str'>
Fake: False <class 'bool'>
Type not Found
1
```
▶️ [**ex03**](https://github.com/antonimodev/python-for-data-science/tree/main/module_0_starting/ex03)

<br>

## **ex04** - The Even and the Odd

This script takes a number as an argument and determines whether it is even or odd.
It also handles invalid input and argument errors with clear assertion messages.

```
$ python whatis.py 14
I'm Even.

$ python whatis.py -5
I'm Odd.

$ python whatis.py Hi!
AssertionError: argument is not an integer

$ python whatis.py 13 5
AssertionError: more than one argument is provided
```

▶️ [**ex04**](https://github.com/antonimodev/python-for-data-science/blob/main/module_0_starting/ex04/whatis.py)

<br>

## **ex05** - First standalone program python

I build a program that analyzes a text and counts uppercase letters, lowercase letters, punctuation marks, spaces, and digits.
If no argument is provided, it prompts the user to input text.

```
$ python building.py "Python 3.0, released in 2008, was a major revision that is not completely backward
compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020."
The text contains 171 characters:
2 upper letters
121 lower letters
7 punctuation marks
26 spaces
15 digits
```

▶️ [**ex05**](https://github.com/antonimodev/python-for-data-science/blob/main/module_0_starting/ex05/building.py)

<br>

## **ex06** - Filter function

I recreate Python's built-in `filter()` function as `ft_filter()`. The goal is understand how iterators, callables and truthy evaluation work in Python.

Then, I create a program that uses `ft_filter()`to process input:
Take string `S` and an integer `N`, and prints a list of words from `S` longer than `N`.

It also makes use of both a **list comprehension** and a **lambda** expression.

```
$ python filterstring.py "Hello the World" 4
['Hello', 'World']

$ python filterstring.py "Hello the World" 99
[]

$ python filterstring.py 3 "Hello the World"
AssertionError: the arguments are bad
```

▶️ [**ex06**](https://github.com/antonimodev/python-for-data-science/blob/main/module_0_starting/ex06/)