import pandas as pd
from geopy.geocoders import GoogleV3

def get_coordinates_by_zip(api_key, zip_code):
    geolocator = GoogleV3(api_key=api_key)

    try:
        location = geolocator.geocode(zip_code, components={"country": "US"})  # Adjust the country code if needed
        if location:
            return location.latitude, location.longitude
        return None
    except Exception as e:
        print(f"Error geocoding {zip_code}: {e}")
        return None


df = pd.read_excel('output_with_zip_codes_4.xlsx')

api_key = 'redacted'

df[['latitude', 'longitude']] = df['zip_code'].apply(lambda x: pd.Series(get_coordinates_by_zip(api_key, x) if get_coordinates_by_zip(api_key, x) else [None, None]))

# Save the updated DataFrame to a new Excel file
df.to_excel('/Users/christiangentry/Documents/gulp_v2/output_with_coordinates_by_zip.xlsx', index=False)