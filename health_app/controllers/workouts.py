from flask import render_template, request, redirect, session, flash
from health_app.models.user import User
from health_app.models.meal import Meal
from health_app.models.vitamin import Vitamin
from health_app.models.workout import Workout
from health_app.models.sleep import Sleep
from health_app import app

@app.route('/add/workout/<int:id>')
def new_workout(id):
    data ={
        "id":id
    }
    return render_template("new_workout.html", user=User.get_by_id(data))

@app.route('/process/<int:id>',  methods=["POST"])
def process_workout(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "workout_name": request.form["workout_name"],
        "date": request.form["date"],
        "time_lasted": request.form["time_lasted"],
        "calorie_count": request.form["calorie_count"],
        "notes": request.form["notes"],
        "user_id": session["user_id"]
    }
    Workout.new_workout(data)
    return redirect('/dashboard')

@app.route('/delete/workout/<int:id>')
def remove(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Workout.delete_workout(data)
    return redirect('/dashboard')