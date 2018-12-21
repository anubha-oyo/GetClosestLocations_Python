#!/usr/bin/env python3

import urllib.request
import urllib.parse
import sys
import csv
import requests
import json
import requests
import pickle

dictList = []
input_file = csv.DictReader(open("Film_Locations_in_San_Francisco.csv"))
for row in input_file:
    dictList.append(row)

for d in dictList:
  location = d['Locations']
  api_key = 'AIzaSyALzoro2MmWJmlosX7AVBrm5vFq8U67O0Q'
  api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(location, api_key))
  api_response_dict = api_response.json()
  if api_response_dict['status'] == 'OK':
    latitude = api_response_dict['results'][0]['geometry']['location']['lat']
    longitude = api_response_dict['results'][0]['geometry']['location']['lng']
    d['Latitude'] = latitude
    d['Longitude'] = longitude

with open('outfile', 'wb') as fp:
    pickle.dump(dictList, fp)
