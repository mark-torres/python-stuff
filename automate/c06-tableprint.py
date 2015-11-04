#! /usr/local/bin/python3

def printTable(tableData):
	"""
	HINT:
	Your code will first have to find the longest string in each of the inner lists
	so that the whole column can be wide enough to fit all the strings. You can store
	the maximum width of each column as a list of integers The printTable() function
	can begin with colWidths = [0] * len(tableData), which will create a list containing
	the same number of 0 values as the number of inner lists in tableData. That way,
	colWidths[0] can store the width of the longest string in tableData[0], colWidths[1]
	can store the width of the longest string in tableData[1], and so on. You can then
	find the largest value in the colWidths list to find out what integer width to pass
	to the rjust() string method.
	"""
	colWidths = [0] * len(tableData)
	# get max widths
	for i in range(0, len(tableData)):
		maxWidth = 0
		for j in range(0, len(tableData[i])):
			if len(tableData[i][j]) > maxWidth:
				maxWidth = len(tableData[i][j])
		colWidths[i] = maxWidth
	# print('max widths:', colWidths)
	# print rows
	for i in range(0, len(tableData[0])):
		for j in range(0, len(tableData)):
			# print(j, i, end = ' ', sep = ',')
			print( tableData[j][i].rjust(colWidths[j]), end = ' ')
		print('')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
	['Alice', 'Bob', 'Carol', 'David'],
	['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)