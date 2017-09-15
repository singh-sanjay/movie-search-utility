import re
import urllib2

MOVIE_NAME_REGEX = '"VenueCode":"PVPB"'
url = "https://in.bookmyshow.com/buytickets/baahubali-2-the-conclusion-hindi-bengaluru/movie-bang-ET00050679-MT/20170429"
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
html = urllib2.urlopen(req).read()
in_pvr = re.findall(MOVIE_NAME_REGEX, html)
print len(in_pvr) > 0