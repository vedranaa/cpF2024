---
layout: default
---
# Exercises Re04

> You must start by downloading the script
>
> [download_re04.py](download_scripts/download_re04.py)
>
> Right-click and select “Save link as…”
> Run this script in VSCode to download the files you need for today's exercise. The script does not need to be located a specific place on your computer.

The following exercises are not all supposed to be completed today. This is a collection of exercises that you can use to practice your skills on your own as well, but all of the TA's are more than capable of helping you with it.

This week there are 13 exercises.  The exercises are divided into 2 parts, the first part is normal exercises to practice your skills (1-10). The second part is a similar to the exam, where you have to write a function that solves a specific problem (11-13).

If you have any questions, feel free to ask. Send an email to [s194113@dtu.dk](matilto:s194113@dtu.dk?subject=02002_Brush_Up_Course).

## Exercise 4.1: Sort a dictionary by its values

Create a function called `sort_dict_by_values` that takes a dictionary `d` as input and returns a list of tuples containing the dictionary's items, sorted by values.

```python
>>> d = {"a": 3, "b": 2, "c": 1}
>>> sort_dict_by_values(d)
[("c", 1), ("b", 2), ("a", 3)]
```

The function tests can be run by inserting your solution into the file `cp/re04/sort`.

__cp.re04.sort.sort_dict_by_values(d)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sort a dictionary by its values.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __d__ (``dict``) - a dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``list``) - a list of tuples containing the dictionary's items, sorted by values.

## Exercise 4.2: Map Two Lists into a Dictionary

Create a function `map_lists_into_dict` that maps two lists into a dictionary.

This function takes two parameters:
- `keys`: a list of keys.
- `values`: a list of values.

Your task is to implement the `map_lists_into_dict` function according to the specifications provided.

```python
>>> keys = ["a", "b", "c"]
>>> values = [1, 2, 3]
>>> map_lists_into_dict(keys, values)
{'a': 1, 'b': 2, 'c': 3}
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re04/maplists`.

__cp.re04.maplists.map_lists_into_dict(keys, values)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Map two lists into a dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __keys__ (``list``) - a list of keys.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __values__ (``list``) - a list of values.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``dict``) - a dictionary.

## Exercise 4.3: Coutning Characters in a String

Create a function called `count_chars` that takes a string `s` as input and returns a dictionary containing the characters as keys and their counts as values. It should turn all letters lowercase as well.

```python
>>> count_chars("hello")
{"h": 1, "e": 1, "l": 2, "o": 1}
```

The function tests can be run by inserting your solution into the file `cp/re04/string`.

__cp.re04.string.count_chars(s)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Count the characters in a string.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __s__ (``str``) - a string.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``dict``) - a dictionary containing the characters as keys and their counts as values.

## Exercise 4.4: Extract Key's Value if Key is Present

Implement the function `extract_key_value` that extracts the value corresponding to keys present in both a list and a dictionary.

This function takes two parameters:
- `lst`: a list of keys.
- `dict`: a dictionary.

Your task is to implement the `extract_key_value` function according to the specifications provided.

```python
>>> d = {"a": 1, "b": 2, "c": 3}
>>> extract_key_value(["a", "b", "c"], d)
[1, 2, 3]
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re04/extractkeys`.

__cp.re04.extractkeys.extract_key_value(lst, dict)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extract Key's Value if key is present in list and dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __lst__ (``list``) - a list of keys.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __dict__ (``dict``) - a dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``list``) - the value corresponding to the key in the data.

## Exercise 4.5: Encryption via Dictionary

Implement the function `encrypt` that encrypts a text using a provided dictionary as a key.

This function takes two parameters:
- `text`: a string.
- `key`: a dictionary.

Your task is to implement the `encrypt` function according to the specifications provided.

```python
>>> key1 = {"a" : "b", "b" : "c", "c" : "d", "d" : "e", "e" : "f", "f" : "g", "g" : "h", "h" : "i", "i" : "j", "j" : "k", "k" : "l", "l" : "m", "m" : "n", "n" : "o", "o" : "p", "p" : "q", "q" : "r", "r" : "s", "s" : "t", "t" : "u", "u" : "v", "v" : "w", "w" : "x", "x" : "y", "y" : "z", "z" : "a"}
>>> encrypt("hello", key1)
'ifmmp'
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re04/encryption`.

__cp.re04.encryption.encrypt(text, key)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Encrypt a text using a dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __text__ (``str``) - a string.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __key__ (``dict``) - a dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``str``) - a string.  

## Exercise 4.6: Star Sign

You are provided with a dictionary `signs` containing information about star signs, including their start and end dates, associated elements, and ruling planets.

```python
signs = {
    'aries': ('21/03', '20/04', 'fire', 'mars'),
    'taurus': ('21/04', '20/05', 'earth', 'venus'),
    'gemini': ('21/05', '20/06', 'air', 'mercury'),
    'cancer': ('21/06', '22/07', 'water', 'moon'),
    'leo': ('23/07', '22/08', 'fire', 'sun'),
    'virgo': ('23/08', '22/09', 'earth', 'mercury'),
    'libra': ('23/09', '22/10', 'air', 'venus'),
    'scorpio': ('23/10', '21/11', 'water', 'mars'),
    'sagittarius': ('22/11', '21/12', 'fire', 'jupiter'),
    'capricorn': ('22/12', '19/01', 'earth', 'saturn'),
    'aquarius': ('20/01', '18/02', 'air', 'uranus'),
    'pisces': ('19/02', '20/03', 'water', 'neptune')
}
```

Write a function called `starsign` that takes a string `date` in the format 'dd/mm' as input and returns a tuple containing the star sign, element, and ruling planet associated with that date.

```python
>>> starsign("01/01")
("capricorn", "earth", "saturn")
```

The function tests can be run by placing your solution in the file `cp/re04/starsign`.

__cp.re04.starsign.starsign(date)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Get star sign, element, and ruling planet.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __date__ (``str``) - a string in the format 'dd/mm'.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``tuple``) - a tuple containing the star sign, element, and ruling planet.

## Exercise 4.7: Stem and Leaf Dictionary

Create a function named `stem_and_leaf` that accepts two parameters: a list of integers `data` and an integer `key`. This function should return a dictionary where the keys are the stems obtained by dividing each number in the `data` list by the `key`, and the values are lists containing the corresponding leaves.

```python
>>> stem_and_leaf([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
{0: [1, 2, 3, 4, 5, 6, 7, 8, 9]}
```

The function tests can be executed by placing your implementation in the file `cp/re04/stem_and_leaf`.

__cp.re04.stem_and_leaf.stem_and_leaf(data, key)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate a stem and leaf dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __data__ (``List[int]``) - a list of integers.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __key__ (``int``) - an integer.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``dict``) - a dictionary containing the stems as keys and the leaves as values.

Remember to implement the `stem_and_leaf` function according to the provided specifications.

## Exercise 4.8: One-to-One Dictionary Check

Implement the function `one_to_one` that determines if there are any dictionary values that violate the one-to-one principle. This means that all the values only appear once.

This function takes one parameter:
- `d`: a dictionary.

Your task is to implement the `one_to_one` function according to the specifications provided.

```python
>>> one_to_one({"a": 1, "b": 2, "c": 3})
True
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re04/onetoone`.

__cp.re04.onetoone.one_to_one(d)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find out if there are any dictionary values that go against the one-to-one principle.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __d__ (``dict``) - a dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``bool``) - a boolean value.


## Exercise 4.9: Turn a list of tuples into a dictionary

Create a function called `tuple_list_to_dict` that takes a list of tuples `lst` as input and returns a dictionary.

```python
>>> tuple_list_to_dict([("a", 1), ("b", 2), ("c", 3)])
{"a": 1, "b": 2, "c": 3}
```

The function tests can be run by inserting your solution into the file `cp/re04/tupledict`.

__cp.re04.tupledict.tuple_list_to_dict(lst)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn a list of tuples into a dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __lst__ (``list``) - a list of tuples.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``dict``) - a dictionary.

## Exercise 4.10: Convert Dictionary to List of Tuples

Implement the function `dict_to_tuple_list` that converts a dictionary into a list of tuples.

This function takes one parameter:
- `d`: a dictionary.

Your task is to implement the `dict_to_tuple_list` function according to the specifications provided.

```python
>>> dict_to_tuple_list({"a": 1, "b": 2, "c": 3})
[("a", 1), ("b", 2), ("c", 3)]
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re04/dicttuple`.

__cp.re04.dicttuple.dict_to_tuple_list(d)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Turn a dictionary into a list of tuples.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __d__ (``dict``) - a dictionary.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``list``) - a list of tuples.

## Exercise 4.11: Department Top Salaries

Complete the function `salaries` that returns the top k salaries in a specified department.

This function takes three parameters:
- `d`: a dictionary where the key is the employee and the value is a tuple of the salary and the department.
- `department`: the department to filter.
- `k`: the number of top salaries to return.

Your task is to implement the `salaries` function according to the specifications provided.

```python
>>> d = {'Alice': (100000, 'HR'), 'Bob': (150000, 'Engineering'), 'Charlie': (120000, 'Engineering'), 'David': (200000, 'HR'), 'Eve': (180000, 'Engineering')}
>>> salaries(d, 'HR', 1)
[('David', (200000, 'HR'))]
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re04/salaries`.

__cp.re04.salaries.salaries(d, department, k)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the top k salaries in a department.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __d__ (``dict``) - a dictionary where the key is the employee and the value is a tuple of the salary and the department.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __department__ (``str``) - the department to filter.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __k__ (``int``) - the number of top salaries to return.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``list``) - a list of tuples with the top salaries.

## Exercise 4.12: Phonebook Area Code Percentage

Implement the function `percentage` that creates a dictionary with the state as the key and the percentage of phone numbers with that state's area code as the value. The returned dictionary should include all possible states, even if the percentage is 0.

This function takes one parameter:
- `phonebook`: a dictionary containing names and phone numbers.

Your task is to implement the `percentage` function according to the specifications provided. 

```python
>>> phonebook = {"Alice": "408-123-4567", "Bob": "415-234-5678", "Charlie": "831-345-6789", "David": "510-456-7890"}
>>> percentage(phonebook)
{'CA': 100, 'NY': 0, 'WA': 0, 'TX': 0, 'FL': 0, 'CO': 0, 'DC': 0, 'VA': 0, 'IL': 0, 'MI': 0, 'OH': 0}
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re04/phonebook`.

__cp.re04.phonebook.percentage(phonebook)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Create a dictionary with the state as the key and the percentage of phone numbers with that state's area code as the value.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __phonebook__ (``dict``) - a dictionary containing names and phone numbers.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``dict``) - a dictionary with the state as the key and the percentage of phone numbers with that state's area code as the value.

## Exercise 4.13: Degrees of Separation

Please complete the function `degrees_of_separation`, which calculates how many friends are between people in a social network. This is a very hard question, so please do not be discouraged. It should be solved with regression, lists and dictionaries. The users will be given as a dictionary of users of a website, and who their friends are. It will always be given that if Emma is friends with Alan, then Alan is friends with Emma.

This function takes four parameters:
- `users`: a dictionary containing the users and their friends.
- `start`: the starting user.
- `end`: the ending user.
- `visited`: a set of visited users. Will always be an empty list at the start.

Your task is to implement the `degrees_of_separation` function according to the specifications provided. Ensure that if the start and end users are the same, the degrees of separation is 0. If the start user and the end user have no connection, the degrees of separation should be `float('inf')`.

```python
>>> users = {
    'Robert': ['Brian', 'Mark'],
    'Mark': ['Eric', 'Brian', 'Robert'],
    'Brian': ['Eric', 'Mark', 'Robert'],
    'Eric': ['Mark', 'Brian'],
    'Albert': []
    }
>>> degrees_of_separation(users, 'Robert', 'Eric', [])
2
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re04/seperation`.

__cp.re04.seperation.degrees_of_separation(users, start, end, visited)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find the degrees of separation between two users.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __users__ (``dict``) - a dictionary containing the users and their friends.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __start__ (``str``) - the starting user.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __end__ (``str``) - the ending user.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __visited__ (``set``) - a set of visited users.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``float``) - the degrees of separation.