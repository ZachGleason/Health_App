from health_app.config.mysqlconnection import connectToMySQL

class Workout:
    def __init__(self,data):
        self.id = data["id"]
        self.workout_name = data["workout_name"]
        self.date = data["date"]
        self.time_lasted = data["time_lasted"]
        self.calorie_count = data["calorie_count"]
        self.notes = data["notes"]
        self.user_id = data["user_id"]

    @classmethod
    def new_workout(cls,data):
        query = "INSERT INTO fitness (workout_name, date, time_lasted, calorie_count, notes, user_id) VALUES (%(workout_name)s, %(date)s, %(time_lasted)s, %(calorie_count)s, %(notes)s, %(user_id)s);"
        return connectToMySQL("fitness").query_db(query, data)

    @classmethod
    def get_all_workouts(cls):
        query = "SELECT * FROM fitness;"
        results = connectToMySQL("fitness").query_db(query)
        all_workouts = []
        for row in results:
            all_workouts.append( cls(row) )
        return all_workouts

    @classmethod
    def delete_workout(cls,data):
        query = "DELETE FROM fitness WHERE id = %(id)s;"
        return connectToMySQL("fitness").query_db(query, data)
