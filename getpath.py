import sys, requests, re
from optparse import OptionParser
from printpath import print_path
from termcolor import colored, cprint
import parsedatetime.parsedatetime as pdt
from time import mktime

def make_url(parser, options, args):
  url_end = ''

  if(options.mode == "transit" and not (options.departure_time or options.arrival_time)):
    parser.error("Can't specify transit without either arrival or departure time")
  else:
    if options.avoid not in ["tolls", "highways", None]:
      parser.error("Must specify either tolls or highways to evade")

  cal = pdt.Calendar()

  for key,value in options.__dict__.items():
    if(value != None):
      if key in ["departure_time", "arrival_time"]:
        value = str(int(mktime(cal.parse(value)[0])))
      re.sub(' ', '+', value)
      url_end += key + '=' + value + '&'
  
  origin = re.sub(' ', '+', args[1]) 
  destination = re.sub(' ', '+', args[2])

  cprint ("To view these directions online, follow this link: " + "http://mapof.it/" + origin + '/' + destination, 'cyan')

  base_url = 'http://maps.googleapis.com/maps/api/directions/json?origin=' + origin + '&destination=' + destination + '&'
  
  url = (base_url + url_end)[:-1]
  print_path(url)
