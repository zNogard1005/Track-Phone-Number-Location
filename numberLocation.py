import folium
import phonenumbers

from myPhone import number

from phonenumbers import geocoder
from phonenumbers import carrier

# Warning
# key = "you can get key in: https://opencagedata => search: How to get key Api opencagedata"

# Get Nation
samNumber = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(samNumber, "en")
print("Your Location: ", yourLocation)


service_provider = phonenumbers.parse(number)
# MNO = Mobile netword operator
yourMNO = carrier.name_for_number(service_provider, "en")
print("Your Mobile network operator: ", yourMNO)

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(key)

query = str(yourLocation)

results = geocoder.geocode(query)
# print(results)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=10)

folium.Marker([lat, lng], popup=yourLocation).add_to((myMap))

## Save Map

myMap.save("Location_1.html")

