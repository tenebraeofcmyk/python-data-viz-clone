from geopy.geocoders import Nominatim
import pandas as pd
import time

# Load your data
data = pd.read_csv('data-h5n1.csv')

# Initialize geocoder
geolocator = Nominatim(user_agent="geoapiExercises")

# Function to get coordinates
def get_coordinates(location):
    try:
        time.sleep(0.3)  # to comply with rate limiting
        print(location)
        return geolocator.geocode(location)
    except:
        return None

# Unique county-state combinations
unique_locations = data[['County', 'State']].drop_duplicates()
unique_locations['Location'] = unique_locations['County'] + ', ' + unique_locations['State']

# Geocode locations
unique_locations['Coordinates'] = unique_locations['Location'].apply(get_coordinates)
unique_locations['Latitude'] = unique_locations['Coordinates'].apply(lambda loc: loc.latitude if loc else None)
unique_locations['Longitude'] = unique_locations['Coordinates'].apply(lambda loc: loc.longitude if loc else None)

print(unique_locations)

# Merge coordinates back into original data
data = data.merge(unique_locations[['Location', 'Latitude', 'Longitude']], on='Location', how='left')

# Save the updated DataFrame to a new CSV file
data.to_csv('updated_data.csv', index=False)
