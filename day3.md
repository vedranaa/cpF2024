---
layout: default
---
# Exercises Re03

> You must start by downloading the script
>
> [download_re03.py](download_scripts/download_re03.py)
>
> Right-click and select “Save link as…”
> Run this script in VSCode to download the files you need for today's exercise. The script does not need to be located a specific place on your computer.

The following exercises are not all supposed to be completed today. This is a collection of exercises that you can use to practice your skills on your own as well, but all of the TA's are more than capable of helping you with it.

This weeks exercises are a little different to the last 2 weeks. Here the exercises are to give you the tools to understand how folder systems in your operating system work, and how files work in there as well. Only a few of these exercises could be considered exam questions, and most are to give you and understanding of how folders, files and directories work.

If you have any questions, feel free to ask. Send an email to [s194113@dtu.dk](matilto:s194113@dtu.dk?subject=02002_Brush_Up_Course).

## Exercise 3.1: Read a file

Complete the function ``read_file`` which takes ``file_name`` as input and returns the number of lines, words and characters that the file has.

```python
>>> read_file('cp/re03/files/1.txt')
4, 25, 171
```

The tests for the function ``read_file`` can be run by inserting your solution into the file ``cp/re03/readfiles``.

__cp.re03.readfiles.read_file(_file_name_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read a file and return the number of lines, words, and characters.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **file_name**(``string``) - file name to look at
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **l**(``int``) - number of lines
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **w**(``int``) - number of words
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **c**(``int``) - number of characters

## Exercise 3.2: Write a file

Complete the function ``write_file`` which takes ``file_name`` and `text` as input and creates a file with the name `file_name` and the text `text` as the text in the file.

```python
>>> write_file('cp/re03/files/Hello.txt','Hello World')
```

There are no tests for this function, however you should easily be able to see if the file is created and if it has the right writting on it.

__cp.re03.writefiles.write_file(_file_name,text_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Write the input to a file.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **file_name**(``string``) - file name to write to
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **text**(``string``) - text to write on file

## Exercise 3.3: Read a csv

A csv file is a common way to store data, as it is "Comma Separated Values" (CSV). Complete the function ``read_csv`` which takes ``file_name`` as input and returns a list of lists of floats, which represent the data that was stored in the csv file. 

```python
>>> read_csv('cp/re03/files/csv1.csv')
[[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], [8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0], [15.0, 16.0, 17.0, 18.0, 19.0, 20.0, 21.0]]
```

The tests for the function ``read_csv`` can be run by inserting your solution into the file ``cp/re03/readcsv``.

__cp.re03.readcsv.read_csv(_file_name_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read a CSV file and return the data as a list of lists.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **file_name**(``string``) - a string representing the name of the file.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **l**(``lst``) - a list of lists of floats containing the data in the CSV file.

## Exercise 3.4: Search Word

Complete the function ``search_word`` which takes ``file_name`` and `word` as input and returns the line number and line in which the word shows up for the first time. If the word is not there return ``-1```.

```python
>>> search_word('cp/re03/files/1.txt', 'Nunc')
3, "Nunc tempus turpis a fermentum fringilla. \n"
```

The tests for the function ``search_word`` can be run by inserting your solution into the file ``cp/re03/filesearch``.

__cp.re03.filesearch.search_file(_file_name_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search a file for a word and return the line number and the line.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **file_name**(``string``) - a string representing the name of the file.
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **word**(``string``) -a string representing the word to search for.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **i**(``int``) - the number of the line where the string first shows up
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - l(``str``) - the line where the string first shows up

## Exercise 3.5: Sort a file

Complete the function ``sort_file`` which takes ``file_name`` and `new_file_name` as input and creates a file with the name `new_file_name` and puts in the text from the file `file_name` but sorted.

```python
>>> sort_file("cp/re03/files/unsorted.txt","cp/re03/files/sorted.txt")
```

There are no tests for this function, however you should easily be able to see if the file is created and if the text is sorted. An example of this would be letting a file with the following text:

```python
10
21
8
5
9
```

Be sorted to:

```python
5
8
9
10
21
```

__cp.re03.filesort.sort_file(_file_name,new_file_name_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sort a file and write the sorted lines to a new file.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **file_name**(``string``) - file name to read from
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **new_file_name**(``string``) - file name to write to

## Exercise 3.6: Folders

Other than files, python also can look at the different folders that are on your computer. One way to look at all files and folders in a directory is with the function `os.walk()`, which walks through all of the folders in your directory and can give you all of the information. Try to play around with this function and then do the following.

Complete the function ``folders`` which takes ``path`` as input and returns the number of folders in this path

```python
>>> folders('cp/re03/files/')
11
```

The tests for the function ``folders`` can be run by inserting your solution into the file ``cp/re03/folders``.

__cp.re03.folders.folders(_path_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the total numbers of folders and subfolders in a folder.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **path**(``string``) - a string representing the name of the path.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - n(``int``) - the number of folders in the path

## Exercise 3.7: Extensions

Files also have a small nuance to them, which is that they all end in a specific "extensions". Fx. all python files end in ".py", all text files end in ".txt" and all websites end in ".html".

Complete the function ``extensions`` which takes ``path`` and `extension` as input and returns the number of files in this path with this extension

```python
>>> extensions('cp/re03/', '.py')
13
```

The tests for the function ``extensions`` can be run by inserting your solution into the file ``cp/re03/extensions``.

__cp.re03.extensions.extensions(_path,extension_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Return the total numbers of files with a specific extension in a folder.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **path**(``string``) - a string representing the name of the path.
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **extension**(``string``) - a string representing the name of the extension Fx. ".py", ".txt"
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - n(``int``) - the number of files with the extension in the path

## Exercise 3.8: File difference

Complete the function ``diff`` which takes ``file1`` and `file2` as input and finds the indexes of the lines in which there are differences between the files `file1` and `file2`, and return a list of these indexes. The files do not need to be the same length, but if they are not, the missing indexes between the two should be appended on the list of idex as well.

```python
>>> diff('cp/re03/files/diff1.txt', 'cp/re03/files/diff2.txt')
[2, 3, 8, 13, 22, 23, 24, 25, 26, 27, 28]
```

The tests for the function ``diff`` can be run by inserting your solution into the file ``cp/re03/diff``.

__cp.re03.diff.diff(_file1,file2_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find the lines in which there are differences between two files.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **file1**(``string``) - file name to read from
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **file2**(``string``) - file name to read from
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Returns
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **indexes**(``list``) - a list containing the indexes of the lines which are not the same in the files.

## Exercise 3.9: File Splitting

Complete the function ``split_file`` which takes ``file_name`` and `size` as input and splits the file with name `file_name` into an amount of files that have `size` amount of lines. Fx. a file with 20 lines, where the input of size is 5, will be split into 4 files of 5 lines each. The new files should be names "file_name_{n}", where n is the file number going from 1 to however many files are needed.

There are no tests for this function, however, do test it out on the file `cp/re03/files/split.txt`, with different amounts of lines needed. You should be able to validate that your test works fine.

__cp.re03.filesplitting.split_file(_file__name,size_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Split a file into smaller files.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **file_name**(``string``) - file name to read from
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **size**(``int``) - number of lines in each file.

## Exercise 3.10: Duplicates

Complete the function ``duplicates`` which takes ``path`` as input and finds the amount of duplicates of each file. This can be done either recursivley or by the use of os.walk(). The function should look at all files in the path and in the subfolders of the path, and returns a dictionary with the keys being file names and the values being the amount of times they have a duplicate. It is only the name of the file that should match for it to be a duplicate

```python
>>> duplicates('cp/re03/files')
{'1.txt': 3, '2.txt': 2, '3.txt': 2}
```

The tests for the function ``duplicates`` can be run by inserting your solution into the file ``cp/re03/duplicates``.

__cp.re03.diff.diff(_file1,file2_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Find the lines in which there are differences between two files.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **path**(``string``) - path to look at all the files from
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      Returns
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **dup**(``dict``) - a dictionary containing the names of the duplicate files and how many times they show up.



## Exercise 3.11: Read Data

Complete the function ``read_data`` which takes ``file_name`` as input and reads the data stored on the file. This exercise is meant as an example of how you in the future might have to read data files, either in courses or at a job. The function should return two things: A list of lists filled with the data, and a dictionary filled with the parameters of the experiment. The parameter lines all start with a #, and can easily be sorted in this way. However, some parameter lines start with # Param, where the parameter and their value follow "# Param: L0=4", while other parameters are formated as such: "# xlabel: Energy [meV]". The first parameter should be saved in the dictionary with the key "L0" and value 4, while the second parameter should be saved with the key "xlabel" and value "Energy [meV]".

```python
>>> read_data('cp/re03/files/data1.txt')
[['19.0075', '0', '0', '0'], ['19.0225', '0', '0', '0'], ['19.0375', '0', '0', '0'], ... ['21.9925', '0', '0', '0']], 
{' L0': '4', ' dL': '2', ... , '# xlimits': ' 19 22', '# variables': ' E I I_err N'} 
```

The tests for the function ``read_data`` can be run by inserting your solution into the file ``cp/re03/readdata``.

__cp.re03.readdata.read_data(_file_name_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Read a txt file that contains two lists and a dictionary.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;All the dictionary lines start with "#", and the key and values are seperated by a colon
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Some of the parameters come after the colon, and should be split by a "=".
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The lists are seperated by a blank line.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **path**(``string``) - path to look at all the files from
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      Returns
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **dup**(``dict``) - a dictionary containing the names of the duplicate files and how many times they show up.
>

## Exercise 3.12: Encryption

Encryption is vital for safeguarding sensitive information from unauthorized access, ensuring privacy and security in digital communications. By scrambling plaintext into ciphertext, encryption prevents interception and decryption by malicious actors.

The Caesar cipher, a simple substitution technique, shifts each letter in the plaintext by a fixed number of positions down the alphabet. For instance, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so on. Despite its simplicity, Caesar cipher demonstrates the fundamental concept of encryption, albeit it's susceptible to brute-force attacks due to its predictability and lack of complexity.

Complete the function ``encrypt_file`` which takes ``file_name``, ``key`` abnd ``new_file_name`` as input. It should read the file with the file_name. Then it should encrypt all of the letters (letting any characters that aren't letters be), and then write it to a new file with the name new_file_name.

```python
>>> encrypt_file('cp/re03/files/non-encrypted.txt',3,'cp/re03/files/encrypted.txt')
```

There are no tests for this exercise, so to test it, please encrypt the file with a key (fx. 3), and then run it again with the minus value of the key (fx. -3). If the same origional file is returned, then it works!

__cp.re03.encryption.encryption(_file_name,key,new_file_name_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Encrypt a file using a Ceaser cypher.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **file_name**(``string``) - a string representing the name of the file.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **key**(``int``) - an integer representing the key for the Ceaser cypher.
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **new_file_name**(``string``) - a string representing the name of the file.

## Exercise 3.13: Visual Representation of files

This exercise is to test your understanding of the files concept completely and futhering your knowledge on the os package. 

Complete the function ``visualrep`` which takes ``path`` as input. It should print all folders and files in this path in an intutive way such that it is visually understood how your path looks. This can be seen below in the example run, where the folder "cp" is at the top, and the only file in the cp folder "__init__.py" is intented with four dashes. Then the folders in cp, such as ex00, ex01, ex02 are indented with four dashes as well. Files in these folders are intented with 8 dashes ans so on.

```python
>>> visualrep('cp')
cp/
----__init__.py
----ex00/
--------say_hello.py
--------__init__.py
----ex01/
--------__init__.py
----ex02/
--------full_name.py
--------hadlock.py
--------name_length.py
--------next_thousand.py
--------normal_weight.py
--------survival_temperature.py
--------unit_conversion.py
--------wind_chill.py
--------__init__.py
...
```

There are no tests for this exercise, if you understand how your file system looks, and you can make sense of it yourself, you have completed the exercise.

__cp.re03.visualrep.visualrep(_path_)__

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Visual representation of the folder and file structure.

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  Parameters
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - **path**(``string``) - a string representing the main path.
