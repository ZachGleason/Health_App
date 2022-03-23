from health_app.config.mysqlconnection import connectToMySQL

class Vitamin:
    def __init__(self,data):
        self.id = data["id"]
        self.vitamin_name= data["vitamin_name"]
        self.dosage = data["dosage"]
        self.user_id = data["user_id"]

    @classmethod
    def new_vitamin(cls,data):
        query = "INSERT INTO vitamins (vitamin_name, dosage, user_id) VALUES (%(vitamin_name)s, %(dosage)s, %(user_id)s);"
        return connectToMySQL("fitness").query_db(query, data)

    @classmethod
    def get_all_vitamins(cls):
        query = "SELECT * FROM vitamins;"
        results = connectToMySQL("fitness").query_db(query)
        all_vitamins = []
        for row in results:
            all_vitamins.append( cls(row) )
        return all_vitamins

    @classmethod
    def delete_vitamin(cls,data):
        query = "DELETE FROM vitamins WHERE id = %(id)s;"
        return connectToMySQL("fitness").query_db(query, data)