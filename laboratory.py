from flask import *
from database import *
from datetime import datetime
import uuid
		
laboratory=Blueprint('laboratory',__name__)

@laboratory.route('/lab_home')
def lab_home():
	return render_template('lab_home.html')

@laboratory.route('/lab_test',methods=['get','post'])
def lab_test():
	data={}
	q="select * from lab_test where lab_id='%s'"%(session['lab_id'])
	data['view']=select(q)
	if 'submit' in request.form:
		test_name=request.form['test_name']
		description=request.form['description']
		rate=request.form['rate']
		q="insert into lab_test values(null,'%s','%s','%s','%s')"%(session['lab_id'],test_name,description,rate)
		result=insert(q)
		return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'lab_test';
        }, 2000); // Redirect after 2 seconds
    </script>
"""	
	if 'action' in request.args:
		action=request.args['action']
		test_id=request.args['test_id']
	else:
		action=None
	if action=='update':
		q="select * from lab_test where test_id='%s'"%(test_id)
		data['up']=select(q)
	if action=='delete':
		q="delete from lab_test where test_id='%s'"%(test_id)
		delete(q)
		return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully deleted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'lab_test';
        }, 2000); // Redirect after 2 seconds
    </script>
"""	
	if 'update' in request.form:
		test_name=request.form['test_name']
		description=request.form['description']
		rate=request.form['rate']
		q="update lab_test set test_name='%s',description='%s',rate='%s' where test_id='%s'"%(test_name,description,rate,test_id)
		update(q)
		return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'lab_test';
        }, 2000); // Redirect after 2 seconds
    </script>
"""	
	return render_template('lab_tests.html',data=data)

@laboratory.route('/lab_patients',methods=['get','post'])
def lab_patients():
	data={}
	q="SELECT *	 FROM `patients` WHERE `patient_id` IN (SELECT DISTINCT(`patient_id`) FROM `booking` INNER JOIN `test_prescription` USING(`booking_id`) INNER JOIN  `lab_test` USING(`test_id`) WHERE `lab_id`='%s' )"%(session['lab_id'])
	data['view']=select(q)
	return render_template('lab_patients.html',data=data)

@laboratory.route('/lab_prescribed',methods=['get','post'])
def lab_prescribed():
	data={}
	session['patient_id']=request.args['patient_id']
	q="SELECT *,test_prescription.date_time as tdate FROM `test_prescription` INNER JOIN `lab_test`USING(`test_id`) INNER JOIN `booking` USING(`booking_id`) WHERE `patient_id`='%s' AND `lab_id`='%s'"%(session['patient_id'],session['lab_id'])
	data['view']=select(q)
	return render_template('lab_prescribed.html',data=data)

@laboratory.route('/lab_prescribed_up',methods=['get','post'])
def lab_prescribed_up():
	test_pres_id=request.args['test_pres_id']
	if 'submit' in request.form:
		report_file=request.files['report_file']
		path="static/"+str(uuid.uuid4())+report_file.filename
		report_file.save(path)
		rate=request.form['rate']
		date = datetime.now().strftime("%Y-%m-%d")
		q="update test_prescription set report_file='%s',rate='%s',date_time='%s' where test_pres_id='%s'"%(path,rate,date,test_pres_id)
		update(q)
		return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'lab_prescribed?patient_id={session['patient_id']}';
        }}
        , 2000); // Redirect after 2 seconds
    </script>
"""	
	return render_template('lab_prescribed_up.html')

@laboratory.route('/lab_report')
def lab_report():
	data={}
	test_pres_id=request.args['test_pres_id']
	q="select * from test_prescription where test_pres_id='%s'"%(test_pres_id)
	data['view']=select(q)
	return render_template('lab_report.html',data=data)

@laboratory.route('/lab_payment')
def lab_payment():
	data={}
	test_pres_id=request.args['test_pres_id']
	q="select * from payments inner join test_prescription using(booking_id) where test_pres_id='%s' and payment_type='test_prescription_payment'"%(test_pres_id)
	data['view']=select(q)
	if 'pay_id' in request.args:
		pay_id=request.args['pay_id']
		q="update payments set status='paid' where pay_id='%s'"%(pay_id)
		update(q)
		return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'lab_payment?test_pres_id={test_pres_id}';
        }}
        , 2000); // Redirect after 2 seconds
    </script>
"""
	return render_template('lab_payment.html',data=data)

