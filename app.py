import os
from flask import Flask, flash, request, redirect, url_for, render_template, send_file, jsonify, session
import datetime
import requests
import json
from io import BytesIO

app = Flask(__name__)

@app.route('/house_image/<string:parcel>', methods = ['GET'])
def home_stats(parcel):
    parcel = parcel
    return parcel

@app.route('/')
def upload_form():
	return render_template('map.html')

@app.route('/map_usage/<string:z>/<string:x>/<string:y>.png', methods=['GET'])
def get_tiles(z,x,y):
    URL = "http://b.tile.stamen.com/toner/"+z+"/"+x+"/"+y+".png"
    r = requests.get(url = URL, stream=False) 
    return send_file(BytesIO(r.content), attachment_filename='map_tile.png', mimetype='image/png')

if __name__ == '__main__':
    
    app.secret_key = os.urandom(12)
    app.run(host='localhost',debug = True)
	
	 #ssl_context=("cert.pem", "key.pem"), 
    