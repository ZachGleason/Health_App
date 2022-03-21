from health_app import app
from health_app.controllers import users
from health_app.controllers import meals
from health_app.controllers import vitamins
from health_app.controllers import workouts

if __name__ == '__main__':
    app.run(debug = True)