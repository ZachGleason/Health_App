from flask import render_template, request, redirect, session, flash
from health_app.models.user import User
from health_app.models.meal import Meal
from health_app.models.vitamin import Vitamin
from health_app.models.workout import Workout
from health_app import app

@app.route('/add/meal/<int:id>')
def new_meal(id):
    data ={
        "id":id
    }
    return render_template("new_meal.html", user=User.get_by_id(data))

@app.route('/add/<int:id>',  methods=["POST"])
def process_meal(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "meal_name": request.form["meal_name"],
        "calories": request.form["calories"],
        "protein": request.form["protein"],
        "notes": request.form["notes"],
        "meal_date": request.form["meal_date"],
        "user_id": session["user_id"]
    }
    Meal.new_meal(data)
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Meal.delete_meal(data)
    return redirect('/dashboard')
