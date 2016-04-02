#IGNORE THIS FILE
import os,sys
from PIL import Image
import glob
import Image
mainImage = Image.open("/home/alibunny/Desktop/project2/dog.jpg")
im = Image.new("RGB", (1024,1024), "white")
width, height = mainImage.size
pix = mainImage.load()

#sets an array of the images
path = "/home/alibunny/Desktop/project2/ImageTiles/*.jpg"
files = glob.glob(path)
array = []
for file in files:
	array.append(file)

#main image pixal 
#for i in range (width):
	#for j in range (height):
		#pix[i,j] = bestMatch()
#Function ot get Average
def bestMatch(mainImage,pix,array = []):
	bestMatch1 = array[0]
	mainW,mainH = mainImage.size
	l=0
	m=0
	sumGreen = 0
	sumRed =0
	sumBlue=0
	count = 0
	averageGreen =0
	averageBlue=0	
	averageRed=0
	numDifference1=0
	numDifference11=0
	numDifference2=0
	numDifference22=0
	numDifference3=0
	numDifference33=0
	for i in range (0,5):
		mainRGB = pix[l,m]
		mainR,mainG,mainB = mainRGB
		width,height =Image.open(array[i]).size
		for j in range (width):
			count = 0
			for k in range (height):
				RGB = Image.open(array[i]).getpixel((j,k))
				R,G,B = RGB
				sumGreen = G + sumGreen
				sumRed = R + sumRed
				sumBlue = B + sumBlue
				count = 1 + count
		averageGreen = sumGreen / count
		averageRed = sumRed / count
		averageBlue = sumBlue /count
		if(i % 2 == 0):
			if(mainR < averageRed):
				numDifference1 = averageRed - mainR
			else:
				numDifference1 = mainR - averageRed
			if(mainG < averageGreen):
				numDifference2 = averageGreen - mainG
			else:
				numDifference2 = mainG - averageGreen
			if(mainB < averageBlue):
				numDifference3 = averageBlue - mainB
			else:
				numDifference3 = mainB - averageBlue
		else:
			if(mainR < averageRed):
				numDifference11 = averageRed - mainR
			else:
				numDifference11 = mainR - averageRed
			if(mainG < averageGreen):
				numDifference22 = averageGreen - mainG
			else:
				numDifference22 = mainG - averageGreen
			if(mainB < averageBlue):
				numDifference33 = averageBlue - mainB
			else:
				numDifference33 = mainB - averageBlue
		if(numDifference11 > numDifference1):
			bestMatch1 = array[i-1]
		im.paste(Image.open(bestMatch1),(l,m))
		print "L", l
		print "M",m
		print "CALLED"
		if( m == mainW):
			l = l +1
			m=0
		else:
			l = l=1
			m = m+1
		
	print "Goes here"
	im.show()				
bestMatch(mainImage,pix,array)


#im = Image.open("/home/alibunny/Desktop/project2/ImageTiles/")
