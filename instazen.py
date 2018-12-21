#!/usr/bin/env python3

import urllib.request
import urllib.parse
import sys
import csv
import requests
import json
import requests
from math import sin, cos, sqrt, atan2, radians
from operator import itemgetter
import pickle

api_key = 'AIzaSyALzoro2MmWJmlosX7AVBrm5vFq8U67O0Q'

with open ('outfile', 'rb') as fp:
    dictList = pickle.load(fp)

user_location = input("Enter your location : ")
api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(user_location, api_key))
api_response_dict = api_response.json()
if api_response_dict['status'] == 'OK':
   user_latitude = api_response_dict['results'][0]['geometry']['location']['lat']
   user_longitude = api_response_dict['results'][0]['geometry']['location']['lng']

for d in dictList:
  d['User_longitude'] = user_longitude
  d['User_latitude']  = user_latitude

for d in dictList:
  if 'Latitude' in d:
    radius = 6371  # km
    lat2 = d['Latitude']
    lon2 = d['Longitude']
    lat1 = d['User_latitude']
    lon1 = d['User_longitude']

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (sin(dlat / 2) * sin(dlat / 2) +
         cos(radians(lat1)) * cos(radians(lat2)) *
         sin(dlon / 2) * sin(dlon / 2))
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    dist = radius * c
    d['Distance'] = dist
  else:
    d['Distance'] = 100000.69702662465258

dictListSorted = sorted(dictList, key=itemgetter('Distance'))

for i in range(4):
 d = dictListSorted[i] 
 print("Title : %s , Location: %s , Distance: %s" % (d['Title'], d['Locations'], d['Distance'] ))
