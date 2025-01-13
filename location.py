import geocoder

def get_current_location():
    current_location = geocoder.ip("me")
    if current_location.latlng:
        latitude, longitude = current_location.latlng
        address = current_location.address
        return latitude, longitude, address
    else:
        return None

def get_coordinates_from_address(address):
    location = geocoder.osm(address)
    if location.latlng:
        return location.latlng
    else:
        return None