Googmaps : Command line client for Google Maps

Quick project I put together using the Google Maps API to quickly grab directions. I will be adding more features as time goes on

FEATURES
=============
- Natural language support for departure/arrival times
- Ability to specify desired mode of transport (biking, transit, driving)
- Option to avoid roads
- Linking to actual page in case you wanna look at a map

More to come..

Usage: main.py [options] origin destination

Options:
  -h, --help                                      show this help message and exit
  -m MODE, --mode=MODE                            specifies type of transportation desired
  -u UNITS, --units=UNITS                         specifies choice between metric and imperial systems
  -s SENSOR, --sensor=SENSOR
  -a ARRIVAL_TIME, --arrival=ARRIVAL_TIME         specifies desired time of arrival. can be stated in natural language
  -d DEPARTURE_TIME, --departure=DEPARTURE_TIME   specifies desired time of departure, can be stated in natural language
  -e AVOID, --evade=AVOID                         specifies choice in avoiding tolls or highways

