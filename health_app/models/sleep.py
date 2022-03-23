from health_app.config.mysqlconnection import connectToMySQL

class Sleep:
    def __init__(self,data):
        self.id = data["id"]
        self.sleep_time = data["sleep_time"]
        self.deep_sleep = data["deep_sleep"]
        self.heart_rate = data["heart_rate"]
        self.date = data["date"]
        self.user_id = data["user_id"]
        
    @classmethod
    def new_sleep(cls,data):
        query = "INSERT INTO sleep (sleep_time, deep_sleep, heart_rate, date, user_id) VALUES (%(sleep_time)s, %(deep_sleep)s, %(heart_rate)s, %(date)s, %(user_id)s);"
        return connectToMySQL("fitness").query_db(query, data)

    @classmethod
    def get_all_sleep(cls):
        query = "SELECT * FROM sleep;"
        results = connectToMySQL("fitness").query_db(query)
        all_sleep = []
        for row in results:
            all_sleep.append( cls(row) )
        return all_sleep

    @classmethod
    def delete_sleep(cls,data):
        query = "DELETE FROM sleep WHERE id = %(id)s;"
        return connectToMySQL("fitness").query_db(query, data)