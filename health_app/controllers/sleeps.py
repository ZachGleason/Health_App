from flask import render_template, request, redirect, session, flash
from health_app.models.user import User
from health_app.models.meal import Meal
from health_app.models.vitamin import Vitamin
from health_app.models.workout import Workout
from health_app.models.sleep import Sleep
from health_app import app

@app.route('/add/sleep/<int:id>')
def new_sleep(id):
    data ={
        "id":id
    }
    return render_template("new_sleep.html", user=User.get_by_id(data))

@app.route('/process/sleep/<int:id>',  methods=["POST"])
def process_sleep(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "sleep_time": request.form["sleep_time"],
        "deep_sleep": request.form["deep_sleep"],
        "heart_rate": request.form["heart_rate"],
        "date": request.form["date"],
        "user_id": session["user_id"]
    }
    Sleep.new_sleep(data)
    return redirect('/dashboard')

@app.route('/delete/sleep/<int:id>')
def remove_sleep(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Sleep.delete_sleep(data)
    return redirect('/dashboard')