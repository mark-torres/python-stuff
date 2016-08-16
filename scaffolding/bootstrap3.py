#!/usr/bin/env python3
import argparse, random

def str_to_var(str):
	str = str.lower().strip()
	tokens = str.split(' ')
	return '_'.join(tokens)

def bstrap3_form_horizontal(prefix, titles, varNames):
	lines = []
	# start form
	lines.append('<form id="%s" class="form-horizontal">' % (prefix) )
	for i in range( len(titles) ):
		fieldId = "%s_%s" % (prefix,varNames[i])
		lines.append('\t<div class="form-group">')
		lines.append('\t\t<label for="%s" class="col-md-2 control-label">%s:</label>' % (fieldId, titles[i]))
		lines.append('\t\t<div class="col-md-10">')
		lines.append('\t\t\t<input type="text" class="form-control" name="%s" id="%s">' % (varNames[i],fieldId))
		lines.append('\t\t</div>')
		lines.append('\t</div>')
	lines.append('\t<div class="form-group">')
	lines.append('\t\t<div class="col-sm-offset-2 col-sm-10">')
	lines.append('\t\t\t<div class="alert alert-danger" role="alert" id="%s_error_msg" style="display: none;">Some error</div>' % (prefix))
	lines.append('\t\t\t<button type="submit" class="btn btn-primary">Submit</button>')
	lines.append('\t\t</div>')
	lines.append('\t</div>')
	lines.append('</form>')
	return '\n'.join(lines)

def bstrap3_form(prefix, titles, varNames):
	lines = []
	# start form
	lines.append('<form id="%s">' % (prefix) )
	for i in range( len(titles) ):
		fieldId = "%s_%s" % (prefix,varNames[i])
		lines.append('\t<div class="form-group">')
		lines.append('\t\t<label for="%s" >%s:</label>' % (fieldId, titles[i]))
		lines.append('\t\t<input type="text" class="form-control" name="%s" id="%s">' % (varNames[i],fieldId))
		lines.append('\t</div>')
	lines.append('\t<div class="alert alert-danger" role="alert" id="%s_error_msg" style="display: none;">Some error</div>' % (prefix))
	lines.append('\t<button type="submit" class="btn btn-primary">Submit</button>')
	lines.append('</form>')
	return '\n'.join(lines)

def bstrap3_form_nolabels(prefix, titles, varNames):
	lines = []
	# start form
	lines.append('<form id="%s">' % (prefix) )
	for i in range( len(titles) ):
		fieldId = "%s_%s" % (prefix,varNames[i])
		lines.append('\t<div class="form-group">')
		lines.append('\t\t<input type="text" class="form-control" name="%s" id="%s" placeholder="%s">' % (varNames[i],fieldId, titles[i]))
		lines.append('\t</div>')
	lines.append('\t<div class="alert alert-danger" role="alert" id="%s_error_msg" style="display: none;">Some error</div>' % (prefix))
	lines.append('\t<button type="submit" class="btn btn-primary">Submit</button>')
	lines.append('</form>')
	return '\n'.join(lines)


parser = argparse.ArgumentParser(description='Generates Bootstrap markup code for different components')

parser.add_argument('--type','-t',
	dest='argType',
	required=True,
	nargs=1,
	choices=['tabpanel','form'],
	help="Scaffold type")

parser.add_argument('--data','-d',
	dest='argData',
	required=True,
	nargs=1,
	help="A quoted list of tab titles (for tabs) or fields (for forms), separated by comma.")


args = parser.parse_args()

argType = args.argType[0]
argData = args.argData[0]

argData = argData.strip(',').strip()
names = argData.split(',')

rand = "%s" % (random.random())
rand = rand.split('.')[1]
prefix = "%s%s" % (argType, rand)

titles = []
varNames = []
for i in range( len(names) ):
	names[i] = names[i].strip()
	if names[i] != '':
		titles = titles + [ names[i].title() ]
		varNames = varNames + [ str_to_var(names[i]) ]

print(bstrap3_form(prefix, titles, varNames))
print("\n\n")
print(bstrap3_form_horizontal(prefix, titles, varNames))
print("\n\n")
print(bstrap3_form_nolabels(prefix, titles, varNames))


