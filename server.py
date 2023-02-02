from flask import Flask, request
app = Flask(__name__)

def coordinate_combiner(latitudes, longitudes):
    result = []
    for lat, lon in zip(latitudes, longitudes):
        if lon <= 0:
            lon = "WEST"
        result.append((lat, lon))
    return result

@app.route('/coordinate_combiner', methods=['POST'])

def combine_coordinates():
    latitudes = request.form.getlist('latitudes')
    longitudes = request.form.getlist('longitudes')
    latitudes = [float(lat) for lat in latitudes]
    longitudes = [float(lon) for lon in longitudes]
    result = coordinate_combiner(latitudes, longitudes)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)