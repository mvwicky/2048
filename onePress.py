import sfml as sf 
import random
import math


def main():
	colors=[]
	for i in range(16):
		colors.append(sf.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255),255))
	values=[]
	for i in range(1,13):
		values.append(2**i)
	colorValues=dict(zip(values,colors))
	print colorValues
	return 0

if __name__=='__main__':
	main()