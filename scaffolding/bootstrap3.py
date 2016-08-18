#!/usr/bin/env python3
import argparse, random

# ====================
# = ARGUMENTS PARSER =
# ====================

parser = argparse.ArgumentParser(description='Generates Bootstrap markup code for different components')

parser.add_argument('--type','-t',
	dest='argType',
	required=True,
	nargs=1,
	choices=['tabpanel','form','form-nolabels','form-horizontal'],
	help="Scaffold type")

parser.add_argument('--data','-d',
	dest='argData',
	required=True,
	nargs=1,
	help="A quoted list of tab titles (for tabs) or fields (for forms), separated by comma.")

args = parser.parse_args()

argType = args.argType[0]
argData = args.argData[0]

# =============
# = FUNCTIONS =
# =============

def str_to_var(str):
	str = str.lower().strip()
	tokens = str.split(' ')
	return '_'.join(tokens)
	
def bstrap3_tabpanel(prefix, titles, varNames):
	lines = []
	lines.append('<style>')
	lines.append('.tab-pane.active > .panel {border-top: 0;border-top-left-radius: 0;border-top-right-radius: 0;}')
	lines.append('</style>')
	lines.append('<div id="%s">' % (prefix))
	# tabs
	lines.append('\t<ul class="nav nav-tabs" role="tablist">')
	for i in range( len(titles) ):
		tabId = "%s_%s" % (prefix,varNames[i])
		tabClass = 'active' if i == 0 else ''
		lines.append('\t\t<li role="presentation" class="%s">' % (tabClass))
		lines.append('\t\t\t<a data-target="#%s" aria-controls="%s" role="tab" data-toggle="tab">%s</a>' % (tabId, tabId, titles[i]))
		lines.append('\t\t</li>')
	lines.append('\t</ul>')
	# tabs content
	lines.append('\t<div class="tab-content">')
	for i in range( len(titles) ):
		tabId = "%s_%s" % (prefix,varNames[i])
		tabClass = 'active' if i == 0 else ''
		lines.append('\t\t<div role="tabpanel" class="tab-pane %s" id="%s">' % (tabClass, tabId))
		lines.append('\t\t\t<!-- Tab %s starts -->' % (titles[i]))
		lines.append('\t\t\t<div class="panel panel-default">')
		lines.append('\t\t\t\tContent for %s tab' % (titles[i]))
		lines.append('\t\t\t</div>')
		lines.append('\t\t\t<!-- Tab %s ends -->' % (titles[i]))
		lines.append('\t\t</div>')
	lines.append('\t</div>')
	lines.append('</div>')
	return '\n'.join(lines)

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

# ==================
# = IMPLEMENTATION =
# ==================

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

if argType == 'tabpanel':
	print(bstrap3_tabpanel(prefix, titles, varNames))
elif argType == 'form':
	print(bstrap3_form(prefix, titles, varNames))
elif argType == 'form-horizontal':
	print(bstrap3_form_horizontal(prefix, titles, varNames))
elif argType == 'form-nolabels':
	print(bstrap3_form_nolabels(prefix, titles, varNames))
else:
	print("Unrecognized option: %s" % (argType))
