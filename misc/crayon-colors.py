#!/usr/bin/env python3
import argparse

# ====================
# = ARGUMENTS PARSER =
# ====================

parser = argparse.ArgumentParser(description='Generates code to declare the crayon color constants in different development platforms.')

parser.add_argument('--platform','-p',
	dest='platform',
	required=True,
	nargs=1,
	help="Target development platform.")
	
args = parser.parse_args()

platform = args.platform[0]

# ===============
# = DEFINITIONS =
# ===============

groupCrayons = {
	"Licorice"   : "#000000",
	"Lead"       : "#212121",
	"Tungsten"   : "#424242",
	"Iron"       : "#5F5E5F",
	"Steel"      : "#797979",
	"Tin"        : "#919191",
	"Nickel"     : "#929292",
	"Aluminum"   : "#A9A9A9",
	"Magnesium"  : "#C0C0C0",
	"Silver"     : "#D6D6D6",
	"Mercury"    : "#EBEBEB",
	"Snow"       : "#FFFFFF",
	"Cayenne"    : "#941100",
	"Mocha"      : "#945200",
	"Asparagus"  : "#929000",
	"Fern"       : "#4F9000",
	"Clover"     : "#1F8F00",
	"Moss"       : "#1F8F51",
	"Teal"       : "#1F9293",
	"Ocean"      : "#0C5393",
	"Mignight"   : "#021992",
	"Eggplant"   : "#531B93",
	"Plum"       : "#952192",
	"Maroon"     : "#941651",
	"Maraschino" : "#FA2500",
	"Tangerine"  : "#FB9300",
	"Lemon"      : "#FFFC00",
	"Lime"       : "#8EFA00",
	"Spring"     : "#3DF900",
	"Seafoam"    : "#3EFB92",
	"Turquoise"  : "#3DFCFF",
	"Aqua"       : "#1F96FF",
	"Blueberry"  : "#0433FF",
	"Grape"      : "#9538FF",
	"Magenta"    : "#FA40FF",
	"Strawberry" : "#FA2E93",
	"Salmon"     : "#FB7D79",
	"Cantaloupe" : "#FDD479",
	"Banana"     : "#FFFC78",
	"Honeydew"   : "#D4FB78",
	"Flora"      : "#73FA79",
	"Spindrift"  : "#73FCD6",
	"Ice"        : "#73FDFF",
	"Sky"        : "#76D6FF",
	"Orchid"     : "#7A81FF",
	"Lavender"   : "#D883FF",
	"Bubblegum"  : "#FB85FF",
	"Carnation"  : "#FB89D8",
}

# color groups 
colorGroups = {
	"Crayon": groupCrayons,
}

# =============
# = FUNCTIONS =
# =============

def android_color(colorName, hexCode):
	print("<color name=\"crayon%s\">%s</color>" % (colorName, hexCode))

def ios_color(colorName, hexCode):
	rComp = int(hexCode[1:3], 16)
	gComp = int(hexCode[3:5], 16)
	bComp = int(hexCode[5:], 16)
	print("static let %s = UIColor(red: %.3f, green: %.3f, blue: %.3f, alpha:1)" % (colorName, rComp/256, gComp/256, bComp/256))

# ===========
# = PROGRAM =
# ===========
platform = platform.lower()

if (platform == "android"):
	for groupName, group in colorGroups.items():
		print("<!-- %s Colors -->" % (groupName))
		for colorName, hexCode in group.items():
			android_color(colorName, hexCode)
elif (platform == "ios"):
	for groupName, group in colorGroups.items():
		print("// %s Colors" % (groupName))
		for colorName, hexCode in group.items():
			ios_color(colorName, hexCode)
else:
	print("Unknown platform")