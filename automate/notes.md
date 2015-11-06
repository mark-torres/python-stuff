
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

This value-without-a-value can be helpful when you need to store something that won’t be confused for a real value in a variable.

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

**Getting a list’s length with `len()`**

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

**The `copy` module’s `copy()` and `deepcopy()` functions**

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

## Manipulating Strings <a name="ch06">&nbsp;</a>

## Pattern Matching with Regular Expressions <a name="ch07">&nbsp;</a>

## Reading and Writing Files <a name="ch08">&nbsp;</a>

## Organizing Files <a name="ch09">&nbsp;</a>

## Debugging <a name="ch10">&nbsp;</a>

## Web Scraping <a name="ch11">&nbsp;</a>

## Working with Excel Spreadsheets <a name="ch12">&nbsp;</a>

## Working with PDF and Word Documents <a name="ch13">&nbsp;</a>

## Working with CSV Files and JSON Data <a name="ch14">&nbsp;</a>

## Time, Scheduling Tasks, and Launching Programs <a name="ch15">&nbsp;</a>

## Sending Email and Text Messages <a name="ch16">&nbsp;</a>

## Manipulating Images <a name="ch17">&nbsp;</a>

## Controlling the Keyboard and Mouse with GUI Automation <a name="ch18">&nbsp;</a>
