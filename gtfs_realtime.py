from google.transit import gtfs_realtime_pb2
import urllib

feed = gtfs_realtime_pb2.FeedMessage()
response = urllib.request.urlopen('http://realtime.cota.com/TMGTFSRealTimeWebService/Vehicle/VehiclePositions.pb')
feed.ParseFromString(response.read())
print(feed.entity) # prints entire feed. Code after this prints each vehicle in feed
"""
for entity in feed.entity:
    if entity.HasField('trip_update'):
        print(entity.trip_update)
"""
