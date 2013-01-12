#!/usr/bin/env python
import sys
from optparse import OptionParser
from getpath import make_url

def main():
  args = sys.argv

  parser = OptionParser()
  usage = "usage: %prog [options] origin destination"
  parser = OptionParser(usage=usage)
  parser.add_option("-m", "--mode", action="store", dest="mode", help="specifies type of transportation desired", default="driving")
  parser.add_option("-u", "--units", action="store", dest="units", help="specifies choice between metric and imperial systems")
  parser.add_option("-s", "--sensor", action="store", dest="sensor", default="false")
  parser.add_option("-a", "--arrival", action="store", dest="arrival_time", help="specifies desired time of arrival. can be stated in natural language")
  parser.add_option("-d", "--departure", action="store", dest="departure_time", help="specifies desired time of departure. can be stated in natural language")
  parser.add_option("-e", "--evade", action="store", dest="avoid", help="specifies choice in avoiding tolls or highways")

  (options, args) = parser.parse_args(args)
  if len(args) != 3:
    parser.error("Incorrect number")
  make_url(parser, options, args)

main()
