from flask import *
from database import *
from datetime import datetime
import random

patient=Blueprint('patient',__name__)

@patient.route('/patient_home')
def patient_home():
    return render_template('patient_home.html')

@patient.route('/patients_view_doctors')
def patients_view_doctors():
    data={}
    qa="select * from doctors"
    res=select(qa)
    data['view']=res
    return render_template('patients_view_doctors.html',data=data)

@patient.route('/view_schedule',methods=['get','post'])
def view_schedule():
    data={}
    id=request.args['id']
    qa="select * from schedule where doctor_id='%s'"%(id)
    res=select(qa)
    data['view']=res
    print(data['view'],'/////////////////////////')
    return render_template('patient_view_schedule.html',data=data)

@patient.route('/book_doctor',methods=['get','post'])
def book_doctor():
    id=request.args['id']
    qa="select * from booking where schedule_id='%s' and patient_id='%s' and date_time=curdate()"%(id,session['pid'])
    res=select(qa)
    if res:
        return render_template('popup.html')
    else:
        qa="insert into booking values(NULL,'%s','%s',curdate(),'pending')"%(id,session['pid'])
        insert(qa)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
            <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
            <h3 style="color:red;">Successfully Booked 😄</h3>
        </div>
        <script>
            setTimeout(function() {
                window.location.href = 'patients_view_doctors';
            }, 2000); // Redirect after 2 seconds
       </script>
    """

@patient.route('/view_my_bookings')
def view_my_bookings():
    data={}
    type='doctor_payment'
    qa="select * from booking inner join schedule using(schedule_id) inner join doctors using(doctor_id) where patient_id='%s'"%(session['pid'])
    res=select(qa)
    data['view']=res
    return render_template('patient_view_my_bookings.html',data=data,type=type)


@patient.route('/view_invoice',methods=['get','post'])
def view_invoice():
    data={}
    sum=0
    id=request.args['id']
    qa="select * from booking where booking_id='%s'"%(id)
    res=select(qa)
    pid=res[0]['patient_id']
    q1="select * from patients  where patient_id='%s'"%(pid)
    r1=select(q1)
    data['patient']=r1
    q2="select * from payments where booking_id='%s'"%(id)
    r2=select(q2)
    data['pay']=r2
    for i in r2:
        amt=i['amount']
        print(amt)
        sum=int(sum)+int(amt)
    print(sum,'/////////////////////')
    today=datetime.now().date()
    rand=random.randint(100000,999999)
    return render_template('invoice.html',data=data,today=today,rand=rand,id=id,sum=sum)

@patient.route('/view_prescription',methods=['get','post'])
def view_prescription():
    data={}
    id=request.args['id']
    qa="SELECT *,`prescription`.description AS pres_desc FROM prescription INNER JOIN medicines USING(medicine_id) WHERE booking_id='%s'"%(id)
    res=select(qa)
    data['view']=res
    type='prescription_payment'
    return render_template('patient_view_prescription.html',data=data,type=type)


@patient.route('/view_test_prescription',methods=['get','post'])
def view_test_prescription():
    data={}
    id=request.args['id']
    qa="select * from test_prescription inner join lab_test using(test_id) where booking_id='%s'"%(id)
    res=select(qa)
    data['view']=res
    q1="select * from payments where booking_id='%s' and payment_type='test_prescription_payment'"%(id)
    r1=select(q1)
    data['val']=r1
    type='test_prescription_payment'
    return render_template('patient_view_test_prescription.html',data=data,type=type)

@patient.route('/request_ambulance',methods=['get','post'])
def request_ambulance():
    data={}
    q2="select * from ambulance_request where patient_id='%s'"%(session['pid'])
    ra=select(q2)
    data['view']=ra
    q1="select * from ambulances where status='active'"
    res=select(q1)
    data['amb']=res

    if 'submit' in request.form:
        amb=request.form['amb']
        date=request.form['date']
        q3="select * from ambulance_request where ambulance_id='%s' and patient_id='%s' and `date`='%s'"%(amb,session['pid'],date)
        print(q3)
        r3=select(q3)
        print(r3)
        if r3:
            return render_template('pop.html')
        else:
            qa="insert into ambulance_request values(NULL,'%s','%s','pending','%s',curtime())"%(session['pid'],amb,date)
            insert(qa)
            return """
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
                <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
                <h3 style="color:red;">Successfully Requested 😄</h3>
            </div>
            <script>
                setTimeout(function() {
                    window.location.href = 'request_ambulance';
                }, 2000); // Redirect after 2 seconds
           </script>
        """
    
    return render_template('patient_request_ambulance.html',data=data)


@patient.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()

    sql = f"SELECT * FROM doctors WHERE LOWER(first_name) LIKE CONCAT('%', '{query}', '%') OR LOWER(last_name) LIKE CONCAT('%', '{query}', '%') OR LOWER(place) LIKE CONCAT('%', '{query}', '%') OR LOWER(email) LIKE CONCAT('%', '{query}', '%')"

    results = select(sql)
    print(results)

    return jsonify(results)


@patient.route('/make_payment',methods=['get','post'])
def make_payment():
    data={}
    q1="select * from patients where patient_id='%s'"%(session['pid'])
    r1=select(q1)
    data['deta']=r1
    id=request.args['id']
    type=request.args['type']
    amt=request.args['amt']

    qa="select * from payments where booking_id='%s' and payment_type='%s'"%(id,type)
    res=select(qa)
    if res:
        return render_template('pop_pay.html')
    else:
        if 'pay' in request.form:
            qa="insert into payments values(NULL,'%s','%s',curdate(),'%s','paid')"%(id,amt,type)
            insert(qa)
            q3="update booking set status='paid' where booking_id='%s'"%(id)
            update(q3)
            return """
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
                <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
                <h3 style="color:red;">Successfully Paid 😄</h3>
            </div>
            <script>
                setTimeout(function() {
                    window.location.href = 'view_my_bookings';
                }, 2000); // Redirect after 2 seconds
           </script>
        """
    return render_template('patient_make_payment.html',amt=amt,data=data)


@patient.route("/patient_to_doctor_chat",methods=['get','post'])
def patient_to_doctor_chat():
    data={}
    d_id=session['lid']
    data['d_id']=d_id
    id=request.args['id']
    q1="select * from chats where  (sender_id='%s' and receiver_id='%s') or (sender_id='%s' and receiver_id='%s') "%(d_id,id,id,d_id)
    res=select(q1)
    data['view']=res

    if 'submit' in request.form:
        msg=request.form['msg']
        q="insert into chats values(NULL,'%s','%s','patient_to_doctor','%s',now())"%(d_id,id,msg)
        res=insert(q)
        print(res)
        return redirect(url_for("patient.patient_to_doctor_chat",id=id,d_id=d_id))
    return render_template("patient_to_doctor_chat.html",data=data)

@patient.route("/patient_view_medical_history",methods=['get','post'])

def patient_view_medical_history():
    data={}

    bid=request.args['bid']

    ju="SELECT * FROM `medical_notes` WHERE `booking_id`='%s'"%(bid)
    data['view_history']=select(ju)
    return render_template("patient_view_medical_history.html",data=data)

