#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route("/")
def home():
    return "<h1>Zoo app</h1>"


@app.route("/animal/<int:id>")
def animal_by_id(id):
    animal = Animal.query.filter(Animal.id == id).first()

    # response_body = f"""
    #         <ul>Information for {animal.name}</ul>
    #         <ul>Animal species is {animal.species}</ul>
    #         <ul>Zookeeper name is {animal.zookeeper.name}</ul>
    #         <ul>Enclosure environment is {animal.enclosure.environment}</ul>
    # """

    response_body = f"""
                <ul>Name</ul>
                <ul>Species</ul>  
                <ul>Zookeeper</ul>
                <ul>Enclosure</ul>
             """
    response = make_response(response_body, 200)
    return response


@app.route("/zookeeper/<int:id>")
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Zookeeper.id == id).first()

    # response_body = f"""
    #         <ul>Zookeeper name: {zookeeper.name}</ul>
    #         <ul>Zookeeper DOB: {zookeeper.birthday}</ul>
    # """

    response_body = f"""
                <ul>Name</ul>
                <ul>Birthday</ul>
                <ul>Animal</ul>
              """

    response = make_response(response_body, 200)
    return response


@app.route("/enclosure/<int:id>")
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id == id).first()

    # response_body = f"""
    #         <ul>Enclosure environment: {enclosure.environment}</ul>
    #         <ul>Is it open to visitors: {enclosure.open_to_visitors}</ul>
    # """

    response_body = f"""
            <ul>Environment</ul>
            <ul>Open To Visitors</ul>
            <ul>Animal</ul>
           """
    response = make_response(response_body, 200)
    return response


if __name__ == "__main__":
    app.run(port=5555, debug=True)
