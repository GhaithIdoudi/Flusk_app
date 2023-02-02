import requests

def combine_coordinates(latitudes, longitudes):
    response = requests.post('http://localhost:5000/coordinate_combiner', data={
        'latitudes': latitudes,
        'longitudes': longitudes
    })
    return response.text

if __name__ == '__main__':
    latitudes = [31.24,-2.34,45.12,12.56]
    longitudes = [-20.18, -10.15, 2.41]
    merged = combine_coordinates(latitudes, longitudes)
    print(merged)