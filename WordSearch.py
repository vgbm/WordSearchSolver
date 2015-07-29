import string

def readPuzzle(fileName):
	with open(fileName) as File:
		lines = File.readlines()
		
	return [list(string.replace(line," ","")) for line in lines]
	
# 0 1 2
# 3 4 5
# 6 7 8
def moveDirection(point, direction):
	newY,newX=point[0],point[1]
	if direction in [0,3,6]:
		newY -= 1	
	elif direction in [2,5,8]:
		newY += 1

	if direction in [0,1,2]:
		newX -= 1
	elif direction in [6,7,8]:
		newX += 1
	return (newY,newX)

def readWord(grid, point, direction, length):
	word = []
	for i in range(length):
		if point[0]<0 or point[1]<0 or point[0] >= len(grid[0]) or point[1] >= len(grid):
			return None

		word.append(grid[point[1]][point[0]])
		point = moveDirection(point, direction)

	return "".join(word)

grid = readPuzzle('puzzle.txt')
wordList = raw_input("Word list: ").split()
dirMap = {0:"NW",1:"N",2:"NW",3:"W",5:"E",6:"SW",7:"S",8:"SE"}

for word in wordList:
	for y in range(len(grid[0])):
		for x in range(len(grid)):
			for direction in range(9):
				if word == readWord(grid, (x,y), direction, len(word)):
					print word+"\t\t("+str(x+1)+","+str(y+1)+")\t\t"+dirMap[direction]
