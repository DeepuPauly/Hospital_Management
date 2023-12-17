from django.http import JsonResponse
from flask import *
from database import *


department=Blueprint('department',__name__)


@department.route('/dept_home')
def dept_home():
    return render_template('dept_home.html')



@department.route('/dept_view_doctors')
def dept_view_doctors():
    data={}
    q1="select * from doctors"
    res=select(q1)
    data['view']=res
    return  render_template('dept_view_doctors.html',data=data)




@department.route('/dept_schedule_consulting',methods=['get','post'])
def dept_schedule_consulting():
    if'action' in request.args:
         action = request.args['action']
         doctor_id=request.args['doctor_id']

         if action=='schedule':
             if 'submit' in request.form:
                 s_time=request.form['s_time']
                 e_time=request.form['e_time']
                 date=request.form['date']
                 fee_amount=request.form['fee_amount']
                 q = "SELECT * FROM schedule WHERE doctor_id='%s' AND date='%s' AND ( start_time BETWEEN '%s' AND '%s' OR end_time BETWEEN '%s' AND '%s')" % (doctor_id, date,s_time,e_time,s_time,e_time)
                 res=select(q)
                 print(res)
                 print("...........................................................................")
                 if res:
                   
                    return render_template ('pop_schedule.html')       
                 else:
           
                    q1="insert into schedule values(NULL,'%s','%s','%s','%s','%s')"%(s_time,e_time,date,doctor_id,fee_amount)
                    insert(q1)
                    return """
                    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
                    <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
                    <h3 style="color:green;">Successfully Scheduled 😄</h3>
                    </div>
                    <script>
        setTimeout(function() {
            window.location.href = 'dept_view_doctors';
        }, 2000); // Redirect after 2 seconds
    </script>
"""   
    return render_template('dept_schedule_consulting.html')
#                  q = "SELECT * FROM schedule WHERE doctor_id='%s' AND date='%s' AND NOT ('%s' >= e_time OR '%s' <= s_time)" % (doctor_id, date, e_time, s_time)
#                  res=select(q)
#                  if res:
#                      return """
#     <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
#        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
#         <h3 style="color:green;">Successfully Scheduled 😄</h3>
#     </div>
#     <script>
#         setTimeout(function() {
#             window.location.href = 'dept_view_doctors';
#         }, 2000); // Redirect after 2 seconds
#     </script>
# """           
#                  else:
           



@department.route('/dept_view_patients',methods=['get','post'])
def dept_view_patients():

    data={}
    q1="select * from patients"
    res=select(q1)
    data['view']=res
    return render_template('dept_view_patients.html',data=data)



@department.route('/dept_view_history',methods=['get','post'])
def dept_view_history():
    data={}
    if 'action' in request.args:
        action=request.args['action']
        patient_id=request.args['patient_id']
        if action=='view':
            q1="select * from medical_notes inner join booking using(booking_id) where patient_id='%s'"%(patient_id)
            res=select(q1)
            data['view']=res
    
    return render_template('dept_view_history.html',data=data)