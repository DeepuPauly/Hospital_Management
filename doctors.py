from flask import *
from database import *
from datetime import datetime



doctors=Blueprint ('doctors',__name__)

@doctors.route('/doctorshome')
def doctorshome():
	return render_template('doctorshome.html')

@doctors.route('/doctorpatiens')
def doctorpatiens():
	data={}
	q="select * from patients inner join booking using(patient_id) inner join schedule using(schedule_id) where status='paid' and doctor_id='%s'"%(session['doctor_id'])
	data['view']=select(q)
	return render_template('doctorpatiens.html',data=data)

@doctors.route('/d_patientshistory')
def d_patientshistory():
    data = {}
    session['patient_id'] = request.args['patient_id']
    session['booking_id'] = request.args['booking_id']
    q = "select *, medical_notes.date_time as mdate from medical_notes inner join booking using(booking_id) where patient_id='%s'" % (session['patient_id'])
    data['view'] = select(q)
    return render_template('d_patientshistory.html',data=data)


@doctors.route('/d_patientsphysical')
def d_patientsphysical():
    data = {}
    patient_id = request.args['patient_id']
    q = "select * from physical_conditions where patient_id='%s'" % (patient_id)
    data['view'] = select(q)
    return render_template('d_patientsphysical.html', data=data)


@doctors.route('/d_addprescriptions', methods=['get', 'post'])
def d_addprescriptions():
    data = {}
    q = "select * from medicines"
    data['view'] = select(q)
    
    if 'submit' in request.form:
        medicine_id = request.form['medicine_id']
        description = request.form['description']
        date = datetime.now().strftime("%Y-%m-%d")
        q="select * from medicines where medicine_id='%s'"%(medicine_id)
        res=select(q)
        qty=res[0]['available_qty']
        if int(qty) > 0:
            q = "insert into prescription values(null,'%s','%s','%s','%s','pending')"%(session['booking_id'], medicine_id, date, description)
            insert(q)
            q="update medicine_stock set quantity=quantity-1 where medicine_id='%s'"%(medicine_id)
            update(q)
            qi="update medicines set available_qty=available_qty-1 where medicine_id='%s'"%(medicine_id)
            update(qi)
            return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'd_patientshistory?patient_id={session['patient_id']}&booking_id={session['booking_id']}';
        }}
        , 2000); // Redirect after 2 seconds
           </script>
        """	
        else:
            return f"""
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">out of stock 😄</h3>
        </div>
        <script>
        setTimeout(function() {{
        window.location.href = 'd_patientshistory?patient_id={session['patient_id']}&booking_id={session['booking_id']}';
        }}
        , 2000); // Redirect after 2 seconds
           </script>
        """ 
    return render_template('d_addprescriptions.html', data=data)

@doctors.route('/d_adddisease', methods=['get', 'post'])
def d_adddisease():
	if 'submit' in request.form:
		description=request.form['description']
		date = datetime.now().strftime("%Y-%m-%d")
		q="insert into medical_notes values(null,'%s','%s','%s')"%(session['booking_id'],description,date)
		insert(q)


		return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'd_patientshistory?patient_id={session['patient_id']}&booking_id={session['booking_id']}';
        }}
        , 2000); // Redirect after 2 seconds
    </script>
""" 
	return render_template('d_adddisease.html')

@doctors.route('/d_addlabtest',methods=['get','post'])
def d_addlabtest():
	data={}
	q="select * from lab_test"
	data['view']=select(q)
	if 'submit' in request.form:
		test_id=request.form['test_id']
		description=request.form['description']
		date = datetime.now().strftime("%Y-%m-%d")
		q="select * from lab_test where test_id='%s'"%(test_id)
		res=select(q)
		rate=res[0]['rate']
		q="insert into test_prescription values(null,'%s','%s','%s','pending','%s','%s')"%(session['booking_id'],test_id,description,rate,date)
		insert(q)
		return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'd_patientshistory?patient_id={session['patient_id']}&booking_id={session['booking_id']}';
        }}
        , 2000); // Redirect after 2 seconds
    </script>
""" 
	return render_template('d_addlabtest.html',data=data)

@doctors.route('/d_requestspecialist')
def d_requestspecialist():
	data={}
	q="select * from specialist inner join doctors using(doctor_id)"
	data['view']=select(q)
	date = datetime.now().strftime("%Y-%m-%d")
	if 'specialist_id' in request.args:
		specialist_id=request.args['specialist_id']
		q="select * from request where booking_id='%s' and specialist_id='%s'"%(session['booking_id'],specialist_id)
		res=select(q)
		if res:
			return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Already requested 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'd_requestspecialist';
        }}
        , 2000); // Redirect after 2 seconds
    </script>
""" 
		else:
			q="insert into request values(null,'%s','%s','%s','pending')"%(specialist_id,session['booking_id'],date)
			insert(q)
			return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'd_requestspecialist';
        }}
        , 2000); // Redirect after 2 seconds
    </script>
""" 
	return render_template('d_requestspecialist.html',data=data)

@doctors.route('/d_viewlabtest')
def d_viewlabtest():
	data={}
	q="select * from test_prescription where booking_id='%s'"%(session['booking_id'])
	data['view']=select(q)
	return render_template('d_viewlabtest.html',data=data)

@doctors.route('/d_chat',methods=['get','post'])
def d_chat():
    data = {}
    sender_id = session['lid']
    data['sender_id'] = sender_id
    receiver_id = request.args['patient_id']
    q1 = "select * from chats where (sender_id='%s' and receiver_id='%s') or (sender_id='%s' and receiver_id='%s')" % (sender_id, receiver_id, receiver_id, sender_id)
    res = select(q1)
    data['view'] = res

    if 'submit' in request.form:
        msg = request.form['msg']
        q = "insert into chats values(NULL,'%s','%s','doctor to patient','%s',now())" % (sender_id, receiver_id, msg)
        res = insert(q)
        return redirect(url_for('doctors.d_chat', patient_id=receiver_id))

    return render_template('d_chat.html', data=data)

	
