import sfml as sf 
import random
import math

def main():

	pad=20
	blockSize=150
	iBlockSize=26

	boardSide=500

	boardColor=sf.Color(210,210,210,255)
	blockColor=sf.Color(135,135,135,255)

	try:
		font=sf.Font.from_file("calibri.ttf")
	except IOError: exit(1)

	text=sf.Text("Text Test")
	text.font=font

	window=sf.RenderWindow(sf.VideoMode(boardSide,boardSide), "2048")
	window.icon=sf.Image.from_file("2048.png").pixels

	while window.is_open:
		window.clear(boardColor)

		window.draw(text)
		
		for event in window.events:
			if type(event) == sf.CloseEvent:
				window.close()	

		window.display()

if __name__=='__main__':
	main()