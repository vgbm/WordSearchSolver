import multiprocessing
import string
import time

def readPuzzle(fileName):
	with open(fileName) as File:
		lines = File.readlines()
	
	lines = (filter(lambda line: line!="\n",lines))
	return [list(string.replace(line," ","")) for line in lines]
	
def readWordList(fileName):
	with open(fileName) as File:
		lines = File.readlines()
	
	lines = (filter(lambda line: line!="\n",lines))
	lines = [line.split() for line in lines]
	
	return [word for line in lines for word in line] #flattens array
      
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

#returns if found, but results never utilized
#breaks at first occurance; remove return to continue search
def findWord(grid, word, dirMap):
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			for direction in range(9):
				if direction!= 4 and word == readWord(grid, (x,y), direction, len(word)):
					print "{}\t\t({},{})\t\t{}".format(word,x+1,y+1,dirMap[direction])
					return True
	return False
	        
grid = readPuzzle('puzzle.txt')
wordList = readWordList('word_list.txt')
dirMap = {0:"NW",1:"N",2:"NW",3:"W",5:"E",6:"SW",7:"S",8:"SE"}

#processed in parallel
for word in wordList:
	p = multiprocessing.Process(target=findWord, args=(grid,word,dirMap))
	p.start()
