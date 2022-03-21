from health_app.config.mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from flask import flash

class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.age = data["age"]
        self.weight = data["weight"]
        self.location = data["location"]
        self.gender = data["gender"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results =  connectToMySQL("fitness").query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password, age, weight, location, gender, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(age)s, %(weight)s, %(location)s, %(gender)s, NOW(), NOW() );"
        return connectToMySQL("fitness").query_db(query, data)

    @classmethod
    def get_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results =  connectToMySQL("fitness").query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("fitness").query_db(query,data)
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('fitness').query_db(query, user)
        print(results)
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters","register")
            is_valid= False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters","register")
            is_valid= False
        if len(results) >= 1:
            flash("Email already taken.","register")
            is_valid=False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email!!!","register")
            is_valid=False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters","register")
            is_valid = False
        if not any(char.isdigit() for char in user['password']):
            flash('Password should have at least one number')
            is_valid = False
        if not any(char.isupper() for char in user['password']):
            flash('Password should have at least one uppercase letter')
            is_valid = False
        return is_valid
