from geopy.geocoders import Nominatim


geolocator = Nominatim()
location_fake = geolocator.geocode("Somewhere I belong")
location_real = geolocator.geocode("Pune, India")

if location_fake is None or location_fake.address is None:
    print("we're not including this fake address")
    
else:
    print("we're including this fake address")
    print(location_fake.address)
    print((location_fake.latitude, location_fake.longitude))
    print(location_fake.raw)


if location_real.address is None:
    print("we're not including this real address")
    
else:
    print("we're including this real address")
    print(location_real.address)
    print((location_real.latitude, location_real.longitude))
    print(location_real.raw)