#!/usr/bin/env python3
import argparse

# ====================
# = ARGUMENTS PARSER =
# ====================

parser = argparse.ArgumentParser(description='Generates code to declare the material colors constants in different development platforms.')

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

redGroup = {
	"Red"     : "#f44336",
	"Red50"   : "#ffebee",
	"Red100"  : "#ffcdd2",
	"Red200"  : "#ef9a9a",
	"Red300"  : "#e57373",
	"Red400"  : "#ef5350",
	"Red500"  : "#f44336",
	"Red600"  : "#e53935",
	"Red700"  : "#d32f2f",
	"Red800"  : "#c62828",
	"Red900"  : "#b71c1c",
	"RedA100" : "#ff8a80",
	"RedA200" : "#ff5252",
	"RedA400" : "#ff1744",
	"RedA700" : "#d50000",
}

pinkGroup = {
	"Pink"     : "#E91E63",
	"Pink50"   : "#FCE4EC",
	"Pink100"  : "#F8BBD0",
	"Pink200"  : "#F48FB1",
	"Pink300"  : "#F06292",
	"Pink400"  : "#EC407A",
	"Pink500"  : "#E91E63",
	"Pink600"  : "#D81B60",
	"Pink700"  : "#C2185B",
	"Pink800"  : "#AD1457",
	"Pink900"  : "#880E4F",
	"PinkA100" : "#FF80AB",
	"PinkA200" : "#FF4081",
	"PinkA400" : "#F50057",
	"PinkA700" : "#C51162",
}

purpleGroup = {
	"Purple"     : "#9C27B0",
	"Purple50"   : "#F3E5F5",
	"Purple100"  : "#E1BEE7",
	"Purple200"  : "#CE93D8",
	"Purple300"  : "#BA68C8",
	"Purple400"  : "#AB47BC",
	"Purple500"  : "#9C27B0",
	"Purple600"  : "#8E24AA",
	"Purple700"  : "#7B1FA2",
	"Purple800"  : "#6A1B9A",
	"Purple900"  : "#4A148C",
	"PurpleA100" : "#EA80FC",
	"PurpleA200" : "#E040FB",
	"PurpleA400" : "#D500F9",
	"PurpleA700" : "#AA00FF",
}

deepPurpleGroup = {
	"DeepPurple"     : "#673AB7",
	"DeepPurple50"   : "#EDE7F6",
	"DeepPurple100"  : "#D1C4E9",
	"DeepPurple200"  : "#B39DDB",
	"DeepPurple300"  : "#9575CD",
	"DeepPurple400"  : "#7E57C2",
	"DeepPurple500"  : "#673AB7",
	"DeepPurple600"  : "#5E35B1",
	"DeepPurple700"  : "#512DA8",
	"DeepPurple800"  : "#4527A0",
	"DeepPurple900"  : "#311B92",
	"DeepPurpleA100" : "#B388FF",
	"DeepPurpleA200" : "#7C4DFF",
	"DeepPurpleA400" : "#651FFF",
	"DeepPurpleA700" : "#6200EA",
}

indigoGroup = {
	"Indigo"     : "#3F51B5",
	"Indigo50"   : "#E8EAF6",
	"Indigo100"  : "#C5CAE9",
	"Indigo200"  : "#9FA8DA",
	"Indigo300"  : "#7986CB",
	"Indigo400"  : "#5C6BC0",
	"Indigo500"  : "#3F51B5",
	"Indigo600"  : "#3949AB",
	"Indigo700"  : "#303F9F",
	"Indigo800"  : "#283593",
	"Indigo900"  : "#1A237E",
	"IndigoA100" : "#8C9EFF",
	"IndigoA200" : "#536DFE",
	"IndigoA400" : "#3D5AFE",
	"IndigoA700" : "#304FFE",
}

blueGroup = {
	"Blue"     : "#2196F3",
	"Blue50"   : "#E3F2FD",
	"Blue100"  : "#BBDEFB",
	"Blue200"  : "#90CAF9",
	"Blue300"  : "#64B5F6",
	"Blue400"  : "#42A5F5",
	"Blue500"  : "#2196F3",
	"Blue600"  : "#1E88E5",
	"Blue700"  : "#1976D2",
	"Blue800"  : "#1565C0",
	"Blue900"  : "#0D47A1",
	"BlueA100" : "#82B1FF",
	"BlueA200" : "#448AFF",
	"BlueA400" : "#2979FF",
	"BlueA700" : "#2962FF",
}

lightBlueGroup = {
	"LightBlue"     : "#03A9F4",
	"LightBlue50"   : "#E1F5FE",
	"LightBlue100"  : "#B3E5FC",
	"LightBlue200"  : "#81D4FA",
	"LightBlue300"  : "#4FC3F7",
	"LightBlue400"  : "#29B6F6",
	"LightBlue500"  : "#03A9F4",
	"LightBlue600"  : "#039BE5",
	"LightBlue700"  : "#0288D1",
	"LightBlue800"  : "#0277BD",
	"LightBlue900"  : "#01579B",
	"LightBlueA100" : "#80D8FF",
	"LightBlueA200" : "#40C4FF",
	"LightBlueA400" : "#00B0FF",
	"LightBlueA700" : "#0091EA",
}

cyanGroup = {
	"Cyan"     : "#00BCD4",
	"Cyan50"   : "#E0F7FA",
	"Cyan100"  : "#B2EBF2",
	"Cyan200"  : "#80DEEA",
	"Cyan300"  : "#4DD0E1",
	"Cyan400"  : "#26C6DA",
	"Cyan500"  : "#00BCD4",
	"Cyan600"  : "#00ACC1",
	"Cyan700"  : "#0097A7",
	"Cyan800"  : "#00838F",
	"Cyan900"  : "#006064",
	"CyanA100" : "#84FFFF",
	"CyanA200" : "#18FFFF",
	"CyanA400" : "#00E5FF",
	"CyanA700" : "#00B8D4",
}

tealGroup = {
	"Teal"     : "#009688",
	"Teal50"   : "#E0F2F1",
	"Teal100"  : "#B2DFDB",
	"Teal200"  : "#80CBC4",
	"Teal300"  : "#4DB6AC",
	"Teal400"  : "#26A69A",
	"Teal500"  : "#009688",
	"Teal600"  : "#00897B",
	"Teal700"  : "#00796B",
	"Teal800"  : "#00695C",
	"Teal900"  : "#004D40",
	"TealA100" : "#A7FFEB",
	"TealA200" : "#64FFDA",
	"TealA400" : "#1DE9B6",
	"TealA700" : "#00BFA5",
}

greenGroup = {
	"Green"     : "#4CAF50",
	"Green50"   : "#E8F5E9",
	"Green100"  : "#C8E6C9",
	"Green200"  : "#A5D6A7",
	"Green300"  : "#81C784",
	"Green400"  : "#66BB6A",
	"Green500"  : "#4CAF50",
	"Green600"  : "#43A047",
	"Green700"  : "#388E3C",
	"Green800"  : "#2E7D32",
	"Green900"  : "#1B5E20",
	"GreenA100" : "#B9F6CA",
	"GreenA200" : "#69F0AE",
	"GreenA400" : "#00E676",
	"GreenA700" : "#00C853",
}

lightGreenGroup = {
	"LightGreen"     : "#8BC34A",
	"LightGreen50"   : "#F1F8E9",
	"LightGreen100"  : "#DCEDC8",
	"LightGreen200"  : "#C5E1A5",
	"LightGreen300"  : "#AED581",
	"LightGreen400"  : "#9CCC65",
	"LightGreen500"  : "#8BC34A",
	"LightGreen600"  : "#7CB342",
	"LightGreen700"  : "#689F38",
	"LightGreen800"  : "#558B2F",
	"LightGreen900"  : "#33691E",
	"LightGreenA100" : "#CCFF90",
	"LightGreenA200" : "#B2FF59",
	"LightGreenA400" : "#76FF03",
	"LightGreenA700" : "#64DD17",
}

limeGroup = {
	"Lime"     : "#CDDC39",
	"Lime50"   : "#F9FBE7",
	"Lime100"  : "#F0F4C3",
	"Lime200"  : "#E6EE9C",
	"Lime300"  : "#DCE775",
	"Lime400"  : "#D4E157",
	"Lime500"  : "#CDDC39",
	"Lime600"  : "#C0CA33",
	"Lime700"  : "#AFB42B",
	"Lime800"  : "#9E9D24",
	"Lime900"  : "#827717",
	"LimeA100" : "#F4FF81",
	"LimeA200" : "#EEFF41",
	"LimeA400" : "#C6FF00",
	"LimeA700" : "#AEEA00",
}

yellowGroup = {
	"Yellow"     : "#FFEB3B",
	"Yellow50"   : "#FFFDE7",
	"Yellow100"  : "#FFF9C4",
	"Yellow200"  : "#FFF59D",
	"Yellow300"  : "#FFF176",
	"Yellow400"  : "#FFEE58",
	"Yellow500"  : "#FFEB3B",
	"Yellow600"  : "#FDD835",
	"Yellow700"  : "#FBC02D",
	"Yellow800"  : "#F9A825",
	"Yellow900"  : "#F57F17",
	"YellowA100" : "#FFFF8D",
	"YellowA200" : "#FFFF00",
	"YellowA400" : "#FFEA00",
	"YellowA700" : "#FFD600",
}

amberGroup = {
	"Amber"     : "#FFC107",
	"Amber50"   : "#FFF8E1",
	"Amber100"  : "#FFECB3",
	"Amber200"  : "#FFE082",
	"Amber300"  : "#FFD54F",
	"Amber400"  : "#FFCA28",
	"Amber500"  : "#FFC107",
	"Amber600"  : "#FFB300",
	"Amber700"  : "#FFA000",
	"Amber800"  : "#FF8F00",
	"Amber900"  : "#FF6F00",
	"AmberA100" : "#FFE57F",
	"AmberA200" : "#FFD740",
	"AmberA400" : "#FFC400",
	"AmberA700" : "#FFAB00",
}

orangeGroup = {
	"Orange"     : "#FF9800",
	"Orange50"   : "#FFF3E0",
	"Orange100"  : "#FFE0B2",
	"Orange200"  : "#FFCC80",
	"Orange300"  : "#FFB74D",
	"Orange400"  : "#FFA726",
	"Orange500"  : "#FF9800",
	"Orange600"  : "#FB8C00",
	"Orange700"  : "#F57C00",
	"Orange800"  : "#EF6C00",
	"Orange900"  : "#E65100",
	"OrangeA100" : "#FFD180",
	"OrangeA200" : "#FFAB40",
	"OrangeA400" : "#FF9100",
	"OrangeA700" : "#FF6D00",
}

deepOrangeGroup = {
	"DeepOrange"     : "#FF5722",
	"DeepOrange50"   : "#FBE9E7",
	"DeepOrange100"  : "#FFCCBC",
	"DeepOrange200"  : "#FFAB91",
	"DeepOrange300"  : "#FF8A65",
	"DeepOrange400"  : "#FF7043",
	"DeepOrange500"  : "#FF5722",
	"DeepOrange600"  : "#F4511E",
	"DeepOrange700"  : "#E64A19",
	"DeepOrange800"  : "#D84315",
	"DeepOrange900"  : "#BF360C",
	"DeepOrangeA100" : "#FF9E80",
	"DeepOrangeA200" : "#FF6E40",
	"DeepOrangeA400" : "#FF3D00",
	"DeepOrangeA700" : "#DD2C00",
}

brownGroup = {
	"Brown"    : "#795548",
	"Brown50"  : "#EFEBE9",
	"Brown100" : "#D7CCC8",
	"Brown200" : "#BCAAA4",
	"Brown300" : "#A1887F",
	"Brown400" : "#8D6E63",
	"Brown500" : "#795548",
	"Brown600" : "#6D4C41",
	"Brown700" : "#5D4037",
	"Brown800" : "#4E342E",
	"Brown900" : "#3E2723",
}

greyGroup = {
	"Grey"    : "#9E9E9E",
	"Grey50"  : "#FAFAFA",
	"Grey100" : "#F5F5F5",
	"Grey200" : "#EEEEEE",
	"Grey300" : "#E0E0E0",
	"Grey400" : "#BDBDBD",
	"Grey500" : "#9E9E9E",
	"Grey600" : "#757575",
	"Grey700" : "#616161",
	"Grey800" : "#424242",
	"Grey900" : "#212121",
}

blueGreyGroup = {
	"BlueGrey"    : "#607D8B",
	"BlueGrey50"  : "#ECEFF1",
	"BlueGrey100" : "#CFD8DC",
	"BlueGrey200" : "#B0BEC5",
	"BlueGrey300" : "#90A4AE",
	"BlueGrey400" : "#78909C",
	"BlueGrey500" : "#607D8B",
	"BlueGrey600" : "#546E7A",
	"BlueGrey700" : "#455A64",
	"BlueGrey800" : "#37474F",
	"BlueGrey900" : "#263238",
}

# groups
materialGroups = {
	"Red"        : blueGreyGroup,
	"Pink"       : greyGroup,
	"Purple"     : brownGroup,
	"DeepPurple" : deepOrangeGroup,
	"Indigo"     : orangeGroup,
	"Blue"       : amberGroup,
	"LightBlue"  : yellowGroup,
	"Cyan"       : limeGroup,
	"Teal"       : lightGreenGroup,
	"Green"      : greenGroup,
	"LightGreen" : tealGroup,
	"Lime"       : cyanGroup,
	"Yellow"     : lightBlueGroup,
	"Amber"      : blueGroup,
	"Orange"     : indigoGroup,
	"DeepOrange" : deepPurpleGroup,
	"Brown"      : purpleGroup,
	"Grey"       : pinkGroup,
	"BlueGrey"   : redGroup,
}

# =============
# = FUNCTIONS =
# =============

def android_color(colorName, hexCode):
	print("<color name=\"material%s\">%s</color>" % (colorName, hexCode))

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
	for groupName, group in materialGroups.items():
		print("<!-- %s Colors -->" % (groupName))
		for colorName, hexCode in group.items():
			android_color(colorName, hexCode)
elif (platform == "ios"):
	for groupName, group in materialGroups.items():
		print("// %s Colors" % (groupName))
		for colorName, hexCode in group.items():
			ios_color(colorName, hexCode)
else:
	print("Unknown platform")

