---
layout: default
---


# Exercises Re01

> You must start by downloading the script
>
> [download_re01.py](download_scripts/download_re01.py)
>
> Right-click and select “Save link as…”.
> Run this script in VSCode to download the files you need for today's exercise. The script does not need to be located a specific place on your computer.

The following exercises are not all supposed to be completed today. This is a collection of exercises that you can use to practice your skills on your own as well, but all of the TA's are more than capable of helping you with it.

This week there are 13 exercises.  The exercises are divided into 2 parts, the first part is normal exercises to practice your skills (1-10). The second part is a similar to the exam, where you have to write a function that solves a specific problem (11-13).

If you have any questions, feel free to ask. Send an email to [s194113@dtu.dk](matilto:s194113@dtu.dk?subject=02002_Brush_Up_Course).

## Exercise 2.1: Simulate Collision

Complete the function called `simulate_motion` that takes four parameters: `v1` and `v2`; The initial speeds of the cars, and `x1` and `x2`; The initial positions of the cars. This function should return one of two strings: If the cars at any time in the future would collide, return a string that states `"The objects will collide at time x seconds."`, where `x` is the time it would take. If the cars wouldn't collide, it should return the string `"The objects will never collide."`.

Please use what you have learned in Physics to solve this question. If in doubt, the position of a car with a given initial speed and position is:

$$
x(t)= x_0 + v_0*t
$$

```python
>>> simulate_motion(1, 2, 3, 6)
The objects will never collide.
>>> simulate_motion(3,4,5)
The objects will collide at time 3.0 seconds.
```

The tests for the function ```simulate_motion``` can be run by inserting your solution into the file ```cp/re02/physics```.

__cp.re01.physics.simulate_motion(_v1_,_v2_,_x1_,_x2_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Simulate the motion of two objects. Tell when they will collide.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __v1__ (```float```) - the velocity of the first object \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __v2__ (```float```) - the velocity of the second object \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __x1__ (```float```) - the initial position of the first object \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __x2__ (```float```) - the initial position of the second object \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __string__ (```string```) - When and if the objects will collide

## Exercise 2.2: Dictionary of strings

Complete the function `dictionary_length` that takes a list `l` of strings and returns a dictionary, `d`, that has the strings as keys and the length of the strings as the value.

```python
>>> dictionary_length(["hello", "world", "python", "programming", "language"])
{'hello': 5, 'world': 5, 'python': 6, 'programming': 11, 'language': 8}
>>> dictionary_length(['a', 'ab', 'abc', 'abcd'])
{'a': 1, 'ab': 2, 'abc': 3, 'abcd': 4}
```

The tests for the function ```dictionary_length``` can be run by inserting your solution into the file ```cp/re02/dictionary1```.

__cp.re01.permutations.permutations(_s_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Given a list of strings, return a dictionary with the length of each string as values and the strings as keys.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __l__ (```list```) - list of words \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Return \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __d__ (```dict```) - dictionary with words as keys and lengths as values \

## Exercise 2.3: Dictionary of strings 2

Complete the function `dictionary_lengths` that takes a list `l` of strings and returns a dictionary, `d`, that has the lengths as the keys, and a list of all strings in `l` with that length as the value.

```python
>>> dictionary_length(["hello", "world", "python", "programming", "language"])
{5: ['hello', 'world'], 6: ['python'], 11: ['programming'], 8: ['language']}>>> dictionary_length(['a', 'ab', 'abc', 'abcd'])
{1: ["a"], 2: ["ab"], 3: ["abc"], 4: ["abcd"]}
```

The tests for the function ```dictionary_lengths``` can be run by inserting your solution into the file ```cp/re02/dictionary2```.

__cp.re01.permutations.permutations(_s_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Given a list of strings, return a dictionary with the length of each string as keys and a list of strings with that length as the value.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __l__ (```list```) - list of words \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Return \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __d__ (```dict```) - dictionary with words as values and lengths as keys \

## Exercise 2.4: Palindrome Check

Complete the function `is_palindrome` that takes a string `s` and returns `True` if the string is a palindrome, and `False` otherwise. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward. Your function should ignore any non-alphanumeric characters and should be case-insensitive.

```python
>>> is_palindrome('abba')
True
>>> is_palindrome('abab')
False
```

The tests for the function ```is_palindrome``` can be run by inserting your solution into the file ```cp/re02/palindrome```.

__cp.re01.palindrome.is_palindrome(_s_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return True if the input string is a palindrome, False otherwise.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __s__ (```str```) - string \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Return \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __b__ (```bool```) - True or False if palindrome or not \

## Exercise 2.5: Pascals Triangle

Complete the function `pascals_triangle` that takes a positive integer `n` and returns a list of elements on the nth row of pascals triangle.

Pascal's triangle is made by summing the two numbers above it self (see the figure below). This means that if the two numbers above are 1 and 1, the number below will become 2. The number on the edges is always 1.

![Picture](download.png)

```python
>>> pascals_triangle(1)
[1, 1]
>>> pascals_triangle(3)
[1, 3, 3, 1]
```

The tests for the function ```pascals_triangle``` can be run by inserting your solution into the file ```cp/re02/pascals_triangle```.

__cp.re01.pascals_triangle.pascals_triangle(_n_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return Pascal's nth row.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __n__ (```int```) - line number to generate \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Return \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __l__ (```list```) - list of numbers in the nth row of pascals triangle \

## Exercise 2.11: Permutations

Complete the function called `permutations` that takes a string `s`, and returns `perms`, a list of all possible permutations of this string. A permutation is when you shuffle around all of the items in a group. Fx. "ab" has the two permutations "ba" and "ab". Your code should also not include duplicates, such that the only permutation of "bb" is "bb". This function should test your recursive knowledge, and is quite hard.

```python
>>> permutations('aa')
["aa"]
>>> permutations('abc')
['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
```

The tests for the function ```permutations``` can be run by inserting your solution into the file ```cp/re02/permutations```.

__cp.re01.permutations.permutations(_s_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return all possible permutations of a string.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __s__ (```string```) - initial string \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Return \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __perm__ (```list```) - the velocity of the first object \
