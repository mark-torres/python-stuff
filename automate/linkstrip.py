#!/usr/bin/env python3
import bs4, pyperclip, sys, argparse

parser = argparse.ArgumentParser(description='Strips URL from links in clipboard')

parser.add_argument('--siteurl',
	dest='siteUrl',
	nargs=1,
	help="Site's main URL (for links with relative URLs)")
args = parser.parse_args()

siteUrl = args.siteUrl[0] if (args.siteUrl != None) else None

try:
	html = pyperclip.paste()
except Exception as e:
	print('Error reading from clipboard. Make sure the pyperclip module is installed.')
	sys.exit()

try:
	parser = bs4.BeautifulSoup(html, "html.parser")
except Exception as e:
	print('Error parsing HTML. Make sure bs4 module is installed.')
	sys.exit()

links = parser.select('a')
if len(links) > 0:
	for link in links:
		text = link.getText()
		toks = text.split()
		if len(toks) > 0:
			text = ' '.join(toks)
		url = link.attrs['href'] if 'href' in link.attrs else '-'
		if siteUrl != None:
			url = siteUrl + url
		print('%s\n%s\n' % (text, url))
