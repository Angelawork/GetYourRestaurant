import pandas as pd, numpy as np
import requests
import json
import random
#import gmplot
import time
final_data = []
# Parameters
coordinates = ['45.505143,-73.577356']
keywords = ['restaurant']
radius = '2000'
api_key = 'AIzaSyAbQf2o1IyCiw55jhFCzaTkmsaRpQlQHac'
def get_List():
  for coordinate in coordinates:
    for keyword in keywords:
      url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+coordinate+'&radius='+str(radius)+'&keyword='+str(keyword)+'&key='+str(api_key)
    for i in range(1):
      print(url)
      respon = requests.get(url)
      jj = json.loads(respon.text)
      results = jj['results']
      for result in results:
        name = result['name']
        place_id = result ['place_id']
        lat = result['geometry']['location']['lat']
        lng = result['geometry']['location']['lng']
        rating = result['rating']
        types = result['types']
        vicinity = result['vicinity']
        data = [name, place_id, lat, lng, rating, types, vicinity]
        final_data.append(data)
        labels = ['Place Name','Place ID', 'Latitude', 'Longitude', 'Rating', 'Vicinity', 'Address']
        export_dataframe_1_medium = pd.DataFrame.from_records(final_data, columns=labels)
        export_dataframe_1_medium.to_csv('export_dataframe_1_medium.csv')

get_List()

index = random.randint(0,19)
df = pd.read_csv('export_dataframe_1_medium.csv')
r_name = df.iloc[index]['Place Name']
r_address = df.iloc[index]['Address']
r_rating = df.iloc[index]['Rating']
r_lat = df.iloc[index]['Latitude']
r_lnt = df.iloc[index]['Longitude']
print(r_name,end='')
print(",", end=' ')
print(r_rating,end='')
print(",", end=' ')
print(r_address)
