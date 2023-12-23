import pandas as pd
from geopy.geocoders import GoogleV3

def get_zip_code(api_key, business_name):
    geolocator = GoogleV3(api_key=api_key)

    try:
        location = geolocator.geocode(business_name)
        if location:
            for component in location.raw.get('address_components', []):
                if 'postal_code' in component['types']:
                    return component['long_name']
        return None
    except Exception as e:
        print(f"Error geocoding {business_name}: {e}")
        return None


df = pd.read_excel('brewery_zips_empty2.xlsx')


api_key = 'redacted for privacy'


df['zip_code'] = df['brewery'].apply(lambda x: get_zip_code(api_key, x))

df.to_excel('output_with_zip_codes.xlsx', index=False)


