---
layout: default
---
# Exercises Re05

> You must start by downloading the script
>
> [download_re05.py](download_scripts/download_re05.py)
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

Lastly, `to_fahrenheit(self)` should return the defined temperature if `"F"` was specified at the start, or the coresponding temperature in Celcius if `"C"` was specified at the start. 

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

>__cp.re05.temperature.Temperature.\_\_init\_\_()__


> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __type__ (``str``) - Type of temperature ("C" for celcius, "F" for farenheit)

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __temp__ (``int``) - Temperature in set type of measurement

>__cp.re05.temperature.Temperature.get_temp()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the temperature in the set temperature scale

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``int``) - Temperature

>__cp.re05.temperature.Temperature.set_temp()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Set the temperature in the set temperature scale

>__cp.re05.temperature.Temperature.to_celcius()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the temperature in celcius no matter the set temperature scale

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``int``) - Temperature in celcius

>__cp.re05.temperature.Temperature.to_fahrenheit()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the temperature in farenheit no matter the set temperature scale

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``int``) - Temperature in farenheit

## Exercise 5.4 Books - Introduction

The focus of this exercise will be to create a representation of a library of books. All books have a title, author and ISBN number (number to recognize a book from).

Your first task is to implement the `Book` class, which describes a book with the title, author and ISBN number. 

```python
>>> b = Book("Moby Dick", "Herman Melville", 9780142437247)
>>> b.title
"Moby Dick"
```

You should also implement 6 functions, three to change the title, author or ISBN if that ever should change.

```python
>>> b.set_title("The Whale")
>>> b.get_author()
"Herman Melville"
```
You can test your function in `cp/re05/books.py`

>__cp.re05.books.Book(title, author, ISBN)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initilize a class representing a book

>__cp.re05.books.Book.\_\_init\_\_()__

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __title__ (``str``) - Title of the book

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __author__ (``str``) - Author of the book

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __ISBN__ (``int``) - ISBN of the book

>__cp.re05.books.Book.get\_"X"()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the specified parameter from the book (so implement get_title, get_author and get_ISBN)

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``-``) - "X"

>__cp.re05.books.Book.set\_"X"()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set specified parameter from the book (so implement set_title, set_author and set_ISBN)

## Exercise 5.5 Get Info

Implement a function in the class `Book` called `info`, which takes no input, but returns the title, author and ISBN in a certain format: "_Book Name_ by _Author_, ISBN: _ISBN_":

```python
>>> b.info()
"The Whale by Herman Melville, ISBN: 9780142437247"
```

You can test your function in `cp/re05/books.py`

>__cp.re05.books.Book.info()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return the information that is specified.

## Exercise 5.6 Format Title

Implement a function, `format_title`, in the class, `Book` that takes a string of a books name as input, and returns the title with all of the words in the title capitalized.

```python
>>> b1 = Book("Ready Player One","Ernest Cline", 9780307887443)
>>> b1.format("the hunger games")
"The Hunger Games"
```

You can test your function in `cp/re05/books.py`

>__cp.re05.books.Book.format_title(title)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Format title with all words having a capitalized first letter.

## Exercise 5.7 Ebooks Introduction

Implement the new class `Ebook`, which is a subclass of the `Book` class introduced in 5.4. This class should take one more input than a book, being `file_size`. One should be able to use the function `get_file_size` and `set_file_size`, much like the functions from exercise 5.4.

You can test your function in `cp/re05/ebooks.py`

>__cp.re05.ebooks.EBook.(title, author, ISBN, file_size)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initilize a class representing an EBook

>__cp.re05.ebooks.EBook.\_\_init\_\_()__

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __title__ (``str``) - Title of the EBook

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __author__ (``str``) - Author of the EBook

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __ISBN__ (``int``) - ISBN of the EBook

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __file_size__ (``float``) - File size of the EBook

>__cp.re05.books.EBook.get\_file_size()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the file size

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return 

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; file_size (``float``) - File size of the EBook

>__cp.re05.ebooks.EBook.set\_file_size()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Set the file size of the EBook

## Exercise 5.8 Ebook info

Test to see if you can use the function implemented in the `Book` class using the `EBook` class. If this is possible, then implement the `info` function, much like in the `Book` Class. This time it should print out as follows "_Book Name_ by _Author_, ISBN: _ISBN_, File Size: _file\_size_":

```python
>>> e = EBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "1.5")
>>> e.info()
"The Great Gatsby by F. Scott Fitzgerald, ISBN: 9780743273565, File Size: 1.5"
```

>__cp.re05.ebooks.EBook.info()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return the information that is specified.

## Exercise 5.9 Library introduction

Create a respresentation of a library, which can hold both books and ebooks. The library should have a function `add_book` and `add_ebook`, which should add a book or ebook to the library. The library should also have a function `get_books` and `get_ebooks`, which should return all the books and ebooks in the library.

```python	
>>> l = Library()
>>> b = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565")
>>> e = EBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "1.5")
>>> l.add_book(b)
>>> l.add_ebook(e)
>>> l.get_num_books()
1
>>> l.get_num_ebooks()
1
```

You can test your function in `cp/re05/library.py`

>__cp.re05.library.Library()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initilize a class representing a library

>__cp.re05.library.Library.add_book(book)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add a book to the library

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __book__ (``Book``) - Book to be added to the library

>__cp.re05.library.Library.add_ebook(ebook)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add an EBook to the library

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __ebook__ (``EBook``) - EBook to be added to the library

>__cp.re05.library.Library.get_num_books()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the number of books in the library

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``int``) - Number of books in the library

>__cp.re05.library.Library.get_num_ebooks()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the number of EBooks in the library

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``int``) - Number of EBooks in the library

## Exercise 5.10 Library search

Implement a function in the `Library` class called `search`, which takes a string as input, and returns the info all the books and ebooks in the library that contains the string in the title. If no books are found, return "No books found".

```python
>>> l = Library()
>>> b = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780743273564")
>>> e = EBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", "1.5")
>>> l.add_book(b)
>>> l.add_ebook(e)
>>> l.search("Gatsby")
["The Great Gatsby by F. Scott Fitzgerald, ISBN: 9780743273564", "The Great Gatsby by F. Scott Fitzgerald, ISBN: 9780743273565, File Size: 1.5"]
```

You can test your function in `cp/re05/library.py`

>__cp.re05.library.Library.search(title)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the information of all books and EBooks that contains the title

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``list``) - List of all books and EBooks that contains the title

# Exercise 5.11: Atoms and Reactions - Introduction

In this exercise, you will be working with atoms and reactions. You will be creating a class called `Atom`, which will represent an atom. The `Atom` class should have the following attributes:

- `element` (str): The element of the atom (e.g. "H", "O", "C", etc.)
- `atomic_number` (int): The atomic number of the atom
- `atomic_mass` (float): The atomic mass of the atom

You should also implement the following methods in the `Atom` class:

- `get_element()`: Returns the element of the atom
- `__str__()`: Returns a string representation of the atom in the format "{element} ({atomic_number})"

```python
>>> atom = Atom("H", 1, 1.008)
>>> atom.get_element()
'H'
>>> print(atom)
'H (1)'
```

You can test your function in `cp/re05/chemical_reaction.py`

>__cp.re05.chemical_reaction.Atom(element, atomic_number, atomic_mass)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initilize a class representing an atom

>__cp.re05.chemical_reaction.Atom.\_\_init\_\_()__

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __element__ (``str``) - Element of the atom

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __atomic_number__ (``int``) - Atomic number of the atom

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __atomic_mass__ (``float``) - Atomic mass of the atom

>__cp.re05.chemical_reaction.Atom.get_element()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the element of the atom

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``str``) - Element of the atom

>__cp.re05.chemical_reaction.Atom.\_\_str\_\_()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return a string representation of the atom

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``str``) - String representation of the atom

## Exercise 5.12: Molecule Class

Create a class called `Molecule`, which will represent a molecule. The `Molecule` class should have the following attributes:

- `atoms` (list): A list of `Atom` objects that make up the molecule

You should also implement the following methods in the `Molecule` class:

- `add_atom(atom)`: Adds an `Atom` object to the list of atoms in the molecule
- `get_atoms()`: Returns the list of `Atom` objects in the molecule
- `get_formula()`: Returns the chemical formula of the molecule in the format "{element1}{element2}{element3}..." fx. "H2O"

```python
>>> h = Atom("H", 1, 1.008)
>>> o = Atom("O", 8, 15.999)
>>> h2o = Molecule()
>>> h2o.add_atom(h)
>>> h2o.add_atom(h)
>>> h2o.add_atom(o)
>>> h2o.get_formula()
'H2O'
>>> h2o.get_atoms()
[<cp.re05.chemical_reaction.Atom object at 0x7f8d3c7b5d30>, <cp.re05.chemical_reaction.Atom object at 0x7f8d3c7b5d60>, <cp.re05.chemical_reaction.Atom object at 0x7f8d3c7b5d90>]
```

The last part of this, while it seems like a bug, is actually the way python prints out the memory location of the object. This is not something you need to worry about, but it is good to know that this is what is happening. However, the list of atoms can be tested by doing this:

```python
>>> h2o.get_atoms()[0].get_element()
'H'
```

You can test your function in `cp/re05/chemical_reaction.py`

>__cp.re05.chemical_reaction.Molecule()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initilize a class representing a molecule

>__cp.re05.chemical_reaction.Molecule.add_atom(atom)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Add an atom to the molecule

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __atom__ (``Atom``) - Atom to be added to the molecule

>__cp.re05.chemical_reaction.Molecule.get_formula()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the chemical formula of the molecule

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``str``) - Chemical formula of the molecule

## Exercise 5.13: Chemical Reaction Class

Create a class called `Reaction`, which will represent a chemical reaction. The `Reaction` class should have the following attributes:

- `reactants` (list): A list of `Molecule` objects that are the reactants in the reaction
- `products` (list): A list of `Molecule` objects that are the products in the reaction

You should also implement the following methods in the `Reaction` class:

- `__str__()`: Returns a string representation of the reaction in the format "{reactant1} + {reactant2} + ... -> {product1} + {product2} + ..."
- `balance_reaction()`: Returns True or False depending on if the reaction is balanced or not. A reaction is balanced if the number of atoms of each element is the same on both sides of the reaction.

```python
>>> c = Atom("C", 6, 12.011)
>>> o = Atom("O", 8, 15.999)
>>> co2  = Molecule()
>>> co2.add_atom(c)
>>> co2.add_atom(o)
>>> co2.add_atom(o)
>>> h = Atom("H", 1, 1.008)
>>> h2 = Molecule()
>>> h2.add_atom(h)
>>> h2.add_atom(h)
>>> methanol = Molecule()
>>> methanol.add_atom(c)
>>> methanol.add_atom(o)
>>> methanol.add_atom(h)
>>> methanol.add_atom(h)
>>> methanol.add_atom(h)
>>> methanol.add_atom(h)
>>> h2o = Molecule()
>>> h2o.add_atom(h)
>>> h2o.add_atom(h)
>>> h2o.add_atom(o)
>>> r = Reaction([co2, h2, h2, h2], [methanol, h2o])
>>> r.balance_reaction()
True
```

You can test your function in `cp/re05/chemical_reaction.py`

>__cp.re05.chemical_reaction.Reaction(reactants, products)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initilize a class representing a reaction

>__cp.re05.chemical_reaction.Reaction.\_\_init\_\_()__

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Parameters

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __reactants__ (``list``) - List of Molecule objects that are the reactants in the reaction

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - __products__ (``list``) - List of Molecule objects that are the products in the reaction

>__cp.re05.chemical_reaction.Reaction.balance_reaction()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return True or False depending on if the reaction is balanced or not

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``bool``) - True if the reaction is balanced, False otherwise

## Exercise 5.14: Isotope Masses

You will now look at the mass of the different classes. Implement a function in the `Atom` class called `get_mass`, which returns the atomic mass of the atom. Along with this in `Atom` implement a function called `is_isotope`, which takes an `Atom` object as input, and returns True if the two atoms are isotopes (i.e. they have the same element but different atomic mass), and False otherwise.

```python
>>> c = Atom("C", 6, 12.011)
>>> c.get_mass()
12.011
>>> c2 = Atom("C", 6, 13.003)
>>> c.is_isotope(c2)
True
```

You can test your function in `cp/re05/chemical_reaction.py`

>__cp.re05.chemical_reaction.Atom.get_mass()__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the atomic mass of the atom

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``float``) - Atomic mass of the atom

>__cp.re05.chemical_reaction.Atom.is_isotope(atom)__

>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return True if the two atoms are isotopes, False otherwise

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Return

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - (``bool``) - True if the two atoms are isotopes, False otherwise