#Flask code for backend
from flask import Flask, jsonify
import requests
from flask_cors import CORS, cross_origin
import click
import os

api_key=os.getenv("API_KEY")
CORS_URL="*"
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#Route to fetch all entries from TMDB API and send it to the front end
@app.route('/', methods=['GET'])
@cross_origin(CORS_URL)
def get_tmdb_details():
    top_20_movies=[] 
    response=requests.get("https://api.themoviedb.org/3/trending/all/day?api_key=8d3919f74770a189380a6856038cb0b1").json()
    for iter in response["results"][:20]:
        top_20_movies.append(iter)
    click.echo(f"{str(len(top_20_movies))}")
    movie_names=[]
    for iter in top_20_movies:
        single_movie={}
        single_movie["rating"]=iter["vote_average"]
        if iter["media_type"]=="movie":
            single_movie["name"]=iter["title"]
        else:
            single_movie["name"]=iter["name"]
        click.echo("movie name is "+single_movie["name"]+"")
        movie_names.append(single_movie)
    return(jsonify(movie_names))


#Running the app
app.static_folder = 'static'
app.debug = True
app.run(host='0.0.0.0')
