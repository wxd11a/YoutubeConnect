import urllib.request # for the request.open to Youtube
import collections # for the ordered dictionary
#import urllib2


def getAllTitles(r):
	titles = []

	# video-title is where Youtube holds the song titles
	# <span class="title video-title" dir="ltr">Minecraft‌·Music</span>
	vt = "title video-title"

	for line in r:
		unencLine = str(line, encoding='utf8')
		if vt in unencLine:
			titles.append(htmlTitleStrip(unencLine))
			#print(htmlTitleStrip(unencLine))
			#print(unencLine)

	return(titles)

	# for line in iter(r.readline.decode("utf-8"),b''):
	# 	print(line.lstrip('\'b'))

def htmlTitleStrip(title):
	title = title.lstrip("<span class=\"title video-title\" dir=\"ltr\">")
	title = title.rstrip("</span>\n")
	return(title)

# if using dictionary might want to pass it or have this as a void function for simply adding
def getSongNames(titles):
	songNames = []
	for name in titles:
		if ' - ' in name:
			stripAtIndex = name.index(' - ')
			songNames.append(name[stripAtIndex+2:].strip())
	return(songNames)

# if using dictionary might want to pass it or have this as a void function for simply adding
def getArtistNames(titles):
	artistNames = []

	for name in titles:
		if ' - ' in name:
			stripAtIndex = name.index(' - ')
			artistNames.append(name[:stripAtIndex].strip())
	return(artistNames)

# use this to replace the previous two function that return two different lists
# this uses a dictionary to assign key, value pairs
def assignSongArtist(titles):
	songsArtists = {}

	for name in titles:
		if ' - ' in name:
			stripAtIndex = name.index(' - ')
			songsArtists[name[:stripAtIndex].strip()] = name[stripAtIndex+2:].strip()
	return(songsArtists)

def main():
	allTitles = []
	songs = []
	artists = []
	songsArtists = {}

	#req = urllib2.Request("https://www.youtube.com/playlist?list=PL629B849A4A58F28D")
	#res = urllib2.urlopen(req)

	res = urllib.request.urlopen('http://www.youtube.com/playlist?list=PLDEE516E6391D2AAC')

	# data = res.read().decode("utf-8")

	allTitles = getAllTitles(res)
	songs = getSongNames(allTitles)
	artists = getArtistNames(allTitles)
	songsArtists = assignSongArtist(allTitles)

	print(len(songs))
	print(len(artists))

	# sort by artist and reassign songsArtists to itself
	songsArtists = collections.OrderedDict(sorted(songsArtists.items()))
	# print all in dict
	for a, s in songsArtists.items(): print(a, s)
	
	#print(type(data))

main()