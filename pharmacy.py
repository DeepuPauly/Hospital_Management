from flask import *
from database import *
		
pharmacy=Blueprint('pharmacy',__name__)

@pharmacy.route('/pharmacyhome')
def pharmacyhome():
	data={}
	q="select * from medicines where pharmacy_id='%s'"%(session['pharmacy_id'])
	data ['view']=select(q)
	return render_template('pharmacyhome.html',data=data)

@pharmacy.route('/p_medicines',methods=['get','post'])
def p_medicines():
	data={}
	q="select * from medicines where pharmacy_id='%s'"%(session['pharmacy_id'])
	data['view']=select(q)
	if 'submit' in request.form:
		medicine_name=request.form['medicine_name']
		description=request.form['description']
		available_qty=request.form['available_qty']
		expiry_date=request.form['expiry_date']
		rate=request.form['rate']
		q="insert into medicines values(null,'%s','%s','%s','%s','%s','%s')"%(session['pharmacy_id'],medicine_name,description,available_qty,expiry_date,rate)
		result=insert(q)
		total=int(rate)*int(available_qty)
		qi="insert into medicine_stock values(null,'%s','%s','%s','paid')"%(result,available_qty,total)
		insert(qi)
		return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully inserted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'p_medicines';
        }, 2000); // Redirect after 2 seconds
    </script>
"""	
	if 'action' in request.args:
		action=request.args['action']
		medicine_id=request.args['medicine_id']
	else:
		action=None
	if action=='update':
		q="select * from medicines where medicine_id='%s'"%(medicine_id)
		data['up']=select(q)
	if action=='delete':
		q="delete from medicines where medicine_id='%s'"%(medicine_id)
		delete(q)
		return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully deleted 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'p_medicines';
        }, 2000); // Redirect after 2 seconds
    </script>
"""	
	if 'update' in request.form:
		medicine_name=request.form['medicine_name']
		description=request.form['description']
		available_qty=request.form['available_qty']
		expiry_date=request.form['expiry_date']
		rate=request.form['rate']
		q="update medicines set medicine_name='%s',description='%s',available_qty='%s',expiry_date='%s',rate='%s' where medicine_id='%s'"%(medicine_name,description,available_qty,expiry_date,rate,medicine_id)
		update(q)
		return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'p_medicines';
        }, 2000); // Redirect after 2 seconds
    </script>
"""	
	return render_template('p_medicines.html',data=data)

@pharmacy.route('/p_updatestock',methods=['get','post'])
def p_updatestock():
	data={}
	medicine_id=request.args['medicine_id']
	q="select * from medicine_stock where medicine_id='%s'"%(medicine_id)
	data['view']=select(q)
	if 'submit' in request.form:
		quantity=request.form['quantity']
		q="select * from medicines where medicine_id='%s'"%(medicine_id)
		res=select(q)
		rate=res[0]['rate']
		total=int(rate)*int(quantity)
		q="update medicine_stock set quantity='%s',total='%s' where medicine_id='%s'"%(quantity,total,medicine_id)
		update(q)
		q="update medicines set available_qty='%s' where medicine_id='%s'"%(quantity,medicine_id)
		update(q)
		return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully updated 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'p_medicines';
        }, 2000); // Redirect after 2 seconds
    </script>
"""	
	return render_template('p_updatestock.html',data=data)

@pharmacy.route('/p_prescriptions',methods=['get','post'])
def p_prescriptions():
	data={}
	q="select *,prescription.description as des from  prescription inner join medicines using(medicine_id) where pharmacy_id='%s'"%(session['pharmacy_id'])
	data['view']=select(q)
	if 'prescription_id' in request.args:
		prescription_id=request.args['prescription_id']
		q="update prescription set status='forward' where prescription_id='%s'"%(prescription_id)
		update(q)
		return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully forward bill 😄</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'p_prescriptions';
        }, 2000); // Redirect after 2 seconds
    </script>
"""
	return render_template('p_prescriptions.html',data=data)

@pharmacy.route('/p_payments')
def p_payments(): 
	data={}
	prescription_id=request.args['prescription_id']
	q="SELECT *,payments.status as pstatus FROM payments INNER JOIN prescription USING(booking_id) INNER JOIN medicines USING(medicine_id) INNER JOIN booking USING(booking_id) INNER JOIN patients USING(patient_id) WHERE payments.payment_type='prescription_payment' and prescription.prescription_id='%s'"%(prescription_id)
	data['view']=select(q)
	if 'payment_id' in request.args:
		payment_id=request.args['payment_id']
		q="update payments set status='paid' where pay_id='%s'"%(payment_id)
		update(q)
		return f"""
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Payment accept successfull 😄</h3>
    </div>
    <script>
        setTimeout(function() {{
            window.location.href = 'p_payments?prescription_id={prescription_id}';
        }}
        , 2000); // Redirect after 2 seconds
    </script>
"""
	return render_template('p_payments.html',data=data)