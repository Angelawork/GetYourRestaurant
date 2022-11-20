import pandas as pd, numpy as np
import requests
import json
import gmplot
import random
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
        labels = ['Place Name','Place ID', 'Latitude', 'Longitude', 'Rating', 'Vicinity', 'Stress']
        export_dataframe_1_medium = pd.DataFrame.from_records(final_data, columns=labels)
        export_dataframe_1_medium.to_csv('export_dataframe_1_medium.csv')
get_List()
target_number = random.randint(0,19)
def drawfile(file, number):
  df = pd.read_csv(file, sep=',',usecols=["Latitude", "Longitude"])
  
  gmap1 = gmplot.GoogleMapPlotter(df.iloc[number]["Latitude"],df.iloc[number]["Longitude"],20)

  gmap1.draw( "achoiceforyou!.html" )

drawfile('export_dataframe_1_medium.csv', target_number)

