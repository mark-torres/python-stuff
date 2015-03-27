import urllib, htmllib, re, sys, formatter
# ==========
max_depth = 6
if len(sys.argv) == 1:
	print("Missing URL to crawl")
	exit()
if len(sys.argv) == 3 and re.match('^\d+$', sys.argv[2]) != None and int(sys.argv[2]) <= max_depth:
	max_depth = int(sys.argv[2])
url = sys.argv[1]
if re.search('^https?', url) == None:
	url = "http://"+url
# ==========
def print_url_links(url, depth = 1):
	global max_depth
	if depth > max_depth:
		return 0
	else:
		# read page HTML
		try:
			website = urllib.urlopen(url)
			data = website.read()
			website.close()
		except:
			print("\nERROR OPENING %s\n" % url)
			data = []
		# get all links
		if len(data) > 0:			
			format = formatter.AbstractFormatter(formatter.NullWriter())
			ptext = htmllib.HTMLParser(format)
			ptext.feed(data)
			# crawl the links
			for link in ptext.anchorlist:
				if re.match('^https?', link) != None:
					print(link)
					print_url_links(link, depth + 1)
# ==========
print_url_links(url)
