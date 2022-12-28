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


class List(Resource):

    def get(self, id):
        print("-------get-------",id)
        movie_id = Movie.query.filter_by(id=id).first()
        if not movie_id:
            return {"message":"Movie doesn't exists"}
        print("-------movie_id-------", movie_id)
        return movie_id.json()

    def delete(self, id):
        data = request.get_json()
        print("---------------delete---------",id)
        movie_id = Movie.query.filter_by(id=id).first()
        print("🚀 ~ file: routes.py:46 ~ movie_id", movie_id)
        if not movie_id:
            return {"message": "Movie doesn't exists"}
        print("--------restaurant111-------",movie_id)
        # movie_id.delete()
        db.session.delete(movie_id)
        db.session.commit()
        print('------------- deleted-------------------')
        return f'Movie deleted'

    def put(self, id):
        movie_id = Movie.query.filter_by(id=id).first()
        print("------------movie_id--put---------",movie_id)
        data = request.get_json()
        print("----------data--------",data)
        if data.get('title'):
            movie_id.title = data['title']
        if data.get('rating'):
            movie_id.rating = data['rating']
        db.session.add(movie_id)
        db.session.commit()
        return 'updated'



api.add_resource(Movies, '/movie'),
api.add_resource(List, '/movie/<int:id>')