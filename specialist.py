from flask import *
from database import *
from datetime import datetime

specialist = Blueprint("specailist",__name__)

@specialist.route('/specialist_home',methods = ['get','post'])
def specialist_home():
    return render_template('specialist_home.html')

@specialist.route("/view_request",methods = ['get','post'])
def view_request():
    data={}
    q = "SELECT * ,CONCAT (`doctors`.`first_name`,' ',`doctors`.`last_name`) AS doctor_name,`request`.`status` AS viewstatus ,`request`.`date_time` AS viewdatetime,CONCAT (`patients`.`first_name`,' ',`patients`.`last_name`) AS patient_name FROM `request` INNER JOIN `booking` USING(`booking_id`)INNER JOIN `schedule` USING(`schedule_id`)INNER JOIN `doctors` USING(`doctor_id`) INNER JOIN `patients` USING(`patient_id`)"
    data['view'] = select(q)
    if 'action' in request.args:
        action=request.args['action']
        request_id=request.args['request_id']
    else:
        action=None
    if action=='accept':
        q="update request set status='accepted' where request_id='%s'"%(request_id)
        update(q)
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'view_request';
        }, 2000); // Redirect after 2 seconds
    </script>
"""
    elif action=='reject':
        q = "update request set status ='rejected' where request_id= '%s'"%(request_id)
        update(q)
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'view_request';
        }, 2000); // Redirect after 2 seconds
    </script>
"""
    return render_template('view_request.html',data=data)

 
@specialist.route('/view_patient_history',methods=['get','post'])
def view_patient_history():
    data = {}
    session['booking_id']=request.args['booking_id']
    q = "select * from medical_notes where booking_id = '%s'"%(session['booking_id'])
    select(q)
    data['view']=select(q)

    return render_template('view_patient_history.html',data=data)

@specialist.route('/view_consultant_patient',methods=['get','post'])
def view_consultant_patient():
    date = datetime.now().strftime("%Y-%m-%d")
    if 'submit' in request.form:
        description = request.form['description']
        q = " insert into medical_notes values(Null,'%s','%s','%s')"%(session['booking_id'],description,date)
        insert(q)
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'view_request';
        }, 2000); // Redirect after 2 seconds
    </script>
"""
    return render_template('view_consultant_patient.html')


@specialist.route('/add_prescription',methods=['get','post'])
def add_prescription():
    data = {}
    q = " Select * from medicines"
    select(q)
    data['view']=select(q)
    date = datetime.now().strftime("%Y-%m-%d")
    if "submit" in request.form:
        medicine_id = request.form['medicine_id']
        description = request.form['description']
        q="select * from medicines where medicine_id='%s'"%(medicine_id)
        res=select(q)
        qty=res[0]['available_qty']
        if int(qty)>0:
            q = "insert into prescription values(Null,'%s','%s','%s','%s','pending')"%(session['booking_id'],medicine_id,date,description)
            insert(q)
            q="update medicine_stock set quantity=quantity-1 where medicine_id='%s'"%(medicine_id)
            update(q)
            qi="update medicines set available_qty=available_qty-1 where medicine_id='%s'"%(medicine_id)
            update(qi)

           
            return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Added 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'view_request';
        }, 2000); // Redirect after 2 seconds
    </script>
"""
        else:
            return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;"> out of stock 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'view_request';
        }, 2000); // Redirect after 2 seconds
    </script>
"""
    return render_template("add_prescription.html",data=data)

