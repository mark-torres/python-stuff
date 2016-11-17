#!/usr/bin/env python3
import argparse, random

# ====================
# = ARGUMENTS PARSER =
# ====================

parser = argparse.ArgumentParser(description='Generates Java code for SQLite in Android.')

parser.add_argument('--type','-t',
	dest='argType',
	required=True,
	nargs=1,
	choices=['tabpanel','form','form-nolabels','form-horizontal','modal','dropdown','btn-group'],
	help="Scaffold type")

parser.add_argument('--data','-d',
	dest='argData',
	required=True,
	nargs=1,
	help="A quoted list of tab titles (for tabs and modals) or fields (for forms), separated by comma.")

args = parser.parse_args()

argType = args.argType[0]
argData = args.argData[0]

# =============
# = FUNCTIONS =
# =============
