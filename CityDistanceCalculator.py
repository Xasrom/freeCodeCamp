import math

# Haversine formula to calculate the distance between two points on the Earth
def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0
    
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    # Distance in kilometers
    distance = R * c
    
    return distance

# Example usage: coordinates of two cities
city1 = {'lat': 52.5200, 'lon': 13.4050}  # Berlin
city2 = {'lat': 48.8566, 'lon': 2.3522}   # Paris

# Calculate the distance
distance = haversine(city1['lat'], city1['lon'], city2['lat'], city2['lon'])

print(f"Minimum distance between the two cities: {distance:.2f} km")
