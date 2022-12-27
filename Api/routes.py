from flask_restful import Resource, Api
from Api import api, db
from Api.models import Movie
from flask import request, jsonify
import json


class Movies(Resource):

    def post(self):
        movie_data = request.get_json()
        print("---movie_data--", movie_data)
        movie_exist = Movie.query.filter_by(title=movie_data['title']).first()
        if movie_exist:
            return f'This movie is exists!!'
        new_movie = Movie(title=movie_data['title'], rating=movie_data['rating'])
        print("---new_movie--", new_movie)
        db.session.add(new_movie)
        db.session.commit()
        return new_movie.json()

    def get(self):
        movies = []
        move_list = Movie.query.all()
        for movie in move_list:
            movies.append({'title': movie.title, 'rating': movie.rating})

        return jsonify({'movies': movies})



api.add_resource(Movies, '/movie'),