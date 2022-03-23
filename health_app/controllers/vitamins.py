from flask import render_template, request, redirect, session, flash
from health_app.models.user import User
from health_app.models.meal import Meal
from health_app.models.vitamin import Vitamin
from health_app.models.workout import Workout
from health_app.models.sleep import Sleep
from health_app import app

@app.route('/add/vitamin/<int:id>')
def new_vitamin(id):
    data ={
        "id":id
    }
    return render_template("new_vitamin.html", user=User.get_by_id(data))

@app.route('/process/vitamin/<int:id>',  methods=["POST"])
def process_vitamin(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        "vitamin_name": request.form["vitamin_name"],
        "dosage": request.form["dosage"],
        "user_id": session["user_id"]
    }
    Vitamin.new_vitamin(data)
    return redirect('/dashboard')

@app.route('/delete/vitamin/<int:id>')
def remove_vitamin(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Vitamin.delete_vitamin(data)
    return redirect('/dashboard')