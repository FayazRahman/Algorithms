def show_path(grid):
	for idx, row in enumerate(grid):
		if 'A' in row:
			A = [idx, row.index('A')]
		if 'B' in row:
			B = [idx, row.index('B')]
	drows = B[0] - A[0]
	dcols = B[1] - A[1]

	return ' '.join([
		'UP\n' * abs(drows) if drows < 0 else 'DOWN\n' * drows, 'LEFT\n' * abs(dcols) if dcols < 0 else 'RIGHT\n' * dcols])

nrows = int(raw_input("No. of rows:"))
	
grid = []
print "Make a grid. '-' for empty spaces, 'A' for point A and 'B' for point B"
for i in xrange(0, nrows):
	grid.append(raw_input().strip())

print ""
print "Your grid looks like this:"
print ""

for row in list(grid):
	print ' '.join(row)

print ""
print "Path from A to B:"
print ""
print show_path(grid)