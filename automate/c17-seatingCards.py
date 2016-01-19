#!/usr/bin/env python3
import argparse, os, sys, re, time
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser(description = "Custom seating cards")
parser.add_argument("--list",
	dest = "namesFile",
	nargs = 1,
	required = True,
	help = "File with the list of guest names")
parser.add_argument("--font",
	dest = "fontFile",
	nargs = 1,
	required = True,
	help = "TTF font file to use")

args = parser.parse_args()

namesFilePath = args.namesFile[0]
fontFilePath = args.fontFile[0]

reNonAlphanum = re.compile(r"[\W\s]+")

# card size = 4x5 inch, resolution = 72 ppi
cardSize = cardWidth, cardHeight = (5 * 72, 4 * 72)
now = time.time()

if not os.path.exists(namesFilePath):
	print("List file not found")
	sys.exit()
try:
	namesFile = open(namesFilePath, "r")
except Exception as e:
	print("Error opening list file")
	sys.exit()

if not os.path.exists(fontFilePath):
	print("Font file not found")
	sys.exit()
try:
	cardFont = ImageFont.truetype(fontFilePath, 40)
except Exception as e:
	print("Error loading font file")
	sys.exit()

for name in namesFile.readlines():
	name = name.strip()
	filename = "card_%d_%s.png" % (now, reNonAlphanum.sub("_", name))
	print("%s [%s]" % (name, filename))
	cardImg = Image.new("RGBA", cardSize, "white")
	draw = ImageDraw.Draw(cardImg)
	draw.polygon( ( (0,0), (cardWidth-1,0), (cardWidth-1,cardHeight-1), (0,cardHeight-1) ), outline = "black" )
	nameText = " " + name + " "
	textWidth, textHeight = draw.textsize(nameText, cardFont)
	textX = int( (cardWidth - textWidth)/2 )
	textY = int( (cardHeight - textHeight)/2 )
	draw.text(xy = (textX,textY), text = nameText, fill = "black", font = cardFont)
	cardImg.save(filename)
