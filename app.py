from flask import Flask, jsonify, request
from flask_cors import CORS
import hack

app = Flask(__name__)

CORS(app)

@app.route('/')

def index():
    artist = request.args.get('artist')
    song = request.args.get('song') 
   
    response = jsonify(hack.getSong(artist, song))

    return response
