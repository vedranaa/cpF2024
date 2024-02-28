---
layout: default
---

# Exercises Re01

> [!IMPORTANT]
> You must start by downloading the script
>
> [Link not working yet - download_re01.py](link.org)
>
> Right-click and select “Save link as…”. You may need to confirm the download in your browser.
> Run this script in VSCode to download the files you need for the first lecture. The script does not need to be located a specific place on your computer.

The following exercises are not all supposed to be completed today. This is a collection of exercises that you can use to practice your skills on your own as well, but all of the TA's are more than capable of helping you with it.

This week there are 13 exercises.  The exercises are divided into 2 parts, the first part is normal exercises to practice your skills (1-10). The second part is a similar to the exam, where you have to write a function that solves a specific problem (11-13).

If you have any questions, feel free to ask. Send an email to [s194113@dtu.dk](matilto:s194113@dtu.dk?subject=02002_Brush_Up_Course).


## Exercise 1.1: Herons Formula

Herons Formula is a formula used to calculate the area of a triangle if you know the sides of it. The equation looks like this:
$A = \sqrt{s(s-a)(s-b)(s-c)}$
Where s is half of the perimeter:
$s = \frac{(a+b+c)}{2}$
Complete the function ```triangle_area``` in file ```cp/re01/heron.py``` which takes as input three floats ```a```, ```b```, and ```c```, which represent the sides of a triangle. The function should _print_ the area of the triangle. Along with this, there is a limit on the triangle, which states that the largest side has to be smaller than the sum of the two other sides.

$$
a+b > c \ \ \ \text{if} \ \ \ c = \max([a,b,c])
$$

If this inequality is not true, then the function should _print_ ```"Not a triangle"```

```python
>>> triangle_area(1,2,2)
The area of the triangle is: 0.96825
>>> triangle_area(3,4,5)
The area of the triangle is: 6
>>> triangle_area(1,2,4)
Not a triangle
```

__cp.re01.heron.triangle\_area(_a_, _b_, _c_)__

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

__cp.re01.vowels.count\_vowels(_word_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Count the number of vowels in a word.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __word__ (```string```) - word to count vowels \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __count__ (```float```) - number of vowels

## Exercise 1.3 Find the longest word in a list of words

Complete the function ```find_longest_word``` to find the longest word in a sentence. It should return the longest word as a string. Punctuation should not count towards a words length. There will not be any words in the sentences with contractions.

```python
>>> print(find_longest_word("This sentence is a test"))
"sentence"
>>> print(find_longest_word("Long words do not have dots."))
"words"
```

__cp.re01.longest_word.find\_longest\_word(_sentence_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find the longest word in a list of words.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __sentence__ (```string```) - Sentence without contractions \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __longest_word__ (```string```) - Longest word in the sentence

## Exercise 1.4: Find the duplicates in a list

Complete the function ```find_duplicates``` to find any duplicates in a list. It takes ```lst``` as input, which is a list and returns a list of only the elements that appear more than once, ```duplicates```. If there are no elements that appear more than once it should return an empty list.

```python
>>> print(find_duplicates([1, 2, 3, 4, 5, 1, 2]))
[1, 2]
>>> print(find_duplicates(["apple", "pear", "banana", "pear", "banana"]))
["pear", "banana"]
>>> print(find_duplicates([1, 2, 3, "a", "b", "c"]))
[]
```

__cp.re01.duplicates.find\_duplicates(_lst_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Finds duplicates in a list.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __lst__ (```list```) - Sentence without contractions \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __duplicates__ (```list```) - Longest word in the sentence

## Exercise 1.5 Remove Duplicates

Complete the function ```remove_duplicates``` that removes duplicates from a list. It takes a list ```lst``` as input and returns the list without duplicates ```new_list```.

```python
>>> print(remove_duplicates([1, 2, 3, 4, 5, 1, 2]))
[1, 2, 3, 4, 5]
>>> print(remove_duplicates(["apple", "pear", "banana", "pear", "banana"]))
["apple", "pear", "banana"]
>>> print(remove_duplicates([1, 2, 3, "a", "b", "c"]))
[1, 2, 3, "a", "b", "c"]
```

__cp.re01.remove_duplicates.remove\_duplicates(_list_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove duplicates from a list.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __lst__ (```list```) - List of items \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __new_list__ (```list```) - List of items with duplicates removed

## Exercise 1.6: Reverse a sentence

Complete the function ```reverse_sentence``` to reverse a sentence. The sentences will not have any punctuation in them. It should take ```sentence```as input, and return ```reversed_sentence``` both as strings.

```python
>>> print(reverse_sentence("This sentence is a test"))
"test a is sentence This"
>>> print(reverse_sentence("Another test sentence"))
"sentence test Another"
```

__cp.re01.reverse_sentence.reverse\_sentence(_sentence_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Reverse a string
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __sentence__ (```string```) - Sentence without punctuation \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __reversed_sentence__ (```string```) - Reversed sentence

## Exercise 1.7: Calculate the GC content of a DNA sequence

Complete the function ```calculate_gc_content``` to calculate the GC content of a DNA sequence. The function takes an input of a DNA string ```dna_sequence```, counts how many "G"s and "C"s there are. This is then returned as a percentage of how many total length of the DNA sequence, ```gc_content```.

```python
>>> print(calculate_gc_content("ATGCGTA"))
42.857142857
>>> print(calculate_gc_content("ATCTAGACTAC"))
36.36363636363637
```

__cp.re01.gc_content.find\_longest\_word(_sentence_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculates the GC content of a DNA sequence.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __dna_sequence__ (```string```) - The DNA sequence. \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __gc_content__ (```float```) - The GC content as a percentage.

## Exercise 1.8: See if two RNA strand could make DNA

Check if two RNA strands can form a DNA strand. The function ```is_dna_possible``` should take two RNA represented by strings ```rna1``` and ```rna2```. It should return ```True``` if the two RNA strands could become DNA together.

The RNA's are composed only of letters in the list ```["A", "T", "G", "C"]```. The two RNA strands fit if at the same index, one has an A and the other has a T, or one has a C and the other has a G. Fx. "AGC" fits with "TCG", but not "TGC". If there is _any_ error, the RNA cannot combine and the function should return ```False```. The two RNA strands should also have the same length.

```python
>>> print(is_dna_possible("ATGCGTAG","TACGCATC"))
True
>>> print(is_dna_possible("AGTCAGTA","TCAGTCAT"))
False
```

__cp.re01.rna.is\_dna\_possible(_rna1_,_rna2_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Check if two RNA strands can form a DNA strand.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __rna1__ (```string```) - a string representing the first RNA strand \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __rna2__ (```string```) - a string representing the second RNA strand \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __x__ (```boolean```) - True if the RNA strands can form a DNA strand, False otherwise.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;False otherwise

## Exercise 1.9: Calculate the deflection of a beam

Complete the function ```calculate_beam_deflection``` to find the deflection of a beam under a given load. The deflection follows the formula:

$$
D = \frac{M*L^3}{3*\lambda*I}
$$

Where D is the deflection, M is the load, L is the length of the beam, $\lambda$ is the modulus of elasticity and $I$ is the moment of inertia. Complete the function using the parameters ```length```, ```load```, ```modulus_of_elasticity``` and ```moment_of_inertia```, which returns the deflection ```deflection```

```python
>>> print(calculate_beam_deflection(1,1,1,1))
0.3333333
>>> print(calculate_beam_deflection(3,2,3,1))
6
```

__cp.re01.beam_deflection.calculate\_beam\_deflection(_length_, _load_, _modulus_of_elasticity_, _moment_of_inertia_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculates the deflection of a beam under a given load using engineering principles.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __length__ (```float```) - Length of the beam in meters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __load__ (```float```) - Magnitude of the load applied to the beam in newtons. \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __modulus_of_elasticity__ (```float```) - Modulus of elasticity of the beam
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;material in pascals. \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __moment_of_inertia__ (```float```) - Moment of inertia of the beam in
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;meters to the fourth power. \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __deflection__ (```float```) - Deflection of the beam in meters.

## Exercise 1.10: Compare the BMI of a person over a period of time

Complete the function ```check_health``` to check the health of a person based on their weights and heights over a period of time. The function takes ```weights``` and ```heights``` as input, which are lists of weights and heights respectively, each item in the list representing a new year. You should calculate the BMI of the person for each year:

$$
BMI = \frac{w}{h^2}
$$

Where h is the height, and w is the weight. If the BMI ever gets over 25, the function should return ```"High BMI detected at index i"```, where i is the index where the BMI went over 25. If the BMI ever changes by more than ```max_bmi_diff``` between two years, the function should return ```"Unstable BMI detected at index i"```. If none of these things happen throughout the list, the function should return the BMI of the last year in the list.

```python
>>> print(check_health([60, 65, 70, 75, 80], [1.65, 1.70, 1.75, 1.80, 1.85], 1.1))
'High BMI detected at index 4'
>>> print(check_health([65, 70, 75, 80], [1.65, 1.70, 1.75, 1.80], 1.0))
24.6913580247
```

__cp.re01.bmi_compare.check\_health(_weights_, _heights_, _max_bmi_diff_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove duplicates from a list.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __weights__ (```list```) - List of weights \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __heights__ (```list```) - List of weights \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __max_bmi_diff__ (```float```) - List of weights \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __bmi__ (```float```) - BMI of last year \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __str__ (```string```) - If the BMI ever becomes too high or unstable

## Exercise 1.11: Median of a list of numbers

Complete the function ```median``` to find the median of a list of numbers. The median is the number that is in the middle of a data set if the set is ordered from largest to smallest. The function should take an input ```numbers``` and return the median. If the list has an even length, take the average of the two middle values.

```python
>>> print(median([1,5,2,4,3]))
3
>>> print(median([2,4,6,8,5,10,12,15,16,17])
9
```

__cp.re01.media.median(_numbers_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Calculate the median of a list of numbers.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __numbers__ (```list```) - Sentence without contractions \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __med__ (```float```) - Median of the list

## Exercise 1.12: Find the highest score in a list of scores

Complete the function ```highest_score``` to find the highest exam score that is not the first or last score. The function takes a list as input ```scores``` and returns a float of the ```score```. There will always be 3 or more scores on the list.

```python
>>> print(highest_score([90.5,80.3,60.2,80.9, 96.5]))
80.9
>>> print(highest_score([62.9,75.5,89.9,60.4]))
89.9
```

__cp.re01.high_score.highest\_score(_scores_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find the highest score in a list of scores that is not the first or last score.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __scores__ (```list```) - List of scores\
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __score__ (```float```) - Highest score on the list.

## Exercise 1.13: List comparison

Complete the function ```sum_index``` to find the index, where the sum of the first list up to that index is larger than the sum of the second list up to the same index. The function takes two lists as input ```list1``` and ```list2``` and returns the index ```i``` where the above occurs. If this never happens, then return ```-1```.

```python
>>> print(sum_index([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
-1
>>> print(sum_index([1,2,3,4,5,6,7,8,9,10],[5,5,5,5,5,5,5,5,5,5]))
9
```

__cp.re01.list_compare.sum\_index(_list1_,_list2_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Remove duplicates from a list.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __list1__ (```list```) - 1. list \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __list2__ (```list```) - 2. list \
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns \
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __i__ (```int```) - Index where the sum of list1 up to this point is larger than
>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list2. Returns -1 if this doesn't occur
