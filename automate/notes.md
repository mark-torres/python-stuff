# Notes from *Automate the Boring Stuff with Python*

* [Python Basics](#ch01)
* [Flow Control](#ch02)
* [Functions](#ch03)
* [Lists](#ch04)
* [Dictionaries and Structuring Data](#ch05)
* [Manipulating Strings](#ch06)
* [Pattern Matching with Regular Expressions](#ch07)
* [Reading and Writing Files](#ch08)
* [Organizing Files](#ch09)
* [Debugging](#ch10)
* [Web Scraping](#ch11)
* [Working with Excel Spreadsheets](#ch12)
* [Working with PDF and Word Documents](#ch13)
* [Working with CSV Files and JSON Data](#ch14)
* [Time, Scheduling Tasks, and Launching Programs](#ch15)
* [Sending Email and Text Messages](#ch16)
* [Manipulating Images](#ch17)
* [Controlling the Keyboard and Mouse with GUI Automation](#ch18)

## Python Basics <a name="ch01">&nbsp;</a>

### Math operators

Math Operators from Highest to Lowest Precedence:

Operator | Operation | Example | Evaluates to...
---- | ---- | ---- | ---- |
** | Exponent | 2 ** 3 | 8
% | Modulus/remainder | 22 % 8 | 6
// | Integer division/floored quotient | 22 // 8 | 2
/ | Division | 22 / 8 | 2.75
* | Multiplication | 3 * 5 | 15
- | Subtraction | 5 - 2 | 3
+ | Addition | 2 + 2 | 4

### The Integer, Floating-Point, and String Data Types

Common Data Types:

Data type | Examples
---- | ----
Integers | -2, -1, 0, 1, 2, 3, 4, 5
Floating-point numbers | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25
Strings | 'a', 'aa', 'aaa', 'Hello!', '11 cats'

### String Concatenation and Replication

Concatenation

	>>> 'Alice' + 'Bob'
	'AliceBob'

Replication

	>>> 'Alice' * 5
	'AliceAliceAliceAliceAlice'

## Flow Control <a name="ch02">&nbsp;</a>

### Boolean values

While the integer, floating-point, and string data types have an unlimited number of possible values, the Boolean data type has only two values: `True` and `False`.

### Comparison Operators

Operator | Meaning
---- | ----
== | Equal to
!= | Not equal to
< | Less than
\> | Greater than
<= | Less than or equal to
\>= | Greater than or equal to

### Flow Control Statements

`if` Statements:

	if name == 'Alice':
		print('Hi, Alice.')

`else` Statements:

	name = 'Bob'
	if name == 'Alice':
		print('Hi, Alice.')
	else:
		print('Hello, stranger')

`elif` Statements

	name = 'Bob'
	age = 30
	if name == 'Alice':
		print('Hi, Alice.')
	elif age < 12:
		print('You are not Alice, kiddo.')
	else:
		print('You are neither Alice nor a little kid.')

`while` Loop statements

	spam = 0
	while spam < 5:
		print('Hello, world.')
		spam = spam + 1

`break` Statements

	while True:
		print('Please type your name.')
		name = input()
		if name == 'your name':
			break
	print('Thank you!')

`continue` Statements

	while True:
		print('Who are you?')
		name = input()
		if name != 'Joe':
			continue
		print('Hello, Joe. What is the password? (It is a fish.)') 
		password = input()
		if password == 'swordfish':
			break
	print('Access granted.')

`for` Loops and the `range()` Function

	print('My name is')
	for i in range(5):
		print('Jimmy Five Times (' + str(i) + ')')

The Starting, Stopping, and Stepping Arguments to `range()`

Some functions can be called with multiple arguments separated by a comma, and `range()` is one of them. This lets you change the integer passed to `range()` to follow any sequence of integers, including starting at a number other than zero.

	for i in range(12, 16):
		print(i)

The `range()` function can also be called with three arguments. The first two arguments will be the start and stop values, and the third will be the step argument. The step is the amount that the variable is increased by after each iteration.

	# count from zero to eight by intervals of two
	for i in range(0, 10, 2):
		print(i)
	# print from five down to zero
	for i in range(5, -1, -1):
		print(i)

### Importing modules

All Python programs can call a basic set of functions called built-in functions, including the `print()`, `input()`, and `len()`. Python also comes with a set of modules called the *standard library*. Each module is a Python program that contains a related group of functions that can be embedded in your programs.

Before you can use the functions in a module, you must import the module with an `import` statement. In code, an `import` statement consists of the following:

* The import keyword
* The name of the module
* Optionally, more module names, as long as they are separated by commas

Example that imports the `random` module:

	import random
	for i in range(5):
		print(random.randint(1, 10))

Ending a Program Early with `sys.exit()`:

	import sys
	while True:
		print('Type exit to exit.')
		response = input()
		if response == 'exit':
			sys.exit()
		print('You typed ' + response + '.')

## Functions <a name="ch03">&nbsp;</a>

`def` Statement

	# declare the 'hello' function
	def hello():
		print('Howdy!')
		print('Howdy!!!')
		print('Hello there.')
	# use the function
	hello()

`def` Statements with Parameters

	def hello(name):
		print('Hello ' + name)
	
	hello('Alice')
	hello('Bob')

Return Values and return Statements

	import random
	def getAnswer(answerNumber):
		if answerNumber == 1:
			return 'It is certain'
		elif answerNumber == 2:
			return 'It is decidedly so'
		elif answerNumber == 3:
			return 'Yes'
		elif answerNumber == 4:
			return 'Reply hazy try again'
		elif answerNumber == 5:
			return 'Ask again later'
		elif answerNumber == 6:
			return 'Concentrate and ask again'
		elif answerNumber == 7:
			return 'My reply is no'
		elif answerNumber == 8:
			return 'Outlook not so good'
		elif answerNumber == 9:
			return 'Very doubtful'
	
	r = random.randint(1, 9)
	fortune = getAnswer(r)
	print(fortune)

### The None Value

In Python there is a value called `None`, which represents the absence of a value. `None` is the only value of the `NoneType` data type. (Other programming languages might call this value `null`, `nil`, or `undefined`.) Just like the Boolean `True` and `False` values, `None` must be typed with a capital *N*.

This value-without-a-value can be helpful when you need to store something that won't be confused for a real value in a variable.

### Keyword Arguments and `print()`

Most arguments are identified by their position in the function call. For example, `random.randint(1, 10)` is different from `random.randint(10, 1)`. The function call `random.randint(1, 10)` will return a random integer between 1 and 10, because the first argument is the low end of the range and the second argument is the high end (while `random.randint(10, 1)` causes an error).

However, keyword arguments are identified by the keyword put before them in the function call. Keyword arguments are often used for optional parameters. For example, the `print()` function has the optional parameters `end` and `sep` to specify what should be printed at the end of its arguments and between its arguments (separating them), respectively.

If you ran the following program:

	print('Hello')
	print('World')

the output would look like this:

	Hello
	World

The two strings appear on separate lines because the `print()` function automatically adds a newline character to the end of the string it is passed. However, you can set the end keyword argument to change this to a different string. For example, if the program were this:

	print('Hello', end='')
	print('World')

the output would look like this:

	HelloWorld

The output is printed on a single line because there is no longer a new-line printed after 'Hello'. Instead, the blank string is printed. This is useful if you need to disable the newline that gets added to the end of every `print()` function call.

Similarly, when you pass multiple string values to print(), the function will automatically separate them with a single space. Enter the following into the interactive shell:

	>>> print('cats', 'dogs', 'mice')
	cats dogs mice

But you could replace the default separating string by passing the sep keyword argument. Enter the following into the interactive shell:

	>>> print('cats', 'dogs', 'mice', sep=',')
	cats,dogs,mice

For more info, check this [tutorial](http://www.tutorialspoint.com/python/python_functions.htm).

### Local and Global Scope

Remember:

* Local variables cannot be used in the global scope
* Local scopes cannot use variables in other local scopes
* Global variables can be read from a local scope
* Avoid local and global variables with the same name

If you need to access a global variable inside a function, you can use the `global` statement.

The `global` Statement

	def spam():
		global eggs
		eggs = 'spam'
	
	eggs = 'global'
	spam()
	print(eggs)

When you run this program, the final `print()` call will output this:

	spam

### Exception Handling

Errors can be handled with `try` and `except` statements. The code that could potentially have an error is put in a `try` clause. The program execution moves to the start of a following `except` clause if an error happens.

	def spam(divideBy):
		try:
			return 42 / divideBy
		except ZeroDivisionError:
			print('Error: Invalid argument.')

	print(spam(2))
	print(spam(12))
	print(spam(0))
	print(spam(1))

When code in a try clause causes an error, the program execution immediately moves to the code in the except clause.

Consider the following program, which instead has the spam() calls in the try block:

	def spam(divideBy):
		return 42 / divideBy

	try:
		print(spam(2))
		print(spam(12))
		print(spam(0))
		print(spam(1))
	except ZeroDivisionError:
		print('Error: Invalid argument.')

When this program is run, the output looks like this:

	21.0
	3.5
	Error: Invalid argument.

The reason `print(spam(1))` is never executed is because once the execution jumps to the code in the `except` clause, it does not return to the `try` clause. Instead, it just continues moving down as normal.

## Lists <a name="ch04">&nbsp;</a>

### The List Data Type

A list value looks like this:

	>>> ['cat', 'bat', 'rat', 'elephant']
	['cat', 'bat', 'rat', 'elephant']
	>>> ['hello', 3.1415, True, None, 42]
	['hello', 3.1415, True, None, 42]

**Getting individual values in a list with indexes:**

	>>> spam = ['cat', 'bat', 'rat', 'elephant']
	>>> spam[0]
	'cat'
	>>> spam[1]
	'bat'
	>>> spam[2]
	'rat'
	>>> spam[3]
	'elephant'
	>>> ['cat', 'bat', 'rat', 'elephant'][3]
	'elephant'
	>>> 'Hello ' + spam[0]
	'Hello cat'
	>>> 'The ' + spam[1] + ' ate the ' + spam[0] + '.'
	'The bat ate the cat.'

**Negative indexes**

	>>> spam = ['cat', 'bat', 'rat', 'elephant']
	>>> spam[-1]
	'elephant'
	>>> spam[-3]
	'bat'
	>>> 'The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.'
	'The elephant is afraid of the bat.'

**Getting sublists with slices**

	>>> spam = ['cat', 'bat', 'rat', 'elephant']
	>>> spam[0:4]
	['cat', 'bat', 'rat', 'elephant']
	>>> spam[1:3]
	['bat', 'rat']
	>>> spam[0:-1]
	['cat', 'bat', 'rat']
	>>> spam[:2]
	['cat', 'bat']
	>>> spam[1:]
	['bat', 'rat', 'elephant']
	>>> spam[:]
	['cat', 'bat', 'rat', 'elephant']

**Getting a list's length with `len()`**

	>>> spam = ['cat', 'dog', 'moose']
	>>> len(spam)
	3

**Changing values in a list with indexes**

	>>> spam = ['cat', 'bat', 'rat', 'elephant']
	>>> spam[1] = 'aardvark'
	>>> spam
	['cat', 'aardvark', 'rat', 'elephant']
	>>> spam[2] = spam[1]
	>>> spam
	['cat', 'aardvark', 'aardvark', 'elephant']
	>>> spam[-1] = 12345
	>>> spam
	['cat', 'aardvark', 'aardvark', 12345]

**List concatenation and list replication**

	>>> [1, 2, 3] + ['A', 'B', 'C']
	[1, 2, 3, 'A', 'B', 'C']
	>>> ['X', 'Y', 'Z'] * 3
	['X', 'Y', 'Z', 'X', 'Y', 'Z', 'X', 'Y', 'Z']
	>>> spam = [1, 2, 3]
	>>> spam = spam + ['A', 'B', 'C']
	>>> spam
	[1, 2, 3, 'A', 'B', 'C']

**Removing values from lists with `del` statements**

	>>> spam = ['cat', 'bat', 'rat', 'elephant']
	>>> del spam[2]
	>>> spam
	['cat', 'bat', 'elephant']
	>>> del spam[2]
	>>> spam
	['cat', 'bat']

**Using `for` loops with lists**

	supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
	for i in range(len(supplies)):
		print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

**The `in` and `not in` operators**

	>>> 'howdy' in ['hello', 'hi', 'howdy', 'heyas']
	True
	>>> spam = ['hello', 'hi', 'howdy', 'heyas']
	>>> 'cat' in spam
	False
	>>> 'howdy' not in spam
	False
	>>> 'cat' not in spam
	True

### The multiple assignment trick

The multiple assignment trick is a shortcut that lets you assign multiple variables with the values in a list in one line of code. So instead of doing this:

	>>> cat = ['fat', 'orange', 'loud']
	>>> size = cat[0]
	>>> color = cat[1]
	>>> disposition = cat[2]

you could type this line of code:

	>>> cat = ['fat', 'orange', 'loud']
	>>> size, color, disposition = cat

The number of variables and the length of the list must be exactly equal, or Python will give you a `ValueError`.

### Augmented Assignment Operators

Augmented assignment statement | Equivalent assignment statement
---- | ----
spam += 1 | spam = spam + 1
spam -= 1 | spam = spam - 1
spam *= 1 | spam = spam * 1
spam /= 1 | spam = spam / 1
spam %= 1 | spam = spam % 1

The `+=` operator can also do string and list concatenation, and the `*=` operator can do string and list replication.

	>>> spam = 'Hello'
	>>> spam += ' world!'
	>>> spam
	'Hello world!'
	>>> bacon = ['Zophie']
	>>> bacon *= 3
	>>> bacon
	['Zophie', 'Zophie', 'Zophie']

### Methods

**Finding a value in a list with the `index()` method**

	>>> spam = ['hello', 'hi', 'howdy', 'heyas']
	>>> spam.index('hello')
	0
	>>> spam.index('heyas')
	3

**Adding values to lists with the `append()` and `insert()` methods**

	>>> spam = ['cat', 'dog', 'bat']
	>>> spam.append('moose')
	>>> spam
	['cat', 'dog', 'bat', 'moose']
	>>> spam = ['cat', 'dog', 'bat']
	>>> spam.insert(1, 'chicken')
	>>> spam
	['cat', 'chicken', 'dog', 'bat']

**Removing values from lists with `remove()`**

The `remove()` method is passed the value to be removed from the list it is called on.

	>>> spam = ['cat', 'bat', 'rat', 'elephant']
	>>> spam.remove('bat')
	>>> spam
	['cat', 'rat', 'elephant']

If the value appears multiple times in the list, only the first instance of the value will be removed.

	>>> spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
	>>> spam.remove('cat')
	>>> spam
	['bat', 'rat', 'cat', 'hat', 'cat']

The `del` statement is good to use when you know the index of the value you want to remove from the list. The `remove()` method is good when you know the value you want to remove from the list.

**Sorting the values in a list with the `sort()` method**

Lists of number values or lists of strings can be sorted with the sort() method.

	>>> spam = [2, 5, 3.14, 1, -7]
	>>> spam.sort()
	>>> spam
	[-7, 1, 2, 3.14, 5]
	>>> spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
	>>> spam.sort()
	>>> spam
	['ants', 'badgers', 'cats', 'dogs', 'elephants']

You can also pass True for the reverse keyword argument to have sort() sort the values in reverse order.

	>>> spam.sort(reverse=True)
	>>> spam
	['elephants', 'dogs', 'cats', 'badgers', 'ants']

### List-like Types: Strings and Tuples

Strings and lists are similar. Many of the things you can do with lists can also be done with strings: indexing; slicing; and using them with for loops, with `len()`, and with the `in` and `not in` operators.

	>>> name = 'Zophie'
	>>> name[0]
	'Z'
	>>> name[-2]
	'i'
	>>> name[0:4]
	'Zoph'
	>>> 'Zo' in name
	True
	>>> 'z' in name
	False
	>>> 'p' not in name
	False
	>>> for i in name:
		print('* * * ' + i + ' * * *')
	* * * Z * * *
	* * * o * * *
	* * * p * * *
	* * * h * * *
	* * * i * * *
	* * * e * * *

**Mutable and immutable data types**

But lists and strings are different in an important way. A list value is a *mutable* data type: It can have values added, removed, or changed. However, a string is *immutable*: It cannot be changed.

	>>> name = 'Zophie a cat'
	>>> name[7] = 'the'
	Traceback (most recent call last):
	  File "<pyshell#50>", line 1, in <module>
	    name[7] = 'the'
	TypeError: 'str' object does not support item assignment

### The Tuple Data Type

The tuple data type is almost identical to the list data type, except in two ways. First, tuples are typed with parentheses, `(` and `)`, instead of square brackets, `[` and `]`. But the main way that tuples are different from lists is that tuples, like strings, are immutable. Tuples cannot have their values modified, appended, or removed.

	>>> eggs = ('hello', 42, 0.5)
	>>> eggs[1] = 99
	Traceback (most recent call last):
	  File "<pyshell#5>", line 1, in <module>
	    eggs[1] = 99
	TypeError: 'tuple' object does not support item assignment

### Converting Types with the `list()` and `tuple()` Functions

Just like how `str(42)` will return '42', the string representation of the integer 42, the functions `list()` and `tuple()` will return list and tuple versions of the values passed to them.

	>>> tuple(['cat', 'dog', 5])
	('cat', 'dog', 5)
	>>> list(('cat', 'dog', 5))
	['cat', 'dog', 5]
	>>> list('hello')
	['h', 'e', 'l', 'l', 'o']

Converting a tuple to a list is handy if you need a mutable version of a tuple value.

### References

Lists assignments work differently from the other value assignments. When you assign a list to a variable, you are actually assigning a list reference to the variable. A reference is a value that points to some bit of data, and a list reference is a value that points to a list.

	>>> spam = [0, 1, 2, 3, 4, 5]
	>>> cheese = spam
	>>> cheese[1] = 'Hello!'
	>>> spam
	[0, 'Hello!', 2, 3, 4, 5]
	>>> cheese
	[0, 'Hello!', 2, 3, 4, 5]

**The `copy` module's `copy()` and `deepcopy()` functions**

Python provides a module named `copy` that provides both the `copy()` and `deepcopy()` functions. The first of these, `copy.copy()`, can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference.

	>>> import copy
	>>> spam = ['A', 'B', 'C', 'D']
	>>> cheese = copy.copy(spam)
	>>> cheese[1] = 42
	>>> spam
	['A', 'B', 'C', 'D']
	>>> cheese
	['A', 42, 'C', 'D']

If the list you need to copy contains lists, then use the `copy.deepcopy()` function instead of `copy.copy()`. The `deepcopy()` function will copy these inner lists as well.

## Dictionaries and Structuring Data <a name="ch05">&nbsp;</a>

### The Dictionary Data Type

Like a list, a dictionary is a collection of many values. But unlike indexes for lists, indexes for dictionaries can use many different data types, not just integers. Indexes for dictionaries are called keys, and a key with its associated value is called a key-value pair.

	>>> myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
	>>> myCat['size']
	'fat'
	>>> 'My cat has ' + myCat['color'] + ' fur.'
	'My cat has gray fur.'
	>>> spam = {12345: 'Luggage Combination', 42: 'The Answer'}

### Dictionaries vs. Lists

Unlike lists, items in dictionaries are unordered. The first item in a list named spam would be `spam[0]`. But there is no "first" item in a dictionary. While the order of items matters for determining whether two lists are the same, it does not matter in what order the key-value pairs are typed in a dictionary.

	>>> spam = ['cats', 'dogs', 'moose']
	>>> bacon = ['dogs', 'moose', 'cats']
	>>> spam == bacon
	False
	>>> eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
	>>> ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
	>>> eggs == ham
	True

Because dictionaries are not ordered, they can't be sliced like lists.

### The `keys()`, `values()`, and `items()` Methods

There are three dictionary methods that will return list-like values of the dictionary's keys, values, or both keys and values: `keys()`, `values()`, and `items()`. The values returned by these methods are not true lists: They cannot be modified and do not have an `append()` method.

	>>> spam = {'color': 'red', 'age': 42}
	>>> for v in spam.values():
			print(v)
	red
	42
	>>> for k in spam.keys():
			print(k)
	color
	age
	>>> for i in spam.items():
			print(i)
	('color', 'red')
	('age', 42)

### Checking Whether a Key or Value Exists in a Dictionary

	>>> spam = {'name': 'Zophie', 'age': 7}
	>>> 'name' in spam.keys()
	True
	>>> 'Zophie' in spam.values()
	True
	>>> 'color' in spam.keys()
	False
	>>> 'color' not in spam.keys()
	True
	>>> 'color' in spam
	False

### The `get()` Method

Dictionaries have a get() method that takes two arguments: the key of the value to retrieve and a fallback value to return if that key does not exist.

	>>> picnicItems = {'apples': 5, 'cups': 2}
	>>> 'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
	'I am bringing 2 cups.'
	>>> 'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.'
	'I am bringing 0 eggs.'

### The `setdefault()` Method

You'll often have to set a value in a dictionary for a certain key only if that key does not already have a value.

	spam = {'name': 'Pooka', 'age': 5}
	if 'color' not in spam:
		spam['color'] = 'black'
	# using the setdefault method
	>>> spam = {'name': 'Pooka', 'age': 5}
	>>> spam.setdefault('color', 'black')
	'black'
	>>> spam
	{'color': 'black', 'age': 5, 'name': 'Pooka'}

## Manipulating Strings <a name="ch06">&nbsp;</a>

### Escape Characters

	>>> spam = 'Say hi to Bob\'s mother.'

These are the escape characters you can use:

Escape character | Prints as
---- | ----
\' | Single quote
\" | Double quote
\t | Tab
\n | Newline (line break)
\\\ | Backslash

	>>> print("Hello there!\nHow are you?\nI\'m doing fine.")
	Hello there!
	How are you?
	I'm doing fine.

### Raw Strings

You can place an `r` before the beginning quotation mark of a string to make it a raw string. A raw string completely ignores all escape characters and prints any backslash that appears in the string.

	>>> print(r'That is Carol\'s cat.')
	That is Carol\'s cat.

### Multiline Strings with Triple Quotes

A multiline string in Python begins and ends with either three single quotes or three double quotes. Any quotes, tabs, or newlines in between the "triple quotes" are considered part of the string. Python's indentation rules for blocks do not apply to lines inside a multiline string.

### Multiline Comments

While the hash character (#) marks the beginning of a comment for the rest of the line, a multiline string is often used for comments that span multiple lines.

	"""This is a test Python program.
	Written by Al Sweigart al@inventwithpython.com
	
	This program was designed for Python 3, not Python 2.
	"""
	def spam():
		"""This is a multiline comment to help
		explain what the spam() function does."""
		print('Hello!')

### Indexing and Slicing Strings

Strings use indexes and slices the same way lists do.

	>>> spam = 'Hello world!'
	>>> spam[0]
	'H'
	>>> spam[4]
	'o'
	>>> spam[-1]
	'!'
	>>> spam[0:5]
	'Hello'
	>>> spam[:5]
	'Hello'
	>>> spam[6:]
	'world!'

As you can see, you can access all the characters the string just like a list, but you can't use any of the list member functions like `append`. If you need to convert the string into a list of single characters, use the `list` function:

	>>> spam = 'Hello!'
	>>> letters = list(spam)
	>>> letters
	>>> ['H','e','l','l','o','!']

### The in and not in Operators with Strings

The `in` and `not in` operators can be used with strings just like with list values.

	>>> 'Hello' in 'Hello World'
	True
	>>> 'Hello' in 'Hello'
	True
	>>> 'HELLO' in 'Hello World'
	False
	>>> '' in 'spam'
	True
	>>> 'cats' not in 'cats and dogs'
	False

### Useful string methods

**The upper(), lower(), isupper(), and islower() String Methods**

Several string methods analyze strings or create transformed string values.

	>>> spam = 'Hello world!'
	>>> spam = spam.upper()
	>>> spam
	'HELLO WORLD!'
	>>> spam = spam.lower()
	>>> spam
	'hello world!'
	>>> spam = 'Hello world!'
	>>> spam.islower()
	False
	>>> spam.isupper()
	False
	>>> 'HELLO'.isupper()
	True
	>>> 'abc12345'.islower()
	True
	>>> '12345'.islower()
	False
	>>> '12345'.isupper()
	False

**The isX String Methods**

Here are some common isX string methods:

* `isalpha()`: returns True if the string consists only of letters and is not blank.
* `isalnum()`: returns True if the string consists only of letters and numbers and is not blank.
* `isdecimal()`: returns True if the string consists only of numeric characters and is not blank.
* `isspace()`: returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
* `istitle()`: returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.

The isX string methods are helpful when you need to validate user input. 

	>>> 'hello'.isalpha()
	True
	>>> 'hello123'.isalpha()
	False
	>>> 'hello123'.isalnum()
	True
	>>> 'hello'.isalnum()
	True
	>>> '123'.isdecimal()
	True
	>>> '    '.isspace()
	True
	>>> 'This Is Title Case'.istitle()
	True
	>>> 'This Is Title Case 123'.istitle()
	True
	>>> 'This Is not Title Case'.istitle()
	False
	>>> 'This Is NOT Title Case Either'.istitle()
	False

**The `startswith()` and `endswith()` String Methods**

	>>> 'Hello world!'.startswith('Hello')
	True
	>>> 'Hello world!'.endswith('world!')
	True
	>>> 'abc123'.startswith('abcdef')
	False
	>>> 'abc123'.endswith('12')
	False
	>>> 'Hello world!'.startswith('Hello world!')
	True
	>>> 'Hello world!'.endswith('Hello world!')
	True

**The `join()` and `split()` String Methods**

	>>> ', '.join(['cats', 'rats', 'bats'])
	'cats, rats, bats'
	>>> ' '.join(['My', 'name', 'is', 'Simon'])
	'My name is Simon'
	>>> 'ABC'.join(['My', 'name', 'is', 'Simon'])
	'MyABCnameABCisABCSimon'

**Justifying Text with `rjust()`, `ljust()`, and `center()`**

	>>> 'Hello'.rjust(10)
	'     Hello'
	>>> 'Hello'.rjust(20)
	'               Hello'
	>>> 'Hello World'.rjust(20)
	'         Hello World'
	>>> 'Hello'.ljust(10)
	'Hello
	>>> 'Hello'.rjust(20, '*')
	'***************Hello'
	>>> 'Hello'.ljust(20, '-')
	'Hello---------------'
	>>> 'Hello'.center(20)
	'       Hello       '
	>>> 'Hello'.center(20, '=')
	'=======Hello========'

**Removing Whitespace with `strip()`, `rstrip()`, and `lstrip()`**

	>>> spam = '    Hello World     '
	>>> spam.strip()
	'Hello World'
	>>> spam.lstrip()
	'Hello World '
	>>> spam.rstrip()
	'    Hello World'
	>>> spam = 'SpamSpamBaconSpamEggsSpamSpam'
	>>> spam.strip('ampS')
	'BaconSpamEggs'

### Copying and Pasting Strings with the pyperclip Module

The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer's clipboard.

	>>> import pyperclip
	>>> pyperclip.copy('Hello world!')
	>>> pyperclip.paste()
	'Hello world!'

If you copy some text into the clipboard, you can "pase" it into a variable:

	>>> text = pyperclip.paste()
	>>> text
	'Some text from clipboard'

## Pattern Matching with Regular Expressions <a name="ch07">&nbsp;</a>

### Creating Regex Objects

All the regex functions in Python are in the re module.

	>>> import re
	>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

Since regular expressions frequently use backslashes in them, it is convenient to pass raw strings to the `re.compile()` function instead of typing extra backslashes. Typing r'\d\d\d-\d\d\d-\d\d\d\d' is much easier than typing '\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d'.

### Matching Regex Objects

A Regex object's `search()` method searches the string it is passed for any matches to the regex. The `search()` method will return `None` if the regex pattern is not found in the string. If the pattern is found, the `search()` method returns a `Match` object. Match objects have a `group()` method that will return the actual matched text from the searched string.

	>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
	>>> print('Phone number found: ' + mo.group())
	Phone number found: 415-555-4242

**Grouping with Parentheses**

	>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
	>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
	>>> mo.group(1)
	'415'
	>>> mo.group(2)
	'555-4242'
	>>> mo.group(0)
	'415-555-4242'
	>>> mo.group()
	'415-555-4242'
	>>> mo.groups()
	('415', '555-4242')
	>>> areaCode, mainNumber = mo.groups()
	>>> print(areaCode)
	415
	>>> print(mainNumber)
	555-4242

### Greedy and Nongreedy Matching

Python's regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible. The non-greedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket followed by a question mark.

	>>> greedyHaRegex = re.compile(r'(Ha){3,5}')
	>>> mo1 = greedyHaRegex.search('HaHaHaHaHa')
	>>> mo1.group()
	'HaHaHaHaHa'
	>>> nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
	>>> mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
	>>> mo2.group()
	'HaHaHa'

### The `findall()` Method

In addition to the `search()` method, Regex objects also have a `findall()` method. While `search()` will return a Match object of the first matched text in the searched string, the `findall()` method will return the strings of every match in the searched string.

	>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
	>>> mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
	>>> mo.group()
	'415-555-9999'
	>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
	>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
	['415-555-9999', '212-555-0000']
	>>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
	>>> phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
	[('415', '555', '9999'), ('212', '555', '0000')]

### The Wildcard Character

The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.

**Matching Newlines with the Dot Character**

The dot-star will match everything except a newline. By passing `re.DOTALL` as the second argument to `re.compile()`, you can make the dot character match all characters, including the newline character.

	>>> noNewlineRegex = re.compile('.*')
	>>> noNewlineRegex.search('Serve the public trust.\nProtect the innocent.
	\nUphold the law.').group()
	'Serve the public trust.'
	>>> newlineRegex = re.compile('.*', re.DOTALL)
	>>> newlineRegex.search('Serve the public trust.\nProtect the innocent.
	\nUphold the law.').group()
	'Serve the public trust.\nProtect the innocent.\nUphold the law.'

### Case-Insensitive Matching

Normally, regular expressions match text with the exact casing you specify. But sometimes you care only about matching the letters without worrying whether they're uppercase or lowercase. To make your regex case-insensitive, you can pass `re.IGNORECASE` or `re.I` as a second argument to `re.compile()`.

	>>> robocop = re.compile(r'robocop', re.I)
	>>> robocop.search('Robocop is part man, part machine, all cop.').group()
	'Robocop'
	>>> robocop.search('ROBOCOP protects the innocent.').group()
	'ROBOCOP'
	>>> robocop.search('Al, why does your programming book talk about robocop so much?').group()
	'robocop'

### Substituting Strings with the `sub()` Method

Regular expressions can not only find text patterns but can also substitute new text in place of those patterns. The `sub()` method for Regex objects is passed two arguments. The first argument is a string to replace any matches. The second is the string for the regular expression. The `sub()` method returns a string with the substitutions applied.

	>>> namesRegex = re.compile(r'Agent \w+')
	>>> namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
	'CENSORED gave the secret documents to CENSORED.'

Sometimes you may need to use the matched text itself as part of the substitution. In the first argument to `sub()`, you can type \1, \2, \3, and so on, to mean "Enter the text of group 1, 2, 3, and so on, in the substitution".

	>>> agentNamesRegex = re.compile(r'Agent (\w)\w*')
	>>> agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent
	Eve knew Agent Bob was a double agent.')
	A**** told C**** that E**** knew B**** was a double agent.'

### Managing Complex Regexes

Regular expressions are fine if the text pattern you need to match is simple. But matching complicated text patterns might require long, convoluted regular expressions. You can mitigate this by telling the `re.compile()` function to ignore whitespace and comments inside the regular expression string. This "verbose mode" can be enabled by passing the variable `re.VERBOSE` as the second argument to `re.compile()`.

	phoneRegex = re.compile(r'''(
		(\d{3}|\(\d{3}\))?            # area code
		(\s|-|\.)?                    # separator
		\d{3}                         # first 3 digits
		(\s|-|\.)                     # separator
		\d{4}                         # last 4 digits
		(\s*(ext|x|ext.)\s*\d{2,5})?  # extension
		)''', re.VERBOSE)

### Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE

If you want a regular expression that's case-insensitive and includes newlines to match the dot character, you would form your `re.compile()` call like this:

	>>> someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

## Reading and Writing Files <a name="ch08">&nbsp;</a>

### Files and File Paths

**Backslash on Windows and Forward Slash on OS X and Linux**

On Windows, paths are written using backslashes (\\) as the separator between folder names. OS X and Linux, however, use the forward slash (/) as their path separator. If you want your programs to work on all operating systems, you will have to write your Python scripts to handle both cases.

Fortunately, this is simple to do with the os.path.join() function:

	>>> import os
	>>> os.path.join('usr', 'bin', 'spam')
	'usr\\bin\\spam'

this was from a Windows machine, from a Unix machine, it would be:

	>>> os.path.join('usr', 'bin', 'spam')
	'usr/bin/spam'

**The Current Working Directory**

	>>> import os
	>>> os.getcwd()
	'C:\\Python34'
	>>> os.chdir('C:\\Windows\\System32')
	>>> os.getcwd()
	'C:\\Windows\\System32'

**Creating New Folders with `os.makedirs()`**

Your programs can create new folders (directories) with the `os.makedirs()` function.

	>>> import os
	>>> os.makedirs('C:\\delicious\\walnut\\waffles')

This will create not just the *C:\delicious* folder but also a *walnut* folder inside *C:\delicious* and a *waffles* folder inside *C:\delicious\walnut*. That is, `os.makedirs()` will create any necessary intermediate folders in order to ensure that the full path exists.

### The `os.path` Module

**Handling Absolute and Relative Paths**

The os.path module provides functions for returning the absolute path of a relative path and for checking whether a given path is an absolute path.

	>>> os.path.abspath('.')
	'C:\\Python34'
	>>> os.path.abspath('.\\Scripts')
	'C:\\Python34\\Scripts'
	>>> os.path.isabs('.')
	False
	>>> os.path.isabs(os.path.abspath('.'))
	True
	>>> os.path.relpath('C:\\Windows', 'C:\\')
	'Windows'
	>>> os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
	'..\\..\\Windows'
	>>> os.getcwd()
	'C:\\Python34'
	>>> path = 'C:\\Windows\\System32\\calc.exe'
	>>> os.path.basename(path)
	'calc.exe'
	>>> os.path.dirname(path)
	'C:\\Windows\\System32'
	>>> calcFilePath = 'C:\\Windows\\System32\\calc.exe'
	>>> os.path.split(calcFilePath)
	('C:\\Windows\\System32', 'calc.exe')

**Finding File Sizes and Folder Contents**

Once you have ways of handling file paths, you can then start gathering information about specific files and folders.

	>>> os.path.getsize('C:\\Windows\\System32\\calc.exe')
	776192
	>>> os.listdir('C:\\Windows\\System32')
	['0409', '12520437.cpx', '12520850.cpx', '5U877.ax', 'aaclient.dll',
	--snip--
	'xwtpdui.dll', 'xwtpw32.dll', 'zh-CN', 'zh-HK', 'zh-TW', 'zipfldr.dll']

**Checking Path Validity**

Many Python functions will crash with an error if you supply them with a path that does not exist. The `os.path` module provides functions to check whether a given path exists and whether it is a file or folder.

	>>> os.path.exists('C:\\Windows')
	True
	>>> os.path.exists('C:\\some_made_up_folder')
	False
	>>> os.path.isdir('C:\\Windows\\System32')
	True
	>>> os.path.isfile('C:\\Windows\\System32')
	False
	>>> os.path.isdir('C:\\Windows\\System32\\calc.exe')
	False
	>>> os.path.isfile('C:\\Windows\\System32\\calc.exe')
	True

### The File Reading/Writing Process

**Opening Files with the open() Function**

	>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt')

Optionally, you can specify the open mode, for example: `r` for read-only.

	>>> helloFile = open('C:\\Users\\your_home_folder\\hello.txt', 'r')

**Reading the Contents of Files**

	>>> helloContent = helloFile.read()
	>>> helloContent
	'Hello world!'
	>>> sonnetFile = open('sonnet29.txt')
	>>> sonnetFile.readlines()
	[When, in disgrace with fortune and men's eyes,\n', ' I all alone beweep my
	outcast state,\n', And trouble deaf heaven with my bootless cries,\n', And
	look upon myself and curse my fate,']

**Writing to Files**

You can't write to a file you've opened in read mode, though. Instead, you need to open it in "write plaintext" mode or "append plaintext" mode, or write mode and append mode for short.

	>>> baconFile = open('bacon.txt', 'w')
	>>> baconFile.write('Hello world!\n')
	13
	>>> baconFile.close()
	>>> baconFile = open('bacon.txt', 'a')
	>>> baconFile.write('Bacon is not a vegetable.')
	25
	>>> baconFile.close()
	>>> baconFile = open('bacon.txt')
	>>> content = baconFile.read()
	>>> baconFile.close()
	>>> print(content)
	Hello world!
	Bacon is not a vegetable.

### Saving Variables with the shelve Module

You can save variables in your Python programs to binary shelf files using the `shelve` module. This way, your program can restore data to variables from the hard drive. The shelve module will let you add Save and Open features to your program.

	>>> import shelve
	>>> shelfFile = shelve.open('mydata')
	>>> cats = ['Zophie', 'Pooka', 'Simon']
	>>> shelfFile['cats'] = cats
	>>> shelfFile.close()

After you save the values, you can recover them:

	>>> shelfFile = shelve.open('mydata')
	>>> shelfFile['cats']
	['Zophie', 'Pooka', 'Simon']
	>>> shelfFile.close()

## Organizing Files <a name="ch09">&nbsp;</a>

### The shutil module

The `shutil` (or shell utilities) module has functions to let you copy, move, rename, and delete files in your Python programs. To use the `shutil` functions, you will first need to use:

	import shutil

**Copying files and folders**

	>>> import shutil, os
	>>> os.chdir('C:\\')
	>>> shutil.copy('C:\\spam.txt', 'C:\\delicious')
	'C:\\delicious\\spam.txt'
	>>> shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')
	'C:\\delicious\\eggs2.txt'

While `shutil.copy()` will copy a single file, `shutil.copytree()` will copy an entire folder and every folder and file contained in it.

	>>> import shutil, os
	>>> os.chdir('C:\\')
	>>> shutil.copytree('C:\\bacon', 'C:\\bacon_backup')
	'C:\\bacon_backup'

**Moving and Renaming Files and Folders**

	>>> import shutil
	>>> shutil.move('C:\\bacon.txt', 'C:\\eggs')
	'C:\\eggs\\bacon.txt'

Move and rename:

	>>> shutil.move('C:\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
	'C:\\eggs\\new_bacon.txt'

The folders that make up the destination must already exist, or else Python will throw an exception.

**Permanently Deleting Files and Folders**

Be careful when using these functions in your programs! It's often a good idea to first run your program with these calls commented out and with print() calls added to show the files that would be deleted.

	import os
	for filename in os.listdir():
		if filename.endswith('.rxt'):
			#os.unlink(filename)
			print('File to delete: '+filename)

**Safe Deletes with the send2trash Module**

Since Python's built-in `shutil.rmtree()` function irreversibly deletes files and folders, it can be dangerous to use. A much better way to delete files and folders is with the third-party `send2trash` module. You can install this module by running `pip install send2trash` from a Terminal window.

	>>> import send2trash
	>>> baconFile = open('bacon.txt', 'a') # creates the file
	>>> baconFile.write('Bacon is not a vegetable.')
	25
	>>> baconFile.close()
	>>> send2trash.send2trash('bacon.txt')

### Walking a Directory Tree

Here is an example program that uses the `os.walk()` function:

	import os
	
	for folderName, subfolders, filenames in os.walk('C:\\delicious'):
		print('The current folder is ' + folderName)
	
		for subfolder in subfolders:
			print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
		for filename in filenames:
			print('FILE INSIDE ' + folderName + ': '+ filename)
	
		print('')

### Compressing Files with the zipfile Module

**Reading ZIP Files**

	>>> import zipfile, os
	>>> os.chdir('C:\\')    # move to the folder with example.zip
	>>> exampleZip = zipfile.ZipFile('example.zip')
	>>> exampleZip.namelist()
	['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
	>>> spamInfo = exampleZip.getinfo('spam.txt')
	>>> spamInfo.file_size
	13908
	>>> spamInfo.compress_size
	3828
	>>> 'Compressed file is %sx smaller!' % (round(spamInfo.file_size / spamInfo
	.compress_size, 2))
	'Compressed file is 3.63x smaller!'
	>>> exampleZip.close()

**Extracting from ZIP Files**

	>>> import zipfile, os
	>>> os.chdir('C:\\')    # move to the folder with example.zip
	>>> exampleZip = zipfile.ZipFile('example.zip')
	>>> exampleZip.extractall()
	>>> exampleZip.close()

The `extract()` method for ZipFile objects will extract a single file from the ZIP file:

	>>> exampleZip.extract('spam.txt')
	'C:\\spam.txt'
	>>> exampleZip.extract('spam.txt', 'C:\\some\\new\\folders')
	'C:\\some\\new\\folders\\spam.txt'
	>>> exampleZip.close()

**Creating and Adding to ZIP Files**

	>>> import zipfile
	>>> newZip = zipfile.ZipFile('new.zip', 'w')
	>>> newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
	>>> newZip.close()

## Debugging <a name="ch10">&nbsp;</a>

### Raising Exceptions

Python raises an exception whenever it tries to execute invalid code. Exceptions are raised with a `raise` statement. In code, a `raise` statement consists of the following:

* The `raise` keyword
* A call to the `Exception()` function
* A string with a helpful error message passed to the `Exception()` function

Example:

	>>> raise Exception('This is the error message.')
	Traceback (most recent call last):
		File "<pyshell#191>", line 1, in <module>
		raise Exception('This is the error message.')
	Exception: This is the error message.

### Assertions

An assertion is a sanity check to make sure your code isn't doing something obviously wrong. These sanity checks are performed by assert statements. If the sanity check fails, then an AssertionError exception is raised. In code, an assert statement consists of the following:

* The `assert` keyword
* A condition (that is, an expression that evaluates to `True` or `False`)
* A comma
* A string to display when the condition is `False`

For example:

	>>> podBayDoorStatus = 'open'
	>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
	>>> podBayDoorStatus = 'I\'m sorry, Dave. I\'m afraid I can't do that.''
	>>> assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
	Traceback (most recent call last):
	  File "<pyshell#10>", line 1, in <module>
	    assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
	AssertionError: The pod bay doors need to be "open".

### Logging

**Using the logging Module**

To enable the logging module to display log messages on your screen as your program runs, copy the following to the top of your program (but under the `#!` python shebang line):

	import logging
	logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

**Logging Levels**

*Logging levels* provide a way to categorize your log messages by importance. There are five logging levels, described below from least to most important. Messages can be logged at each level using a different logging function.

Level | Logging Function | Description
--- | --- | ---
`DEBUG` | `logging.debug()` | The lowest level. Used for small details. Usually you care about these messages only when diagnosing problems.
`INFO` | `logging.info()` | Used to record information on general events in your program or confirm that things are working at their point in the program.
`WARNING` | `logging.warning()` | Used to indicate a potential problem that doesn't prevent the program from working but might do so in the future.
`ERROR` | `logging.error()` | Used to record an error that caused the program to fail to do something.
`CRITICAL` | `logging.critical()` | The highest level. Used to indicate a fatal error that has caused or is about to cause the program to stop running entirely.

	>>> import logging
	>>> logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
	>>> logging.debug('Some debugging details.')
	2015-05-18 19:04:26,901 - DEBUG - Some debugging details.
	>>> logging.info('The logging module is working.')
	2015-05-18 19:04:35,569 - INFO - The logging module is working.
	>>> logging.warning('An error message is about to be logged.')
	2015-05-18 19:04:56,843 - WARNING - An error message is about to be logged.
	>>> logging.error('An error has occurred.')
	2015-05-18 19:05:07,737 - ERROR - An error has occurred.
	>>> logging.critical('The program is unable to recover!')
	2015-05-18 19:05:45,794 - CRITICAL - The program is unable to recover!

**Disabling Logging**

After you've debugged your program, you probably don't want all these log messages cluttering the screen. The `logging.disable()` function disables these so that you don't have to go into your program and remove all the logging calls by hand. You simply pass `logging.disable()` a logging level, and it will suppress all log messages at that level or lower. So if you want to disable logging entirely, just add `logging.disable(logging.CRITICAL)` to your program.

Since `logging.disable()` will disable all messages after it, you will probably want to add it near the `import logging` line of code in your program. This way, you can easily find it to comment out or uncomment that call to enable or disable logging messages as needed.

**Logging to a File**

Instead of displaying the log messages to the screen, you can write them to a text file. The `logging.basicConfig()` function takes a filename keyword argument, like so:

	import logging
	logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

The log messages will be saved to `myProgramLog.txt`. 

## Web Scraping <a name="ch11">&nbsp;</a>

Modules to use:

* Webbrowser. Comes with Python and opens a browser to a specific page.
* Requests. Downloads files and web pages from the Internet.
* Beautiful Soup. Parses HTML, the format that web pages are written in.
* Selenium. Launches and controls a web browser. Selenium is able to fill in forms and simulate mouse clicks in this browser.

**The `webbrowser` module**

The webbrowser module's open() function can launch a new browser to a specified URL:

	>>> import webbrowser
	>>> webbrowser.open('http://inventwithpython.com/')

This is about the only thing the webbrowser module can do.

### Downloading Files from the Web with the requests Module

**Downloading a Web Page with the requests.get() Function**

	>>> import requests
	>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
	>>> type(res)
	<class 'requests.models.Response'>
	>>> res.status_code == requests.codes.ok
	True
	>>> len(res.text)
	178981
	>>> print(res.text[:250])
	The Project Gutenberg EBook of Romeo and Juliet, by William Shakespeare

**Checking for Errors**

As you've seen, the Response object has a `status_code` attribute that can be checked against `requests.codes.ok` to see whether the download succeeded. A simpler way to check for success is to call the `raise_for_status()` method on the Response object. This will raise an exception if there was an error downloading the file and will do nothing if the download succeeded.

	>>> res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
	>>> res.raise_for_status()
	Traceback (most recent call last):
		File "<pyshell#138>", line 1, in <module>
			res.raise_for_status()
		File "C:\Python34\lib\site-packages\requests\models.py", line 773, in raise_for_status
			raise HTTPError(http_error_msg, response=self)
	requests.exceptions.HTTPError: 404 Client Error: Not Found

The `raise_for_status()` method is a good way to ensure that a program halts if a bad download occurs. If a failed download isn't a deal breaker for your program, you can wrap the `raise_for_status()` line with `try` and `except` statements to handle this error case without crashing.

	import requests
	res = requests.get('http://inventwithpython.com/page_that_does_not_exist')
	try:
		res.raise_for_status()
	except Exception as exc:
		print('There was a problem: %s' % (exc))

### Saving Downloaded Files to the Hard Drive

You can save the web page to a file on your hard drive with the standard `open()` function and `write()` method but you must open the file in write binary mode by passing the string 'wb' as the second argument to `open()`. Even if the page is in plaintext you need to write binary data instead of text data in order to maintain the Unicode encoding of the text.

To write the web page to a file, you can use a for loop with the `Response` object's `iter_content()` method.

	>>> import requests
	>>> res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
	>>> res.raise_for_status()
	>>> playFile = open('RomeoAndJuliet.txt', 'wb')
	>>> for chunk in res.iter_content(100000):
			playFile.write(chunk)
	100000
	78981
	>>> playFile.close()

The `iter_content()` method returns "chunks" of the content on each iteration through the loop. Each chunk is of the bytes data type, and you get to specify how many bytes each chunk will contain. One hundred thousand bytes is generally a good size, so pass 100000 as the argument to `iter_content()`.

### Parsing HTML with the BeautifulSoup Module

**Creating a BeautifulSoup Object from HTML**

From a web page:

	>>> import requests, bs4
	>>> res = requests.get('http://nostarch.com')
	>>> res.raise_for_status()
	>>> noStarchSoup = bs4.BeautifulSoup(res.text)
	>>> type(noStarchSoup)
	<class 'bs4.BeautifulSoup'>

From local file:

	>>> exampleFile = open('example.html')
	>>> exampleSoup = bs4.BeautifulSoup(exampleFile)
	>>> type(exampleSoup)
	<class 'bs4.BeautifulSoup'>

**Finding an Element with the select() Method**

You can retrieve a web page element from a `BeautifulSoup` object by calling the `select()` method and passing a string of a CSS selector for the element you are looking for.

Examples of CSS Selectors:

Selector passed to the select() method | Will match...
--- | ---
`soup.select('div')` | All elements named `<div>`
`soup.select('#author')` | The element with an id attribute of author
`soup.select('.notice')` | All elements that use a CSS class attribute named `notice`
`soup.select('div span')` | All elements named `<span>` that are within an element named `<div>`
`soup.select('div > span')` | All elements named `<span>` that are directly within an element named `<div>`, with no other element in between
`soup.select('input[name]')` | All elements named `<input>` that have a name attribute with any value
`soup.select('input[type="button"]')` | All elements named `<input>` that have an attribute named type with value button

	>>> import bs4
	>>> exampleFile = open('example.html')
	>>> exampleSoup = bs4.BeautifulSoup(exampleFile.read())
	>>> elems = exampleSoup.select('#author')
	>>> type(elems)
	<class 'list'>
	>>> len(elems)
	1
	>>> type(elems[0])
	<class 'bs4.element.Tag'>
	>>> elems[0].getText()
	'Al Sweigart'
	>>> str(elems[0])
	'<span id="author">Al Sweigart</span>'
	>>> elems[0].attrs
	{'id': 'author'}

**Getting Data from an Element's Attributes**

	>>> import bs4
	>>> soup = bs4.BeautifulSoup(open('example.html'))
	>>> spanElem = soup.select('span')[0]
	>>> str(spanElem)
	'<span id="author">Al Sweigart</span>'
	>>> spanElem.get('id')
	'author'
	>>> spanElem.get('some_nonexistent_addr') == None
	True
	>>> spanElem.attrs
	{'id': 'author'}

### Controlling the Browser with the selenium Module

The selenium module lets Python directly control the browser by programmatically clicking links and filling in login information, almost as though there is a human user interacting with the page.

**Starting a Selenium-Controlled Browser**

For these examples, you'll need the Firefox web browser.

	>>> from selenium import webdriver
	>>> browser = webdriver.Firefox()
	>>> type(browser)
	<class 'selenium.webdriver.firefox.webdriver.WebDriver'>
	>>> browser.get('http://inventwithpython.com')

**Finding Elements on the Page**

WebDriver objects have quite a few methods for finding elements on a page. They are divided into the `find_element_*` and `find_elements_*` methods. The `find_element_*` methods return a single WebElement object, representing the first element on the page that matches your query. The `find_elements_*` methods return a list of `WebElement_*` objects for every matching element on the page.

Selenium's WebDriver Methods for Finding Elements:

Method name | WebElement object/list returned
--- | ---
`browser.find_element_by_class_name(name)` & `browser.find_elements_by_class_name(name)` | Elements that use the CSS class name
`browser.find_element_by_css_selector(selector)` & `browser.find_elements_by_css_selector(selector)` | Elements that match the CSS selector
`browser.find_element_by_id(id)` & `browser.find_elements_by_id(id)` | Elements with a matching `id` attribute value
`browser.find_element_by_link_text(text)` & `browser.find_elements_by_link_text(text)` | `<a>` elements that completely match the `text` provided
`browser.find_element_by_partial_link_text(text)` & `browser.find_elements_by_partial_link_text(text)` | `<a>` elements that contain the `text` provided
`browser.find_element_by_name(name)` & `browser.find_elements_by_name(name)` | Elements with a matching `name` attribute value
`browser.find_element_by_tag_name(name)` & `browser.find_elements_by_tag_name(name)` | Elements with a matching tag `name` (case insensitive; an `<a>` element is matched by 'a' and 'A')

Except for the *_by_tag_name() methods, the arguments to all the methods are case sensitive. If no elements exist on the page that match what the method is looking for, the selenium module raises a `NoSuchElement` exception.

WebElement Attributes and Methods

Attribute or method | Description
--- | ---
`tag_name` | The tag name, such as 'a' for an `<a>` element
`get_attribute(name)` | The value for the element's name attribute
`text` | The text within the element, such as 'hello' in `<span>hello</span>`
`clear()` | For text field or text area elements, clears the text typed into it
`is_displayed()` | Returns `True` if the element is visible; otherwise returns `False`
`is_enabled()` | For `input` elements, returns `True` if the element is enabled; otherwise returns `False`
`is_selected()` | For checkbox or radio button elements, returns `True` if the element is selected; otherwise returns `False`
`location` | A dictionary with keys 'x' and 'y' for the position of the element in the page

Example:

	from selenium import webdriver
	browser = webdriver.Firefox()
	browser.get('http://inventwithpython.com')
	try:
		elem = browser.find_element_by_class_name('bookcover')
		print('Found <%s> element with that class name!' % (elem.tag_name))
	except:
		print('Was not able to find an element with that name.')

**Clicking the Page**

	>>> from selenium import webdriver
	>>> browser = webdriver.Firefox()
	>>> browser.get('http://inventwithpython.com')
	>>> linkElem = browser.find_element_by_link_text('Read It Online')
	>>> type(linkElem)
	<class 'selenium.webdriver.remote.webelement.WebElement'>
	>>> linkElem.click() # follows the "Read It Online" link

**Filling Out and Submitting Forms**

	>>> from selenium import webdriver
	>>> browser = webdriver.Firefox()
	>>> browser.get('https://mail.yahoo.com')
	>>> emailElem = browser.find_element_by_id('login-username')
	>>> emailElem.send_keys('not_my_real_email')
	>>> passwordElem = browser.find_element_by_id('login-passwd')
	>>> passwordElem.send_keys('12345')
	>>> passwordElem.submit()

**Sending Special Keys**

Commonly Used Variables in the selenium.webdriver.common.keys Module

Attributes | Meanings
--- | ---
`Keys.DOWN`, `Keys.UP`, `Keys.LEFT`, `Keys.RIGHT` | The keyboard arrow keys
`Keys.ENTER`, `Keys.RETURN` | The `ENTER` and `RETURN` keys
`Keys.HOME`, `Keys.END`, `Keys.PAGE_DOWN`, `Keys.PAGE_UP` | The home, end, pagedown, and pageup keys
`Keys.ESCAPE`, `Keys.BACK_SPACE`, `Keys.DELETE` | The `ESC`, `BACKSPACE`, and `DELETE` keys
`Keys.F1`, `Keys.F2`,..., `Keys.F12` | The `F1` to `F12` keys at the top of the keyboard
`Keys.TAB` | The `TAB` key

Example:

	>>> from selenium import webdriver
	>>> from selenium.webdriver.common.keys import Keys
	>>> browser = webdriver.Firefox()
	>>> browser.get('http://nostarch.com')
	>>> htmlElem = browser.find_element_by_tag_name('html')
	>>> htmlElem.send_keys(Keys.END)     # scrolls to bottom
	>>> htmlElem.send_keys(Keys.HOME)    # scrolls to top

**Clicking Browser Buttons**

* `browser.back()`.- Clicks the Back button.
* `browser.forward()`.- Clicks the Forward button.
* `browser.refresh()`.- Clicks the Refresh/Reload button.
* `browser.quit()`.- Clicks the Close Window button.

## Working with Excel Spreadsheets <a name="ch12">&nbsp;</a>

The `openpyxl` module allows your Python programs to read and modify Excel spreadsheet files.

	pip install openpyxl

### Reading Excel Documents

**Opening Excel Documents with OpenPyXL**

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> type(wb)
	<class 'openpyxl.workbook.workbook.Workbook'>

**Getting Sheets from the Workbook**

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> wb.get_sheet_names()
	['Sheet1', 'Sheet2', 'Sheet3']
	>>> sheet = wb.get_sheet_by_name('Sheet3')
	>>> sheet
	<Worksheet "Sheet3">
	>>> type(sheet) <class 'openpyxl.worksheet.worksheet.Worksheet'>
	>>> sheet.title
	'Sheet3'
	>>> anotherSheet = wb.get_active_sheet()
	>>> anotherSheet
	<Worksheet "Sheet1">

**Getting Cells from the Sheets**

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> sheet = wb.get_sheet_by_name('Sheet1')
	>>> sheet['A1']
	<Cell Sheet1.A1>
	>>> sheet['A1'].value
	datetime.datetime(2015, 4, 5, 13, 34, 2)
	>>> c = sheet['B1']
	>>> c.value
	'Apples'
	>>> 'Row ' + str(c.row) + ', Column ' + c.column + ' is ' + c.value
	'Row 1, Column B is Apples'
	>>> 'Cell ' + c.coordinate + ' is ' + c.value
	'Cell B1 is Apples'
	>>> sheet['C1'].value
	73

Specifying a column by letter can be tricky to program, especially because after column Z, the columns start by using two letters: AA, AB, AC, and so on. As an alternative, you can also get a cell using the sheet's `cell()` method and passing integers for its row and column keyword arguments. The first row or column integer is 1, not 0.

	>>> sheet.cell(row=1, column=2)
	<Cell Sheet1.B1>
	>>> sheet.cell(row=1, column=2).value
	'Apples'
	>>> for i in range(1, 8, 2):
		print(i, sheet.cell(row=i, column=2).value)

You can determine the size of the sheet with the Worksheet object's `get_highest_row()` and `get_highest_column()` methods.

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> sheet = wb.get_sheet_by_name('Sheet1')
	>>> sheet.get_highest_row()
	7
	>>> sheet.get_highest_column()
	3

**Converting Between Column Letters and Numbers**

	>>> import openpyxl
	>>> from openpyxl.cell import get_column_letter, column_index_from_string
	>>> get_column_letter(1)
	'A'
	>>> get_column_letter(2)
	'B'
	>>> get_column_letter(27)
	'AA'
	>>> get_column_letter(900)
	'AHP'
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> sheet = wb.get_sheet_by_name('Sheet1')
	>>> get_column_letter(sheet.get_highest_column())
	'C'
	>>> column_index_from_string('A')
	1
	>>> column_index_from_string('AA')
	27

**Getting Rows and Columns from the Sheets**

You can slice Worksheet objects to get all the Cell objects in a row, column, or rectangular area of the spreadsheet. Then you can loop over all the cells in the slice.

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> sheet = wb.get_sheet_by_name('Sheet1')
	>>> tuple(sheet['A1':'C3'])
	((<Cell Sheet1.A1>, <Cell Sheet1.B1>, <Cell Sheet1.C1>), (<Cell Sheet1.A2>,
	<Cell Sheet1.B2>, <Cell Sheet1.C2>), (<Cell Sheet1.A3>, <Cell Sheet1.B3>,
	<Cell Sheet1.C3>))
	>>> for rowOfCellObjects in sheet['A1':'C3']:
			for cellObj in rowOfCellObjects:
				print(cellObj.coordinate, cellObj.value)
			print('--- END OF ROW ---')
	A1 2015-04-05 13:34:02
	B1 Apples
	C1 73
	--- END OF ROW ---
	A2 2015-04-05 03:41:23
	B2 Cherries
	C2 85
	--- END OF ROW ---
	A3 2015-04-06 12:46:51
	B3 Pears
	C3 14
	--- END OF ROW ---

To access the values of cells in a particular row or column, you can also use a Worksheet object's rows and columns attribute.

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> sheet = wb.get_active_sheet()
	>>> sheet.columns[1]
	(<Cell Sheet1.B1>, <Cell Sheet1.B2>, <Cell Sheet1.B3>, <Cell Sheet1.B4>,
	<Cell Sheet1.B5>, <Cell Sheet1.B6>, <Cell Sheet1.B7>)
	>>> for cellObj in sheet.columns[1]:
		print(cellObj.value)
	Apples
	Cherries
	Pears
	Oranges
	Apples
	Bananas
	Strawberries

### Writing Excel Documents

**Creating and Saving Excel Documents**

	>>> import openpyxl
	>>> wb = openpyxl.Workbook()
	>>> wb.get_sheet_names()
	['Sheet']
	>>> sheet = wb.get_active_sheet()
	>>> sheet.title
	'Sheet'
	>>> sheet.title = 'Spam Bacon Eggs Sheet'
	>>> wb.get_sheet_names()
	['Spam Bacon Eggs Sheet']

Any time you modify the `Workbook` object or its sheets and cells, the spreadsheet file will not be saved until you call the `save()` workbook method.

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('example.xlsx')
	>>> sheet = wb.get_active_sheet()
	>>> sheet.title = 'Spam Spam Spam'
	>>> wb.save('example_copy.xlsx')

**Creating and Removing Sheets**

	>>> import openpyxl
	>>> wb = openpyxl.Workbook()
	>>> wb.get_sheet_names()
	['Sheet']
	>>> wb.create_sheet()
	<Worksheet "Sheet1">
	>>> wb.get_sheet_names()
	['Sheet', 'Sheet1']
	>>> wb.create_sheet(index=0, title='First Sheet')
	<Worksheet "First Sheet">
	>>> wb.get_sheet_names()
	['First Sheet', 'Sheet', 'Sheet1']
	>>> wb.create_sheet(index=2, title='Middle Sheet')
	<Worksheet "Middle Sheet">
	>>> wb.get_sheet_names()
	['First Sheet', 'Sheet', 'Middle Sheet', 'Sheet1']
	>>> wb.remove_sheet(wb.get_sheet_by_name('Middle Sheet'))
	>>> wb.remove_sheet(wb.get_sheet_by_name('Sheet1'))
	>>> wb.get_sheet_names()
	['First Sheet', 'Sheet']

**Writing Values to Cells**

	>>> import openpyxl
	>>> wb = openpyxl.Workbook()
	>>> sheet = wb.get_sheet_by_name('Sheet')
	>>> sheet['A1'] = 'Hello world!'
	>>> sheet['A1'].value
	'Hello world!'

### Setting the Font Style of Cells

To customize font styles in cells, important, import the `Font()` and `Style()` functions from the `openpyxl.styles` module:

	from openpyxl.styles import Font, Style

This allows you to type `Font()` instead of `openpyxl.styles.Font()`.

	>>> import openpyxl
	>>> from openpyxl.styles import Font, Style
	>>> wb = openpyxl.Workbook()
	>>> sheet = wb.get_sheet_by_name('Sheet')
	>>> italic24Font = Font(size=24, italic=True)
	>>> styleObj = Style(font=italic24Font)
	>>> sheet['A1'].style = styleObj
	>>> sheet['A1'] = 'Hello world!'
	>>> wb.save('styled.xlsx')

### Font Objects

Keyword arguments for font style attributes

Keyword argument | Data type | Description
--- | --- | ---
name | `String` | The font name, such as 'Calibri' or 'Times New Roman'
size | `Integer` | The point size
bold | `Boolean` | `True`, for bold font
italic | `Boolean` | `True`, for italic font

You can call `Font()` to create a `Font` object and store that `Font` object in a variable. You then pass that to `Style()`, store the resulting `Style` object in a variable, and assign that variable to a `Cell` object's style attribute.

	>>> import openpyxl
	>>> from openpyxl.styles import Font, Style
	>>> wb = openpyxl.Workbook()
	>>> sheet = wb.get_sheet_by_name('Sheet')
	>>> fontObj1 = Font(name='Times New Roman', bold=True)
	>>> styleObj1 = Style(font=fontObj1)
	>>> sheet['A1'].style = styleObj1
	>>> sheet['A1'] = 'Bold Times New Roman'
	>>> fontObj2 = Font(size=24, italic=True)
	>>> styleObj2 = Style(font=fontObj2)
	>>> sheet['B3'].style = styleObj2
	>>> sheet['B3'] = '24 pt Italic'
	>>> wb.save('styles.xlsx')

### Formulas

A formula is set just like any other text value in a cell.

	>>> import openpyxl
	>>> wb = openpyxl.Workbook()
	>>> sheet = wb.get_active_sheet()
	>>> sheet['A1'] = 200
	>>> sheet['A2'] = 300
	>>> sheet['A3'] = '=SUM(A1:A2)'
	>>> wb.save('writeFormula.xlsx')

### Adjusting Rows and Columns

**Setting Row Height and Column Width**

	>>> import openpyxl
	>>> wb = openpyxl.Workbook()
	>>> sheet = wb.get_active_sheet()
	>>> sheet['A1'] = 'Tall row'
	>>> sheet['B2'] = 'Wide column'
	>>> sheet.row_dimensions[1].height = 70
	>>> sheet.column_dimensions['B'].width = 20
	>>> wb.save('dimensions.xlsx')

**Merging and Unmerging Cells**

	>>> import openpyxl
	>>> wb = openpyxl.Workbook()
	>>> sheet = wb.get_active_sheet()
	>>> sheet.merge_cells('A1:D3')
	>>> sheet['A1'] = 'Twelve cells merged together.'
	>>> sheet.merge_cells('C5:D5')
	>>> sheet['C5'] = 'Two merged cells.'
	>>> wb.save('merged.xlsx')

The argument to `merge_cells()` is a single string of the top-left and bottom-right cells of the rectangular area to be merged: 'A1:D3' merges 12 cells into a single cell. To set the value of these merged cells, simply set the value of the top-left cell of the merged group.

To unmerge cells, call the `unmerge_cells()`:

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('merged.xlsx')
	>>> sheet = wb.get_active_sheet()
	>>> sheet.unmerge_cells('A1:D3')
	>>> sheet.unmerge_cells('C5:D5')
	>>> wb.save('merged.xlsx')

**Freeze Panes**

Frozen Pane Settings:

`freeze_panes` setting | Rows and columns frozen
--- | ---
`sheet.freeze_panes = 'A2'` | Row 1
`sheet.freeze_panes = 'B1'` | Column A
`sheet.freeze_panes = 'C1'` | Columns A and B
`sheet.freeze_panes = 'C2'` | Row 1 and columns A and B
`sheet.freeze_panes = 'A1'` or `sheet.freeze_panes = None` | No frozen panes

Example:

	>>> import openpyxl
	>>> wb = openpyxl.load_workbook('produceSales.xlsx')
	>>> sheet = wb.get_active_sheet()
	>>> sheet.freeze_panes = 'A2'
	>>> wb.save('freezeExample.xlsx')

### Charts

OpenPyXL supports creating bar, line, scatter, and pie charts using the data in a sheet's cells. If you want to see what additional features may be available to you, you can check out the full documentation for OpenPyXL at [http://openpyxl.readthedocs.org/](http://openpyxl.readthedocs.org/).

## Working with PDF and Word Documents <a name="ch13">&nbsp;</a>

There are Python modules that make it easy for you to interact with PDFs and Word documents. This chapter will cover two such modules: PyPDF2 and Python-Docx.

### PDF Documents

**Extracting Text from PDFs**

PyPDF2 does not have a way to extract images, charts, or other media from PDF documents, but it can extract text and return it as a Python string.

**Creating PDFs**

PyPDF2 doesn't allow you to directly edit a PDF. Instead, you have to create a new PDF and then copy content over from an existing document.

### Word Documents

Python can create and modify Word documents, which have the .docx file extension, with the python-docx module. You can install the module by running pip install python-docx.

**Reading Word Documents**

	>>> import docx
	>>> doc = docx.Document('demo.docx')
	>>> len(doc.paragraphs)
	7
	>>> doc.paragraphs[0].text
	'Document Title'
	>>> doc.paragraphs[1].text
	'A plain paragraph with some bold and some italic'
	>>> len(doc.paragraphs[1].runs)
	4
	>>> doc.paragraphs[1].runs[0].text
	'A plain paragraph with some '
	>>> doc.paragraphs[1].runs[1].text
	'bold'
	>>> doc.paragraphs[1].runs[2].text
	' and some '
	>>> doc.paragraphs[1].runs[3].text
	'italic'

**Getting the Full Text from a .docx File**

	>>> import readDocx
	>>> print(readDocx.getText('demo.docx'))
	Document Title
	A plain paragraph with some bold and some italic
	Heading, level 1
	Intense quote
	first item in unordered list
	first item in ordered list

**Styling Paragraph and Run Objects**

For Word documents, there are three types of styles: *Paragraph styles* can be applied to `Paragraph` objects, *character styles* can be applied to `Run` objects, and *linked styles* can be applied to both kinds of objects. You can give both `Paragraph` and `Run` objects styles by setting their style attribute to a string. This string should be the name of a style. If style is set to `None`, then there will be no style associated with the `Paragraph` or `Run` object.

The string values for the default Word styles are as follows:

&nbsp; | &nbsp; | &nbsp; | &nbsp;
--- | --- | --- | ---
'Normal' | 'Heading5' | 'ListBullet' | 'ListParagraph'
'BodyText' | 'Heading6' | 'ListBullet2' | 'MacroText'
'BodyText2' | 'Heading7' | 'ListBullet3' | 'NoSpacing'
'BodyText3' | 'Heading8' | 'ListContinue' | 'Quote'
'Caption' | 'Heading9' | 'ListContinue2' | 'Subtitle'
'Heading1' | 'IntenseQuote' | 'ListContinue3' | 'TOCHeading'
'Heading2' | 'List' | 'ListNumber' | 'Title'
'Heading3' | 'List2' | 'ListNumber2' | &nbsp;
'Heading4' | 'List3' | 'ListNumber3' | &nbsp;

When using a *linked style* for a `Run` object, you will need to add 'Char' to the end of its name. For example, to set the `Quote` linked style for a `Paragraph` object, you would use `paragraphObj.style = 'Quote'`, but for a `Run` object, you would use `runObj.style = 'QuoteChar'`.

**Run Attributes**

`Runs` can be further styled using text attributes. Each attribute can be set to one of three values: `True` (the attribute is always enabled, no matter what other styles are applied to the run), `False` (the attribute is always disabled), or `None` (defaults to whatever the run's style is set to).

Run Object text Attributes

Attribute | Description
--- | ---
`bold` | The text appears in bold.
`italic` | The text appears in italic.
`underline` | The text is underlined.
`strike` | The text appears with strikethrough.
`double_strike` | The text appears with double strikethrough.
`all_caps` | The text appears in capital letters.
`small_caps` | The text appears in capital letters, with lowercase letters two points smaller.
`shadow` | The text appears with a shadow.
`outline` | The text appears outlined rather than solid.
`rtl` | The text is written right-to-left.
`imprint` | The text appears pressed into the page.
`emboss` | The text appears raised off the page in relief.

Example

	>>> doc = docx.Document('demo.docx')
	>>> doc.paragraphs[0].text
	'Document Title'
	>>> doc.paragraphs[0].style
	'Title'
	>>> doc.paragraphs[0].style = 'Normal'
	>>> doc.paragraphs[1].text
	'A plain paragraph with some bold and some italic'
	>>> (doc.paragraphs[1].runs[0].text, doc.paragraphs[1].runs[1].text, doc.
	paragraphs[1].runs[2].text, doc.paragraphs[1].runs[3].text)
	('A plain paragraph with some ', 'bold', ' and some ', 'italic')
	>>> doc.paragraphs[1].runs[0].style = 'QuoteChar'
	>>> doc.paragraphs[1].runs[1].underline = True
	>>> doc.paragraphs[1].runs[3].underline = True
	>>> doc.save('restyled.docx')

**Writing Word Documents**

	>>> import docx
	>>> doc = docx.Document()
	>>> doc.add_paragraph('Hello world!')
	<docx.text.Paragraph object at 0x0000000003B56F60>
	>>> doc.save('helloworld.docx')

You can add paragraphs by calling the `add_paragraph()` method again with the new paragraph's text. Or to add text to the end of an existing paragraph, you can call the paragraph's `add_run()` method and pass it a string.

	>>> import docx
	>>> doc = docx.Document()
	>>> doc.add_paragraph('Hello world!')
	<docx.text.Paragraph object at 0x000000000366AD30>
	>>> paraObj1 = doc.add_paragraph('This is a second paragraph.')
	>>> paraObj2 = doc.add_paragraph('This is a yet another paragraph.')
	>>> paraObj1.add_run(' This text is being added to the second paragraph.')
	<docx.text.Run object at 0x0000000003A2C860>
	>>> doc.save('multipleParagraphs.docx')

Both `add_paragraph()` and `add_run()` accept an optional second argument that is a string of the `Paragraph` or `Run` object's style. For example:

	>>> doc.add_paragraph('Hello world!', 'Title')

This line adds a paragraph with the text *Hello world!* in the `Title` style.

**Adding Headings**

	>>> doc = docx.Document()
	>>> doc.add_heading('Header 0', 0)
	<docx.text.Paragraph object at 0x00000000036CB3C8>
	>>> doc.add_heading('Header 1', 1)
	<docx.text.Paragraph object at 0x00000000036CB630>
	>>> doc.add_heading('Header 2', 2)
	<docx.text.Paragraph object at 0x00000000036CB828>
	>>> doc.add_heading('Header 3', 3)
	<docx.text.Paragraph object at 0x00000000036CB2E8>
	>>> doc.add_heading('Header 4', 4)
	<docx.text.Paragraph object at 0x00000000036CB3C8>
	>>> doc.save('headings.docx')

The arguments to `add_heading()` are a string of the heading text and an integer from 0 to 4. The integer 0 makes the heading the `Title` style, which is used for the top of the document. Integers 1 to 4 are for various heading levels, with 1 being the main heading and 4 the lowest subheading. The `add_heading()` function returns a `Paragraph` object to save you the step of extracting it from the `Document` object as a separate step.

**Adding Line and Page Breaks**

	>>> doc = docx.Document()
	>>> doc.add_paragraph('This is on the first page!')
	<docx.text.Paragraph object at 0x0000000003785518>
	>>> doc.paragraphs[0].runs[0].add_break(docx.text.WD_BREAK.PAGE)
	>>> doc.add_paragraph('This is on the second page!')
	<docx.text.Paragraph object at 0x00000000037855F8>
	>>> doc.save('twoPage.docx')

**Adding Pictures**

Document objects have an `add_picture()` method that will let you add an image to the end of the document. Say you have a file zophie.png in the current working directory. You can add *zophie.png* to the end of your document with a width of 1 inch and height of 4 centimeters (Word can use both imperial and metric units) by entering the following:

	>>> doc.add_picture('zophie.png', width=docx.shared.Inches(1),
	height=docx.shared.Cm(4))
	<docx.shape.InlineShape object at 0x00000000036C7D30>

## Working with CSV Files and JSON Data <a name="ch14">&nbsp;</a>

Python also comes with the special `csv` and `json` modules, each providing functions to help you work with these file formats.

### The CSV Module

**Reader Objects**

	>>> import csv
	>>> exampleFile = open('example.csv')
	>>> exampleReader = csv.reader(exampleFile)
	>>> exampleData = list(exampleReader)
	>>> exampleData
	[['4/5/2015 13:34', 'Apples', '73'], ['4/5/2015 3:41', 'Cherries', '85'],
	['4/6/2015 12:46', 'Pears', '14'], ['4/8/2015 8:59', 'Oranges', '52'],
	['4/10/2015 2:07', 'Apples', '152'], ['4/10/2015 18:10', 'Bananas', '23'],
	['4/10/2015 2:40', 'Strawberries', '98']]

**Reading Data from Reader Objects in a for Loop**

	>>> import csv
	>>> exampleFile = open('example.csv')
	>>> exampleReader = csv.reader(exampleFile)
	>>> for row in exampleReader:
			print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
	Row #1 ['4/5/2015 13:34', 'Apples', '73']
	Row #2 ['4/5/2015 3:41', 'Cherries', '85']
	Row #3 ['4/6/2015 12:46', 'Pears', '14']
	Row #4 ['4/8/2015 8:59', 'Oranges', '52']
	Row #5 ['4/10/2015 2:07', 'Apples', '152']
	Row #6 ['4/10/2015 18:10', 'Bananas', '23']
	Row #7 ['4/10/2015 2:40', 'Strawberries', '98']

**Writer Objects**

	>>> import csv
	>>> outputFile = open('output.csv', 'w', newline='')
	>>> outputWriter = csv.writer(outputFile)
	>>> outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
	21
	>>> outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
	32
	>>> outputWriter.writerow([1, 2, 3.141592, 4])
	16
	>>> outputFile.close()

On Windows, you'll also need to pass a blank string for the `open()` function's `newline` keyword argument. For technical reasons beyond the scope of this book, if you forget to set the newline argument, the rows in output.csv will be double-spaced.

**The delimiter and lineterminator Keyword Arguments**

	>>> import csv
	>>> csvFile = open('example.tsv', 'w', newline='')
	>>> csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
	>>> csvWriter.writerow(['apples', 'oranges', 'grapes'])
	24
	>>> csvWriter.writerow(['eggs', 'bacon', 'ham'])
	17
	>>> csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])
	32
	>>> csvFile.close()

### The JSON Module

**Reading JSON with the loads() Function**

	>>> stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,
	"felineIQ": null}'
	>>> import json
	>>> jsonDataAsPythonValue = json.loads(stringOfJsonData)
	>>> jsonDataAsPythonValue
	{'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}

**Writing JSON with the dumps() Function**

	>>> pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
	'felineIQ': None}
	>>> import json
	>>> stringOfJsonData = json.dumps(pythonValue)
	>>> stringOfJsonData
	'{"isCat": true, "felineIQ": null, "miceCaught": 0, "name": "Zophie" }'

## Time, Scheduling Tasks, and Launching Programs <a name="ch15">&nbsp;</a>

### The time module

**The time.time() Function**

The `time.time()` function returns the number of seconds since 12 AM on January 1, 1970, Coordinated Universal Time (UTC) as a float value.

	>>> import time
	>>> time.time()
	1425063955.068649

**The time.sleep() Function**

If you need to pause your program for a while, call the `time.sleep()` function and pass it the number of seconds you want your program to stay paused.

	>>> import time
	>>> for i in range(3):
			print('Tick')
			time.sleep(1)
			print('Tock')
			time.sleep(1)
	Tick
	Tock
	Tick
	Tock
	Tick
	Tock
	>>> time.sleep(5)

**Rounding Numbers**

	>>> import time
	>>> now = time.time()
	>>> now
	1425064108.017826
	>>> round(now, 2)
	1425064108.02
	>>> round(now, 4)
	1425064108.0178
	>>> round(now)
	1425064108

### The datetime Module

The `time` module is useful for getting a Unix epoch timestamp to work with. But if you want to display a date in a more convenient format, or do arithmetic with dates, you should use the `datetime` module.

	>>> import datetime
	>>> datetime.datetime.now()
	datetime.datetime(2015, 2, 27, 11, 10, 49, 55, 53)
	>>> dt = datetime.datetime(2015, 10, 21, 16, 29, 0)
	>>> dt.year, dt.month, dt.day
	(2015, 10, 21)
	>>> dt.hour, dt.minute, dt.second
	(16, 29, 0)

A Unix epoch timestamp can be converted to a datetime object with the `datetime.datetime.fromtimestamp()` function. The date and time of the `datetime` object will be converted for the local time zone.

	>>> datetime.datetime.fromtimestamp(1000000)
	datetime.datetime(1970, 1, 12, 5, 46, 40)
	>>> datetime.datetime.fromtimestamp(time.time())
	datetime.datetime(2015, 2, 27, 11, 13, 0, 604980)

`datetime` objects can be compared with each other using comparison operators to find out which one precedes the other. The later `datetime` object is the "greater" value.

	>>> halloween2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
	>>> newyears2016 = datetime.datetime(2016, 1, 1, 0, 0, 0)
	>>> oct31_2015 = datetime.datetime(2015, 10, 31, 0, 0, 0)
	>>> halloween2015 == oct31_2015
	True
	>>> halloween2015 > newyears2016
	False
	>>> newyears2016 > halloween2015
	True
	>>> newyears2016 != oct31_2015
	True

**The timedelta Data Type**

The datetime module also provides a timedelta data type, which represents a duration of time rather than a moment in time.

	>>> delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
	>>> delta.days, delta.seconds, delta.microseconds
	(11, 36548, 0)
	>>> delta.total_seconds()
	986948.0
	>>> str(delta)
	'11 days, 10:09:08'

**Pausing Until a Specific Date**

	import datetime
	import time
	halloween2016 = datetime.datetime(2016, 10, 31, 0, 0, 0)
	while datetime.datetime.now() < halloween2016:
		time.sleep(1)

**Converting datetime Objects into Strings**

The `strftime()` method uses directives similar to Python's string formatting.

`strftime` directive | Meaning
--- | ---
`%Y` | Year with century, as in '2014'
`%y` | Year without century, '00' to '99' (1970 to 2069)
`%m` | Month as a decimal number, '01' to '12'
`%B` | Full month name, as in 'November'
`%b` | Abbreviated month name, as in 'Nov'
`%d` | Day of the month, '01' to '31'
`%j` | Day of the year, '001' to '366'
`%w` | Day of the week, '0' (Sunday) to '6' (Saturday)
`%A` | Full weekday name, as in 'Monday'
`%a` | Abbreviated weekday name, as in 'Mon'
`%H` | Hour (24-hour clock), '00' to '23'
`%I` | Hour (12-hour clock), '01' to '12'
`%M` | Minute, '00' to '59'
`%S` | Second, '00' to '59'
`%p` | 'AM' or 'PM'
`%%` | Literal '%' character

Example:

	>>> oct21st = datetime.datetime(2015, 10, 21, 16, 29, 0)
	>>> oct21st.strftime('%Y/%m/%d %H:%M:%S')
	'2015/10/21 16:29:00'
	>>> oct21st.strftime('%I:%M %p')
	'04:29 PM'
	>>> oct21st.strftime("%B of '%y")
	"October of '15"

**Converting Strings into datetime Objects**

If you have a string of date information, such as '2015/10/21 16:29:00' or 'October 21, 2015', and need to convert it to a `datetime` object, use the `datetime.datetime.strptime()` function. The `strptime()` function is the inverse of the `strftime()` method. A custom format string using the same directives as `strftime()` must be passed so that `strptime()` knows how to parse and understand the string. (The p in the name of the `strptime()` function stands for parse.)

	>>> datetime.datetime.strptime('October 21, 2015', '%B %d, %Y')
	datetime.datetime(2015, 10, 21, 0, 0)
	>>> datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
	datetime.datetime(2015, 10, 21, 16, 29)
	>>> datetime.datetime.strptime("October of '15", "%B of '%y")
	datetime.datetime(2015, 10, 1, 0, 0)
	>>> datetime.datetime.strptime("November of '63", "%B of '%y")
	datetime.datetime(2063, 11, 1, 0, 0)

### Multithreading

To make a separate thread, you first need to make a `Thread` object by calling the `threading.Thread()` function.

	import threading, time
	print('Start of program.')
		
	def takeANap():
		time.sleep(5)
		print('Wake up!')
		
	threadObj = threading.Thread(target=takeANap)
	threadObj.start()
	
	print('End of program.')

**Passing Arguments to the Thread's Target Function**

Example:

	>>> print('Cats', 'Dogs', 'Frogs', sep=' & ')
	Cats & Dogs & Frogs

Pass arguments:

	>>> import threading
	>>> threadObj = threading.Thread(target=print, args=['Cats', 'Dogs', 'Frogs'],
	kwargs={'sep': ' & '})
	>>> threadObj.start()
	Cats & Dogs & Frogs

### Launching Other Programs from Python

Your Python program can start other programs on your computer with the `Popen()` function in the built-in `subprocess` module (The P in the name of the `Popen()` function stands for process).

Windows example:

	>>> import subprocess
	>>> subprocess.Popen('C:\\Windows\\System32\\calc.exe')
	<subprocess.Popen object at 0x0000000003055A58>

Ubuntu example:

	>>> import subprocess
	>>> subprocess.Popen('/usr/bin/gnome-calculator')
	<subprocess.Popen object at 0x7f2bcf93b20>

The return value is a Popen object, which has two useful methods: `poll()` and `wait()`. The `poll()` method will return None if the process is still running at the time `poll()` is called. If the program has terminated, it will return the process's integer exit code. An exit code is used to indicate whether the process terminated without errors (an exit code of 0) or whether an error caused the process to terminate (a nonzero exit code—generally 1, but it may vary depending on the program). The `wait()` method will block until the launched process has terminated. This is helpful if you want your program to pause until the user finishes with the other program. The return value of `wait()` is the process's integer exit code.

Windows example:

	>>> calcProc = subprocess.Popen('c:\\Windows\\System32\\calc.exe')
	>>> calcProc.poll() == None
	True
	>>> calcProc.wait()
	0
	>>> calcProc.poll()
	0

**Passing Command Line Arguments to Popen()**

To do so, you pass a list as the sole argument to `Popen()`. The first string in this list will be the executable filename of the program you want to launch and all the subsequent strings will be the command line arguments to pass to the program when it starts.

Windows example:

	>>> subprocess.Popen(['C:\\Windows\\notepad.exe', 'C:\\hello.txt'])
	<subprocess.Popen object at 0x00000000032DCEB8>

**Running Other Python Scripts**

On Windows:

	>>> subprocess.Popen(['C:\\python34\\python.exe', 'hello.py'])
	<subprocess.Popen object at 0x000000000331CF28>

**Opening Files with Default Applications**

Each operating system has a program that performs the equivalent of double-clicking a document file to open it. On Windows, this is the `start` program. On OS X, this is the `open` program. On Ubuntu Linux, this is the `see` program.

	>>> fileObj = open('hello.txt', 'w')
	>>> fileObj.write('Hello world!')
	12
	>>> fileObj.close()
	>>> import subprocess
	>>> subprocess.Popen(['open', 'hello.txt'])

On OS X, the open program is used for opening both document files and programs:

	>>> subprocess.Popen(['open', '/Applications/Calculator.app/'])
	<subprocess.Popen object at 0x10202ff98>

## Sending Email and Text Messages <a name="ch16">&nbsp;</a>

**IMPORTANT NOTE**

NEVER WRITE A PASSWORD DIRECTLY INTO YOUR CODE! INSTEAD, DESIGN YOUR PROGRAM TO ACCEPT THE PASSWORD RETURNED FROM `input()`.

### Sending Email (SMTP)

Example:

	>>> import smtplib
	>>> smtpObj = smtplib.SMTP('smtp.example.com', 587)
	>>> smtpObj.ehlo()
	(250, b'mx.example.com at your service, [216.172.148.131]\nSIZE 35882577\
	n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')
	>>> smtpObj.starttls()
	(220, b'2.0.0 Ready to start TLS')
	>>> smtpObj.login('bob@example.com', ' MY_SECRET_PASSWORD')
	(235, b'2.7.0 Accepted')
	>>> smtpObj.sendmail('bob@example.com', 'alice@example.com', 'Subject: So
	long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob')
	{}
	>>> smtpObj.quit()
	(221, b'2.0.0 closing connection ko10sm23097611pbd.52 - gsmtp')

**Connecting to an SMTP Server**

Email Providers and Their SMTP Servers:

Provider | SMTP server domain name
--- | ---
Gmail | smtp.gmail.com
Outlook.com/Hotmail.com | smtp-mail.outlook.com
Yahoo Mail | smtp.mail.yahoo.com
AT&T | smpt.mail.att.net (port 465)
Comcast | smtp.comcast.net
Verizon | smtp.verizon.net (port 465)

Example connection on port 587:

	>>> smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	>>> type(smtpObj)
	<class 'smtplib.SMTP'>

If the `smptlib.SMTP()` call is not successful, your SMTP server might not support TLS on port 587. In this case, you will need to create an SMTP object using `smtplib.SMTP_SSL()` and port 465 instead.

	>>> smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)

**Sending the SMTP "Hello" Message**

This greeting is the first step in SMTP and is important for establishing a connection to the server.

	>>> smtpObj.ehlo()
	(250, b'mx.google.com at your service, [216.172.148.131]\nSIZE 35882577\
	n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nCHUNKING')

If the first item in the returned tuple is the integer 250 (the code for "success" in SMTP), then the greeting succeeded.

**Starting TLS Encryption**

If you are connecting to port 587 on the SMTP server (that is, you're using TLS encryption), you'll need to call the `starttls()` method next. This required step enables encryption for your connection. If you are connecting to port 465 (using SSL), then encryption is already set up, and you should skip this step.

	>>> smtpObj.starttls()
	(220, b'2.0.0 Ready to start TLS')

The 220 in the return value tells you that the server is ready.

**Logging in to the SMTP Server**

	>>> smtpObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')
	(235, b'2.7.0 Accepted')

**Sending an Email**

	>>> smtpObj.sendmail(' my_email_address@gmail.com ', ' recipient@example.com ',
	'Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely,
	Bob')
	{}

The start of the email body string must begin with `'Subject: \n'` for the subject line of the email. The `'\n'` newline character separates the subject line from the main body of the email.

### Retrieving and Deleting Emails with IMAP

**Connecting to an IMAP Server**

Email Providers and Their IMAP Servers

Provider | IMAP server domain name
--- | ---
Gmail | imap.gmail.com
Outlook.com/Hotmail.com | imap-mail.outlook.com
Yahoo Mail | imap.mail.yahoo.com
AT&T | imap.mail.att.net
Comcast | imap.comcast.net
Verizon | incoming.verizon.net

Example:

	>>> import imapclient
	>>> imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)

**Logging in to the IMAP Server**

	>>> imapObj.login(' my_email_address@gmail.com ', ' MY_SECRET_PASSWORD ')

**Selecting a Folder**

	>>> import pprint
	>>> pprint.pprint(imapObj.list_folders())
	[(('\\HasNoChildren',), '/', 'Drafts'),
	 (('\\HasNoChildren',), '/', 'Filler'),
	 (('\\HasNoChildren',), '/', 'INBOX'),
	 (('\\HasNoChildren',), '/', 'Sent'),
	--snip-
	 (('\\HasNoChildren', '\\Flagged'), '/', '[Gmail]/Starred'),
	 (('\\HasNoChildren', '\\Trash'), '/', '[Gmail]/Trash')]

The three values in each of the tuples are:

* A tuple of the folder's flags. (Exactly what these flags represent is beyond the scope of this book, and you can safely ignore this field.)
* The delimiter used in the name string to separate parent folders and subfolders.
* The full name of the folder.

To select a folder to search through, pass the folder's name as a string into the `IMAPClient` object's `select_folder()` method:

	>>> imapObj.select_folder('INBOX', readonly=True)

If the selected folder does not exist, Python will raise an `imaplib.error` exception.

The `readonly=True` keyword argument prevents you from accidentally making changes or deletions to any of the emails in this folder during the subsequent method calls. Unless you want to delete emails, it's a good idea to always set `readonly` to `True`.

**Performing the Search**

With a folder selected, you can now search for emails with the `IMAPClient` object's `search()` method.

IMAP Search Keys:

Search key | Meaning
--- | ---
'ALL' | Returns all messages in the folder. You may run in to imaplib size limits if you request all the messages in a large folder. See Size Limits.
'BEFORE date', 'ON date', 'SINCE date' | These three search keys return, respectively, messages that were received by the IMAP server before, on, or after the given date. The date must be formatted like 05-Jul-2015. Also, while 'SINCE 05-Jul-2015' will match messages on and after July 5, 'BEFORE 05-Jul-2015' will match only messages before July 5 but not on July 5 itself.
'SUBJECT string', 'BODY string', 'TEXT string' | Returns messages where string is found in the subject, body, or either, respectively. If string has spaces in it, then enclose it with double quotes: 'TEXT "search with spaces"'.
'FROM string', 'TO string', 'CC string', 'BCC string' | Returns all messages where string is found in the "from" emailaddress, "to" addresses, "cc" (carbon copy) addresses, or "bcc" (blind carbon copy) addresses, respectively. If there are multiple email addresses in string, then separate them with spaces and enclose them all with double quotes: 'CC "firstcc@example.com secondcc@example.com"'.
'SEEN', 'UNSEEN' | Returns all messages with and without the *\Seen* flag, respectively. An email obtains the *\Seen* flag if it has been accessed with a `fetch()` method call or if it is clicked when you're checking your email in an email program or web browser. It's more common to say the email has been "read" rather than "seen," but they mean the same thing.
'ANSWERED', 'UNANSWERED' | Returns all messages with and without the *\Answered* flag, respectively. A message obtains the *\Answered* flag when it is replied to.
'DELETED', 'UNDELETED' | Returns all messages with and without the *\Deleted* flag, respectively. Email messages deleted with the `delete_messages()` method are given the *\Deleted* flag but are not permanently deleted until the `expunge()` method is called. Note that some email providers, such as Gmail, automatically expunge emails.
'DRAFT', 'UNDRAFT' | Returns all messages with and without the *\Draft* flag, respectively. Draft messages are usually kept in a separate *Drafts* folder rather than in the INBOX folder.
'FLAGGED', 'UNFLAGGED' | Returns all messages with and without the *\Flagged* flag, respectively. This flag is usually used to mark email messages as "Important" or "Urgent."
'LARGER N', 'SMALLER N' | Returns all messages larger or smaller than N bytes, respectively.
'NOT search-key' | Returns the messages that search-key would not have returned.
'OR search-key1 search-key2' | Returns the messages that match either the first or second search-key.

Note that some IMAP servers may have slightly different implementations for how they handle their flags and search keys. It may require some experimentation in the interactive shell to see exactly how they behave.

You can pass multiple IMAP search key strings in the list argument to the `search()` method.

Search examples:

* `imapObj.search(['ALL'])`. Returns every message in the currently selected folder.
* `imapObj.search(['ON 05-Jul-2015'])`. Returns every message sent on July 5, 2015.
* `imapObj.search(['SINCE 01-Jan-2015', 'BEFORE 01-Feb-2015', 'UNSEEN'])`. Returns every message sent in January 2015 that is unread. (Note that this means on and after January 1 and up to but not including February 1.)
* `imapObj.search(['SINCE 01-Jan-2015', 'FROM alice@example.com'])`. Returns every message from alice@example.com sent since the start of 2015.
* `imapObj.search(['SINCE 01-Jan-2015', 'NOT FROM alice@example.com'])`. Returns every message sent from everyone except alice@example.com since the start of 2015.
* `imapObj.search(['OR FROM alice@example.com FROM bob@example.com'])`. Returns every message ever sent from alice@example.com or bob@example.com.
* `imapObj.search(['FROM alice@example.com', 'FROM bob@example.com'])`. Trick example! This search will never return any messages, because messages must match all search keywords. Since there can be only one “from” address, it is impossible for a message to be from both alice@example.com and bob@example.com.

The `search()` method returns unique IDs:

	>>> UIDs = imapObj.search(['SINCE 05-Jul-2015'])
	>>> UIDs
	[40032, 40033, 40034, 40035, 40036, 40037, 40038, 40039, 40040, 40041]

**Size Limits**

If your search matches a large number of email messages, Python might raise an exception that says `imaplib.error: got more than 10000 bytes`. When this happens, you will have to disconnect and reconnect to the IMAP server and try again. You can change this limit from 10,000 bytes to 10,000,000 bytes by running this code:

	>>> import imaplib
	>>> imaplib._MAXLINE = 10000000

You may want to make these two lines part of every IMAP program you write.

**Fetching an Email and Marking It As Read**

	>>> rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
	>>> import pprint
	>>> pprint.pprint(rawMessages)
	{40040: {'BODY[]': 'Delivered-To: my_email_address@gmail.com\r\n'
	                   'Received: by 10.76.71.167 with SMTP id '
	--snip--
	                   '\r\n'
	                   '------=_Part_6000970_707736290.1404819487066--\r\n',
	         'SEQ': 5430}}

When you selected a folder to search through, you called `select_folder()` with the `readonly=True` keyword argument. Doing this will prevent you from accidentally deleting an email—but it also means that emails will not get marked as read if you fetch them with the `fetch()` method. If you do want emails to be marked as read when you fetch them, you will need to pass `readonly=False` to `select_folder()`. If the selected folder is already in readonly mode, you can reselect the current folder with another call to `select_folder()`, this time with the `readonly=False` keyword argument:

	>>> imapObj.select_folder('INBOX', readonly=False)

**Getting Email Addresses from a Raw Message**

The pyzmail module parses these raw messages and returns them as PyzMessage objects, which make the subject, body, `To` field, `From` field, and other sections of the email easily accessible to your Python code.

	>>> import pyzmail
	>>> message = pyzmail.PyzMessage.factory(rawMessages[40041]['BODY[]'])
	>>> message.get_subject()
	'Hello!'
	>>> message.get_addresses('from')
	[('Edward Snowden', 'esnowden@nsa.gov')]
	>>> message.get_addresses('to')
	[(Jane Doe', 'my_email_address@gmail.com')]
	>>> message.get_addresses('cc')
	[]
	>>> message.get_addresses('bcc')
	[]

**Getting the Body from a Raw Message**

	>>> message.text_part != None
	True
	>>> message.text_part.get_payload().decode(message.text_part.charset)
	'So long, and thanks for all the fish!\r\n\r\n-Al\r\n'
	>>> message.html_part != None
	True
	>>> message.html_part.get_payload().decode(message.html_part.charset)
	'<div dir="ltr"><div>So long, and thanks for all the fish!<br><br></div>-Al
	<br></div>\r\n'

**Deleting Emails**

	>>> imapObj.select_folder('INBOX', readonly=False)
	>>> UIDs = imapObj.search(['ON 09-Jul-2015'])
	>>> UIDs
	[40066]
	>>> imapObj.delete_messages(UIDs)
	{40066: ('\\Seen', '\\Deleted')}
	>>> imapObj.expunge()
	('Success', [(5452, 'EXISTS')])

**Disconnecting from the IMAP Server**

	>>> imapObj.logout()``

### Sending Text Messages with Twilio

Twilio is an SMS gateway service, which means it's a service that allows you to send text messages from your programs.

## Manipulating Images <a name="ch17">&nbsp;</a>

### Manipulating images with Pillow

Pillow is a third-party Python module for interacting with image files. The module has several functions that make it easy to crop, resize, and edit the content of an image. With the power to manipulate images the same way you would with software such as Microsoft Paint or Adobe Photoshop, Python can automatically edit hundreds or thousands of images with ease.

To install Pillow, run:

	pip3 install pillow

The module name of Pillow is PIL to make it backward compatible with an older module called Python Imaging Library, which is why you must run `from PIL import Image` instead of `from Pillow import Image`:

	>>> from PIL import Image
	>>> catIm = Image.open('zophie.png')

**Working with the Image Data Type**

	>>> from PIL import Image
	>>> catIm = Image.open('zophie.png')
	>>> catIm.size
	(816, 1088)
	>>> width, height = catIm.size
	>>> width
	816
	>>> height
	1088
	>>> catIm.filename
	'zophie.png'
	>>> catIm.format
	'PNG'
	>>> catIm.format_description
	'Portable network graphics'
	>>> catIm.save('zophie.jpg')

Pillow also provides the `Image.new()` function, which returns an Image object—much like `Image.open()`, except the image will be blank. The arguments to `Image.new()` are as follows:

* The string 'RGBA', which sets the color mode to RGBA.
* The size, as a two-integer tuple of the new image's width and height.
* The background color that the image should start with, as a four-integer tuple of an RGBA value. You can use the return value of the `ImageColor.getcolor()` function for this argument. Alternatively, `Image.new()` also supports just passing the string of the standard color name.

Example:

	>>> from PIL import Image
	>>> im = Image.new('RGBA', (100, 200), 'purple')
	>>> im.save('purpleImage.png')
	>>> im2 = Image.new('RGBA', (20, 20))
	>>> im2.save('transparentImage.png')

**Cropping Images**

	>>> croppedIm = catIm.crop((335, 345, 565, 560))
	>>> croppedIm.save('cropped.png')

**Copying and Pasting Images onto Other Images**

Copy:

	>>> catIm = Image.open('zophie.png')
	>>> catCopyIm = catIm.copy()

Paste:

	>>> faceIm = catIm.crop((335, 345, 565, 560))
	>>> faceIm.size
	(230, 215)
	>>> catCopyIm.paste(faceIm, (0, 0))
	>>> catCopyIm.paste(faceIm, (400, 500))
	>>> catCopyIm.save('pasted.png')

**Pasting Transparent Pixels**

If the image you want to paste has transparent pixels, pass the Image object as the third argument so that a solid rectangle isn't pasted. This third argument is the "mask" Image object.

**Resizing an Image**

	>>> width, height = catIm.size
	>>> quartersizedIm = catIm.resize((int(width / 2), int(height / 2)))
	>>> quartersizedIm.save('quartersized.png')
	>>> svelteIm = catIm.resize((width, height + 300))
	>>> svelteIm.save('svelte.png')

**Rotating and Flipping Images**

	>>> catIm.rotate(90).save('rotated90.png')
	>>> catIm.rotate(180).save('rotated180.png')
	>>> catIm.rotate(270).save('rotated270.png')

The `rotate()` method has an optional expand keyword argument that can be set to True to enlarge the dimensions of the image to fit the entire rotated new image.

	>>> catIm.rotate(6).save('rotated6.png')
	>>> catIm.rotate(6, expand=True).save('rotated6_expanded.png')

You can also get a "mirror flip" of an image with the `transpose()` method. You must pass either `Image.FLIP_LEFT_RIGHT` or `Image.FLIP_TOP_BOTTOM` to the `transpose()` method.

	>>> catIm.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
	>>> catIm.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')

**Changing Individual Pixels**

	>>> im = Image.new('RGBA', (100, 100))
	>>> im.getpixel((0, 0))
	(0, 0, 0, 0)
	>>> for x in range(100):
		for y in range(50):
			im.putpixel((x, y), (210, 210, 210))
	>>> from PIL import ImageColor
	>>> for x in range(100):
			for y in range(50, 100):
				im.putpixel((x, y), ImageColor.getcolor('darkgray', 'RGBA'))
	>>> im.getpixel((0, 0))
	(210, 210, 210, 255)
	>>> im.getpixel((0, 50))
	(169, 169, 169, 255)
	>>> im.save('putPixel.png')

### Drawing on Images

	>>> from PIL import Image, ImageDraw
	>>> im = Image.new('RGBA', (200, 200), 'white')
	>>> draw = ImageDraw.Draw(im)

**Drawing Shapes**

	>>> from PIL import Image, ImageDraw
	>>> im = Image.new('RGBA', (200, 200), 'white')
	>>> draw = ImageDraw.Draw(im)
	>>> draw.line([(0, 0), (199, 0), (199, 199), (0, 199), (0, 0)], fill='black')
	>>> draw.rectangle((20, 30, 60, 60), fill='blue')
	>>> draw.ellipse((120, 30, 160, 60), fill='red')
	>>> draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)),
	fill='brown')
	>>> for i in range(100, 200, 10):
			draw.line([(i, 0), (200, i - 100)], fill='green')
	>>> im.save('drawing.png')

**Drawing Text**

	>>> from PIL import Image, ImageDraw, ImageFont
	>>> import os
	>>> im = Image.new('RGBA', (200, 200), 'white')
	>>> draw = ImageDraw.Draw(im)
	>>> draw.text((20, 150), 'Hello', fill='purple')
	>>> fontsFolder = 'FONT_FOLDER' # e.g. 'Library/Fonts'
	>>> arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32)
	>>> draw.text((100, 150), 'Howdy', fill='gray', font=arialFont)
	>>> im.save('text.png')

## Controlling the Keyboard and Mouse with GUI Automation <a name="ch18">&nbsp;</a>

### Installing the pyautogui Module

The pyautogui module can send virtual keypresses and mouse clicks to Windows, OS X, and Linux. Depending on which operating system you're using, you may have to install some other modules (called dependencies) before you can install PyAutoGUI.

* On Windows, there are no other modules to install.
* On OS X, run `sudo pip3 install pyobjc-framework-Quartz`, `sudo pip3 install pyobjc-core`, and then `sudo pip3 install pyobjc`.
* On Linux, run `sudo pip3 install python3-xlib`, `sudo apt-get install scrot`, `sudo apt-get install python3-tk`, and `sudo apt-get install python3-dev`. (Scrot is a screenshot program that PyAutoGUI uses.)

After these dependencies are installed, run `pip install pyautogui` (or `pip3` on OS X and Linux) to install PyAutoGUI.

**INSTALLATION NOTE**

`pyautogui` cannot be installed with Python 3.5 due to dependency problems on Mac OS X Yosemite but works for Python 3.4.3.

On Yosemite, you can install Python 3.4.3 with `brew` from raw formula on github:

	brew install https://raw.githubusercontent.com/Homebrew/homebrew/7d8b04c417d16f320680c58d0eb335cafd881849/Library/Formula/python3.rb

**Pauses and Fail-Safes**

You can tell your script to wait after every function call, giving you a short window to take control of the mouse and keyboard if something goes wrong. To do this, set the `pyautogui.PAUSE` variable to the number of seconds you want it to pause.

PyAutoGUI also has a fail-safe feature. Moving the mouse cursor to the upper-left corner of the screen will cause PyAutoGUI to raise the `pyautogui.FailSafeException` exception. Your program can either handle this exception with `try` and `except` statements or let the exception crash your program.

	>>> import pyautogui
	>>> pyautogui.PAUSE = 1
	>>> pyautogui.FAILSAFE = True

### Controlling Mouse Movement

The `pyautogui.size()` function returns a two-integer tuple of the screen's width and height in pixels.

	>>> import pyautogui
	>>> pyautogui.size()
	(1920, 1080)
	>>> width, height = pyautogui.size()

**Moving the Mouse**

The `pyautogui.moveTo()` function will instantly move the mouse cursor to a specified position on the screen. Integer values for the x- and y-coordinates make up the function's first and second arguments, respectively. An optional `duration` integer or float keyword argument specifies the number of seconds it should take to move the mouse to the destination.

	>>> import pyautogui
	>>> for i in range(10):
			pyautogui.moveTo(100, 100, duration=0.25)
			pyautogui.moveTo(200, 100, duration=0.25)
			pyautogui.moveTo(200, 200, duration=0.25)
			pyautogui.moveTo(100, 200, duration=0.25)

The `pyautogui.moveRel()` function moves the mouse cursor relative to its current position.

	>>> import pyautogui
	>>> for i in range(10):
			pyautogui.moveRel(100, 0, duration=0.25)
			pyautogui.moveRel(0, 100, duration=0.25)
			pyautogui.moveRel(-100, 0, duration=0.25)
			pyautogui.moveRel(0, -100, duration=0.25)

**Getting the Mouse Position**

	>>> pyautogui.position()
	(311, 622)
	>>> pyautogui.position()
	(377, 481)
	>>> pyautogui.position()
	(1536, 637)

### Controlling Mouse Interaction

**Clicking the Mouse**

To send a virtual mouse click to your computer, call the `pyautogui.click()` method. By default, this click uses the left mouse button and takes place wherever the mouse cursor is currently located. You can pass x- and y-coordinates of the click as optional first and second arguments if you want it to take place somewhere other than the mouse's current position.

	>>> import pyautogui
	>>> pyautogui.click(10, 5)

**Scrolling the Mouse**

The final PyAutoGUI mouse function is `scroll()`, which you pass an integer argument for how many units you want to scroll the mouse up or down. The size of a unit varies for each operating system and application. Passing a positive integer scrolls up, and passing a negative integer scrolls down.

	>>> import time, pyautogui
	>>> time.sleep(5); pyautogui.scroll(100)

### Working with the Screen

PyAutoGUI has screenshot features that can create an image file based on the current contents of the screen. These functions can also return a Pillow Image object of the current screen's appearance.

On Linux computers, the `scrot` program needs to be installed to use the screenshot functions in PyAutoGUI. In a Terminal window, run `sudo apt-get install scrot` to install this program.

**Getting a Screenshot**

	>>> import pyautogui
	>>> im = pyautogui.screenshot()

The `im` variable will contain the `Image` object of the screenshot. You can now call methods on the `Image` object in the im variable, just like any other `Image` object.

**Analyzing the Screenshot**

Before calling the `click()` method, you could take a screenshot and look at the pixel where the script is about to click. If it's not the same gray as the gray button, then your program knows something is wrong.

PyAutoGUI's `pixelMatchesColor()` function will return True if the pixel at the given x- and y-coordinates on the screen matches the given color.

	>>> import pyautogui
	>>> im = pyautogui.screenshot()
	>>> im.getpixel((50, 200))
	(130, 135, 144)
	>>> pyautogui.pixelMatchesColor(50, 200, (130, 135, 144))
	True
	>>> pyautogui.pixelMatchesColor(50, 200, (255, 135, 144))
	False

### Image Recognition

Give PyAutoGUI an image of what you want to click and let it figure out the coordinates.

	>>> import pyautogui
	>>> pyautogui.locateOnScreen('submit.png')
	(643, 745, 70, 29)

The four-integer tuple that `locateOnScreen()` returns has the x-coordinate of the left edge, the y-coordinate of the top edge, the width, and the height for the first place on the screen the image was found.

If the image cannot be found on the screen, `locateOnScreen()` will return None. Note that the image on the screen must match the provided image perfectly in order to be recognized. If the image is even a pixel off, `locateOnScreen()` will return `None`.

If the image can be found in several places on the screen, `locateAllOnScreen()` will return a `Generator` object, which can be passed to `list()` to return a list of four-integer tuples.

	>>> list(pyautogui.locateAllOnScreen('submit.png'))
	[(643, 745, 70, 29), (1007, 801, 70, 29)]

Once you have the four-integer tuple for the area on the screen where your image was found, you can click the center of this area by passing the tuple to the `center()` function to return x- and y-coordinates of the area’s center.

	>>> pyautogui.locateOnScreen('submit.png')
	(643, 745, 70, 29)
	>>> pyautogui.center((643, 745, 70, 29))
	(678, 759)
	>>> pyautogui.click((678, 759))

### Controlling the Keyboard

**Sending a String from the Keyboard**

	>>> pyautogui.click(100, 100); pyautogui.typewrite('Hello world!')

By default, the `typewrite()` function will type the full string instantly. However, you can pass an optional second argument to add a short pause between each character.

	>>> pyautogui.click(100, 100); pyautogui.typewrite('Hello world!', 0.25)

**Key Names**

Instead of a single string argument, a list of keyboard key strings can be passed to `typewrite()`.

	>>> pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])


