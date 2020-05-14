from src.dbConnection import cursor

class PeopleRepo:
    def queryPeople(self):
        cursor.execute("SELECT * FROM People")
        result = cursor.fetchall()
        return result

peopleRepo = PeopleRepo()
