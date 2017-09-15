#!/usr/bin/python
#
# Screen scraper based API for BookMyShow.

import re
import urllib2

class BookMyShowClient(object):
  NOW_SHOWING_REGEX = '{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"Filter Impression:category\\\/now showing"},"products":\[{"name":"(.*?)","id":".*?","category":".*?","variant":".*?","position":.*?,"dimension13":"(.*?)"}\]}}}'
  COMING_SOON_REGEX = '{"event":"productClick","ecommerce":{"currencyCode":"INR","click":{"actionField":{"list":"category\\\/coming soon"},"products":{"name":"(.*?)","id":"(.*?)","category":"(.*?)","variant":"(.*?)","position":(.*?),"dimension13":"(.*?)"}}}}'

  def __init__(self, location = 'bengaluru'):
    self.__location = location.lower()
    self.__url = "https://in.bookmyshow.com/%s/movies/" % self.__location
    self.__html = None

  def __download(self):
    req = urllib2.Request(self.__url, headers={'User-Agent' : "Magic Browser"})
    html = urllib2.urlopen(req).read()
    return html

  def get_now_showing(self):
    if not self.__html:
      self.__html = self.__download()
    now_showing = re.findall(self.NOW_SHOWING_REGEX, self.__html)
    return now_showing

  def get_coming_soon(self):
    if not self.__html:
      self.__html = self.__download()
    coming_soon = re.findall(self.COMING_SOON_REGEX, self.__html)
    return coming_soon

if __name__ == '__main__':
  # Test code.
  bms_client = BookMyShowClient('bengaluru')
  now_showing = bms_client.get_now_showing()
  movie_names = [now_showing[i][0] for i, v in enumerate(now_showing) if v[1] == 'Hindi']
  baahubali_showtime = filter(re.compile(".*[Bb]aahubali.*").match, movie_names)
  print len(baahubali_showtime) > 0