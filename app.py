from objectDetector import Detector
from flask import Flask, render_template, request, Response, jsonify
import os
from flask_cors import CORS, cross_origin
from utils import decodeImage
import appConfig as CONFIG

app = Flask(__name__)

detector = Detector(filename=CONFIG.IMG_IN)

RENDER_FACTOR = 35

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, CONFIG.IMG_IN)
        result = detector.inference(CONFIG.IMG_IN)
        detector.clean_up()

    except ValueError as val:
        print(val)
        return Response("Value not found inside  json data")
    except KeyError:
        return Response("Key value error incorrect key passed")
    except Exception as e:
        print(e)
        result = "Invalid input"
    return jsonify(result)


# port = int(os.getenv("PORT"))
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=CONFIG.PORT)
