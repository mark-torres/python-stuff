#! python3

# chars grid
grid = [['.', '.', '.', '.', '.', '.'],
	['.', 'O', 'O', '.', '.', '.'],
	['O', 'O', 'O', 'O', '.', '.'],
	['O', 'O', 'O', 'O', 'O', '.'],
	['.', 'O', 'O', 'O', 'O', 'O'],
	['O', 'O', 'O', 'O', 'O', '.'],
	['O', 'O', 'O', 'O', '.', '.'],
	['.', 'O', 'O', '.', '.', '.'],
	['.', '.', '.', '.', '.', '.']]

picwidth = len(grid)
picheight = len(grid[0])

for ph in range(0, picheight):
	for pw in range(0, picwidth):
		print( grid[pw][ph], end='' )
	print('')
