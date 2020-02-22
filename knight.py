

def move(p, i):
	x = ord(p[0])
	y = int(p[1])
	dx = ((i + 1) % 2) + 1  # 2, 1, 2, 1...
	dy = (i % 2) + 1  # 1, 2, 1, 2...
	quadrant_x = 1 if i < 2 or i > 5 else -1  # + - - +
	quadrant_y = 1 if i < 4 else -1  # + + - -
	x += dx * quadrant_x
	y += dy * quadrant_y
	if chr(x) > 'h' or chr(x) < 'a' or y > 8 or y < 1:
		return p  # Out of the board
	return chr(x) + str(y)


def possible_moves(p):
	moves = []
	for i in range(0, 8):
		d = move(p, i)
		if d == p: continue  # Out of the board
		moves.append(d)
	return moves
	
	
def one_move(p1, p2, depth, level=1):
	moves = possible_moves(p1)
	for m in moves:
		if m == p2: return True  # This is the destination
	if depth == level: return False  # Not possible in one move
	for m in moves:  # Going a level deeper
		if one_move(m, p2, depth, level + 1): return True
	return False
	

def knight(p1, p2):
	if p1 == p2:
		return 0  # Minimum possible steps: This is the destination	
	else:		
		for depth in range(1, 7):
			if one_move(p1, p2, depth): return depth
		return 6  # Maximum possible steps


def almost_knight(p1, p2):
	dx = abs(ord(p1[0]) - ord(p2[0]))
	dy = abs(int(p1[1]) - int(p2[1]))
	d = dx + dy
	if d % 2 == 1:  # Odd distances
		if d == 3 and d != dx and d != dy:
			return 1  # Distance of 3 but not in the same axis
		elif d < 7:
			return 3  # Average odd distances
		elif d == 7 and abs(dx - dy) < 7:
			return 3  # Non vertical/horizontal moves
		elif d == 9 and abs(dx - dy) < 5:
			return 3  # Not close to vertical/horizontal moves
		else:  # vertical/horizontal moves > 7 and d > 9
			return 5  # Longest odd distances
	else:  # Even distances
		if d == 2:
			return 2  # Shorstest even distances
		elif d == 4:
			if abs(dx - dy) > 0:
				return 2  # Less than 45? moves
			else:
				return 4  # Diagonal moves (45?)
		elif d == 6:
			if abs(dx - dy) < 3:
				return 2  # Almost diagonal moves
			else:
				return 4  # Almost vertical/horizontal moves
		else:  # d > 6
			return 4  # Longest even distances			


def distances(p):
	print(3*' ', end='')
	for x in range(97, 105):
		print(chr(x), end=' ')
	print('\n')
	
	for y in range(8, 0, -1):
		print(y, end='  ')
		for x in range(97, 105):
			dx = abs(ord(p[0]) - x)
			dy = abs(int(p[1]) - y)
			d = dx + dy
			if d % 2 == 0:
				print(d, end=' ')
			else:
				print(' ', end=' ')
		print()
			

print('Knight distance: ' + str(knight('g1', 'h3')))
#distances('g2')