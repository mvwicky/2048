import sfml as sf 
import random
import math
# Grid Format
#  0  1  2  3
#  4  5  6  7
#  8  9 10 11
# 12 13 14 15

def reSeed():
	random.seed()
	sVec=[]
	sVec.append(random.randint(0,15))
	sVec.append(random.randint(0,15))
	while (sVec[0]==sVec[1]):
		sVec=[random.randint(0,15),random.randint(0,15)]
	return sVec

def newBlock(filled):
	random.seed()
	nBlock=random.randint(0,15)
	while (nBlock in filled):
		nBlock=random.randint(0,15)
	return nBlock


def main():
	random.seed()

	score=0

	grid=[] # Contains the blank blocks
	filledBlocks=[] # Contains the filled blocks
	allPositions=[]

	numBlocks=16 # number of blocks 

	initialFilled=reSeed()
	curFilled=initialFilled

	pad=20 
	blockSize=150

	mFactor=1

	boardSide=(5*pad)+(4*blockSize)

	boardColor=sf.Color(210,210,210,255)
	blockColor=sf.Color(135,135,135,255)
	filledColor=sf.Color(0,200,200,255)
	
	colorValues={2: sf.Color(110, 167, 104, 255),
				 4: sf.Color(52, 167, 170, 255), 
				 8: sf.Color(13, 126, 143, 255), 
				 16: sf.Color(168, 34, 162, 255),
				 32: sf.Color(98, 98, 141, 255), 
				 64: sf.Color(243, 42, 201, 255), 
				 128: sf.Color(239, 0, 182, 255), 
				 256: sf.Color(141, 194, 7, 255),
				 512: sf.Color(246, 161, 181, 255),  
				 1024: sf.Color(95, 208, 191, 255),
				 2048: sf.Color(213, 75, 58, 255),
				 4096: sf.Color(99, 195, 181, 255)}
	curX=pad
	curY=pad

	for i in range(numBlocks): # Create Blank Blocks
		grid.append(sf.RectangleShape())
		grid[i].origin=(0,0)
		grid[i].size=(blockSize,blockSize)
		grid[i].position=(curX,curY)
		allPositions.append(sf.Vector2(curX,curY))
		grid[i].fill_color=blockColor
		grid[i].outline_thickness=0
		if i in (3,7,11,15): # if at the end of a row
			curX=pad
			curY+=blockSize+pad
		elif i not in (3,7,11,15):
			curX+=blockSize+pad		

	curX=pad
	curY=pad

	for i in range(numBlocks): # Create Filled Blocks
		filledBlocks.append(sf.RectangleShape())
		filledBlocks[i].origin=(0,0)
		filledBlocks[i].size=(blockSize,blockSize)
		filledBlocks[i].position=(curX,curY)
		filledBlocks[i].fill_color=colorValues[2]
		filledBlocks[i].outline_thickness=0
		if i in (3,7,11,15): # if at the end of a row
			curX=pad
			curY+=blockSize+pad
		elif i not in (3,7,11,15):
			curX+=blockSize+pad		


	window=sf.RenderWindow(sf.VideoMode(boardSide,boardSide), "2048")
	window.icon=sf.Image.from_file("2048.png").pixels
	window.framerate_limit=48

	#					  #
	#	MAIN LOOP START   #
	#					  #

	while window.is_open:
		window.clear(boardColor)
		
		for event in window.events:
			if type(event) == sf.CloseEvent:
				#keysThread.terminate()
				window.close()
			if type(event) == sf.KeyEvent and event.released:
				if event.code is sf.Keyboard.LEFT:
					for i in range(len(curFilled)):
						if curFilled[i] not in (0,4,8,12):
							curFilled[i]-=(1*mFactor)				
				if event.code is sf.Keyboard.UP: 
					for i in range(len(curFilled)):
						if curFilled[i] not in (0,1,2,3):
							curFilled[i]-=(4*mFactor)
				if event.code is sf.Keyboard.RIGHT:
					for i in range(len(curFilled)):
						if curFilled[i] not in (3,7,11,15):
							curFilled[i]+=(1*mFactor)
				if event.code is sf.Keyboard.DOWN:
					for i in range(len(curFilled)):
						if curFilled[i] not in (12,13,14,15):
							curFilled[i]+=(4*mFactor)
				if event.code is sf.Keyboard.SPACE:
					initialFilled=reSeed()
					curFilled=initialFilled
					print "Re-Seeded",initialFilled	
				if event.code is sf.Keyboard.RETURN:
					if len(curFilled)>=16:
						print "Spaces Full"
					else:
						curFilled.append(newBlock(curFilled))
						curFilled.sort()
						print "Block Added"	
				
				print curFilled

		for i in range(16):
			if curFilled.count(i)>1:
					curFilled.remove(i)
					if len(curFilled)>=16:
						print "Spaces Full"
					else:
						curFilled.append(newBlock(curFilled))
					#filledBlocks[curFilled.index(i)].fill_color=colorValues[4]

		for i in range(numBlocks): # draw
			window.draw(grid[i])

		for i in curFilled:
			window.draw(filledBlocks[i])

		window.display()

		curFilled.sort()

if __name__=='__main__':
	main()