import requests, simplejson, re
from termcolor import colored, cprint

def sanitize(sentence):
  result = re.sub('<.*?>', '', sentence.encode('ascii', 'ignore'))
  return result


def print_path(url):
  print url
  resp = requests.get(url)
  myjson= simplejson.loads(resp.text)
  keypoints = myjson['routes'][0]['legs'][0]

  print "From: " + keypoints['start_address']
  print "To: " + keypoints['end_address']
  print "Distance: " + keypoints['distance']['text']
  print "Duration: " + keypoints['duration']['text'] 

  warnings = myjson['routes'][0]['warnings']
  if warnings:
    cprint ("\nWarnings:", 'red')
    for warning in warnings:
      cprint ("- " + sanitize(warning), 'red')

  print "\n"
  
  steps, linenum = keypoints['steps'], 1
  for step in steps:
    instruction = sanitize(step['html_instructions'])
    #fix for formatting issue on last line of instructions
    instruction = re.sub('Destination', '. Destination', instruction)
    print str(linenum) + '. ' + instruction
    linenum += 1

