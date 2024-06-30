from flask import Flask
from flask_cors import CORS
from app.database import init_app
from app.views import *

app=Flask(__name__)

init_app(app)

CORS(app)

# Rutas de la API-REST
app.route('/', methods=['GET'])(index)
app.route('/api/movies/', methods=['POST'])(create_movie)
app.route('/api/movies/', methods=['GET'])(get_all_movies)
app.route('/api/movies/<int:movie_id>', methods=['GET'])(get_movie)
app.route('/api/movies/<int:movie_id>', methods=['PUT'])(update_movie)
app.route('/api/movies/<int:movie_id>', methods=['DELETE'])(delete_movie)

if __name__ == '__main__' :
    app.run(debug=True)



# @app.route('/')
# def index() :
#     return 'Hola desde flask'

# @app.route('/hello')
# def saludo() :
#     return 'Buenas tardes'
