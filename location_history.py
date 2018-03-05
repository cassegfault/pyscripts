# Generates a heatmap based on location history
# For use with google location data
from collections import defaultdict
import math
import json

location_data = None
with open('location_history.json') as jfile:
    location_data = json.loads(jfile.read())

# Thanks https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(math.radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a)) 
    r = 6371.008 # earth's Radius in KM
    return c * r


with open('locations.json','w+') as jfile:
    ls = defaultdict(lambda: 0)
    for l in location_data['locations']:
        ls[str(l['latitudeE7'])+','+str(l['longitudeE7'])] += 1
    nls = []
    for k,v in ls.iteritems():
        los = k.split(',')
        lng = los[1]
        lat = los[0]
        nls.append({
            'lat': float(lat) / 10000000.0,
            'lng': float(lng) / 10000000.0,
            'count': v
        })
    jfile.write(json.dumps({'max': max(nls, key=lambda i: i['count'])['count'], 'data':nls }))
