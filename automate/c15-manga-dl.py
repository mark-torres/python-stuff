#!/usr/bin/env python3
import requests, bs4, os, re, shutil

def downloadMangafox(mangaUrl, dlDir = "."):
	print("Checking MangaFox URL '%s'" % mangaUrl)
	res = requests.get(mangaUrl)
	try:
		res.raise_for_status()
	except:
		print("Error reading URL")
		res = None
	if res != None and os.path.isdir(dlDir):
		# make directory if not exists
		mangaDir = mangaUrl.strip("/").split('/')[-1]
		mangaDir = os.path.join(dlDir, mangaDir)
		if not os.path.exists(mangaDir):
			os.mkdir(mangaDir)
		reNotAlnum = re.compile(r'\W+')
		# start crawling
		mainPage = bs4.BeautifulSoup(res.text, "html.parser")
		chapters = mainPage.select("div#chapters li")
		for chapter in chapters:
			container = None
			chapterImages = []
			if len(chapter.select("h3")):
				container = "h3"
			elif len(chapter.select("h4")):
				container = "h4"
			if container != None:
				chapterIndex = chapter.select(container + " a")[0].getText()
				chapterUrl = chapter.select(container + " a")[0].attrs['href']
				chapterTitle = chapter.select(container + " span")[0].getText()
				chapterDir = reNotAlnum.sub('_', chapterIndex).strip('_')
				chapterDir = os.path.join(mangaDir, chapterDir)
				# check if chapter is already downloaded
				if os.path.exists(chapterDir):
					continue
				# download chapter
				os.mkdir(chapterDir)
				print("%s - %s (%s)" % (chapterIndex, chapterTitle, chapterUrl))
				if chapterUrl.endswith("/"):
					chapterUrl = chapterUrl + "1.html"
				page1res = requests.get(chapterUrl)
				try:
					page1res.raise_for_status()
				except:
					print("Error reading URL")
					continue
				page = bs4.BeautifulSoup(page1res.text, "html.parser")
				images = page.select("div.read_img img#image")
				if len(images) > 0:
					chapterImages.append(images[0].attrs['src'])
				# get number of pages
				div = page.select("form#top_bar div.l")
				if len(div) > 0:
					text = div[0].getText()
					nPages = text.strip().split()[-1]
					if nPages.isdecimal():
						nPages = int(nPages)
					else:
						nPages = 0
					print("%s Pages" % (nPages))
					chapterUrlBase = os.path.dirname(chapterUrl)
					for chpPage in range(2, nPages + 1):
						chpUrl = "%s/%d.html" % (chapterUrlBase, chpPage)
						chpPageRes = requests.get(chpUrl)
						try:
							chpPageRes.raise_for_status()
						except:
							print("Error getting page '%s'" % chpUrl)
							continue
						print("Processing '%s'" % (chpUrl))
						page = bs4.BeautifulSoup(chpPageRes.text, "html.parser")
						images = page.select("div.read_img img#image")
						if len(images) > 0:
							chapterImages.append(images[0].attrs['src'])
					# download images
					for chapterImage in chapterImages:
						print("Getting image '%s'" % (chapterImage))
						imageFileName = os.path.basename(chapterImage)
						imagePath = os.path.join(chapterDir, imageFileName)
						if os.path.exists(imagePath):
							continue
						imageRes = requests.get(chapterImage)
						try:
							imageRes.raise_for_status()
						except:
							print("Error getting image '%s'" % (chapterImage))
							continue
						imageFile = open( imagePath, "wb" )
						for chunk in imageRes.iter_content(100 * 1024):
							imageFile.write(chunk)
						imageFile.close()
			break

downloadDir = "../tmp"

mangafoxUrls = []
mangafoxUrls.append('http://mangafox.me/manga/onepunch_man/')
# mangafoxUrls.append('http://mangafox.me/manga/nanatsu_no_taizai/')
# mangafoxUrls.append('http://mangafox.me/manga/dungeon_ni_deai_o_motomeru_no_wa_machigatte_iru_darou_ka/')

for url in mangafoxUrls:
	print("Processing %s" % url)
	downloadMangafox(url, downloadDir)
