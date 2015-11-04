#! python3

# comma list
def commalist(values):
	"""add comma values and 'and' for the last value"""
	if len(values) == 0:
		print("List is empty")
	elif len(values) == 1:
		print(str(values[0]))
	elif len(values) == 2:
		print(str(values[0]),str(values[1]), sep = ' and ')
	else:
		for val in values[0:-2]:
			print(str(val), end = ', ')
		print(str(values[-2]),str(values[-1]), sep = ' and ')

spam = [3]
commalist(spam)

spam = [4,8]
commalist(spam)

spam = [12,34,675]
commalist(spam)

spam = range(5, 60, 5)
commalist(spam)

