from flask import *
from database import *

ambulance=Blueprint('ambulance',__name__)

@ambulance.route('/ambulance_home')
def ambulance_home():
    return render_template('ambulance_home.html')

@ambulance.route('/view_my_vehicle')
def view_my_vehicle():
    data={}
    qa="select * from ambulances where ambulance_id='%s'"%(session['aid'])
    res=select(qa)
    data['view']=res
    return render_template('amb_view_my_vehicle.html',data=data)

@ambulance.route('/view_requests')
def view_requests():
    data={}
    qa="select * from ambulance_request inner join patients using(patient_id) where ambulance_id='%s'"%(session['aid'])
    res=select(qa)
    data['view']=res

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    

    else:
        action=None
    
    if action=='accept':
        q1="update ambulance_request set status='accept' where ambulance_request_id='%s'"%(id)
        update(q1)
        q2="update ambulances set status='on_duty' where ambulance_id='%s'"%(session['aid'])
        update(q2)
        return """
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
                <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
                <h3 style="color:red;">Successfully Accepted 😄</h3>
            </div>
            <script>
                setTimeout(function() {
                    window.location.href = 'view_requests';
                }, 2000); // Redirect after 2 seconds
           </script>
        """
    
    if action=='reject':
        q1="update ambulance_request set status='reject' where ambulance_request_id='%s'"%(id)
        update(q1)
        return """
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
                <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
                <h3 style="color:red;">Successfully Rejected 😄</h3>
            </div>
            <script>
                setTimeout(function() {
                    window.location.href = 'view_requests';
                }, 2000); // Redirect after 2 seconds
           </script>
        """
    
    if action=='complete':
        q2="update ambulances set status='active' where ambulance_id='%s'"%(session['aid'])
        update(q2)
        q7="update ambulance_request set status='completed' where ambulance_request_id='%s'"%(id)
        update(q7)
        return """
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
                <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
                <h3 style="color:red;">Successfully Completed 😄</h3>
            </div>
            <script>
                setTimeout(function() {
                    window.location.href = 'view_requests';
                }, 2000); // Redirect after 2 seconds
           </script>
        """
    
    return render_template('amb_view_requests.html',data=data)


