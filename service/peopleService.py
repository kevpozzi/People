from src.people.repo.peopleRepo import peopleRepo

class PeopleService:
    def getPeople(self):
        queryData = peopleRepo.queryPeople()
        peopleList = [{
            'id': person.id,
            'name': person.fullname,
            'age': person.age,
            'attribute': person.bestattribute
        } for person in queryData]

        return peopleList

peopleService = PeopleService()