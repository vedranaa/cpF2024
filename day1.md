---
layout: default
---

# Day 1

1. You have two float variables representing the length and the width of a room in meters, say
    ```python
    a = 5.7
    b = 3.9 
    ``` 
    Define a boolean value `bed_fits`, which should assume a value `True` if and only if a bed of the size 2-by-0.9 meters fits in the room.

2. Say you have a variable `k` of the type float, and it represents...

   
3. Make an assignment which creates a integer variable `year`. Its value should be the current year.

4. You have an integer variable `nr_books` indicating the number of books in the library. Make a variable `nr_pages` with the number of pages in all books, if you know that a book has in average 97 pages.

5. You make a web page with recipes. Each recipe is written for 4 people, but the user can choose any number of people. Given variable `nr_eggs_4` ...

6. You have two integer variable representing hours in 24-hour notation. This means that the hour value is always smaller than 24, since one hours grow from 0 to 23, and than start again from 0. The two variables are for example `hours_1 = 16`, and `hours_2 = 12`. Define a variable `hours_sum` which is a sum of two hours, but also 24-hour representation. 

7. In the previous problem, you knew that both `hours_1` and `hours_2` are smaller than 24. Make sure that your definition of `hours_sum` is a correct hour sum in the 24-hour representation, even if the two variables `hours_1` and `hours_2` are larger than 24. It can be, that you don't need to change anything.

8. Similar to previous problem, define the variable `minutes` which is the sum of `minutes_1` and `minutes_2`, but is valid minutes part of the given time, i.e. it should be a number between 0 and 59. 

9. You are writing a program which displays photographs in a grid. The variable representing the number of photographs is `nr_photos`. The user chooses the number of photos to be shown in each row, represented by the value `nr_columns`. The last row may contain fewer photos than `nr_columns`. Define a variable `nr_full_rows` which is a number of rows in the grid which contain `nr_columns` photographs. For example if you have
    ```python
    N = 17
    c = 3 
    ``` 
    The first 15 photos are shown in 5 rows, with 3 photos in each row. The last 2 photos are shown in the 6th row. So, the number of full rows is 5.

10. Continuation of the previous problem. Define the variable `has_extra_row` which is `True` if the last row of photographs contains fewer that `nr_columns` photographs. For the example from previous problem, this variable would be `True`.

11. Continuation of the previous problem. Define the variable `nr_rows` which is the number of rows needed to display all photographs. For the example from the previous problem, you need 6 rows to display the photos. Hint: Notice that `nr_rows` is either `nr_full_rows` or one larger, if `has_extra_rows` is `True` (which is represented by 1). 

12. Make an assignment which creates a float variable `temperature`. Its value should be the mean between 7 and 8.

13. Given the varialbe `t_Celsius` ... define `t_F`

14. Assume you have two variables `a`  and `b` with numerical values (that is, those values may be either integers or floats) representing the length of the legs of the right triangle. For example, you may have 
    ```python
    a = 5.7
    b = 3.9 
    ``` 
    Write the assignment which sets the value of a variable `c` to the length of the hypotenuse. You should use the Pythagorean theorem $a^2+b^2=c^2$. 

15. Create a variable `pi_approx` and assign it the approximate value of $\pi$ rounded to 5 decimals, that is 3.14159.

16. Given two float variables `length` and `width`, calculate the area of a rectangle and assign it to a variable `area`.

17. The distance fallen from the initial position of rest may be computed as $d = \frac{1}{2}g t^2$. Here, $g$ is the acceleration due to gravity, 9.81 m/s2. Say you have a variable with the value of 

18. Given the length (in meters) of a room in a variable `length`, define a variable `bed_fits` which has the value `True` if a bed of the length 200cm fits in the room. You can assume that the room has sufficient width.

19. Given the length and a width (in meters) of a room in variables `length` and `width`, define a variable `bed_fits` which has the value `True` if a bed of the size 200cm-by-90cm fits in the room. You can assume that the length is larger than the width.

20. Given the dimesions of the room in the variables `a` and `b`, define `length` and `width`. Here, you don't know which of the variables `a` and `b` is smaller, and which is bigger. 

21. Given the dimesions of the room in the variables `a` and `b`, define a variable `bed_fits` which has the value `True` if a bed of the size 200cm-by-90cm fits in the room.


22. Make an assignment which creates a variable `name`. Its value should be your first name.

23. Create a string variable `course_name` with the value `'Introduction to Programming'`.

24. You have a string variable, similar to 
    ```python
    first_name = 'Peter'
    ``` 
    Define a variable `greeting` with a value `'Hi, Peter!'`.

25. You have two string variables, similar to 
    ```python
    first_name = 'Anja'
    last_name = 'Andersen' 
    ``` 
    Define a variable `name` with value `'Anja Andersen'`.

26. You have a string and an integer, similar to 
     ```python
    w = 'MK31'
    t = 3
    ``` 
    Define a variable `wtt` with value `'MK31MK31MK31'`.

27. You have a string and an integer, similar to
    ```python
    say = 'Yes!'
    number = 4
    ``` 
    Define a variable `repeat` with value `'Yes! Yes! Yes! Yes!'`. The space should only be added between the repetitions.


28. You have two variables, a string and and integer, as in the example below
    ```python
    name = 'Katja'
    age = 17 
    ``` 
    Write the assignment which sets the value of a variable `statement` to `Katja is 17 years old`. 

29. You have a string variable, where string is representing an integer, like `number = '187'`. Define an integer variable `n` with the value `187`.

30. You have a string variable `number = '253'`. Define a float variable `n_half` with the value being the half of the value given by number.



31. You have a string variable `year='2028'`. Define a string variable `next_year` with a value `'2029'`. (Note that both variables should be strings. Your assignment should work different years.)

32. You have a float variable representing hours, for example for a one third of an hour it would be `h = 1/3`. Define variables `hour` and `minute`...


1.  Assume you have two variables `x` and `y` with numerical values. Write an assignment that swaps their values.

1.  You have a string variable representing a city, like `city = 'New York'`. Define a new string variable `big_city` with the value `'BIG New York'`.

1.  Given a string variable `word`, create a new string variable `repeated_word` with the original word repeated three times.

1.  You are designing a program that calculates the area of a circle. Create a float variable `radius` with a value of 5.7, and then compute and assign the area to a variable `circle_area`.

1.  Assume you have a variable `price` representing the cost of an item. Create a variable `discounted_price` that is 20% less than the original price.

1. You have two float variables `weight_kg` and `height_m`. Calculate the BMI (Body Mass Index) by dividing weight by the square of height and assign it to a variable `bmi`.

1. Create a string variable `favorite_color` and assign it the value of your favorite color.

1.  You are building a shopping cart for an online store. Create a variable `total_price` by adding the prices of three items: $25.50, $12.75, and $8.99.

1.  Assume you have two variables `p` and `q` with boolean values. Write an assignment that creates a new variable `result` with the value of the logical AND of `p` and `q`.

1.  You have two float variables representing the sides of a rectangle: `side1 = 4.2` and `side2 = 6.8`. Write an assignment that calculates the perimeter of the rectangle and assigns it to a variable `perimeter`.

1.  You have two integer variables representing the lengths of sides of a parallelogram: `base = 10` and `height = 8`. Write an assignment that calculates the area of the parallelogram and assigns it to a variable `parallelogram_area`.

1.  Assume you have a variable `is_raining` with a boolean value. Write an assignment that creates a new variable `go_outside` with the opposite boolean value.

1. Normal height for a 14-year boy is between 150 and 176 cm, both numbers inclusive. Assume you have a variable `heigh` representing height in cm. Create a boolean variable `is_normal_height` which has a value `True` if the height is normal.

1. Assume you have a variable `age` with person's age in years. You want to create a string variable `info` with as sentence indicating a ticket price. The price is 0 for persons 17 years old or younger, and 1 for those 18 years old or older. For example if `age = 14` the sentence should be `Price: 0 kr`.  

1. Assume you have a variable `age` with person's age in years. You want to create a string variable `info` with as sentence indicating a ticket price. The price is 0 for persons 17 years old or younger, and 50 for those 18 years old or older. For example if `age = 34` the sentence should be `Price: 50 kr`.  

1. Assume you have a variable `age` with person's age in years. You want to create a string variable `info` with as sentence indicating a ticket price. The price is 50 for persons 17 years old or younger, and 100 for those 18 years old or older. For example if `age = 24` the sentence should be `Price: 100 kr`.  

1. Given three numbers, `a`, `b` and `c`, create a boolean variable `has_root` which assumes a value `True` if and only if the the quadratic equation $ax^2 + bx + c = 0$ has real roots.  

1. You have three integer variables, similar to 
    ```python
    day = 15
    month = 8
    year = 2012 
    ``` 
    Define a variable `date` with value `'15/8-2012'`.

2. You have three integer variables, similar to
    ```python
    hours = 13
    minutes = 24
    delay = 96
    ``` 
    Define a variable string variable `arrival`...

3. You have variables `w` and `l` for the width and the length of a rectangle room in meters. Compute the number of 30-by-30 cm tiles you need to cover the floor. You can cut the tiles, but you should not count on using both parts of the tile which is cut in two. 



