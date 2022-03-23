from health_app.config.mysqlconnection import connectToMySQL

class Meal:
    def __init__(self,data):
        self.id = data["id"]
        self.meal_name = data["meal_name"]
        self.calories = data["calories"]
        self.protein = data["protein"]
        self.notes = data["notes"]
        self.meal_date= data["meal_date"]
        self.user_id = data["user_id"]

    @classmethod
    def new_meal(cls,data):
        query = "INSERT INTO meals (meal_name, calories, protein, notes, meal_date, user_id) VALUES (%(meal_name)s, %(calories)s, %(protein)s, %(notes)s, %(meal_date)s, %(user_id)s);"
        return connectToMySQL("fitness").query_db(query, data)

    @classmethod
    def get_all_meals(cls):
        query = "SELECT * FROM meals;"
        results = connectToMySQL("fitness").query_db(query)
        all_meals = []
        for row in results:
            all_meals.append( cls(row) )
        return all_meals

    @classmethod
    def delete_meal(cls,data):
        query = "DELETE FROM meals WHERE id = %(id)s;"
        return connectToMySQL("fitness").query_db(query, data)