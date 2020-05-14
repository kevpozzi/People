from flask import Blueprint, jsonify, make_response

from src.people.service.peopleService import peopleService

people_api = Blueprint('people_api', __name__)

@people_api.route('/people')
def getPeople():
    people = peopleService.getPeople()
    return make_response(jsonify(people), 200)