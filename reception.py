from flask import *
from database import *
from datetime import datetime

reception = Blueprint('reception',__name__)
# RECEPTION HOME PAGE ################################################################################################################################################################

@reception.route('/reception_home')
def reception_home():
    return render_template('reception_home.html')





# VIEW DOCTORS #######################################################################################################################################################################

@reception.route('/reception_view_doctors')
def reception_view_doctors():
    data = {}
    qa = "select * from doctors"
    r = select(qa)
    data['view']=r
    return render_template('reception_view_doctors.html',data=data)





# VIEW PAYMENT #######################################################################################################################################################################

@reception.route('/reception_view_payment')
def reception_view_payment():
    data = {}
    qa = "select * from payments inner join booking using(booking_id) inner join patients using(patient_id) where booking.status='paid'"
    r = select(qa)
    data['view']=r
    return render_template('reception_view_payment.html',data=data)






# MANAGE PATIENTS BOOKING ###################################################################################################################################################################

@reception.route('/reception_manage_patients_booking')
def reception_manage_patients_booking():
    data = {}
    qa = "select * from schedule inner join booking using(schedule_id) inner join patients using(patient_id)"
    r = select(qa)
    data['view']=r
    if 'action' in request.args:
        action = request.args['action']
        booking_id = request.args['booking_id']
        session["bookid"]=booking_id

    else:
        action = None
    if action == 'accept':
        q = "update booking set status='ACCEPTED' where booking_id='%s'"%(session["bookid"])
        update(q)
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Accepted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'reception_manage_patients_booking';
        }, 2000); // Redirect after 2 seconds
    </script>
"""
    elif action == 'reject':
        q1 = "update booking set status='REJECTED' where booking_id='%s'"%(session["bookid"])
        update(q1)
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Rejected 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'reception_manage_patients_booking';
        }, 2000); // Redirect after 2 seconds
    </script>
"""
    return render_template('reception_manage_patients_booking.html',data=data)

@reception.route('/reception_add_inpatient_details', methods=['get','post'])
def reception_add_inpatient_details():
    data={}
    patient_id=request.args['patient_id']
    if 'submit' in request.form:
        admssion_date=datetime.now().strftime("%Y-%m-%d")
        purpose=request.form['purpose']
        admitting_relative=request.form['relative']
        contact=request.form['contact']

        g = "insert into inpatients values(null,'%s','%s','%s','pending','%s','%s','admitted')"%(patient_id,admssion_date,purpose,admitting_relative,contact)
        insert(g)
        return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Added Successfully 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'reception_man_inpatients?patient_id={patient_id}';
        }}, 2000); // Redirect after 2 seconds
    </script>
"""


    if 'action' in request.args:
        action=request.args['action']
        in_id=request.args['in_id']
    else:
        action=None

    if action=='update':
        fu="select * from inpatients inner join patients using(patient_id) where in_id='%s'"%(in_id)
        data['updates']=select(fu)

    if 'update' in request.form:
        purpose=request.form['purpose']
        discharge_date=datetime.now().strftime("%Y-%m-%d")
        admitting_relative=request.form['relative']
        contact=request.form['contact']
        status=request.form['status']
        yy = "update inpatients set purpose='%s',discharge_date='%s',admitting_relative='%s',contact='%s',status='%s' where in_id='%s'"%(purpose,discharge_date,admitting_relative,contact,status,in_id)
        update(yy)
        return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'reception_man_inpatients?patient_id={patient_id}';
        }}, 1000); // Redirect after 2 seconds
    </script>
"""


    if action=='delete':
        pu="delete from inpatients where in_id='%s'"%(in_id)
        delete(pu)
        return f"""
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
        </div>
        <script>
        setTimeout(function() {{
            window.location.href = 'reception_man_inpatients?patient_id={patient_id}';
        }}, 1000); // Redirect after  seconds
        </script>
            """

    q="select * from patients where patient_id='%s'"%(patient_id)
    data['patients']=select(q)
    return render_template('reception_add_inpatient_details.html',data=data)




# RECEPTION MAN INPATIENTS ##################################################################################################################################################################

@reception.route('/reception_man_inpatients', methods=['get','post'])
def reception_man_inpatients():
    data={}
    patient_id=request.args['patient_id']
    q="select * from inpatients where patient_id='%s'"%(patient_id)
    data['inpatients']=select(q)
    return render_template('reception_man_inpatients.html',data=data)


# RECEPTION VIEW PATIENTS ##################################################################################################################

@reception.route('/reception_view_patients')
def reception_view_patients():
    data = {}
    qa = "select * from patients"
    r = select(qa)
    data['view']=r
    if 'add' in request.args:
        session['patient_id']=request.args['patient_id']
        q="select * from inpatients where patient_id='%s'"%(session['patient_id'])
        res=select(q)
        if res:
           return redirect(url_for('reception.reception_man_inpatients',patient_id=session['patient_id']))
        else:
            return redirect(url_for('reception.reception_add_inpatient_details',patient_id=session['patient_id']))
    return render_template('reception_view_patients.html',data=data)



# RECEPTION ADD PATIENTS #################################################################################################################################################################



@reception.route('/reception_add_patients', methods=['get','post'])
def reception_add_patients():
    data={}
    if 'submit' in request.form:
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        email = request.form['email']
        house_name = request.form['house_name']
        place = request.form['place']
        gender = request.form['gender']
        blood = request.form['blood']
        date = request.form['dob']
        username = request.form['username']
        password = request.form['password']

        f = "insert into login values(null,'%s','%s','patients')"%(username, password)
        t = insert(f)
        g = "insert into patients values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(t, fname, lname, phone, email, house_name, place, gender, blood, date)
        insert(g)
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Added Successfully 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'reception_add_patients';
        }, 2000); // Redirect after 2 seconds
    </script>
"""

    qa = "select * from patients"
    data['viewpatients']=select(qa)

    if 'action' in request.args:
        action=request.args['action']
        patient_id=request.args['patient_id']
    else:
        action=None

    if action=='update':
        fu="select * from patients where patient_id='%s'"%(patient_id)
        data['updates']=select(fu)

    if 'update' in request.form:
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        email = request.form['email']
        house_name = request.form['house_name']
        place = request.form['place']
        blood = request.form['blood']
        date = request.form['date']

        yy = "update patients set first_name='%s',last_name='%s',phone='%s',email='%s',house_name='%s',place='%s',blood_group='%s',dob='%s' where patient_id='%s'"%(fname,lname,phone,email,house_name,place,blood,date,patient_id)
        update(yy)
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'reception_add_patients';
        }, 2000); // Redirect after 2 seconds
    </script>
"""
                
    if action=='delete':
        f = "delete from patients where patient_id='%s'"%(patient_id)
        delete(f)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'reception_add_patients';
        }, 2000); // Redirect after 2 seconds
        </script>
            """

    return render_template('reception_add_patients.html',data=data)

