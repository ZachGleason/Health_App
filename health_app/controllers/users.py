from flask import render_template, request, redirect, session, flash
from health_app.models.user import User
from health_app.models.meal import Meal
from health_app.models.vitamin import Vitamin
from health_app.models.workout import Workout
from crypt import methods
from health_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def register():
    return render_template("home.html")

@app.route('/login')
def main():
    return render_template("login.html")

@app.route('/register')
def link():
    return render_template("register.html")

@app.route('/register/user', methods=["POST"])
def register_user():
    if not User.validate_user(request.form):
        return redirect('/')
    data ={
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']),
        "age": request.form['age'],
        "weight": request.form['weight'],
        "location": request.form['location'],
        "gender": request.form['gender'],
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect('/login')

@app.route('/process', methods=["POST"])
def login():
    user = User.get_email(request.form)
    if not user:
        flash("Invalid Email","login")
        return redirect('/login')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/login')
    session['user_id'] = user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html", meals=Meal.get_all_meals(), user=User.get_by_id(data), workouts=Workout.get_all_workouts(), vitamins=Vitamin.get_all_vitamins())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')