---
layout: default
---
# Exercises Re05

> You must start by downloading the script
>
> [download_re05.py - Not working yet]()
>
> Right-click and select “Save link as…”
> Run this script in VSCode to download the files you need for today's exercise. The script does not need to be located a specific place on your computer.

The following exercises are not all supposed to be completed today. This is a collection of exercises that you can use to practice your skills on your own as well, but all of the TA's are more than capable of helping you with it.

This week, the exercises are formatted a bit different. You will be working on 3 small exercises, and 2 larger exercises, which all have smaller sub-exercises to solve along the way. This is to make sure you understand the reasoning behind doing work in classes instead of other things. If you missed the mini-lecture, please read up on the topic here: [Link](https://cp.pages.compute.dtu.dk/02002public/exercises/ex9.html)

If you have any questions, feel free to ask. Send an email to [s194113@dtu.dk](matilto:s194113@dtu.dk?subject=02002_Brush_Up_Course).

## Exercise 5.1: Full Name Class

Create a class called `Full_Name`. This class should take in a first name and a last name as parameters and should be able to return the full name.

Here's the structure of the `Full_Name` class:

```python
class Full_Name():
    def __init__(self, First_Name, Last_Name):
        """Your answer here"""

    def get_full_name(self):
        """Your answer here"""
```

You can test your class by creating an instance of `Full_Name` and calling the `get_full_name` method:

```python
>>> person = Full_Name("John", "Doe")
>>> person.get_full_name()
'John Doe'
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re05/names`.

>__cp.re05.names.Full_Name()__

>__cp.re05.names.Full_Name.\_\_init\_\_(First_Name, Last_Name)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initialize the Full_Name class.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __First_Name__ (``str``) - The first name.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __Last_Name__ (``str``) - The last name.

>__cp.re05.names.FullName.get_full_name()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the full name.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``str``) - The full name (first name followed by last name and a space in between).

## Exercise 5.2: Counter Class

Create a class called `Counter`. This class should have a method `increment` that increases a count by 1 each time it's called.

You can test your class by creating an instance of `Counter` and calling the `increment` method:

```python
>>> counter = Counter()
>>> counter.increment()
>>> counter.get_count
1
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re05/counter.py`.

>__class cp.re05.counter.Counter()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initialize the Counter class.

>__cp.re05.counter.Counter.increment()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Increase the count by 1.

## Exercise 5.3: Temperature Class

Create a class called `Temperature`. This class should take two inputs, `type`, which can be `"C"` or `"F"` for celcius and farenheit respectively, and `temp`, which should be the temperature in either of these measurement methods. 

The Class should have four methods: 1. `set_temp(self,temp)`, which should set the temperature for either Celcius or Farenheit, depending on which was specified at the start; 2. `set_temp(self,temp)`, which should get the temperature for either Celcius or Farenheit, depending on which was specified at the start; 3. `to_celcius(self)`, should return the defined temperature if `"C"` was specified at the start, or the coresponding temperature in Farenheit if `"F"` was specified at the start. The equation for conversion is:

$$
 T_C = (T_F-32)*5/9
$$

Lastly, `to_farenheit(self)` should return the defined temperature if `"F"` was specified at the start, or the coresponding temperature in Celcius if `"C"` was specified at the start. 

```python
>>> T = Temperature("F",32)
>>> T.to_celcius()
0
>>> T.to_farenheit()
32
>>> T.set_temp(320)
>>> T.to_celcius()
160
```

Once implemented, you can test the function by running the function tests provided in the file `cp/re05/temperature.py`.

>__cp.re05.temperature.Temperature(type,temp)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initilize a class representing the temperature

>__cp.re05.temperature.FullName. \_\_init\_\_()__


> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __type__ (``str``) - Type of temperature ("C" for celcius, "F" for farenheit)

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __temp__ (``int``) - Temperature in set type of measurement

>__cp.re05.temperature.FullName.get_temp()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the temperature in the set temperature scale

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``int``) - Temperature

>__cp.re05.temperature.FullName.set_temp()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set the temperature in the set temperature scale

>__cp.re05.temperature.FullName.to_celcius()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the temperature in celcius no matter the set temperature scale

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``int``) - Temperature in celcius

>__cp.re05.temperature.FullName.to_farenheit()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the temperature in farenheit no matter the set temperature scale

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``int``) - Temperature in farenheit

## Exercise 5.4 Books - Introduction

