from flask import *
from database import *
from public import public
from patients import patient
from ambulance import ambulance
from doctors import doctors
from laboratory import laboratory
from pharmacy import pharmacy
from specialist import specialist
from admin import admin 
from department import department
from reception import reception



app=Flask(__name__)
app.register_blueprint(public)
app.register_blueprint(admin)
app.register_blueprint(patient)
app.register_blueprint(ambulance)
app.register_blueprint(doctors)
app.register_blueprint(laboratory)
app.register_blueprint(pharmacy)
app.register_blueprint(specialist)
app.register_blueprint(department)
app.register_blueprint(reception)


app.secret_key='syam'

app.run(debug=True,port=5754) 