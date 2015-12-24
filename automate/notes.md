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

A multiline string in Python begins and ends with either three single quotes or three double quotes. Any quotes, tabs, or newlines in between the "triple quotes" are considered part of the string. Python’s indentation rules for blocks do not apply to lines inside a multiline string.

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

The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard.

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

A Regex object’s `search()` method searches the string it is passed for any matches to the regex. The `search()` method will return `None` if the regex pattern is not found in the string. If the pattern is found, the `search()` method returns a `Match` object. Match objects have a `group()` method that will return the actual matched text from the searched string.

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

Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible. The non-greedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket followed by a question mark.

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

Normally, regular expressions match text with the exact casing you specify. But sometimes you care only about matching the letters without worrying whether they’re uppercase or lowercase. To make your regex case-insensitive, you can pass `re.IGNORECASE` or `re.I` as a second argument to `re.compile()`.

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

If you want a regular expression that’s case-insensitive and includes newlines to match the dot character, you would form your `re.compile()` call like this:

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

Be careful when using these functions in your programs! It’s often a good idea to first run your program with these calls commented out and with print() calls added to show the files that would be deleted.

	import os
	for filename in os.listdir():
		if filename.endswith('.rxt'):
			#os.unlink(filename)
			print('File to delete: '+filename)

**Safe Deletes with the send2trash Module**

Since Python’s built-in `shutil.rmtree()` function irreversibly deletes files and folders, it can be dangerous to use. A much better way to delete files and folders is with the third-party `send2trash` module. You can install this module by running `pip install send2trash` from a Terminal window.

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

An assertion is a sanity check to make sure your code isn’t doing something obviously wrong. These sanity checks are performed by assert statements. If the sanity check fails, then an AssertionError exception is raised. In code, an assert statement consists of the following:

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
`WARNING` | `logging.warning()` | Used to indicate a potential problem that doesn’t prevent the program from working but might do so in the future.
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

After you’ve debugged your program, you probably don’t want all these log messages cluttering the screen. The `logging.disable()` function disables these so that you don’t have to go into your program and remove all the logging calls by hand. You simply pass `logging.disable()` a logging level, and it will suppress all log messages at that level or lower. So if you want to disable logging entirely, just add `logging.disable(logging.CRITICAL)` to your program.

Since `logging.disable()` will disable all messages after it, you will probably want to add it near the `import logging` line of code in your program. This way, you can easily find it to comment out or uncomment that call to enable or disable logging messages as needed.

**Logging to a File**

Instead of displaying the log messages to the screen, you can write them to a text file. The `logging.basicConfig()` function takes a filename keyword argument, like so:

	import logging
	logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

The log messages will be saved to `myProgramLog.txt`. 

## Web Scraping <a name="ch11">&nbsp;</a>

## Working with Excel Spreadsheets <a name="ch12">&nbsp;</a>

## Working with PDF and Word Documents <a name="ch13">&nbsp;</a>

## Working with CSV Files and JSON Data <a name="ch14">&nbsp;</a>

## Time, Scheduling Tasks, and Launching Programs <a name="ch15">&nbsp;</a>

## Sending Email and Text Messages <a name="ch16">&nbsp;</a>

## Manipulating Images <a name="ch17">&nbsp;</a>

## Controlling the Keyboard and Mouse with GUI Automation <a name="ch18">&nbsp;</a>
