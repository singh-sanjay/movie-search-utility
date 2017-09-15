#!/usr/bin/python
#
# Screen scraper based API for BookMyShow.

import re
import urllib2

class BookMyShowClient(object):
  MOVIE_NAME_REGEX = '<strong>(.*?)</strong>'
  
  def __init__(self, time = '20170429'):
    self.__time = time.lower()
    self.__url = "https://in.bookmyshow.com/buytickets/pvr-vr-bengaluru/cinema-bang-PVPB-MT/%s" % self.__time
    self.__html = None

  def __download(self):
    req = urllib2.Request(self.__url, headers={'User-Agent' : "Magic Browser"})
    html = urllib2.urlopen(req).read()
    return html

  def get_movies_showing(self):
    if not self.__html:
      self.__html = self.__download()
    now_showing = re.findall(self.MOVIE_NAME_REGEX, self.__html)
    return now_showing

if __name__ == '__main__':
  # Test code.
  bms_client = BookMyShowClient('20170429')
  movie_names = bms_client.get_movies_showing()
  baahubali_showtime = filter(re.compile(".*[Bb]aahubali.*").match, movie_names)
  print len(baahubali_showtime) > 0