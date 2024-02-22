---
layout: default
---

# Exercises Re01

> [!IMPORTANT]
> You must start by downloading the script
>
> [download_re01.py](link.org)
>
> Right-click and select “Save link as…”. You may need to confirm the download in your browser.
> Run this script in VSCode to download the files you need for the first lecture. The script does not need to be located a specific place on your computer.

## Exercise 1.1: Herons Formula

Herons Forumla is a formula used to calculate the area of a trangle if you know the sides of it. The equation looks like this:
$$
A = \sqrt{s(s-a)(s-b)(s-c)}
$$
Where s is half of the perimiter:
$$
s = \frac{(a+b+c)}{2}
$$
Complete the function ```triangle_area``` in file ```cp/re01/heron.py``` which takes as input three floats ```a```, ```b```, and ```c```, which represent the sides of a triangle. The function should _print_ the area of the triangle. Along with this, there is a limit on the traingle, which states that the largest side has to be smaller than the sum of the two other sides.

$$
a+b > c \ \ \ \text{if} \ \ \ c = \max([a,b,c])
$$

If this inequality is not true, then the function should _print_ ```"Not a triangle"```

```python
>>> traingle_area(1,2,2)
0.96825
>>> triangle_area(3,4,5)
6
>>> traingle_area(1,2,4)
'Not a triangle'
```

__cp.re01.heron.${\color{purple}\text{triangle\_area}}$(_a_, _b_, _c_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculate and print the area of a triangle using Heron's formula.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __a__ (```float```) - side length 1 \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __b__ (```float```) - side length 2 \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __c__ (```float```) - side length 3

## Exercise 1.2 Vowels

Complete the function ```count_vowels``` which takes ```word``` as input and counts how many vowels [a, e, i, o, u] there are in the word, and returns ```count``` which is the count of vowels.

```python
>>> print(count_vowels("string"))
1
>>> print(count_vowels("alphabet"))
3
>>> print(count_vowels("why"))
0
```

__cp.re01.vowels.${\color{purple}\text{count\_vowels}}$(_word_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Count the number of vowels in a word.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __word__ (```string```) - word to count vowels \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __count__ (```float```) - number of vowels

## Exercise 1.3 Remove Ducplicates

Complete the function ```remove_duplicates``` that removes duplicates from a list. It takes a list ```lst``` as input and returns the list without duplicates ```new_list```.

```python
>>> print(remove_duplicates([1, 2, 3, 4, 5, 1, 2])
[1, 2, 3, 4, 5]
>>> print(remove_duplicates(["apple", "pear", "banana", "pear", "banana"])
["apple", "pear", "banana"]
>>> print(remove_duplicates([1, 2, 3, "a", "b", "c"]))
[1, 2, 3, "a", "b", "c"]
```

__cp.re01.remove_duplicates.${\color{purple}\text{remove\_duplicates}}$(_list_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove duplicates from a list.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __lst__ (```list```) - List of items \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __new_list__ (```list```) - List of items with duplicates removed

## Exercise 1.4 Find the longest word in a list of words
