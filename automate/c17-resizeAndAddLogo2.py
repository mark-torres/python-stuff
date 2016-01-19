#!/usr/bin/env python3
import argparse, os, sys
from PIL import Image

parser = argparse.ArgumentParser(description='Resize images in current folder and add logo')

parser.add_argument("--logo",
	dest = "logoFile",
	nargs = 1,
	required = True,
	help = "Image file fo the logo. MUST be PNG or GIF WITH TRANSPARENCY")
parser.add_argument("--size",
	dest = "squareSize",
	nargs = 1,
	required = True,
	type = int,
	help = "Size (in pixels) of the result square images with logo. Must be in the range of 100 to 800 px.")
args = parser.parse_args()

logoFile = args.logoFile[0]
squareSize = args.squareSize[0]

imageExtensions = ['.jpg','.jpeg','.bmp','.gif','.png']

# validate
if not os.path.exists(logoFile):
	print("Logo file not found")
	sys.exit()

if squareSize < 100 or squareSize > 800:
	print("Square size out of range.")
	sys.exit()

logoName = os.path.basename(logoFile)
logoImg = Image.open(logoFile)
logoWidth, logoHeigth = logoImg.size
# resize logo to 25% of the square
logoWidth = int(squareSize/3)
logoHeigth = int(squareSize/3)
size = logoWidth, logoHeigth
logoImg.thumbnail( size, Image.ANTIALIAS )
print("Logo size: %sx%s" % (logoWidth, logoHeigth))

directory = os.getcwd()
for filename in os.listdir(directory):
	name, ext = os.path.splitext(filename)
	if ext.lower() in imageExtensions and filename != logoName:
		print("Processing '%s'" % (filename))
		try:
			img = Image.open(filename)
		except Exception as e:
			print("\tError reading image")
			continue
		imgWidth, imgHeigth = img.size
		# check image size
		if squareSize > imgWidth or squareSize > imgHeigth:
			print("\tImage too small")
			continue
		print("\tImage size: %dx%d" % (imgWidth, imgHeigth))
		if imgWidth > imgHeigth:
			imgSquare = imgHeigth
		else:
			imgSquare = imgWidth
		# resize if needed
		if imgSquare > squareSize:
			ratio = imgSquare / squareSize
			imgWidth = int(imgWidth/ratio)
			imgHeigth = int(imgHeigth/ratio)
			size = imgWidth, imgHeigth
			img = img.resize( size, Image.ANTIALIAS )
			print("\tResized to %sx%s" % (imgWidth, imgHeigth))
		# add logo
		print("\tAdding logo...")
		logoPos = (imgWidth - logoWidth, imgHeigth - logoHeigth)
		img.paste(logoImg, logoPos, logoImg)
		# save new image
		img.save("%s + logo%s" % (name, ext))
