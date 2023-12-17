from flask import *
from database import *
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
import random

public=Blueprint('public',__name__)

@public.route('/')
def public_home():
    return render_template('public_home.html')

@public.route('/login_all',methods=['get','post'])
def login_all():

    if 'submit' in request.form:
        uname=request.form['uname']
        psw=request.form['psw']

        qa="select * from login where username='%s' and password='%s'"%(uname,psw)
        res=select(qa)
        if res:
            print('hello')
            session['lid']=res[0]['login_id']

            if res[0]['usertype']=='admin':
                return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/loading.gif" alt="Smiley Image" style="width: 200px; height: 300px;border-radius: 20px;">
        <h3 style="color: red;">Loading......</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_home';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
            elif res[0]['usertype']=='patients':
                    print('haiii')
                    qa="select * from patients where login_id='%s'"%(session['lid'])
                    ra=select(qa)
                    if ra:
                        session['pid']=ra[0]['patient_id']
                        return """
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
                <img src="/static/loading.gif" alt="Smiley Image" style="width: 200px; height: 300px;border-radius: 20px;">
                <h3 style="color: red;">Loading......</h3>
            </div>
            <script>
                setTimeout(function() {
                    window.location.href = 'patient_home';
                }, 4000); // Redirect after 2 seconds
           </script>
            """
                    
            elif res[0]['usertype']=='ambulance':
                    print('haiii')
                    qa="select * from ambulances where login_id='%s'"%(session['lid'])
                    ra=select(qa)
                    if ra:
                        session['aid']=ra[0]['ambulance_id']
                        return """
            <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
                <img src="/static/loading.gif" alt="Smiley Image" style="width: 200px; height: 300px;border-radius: 20px;">
                <h3 style="color: red;">Loading......</h3>
            </div>
            <script>
                setTimeout(function() {
                    window.location.href = 'ambulance_home';
                }, 4000); // Redirect after 2 seconds
           </script>
            """
                    
            elif res[0]['usertype']=='doctor':
                q="select * from doctors where login_id='%s'"%(session['lid'])
                result=select(q)
                session['doctor_id']=result[0]['doctor_id']
                return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/loading.gif" alt="Smiley Image" style="width: 200px; height: 300px;border-radius: 20px;">
        <h3 style="color: red;">Loading......</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'doctorshome';
        }, 4000); // Redirect after 2 seconds
    </script>

"""
            elif res[0]['usertype']=='laboratory':
                q="select * from laboratory where login_id='%s'"%(session['lid'])
                result=select(q)
                session['lab_id']=result[0]['lab_id']
                return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/loading.gif" alt="Smiley Image" style="width: 200px; height: 300px;border-radius: 20px;">
        <h3 style="color: red;">Loading......</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'lab_home';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
            elif res[0]['usertype']=='pharmacy':
                q="select * from pharmacy where login_id='%s'"%(session['lid'])
                result=select(q)
                session['pharmacy_id']=result[0]['pharmacy_id']
                return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/loading.gif" alt="Smiley Image" style="width: 200px; height: 300px;border-radius: 20px;">
        <h3 style="color: red;">Loading......</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'pharmacyhome';
        }, 4000); // Redirect after 2 seconds
    </script>
"""         
            elif res[0]['usertype']=='specialist':
                q1 = "select * from specialist where login_id='%s'"%(session['lid'])
                m=select(q1)
                session['sid']=m[0]['specialist_id']
                return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/loading.gif" alt="Smiley Image" style="width: 200px; height: 300px;border-radius: 20px;">
        <h3 style="color: red;">Loading......</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'specialist_home';
        }, 4000); // Redirect after 2 seconds
    </script>
"""
            elif res[0]['usertype']=='department':
                q1="select * from departments where login_id='%s'"%(session['lid'])
                res1=select(q1)
                if res1:
                    session['d_id']=res1[0]['dept_id']
                    return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/loading.gif" alt="Smiley Image" style="width: 200px; height: 300px;border-radius: 20px;">
        <h3 style="color: red;">Loading......</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'dept_home';
        }, 4000); // Redirect after 2 seconds
    </script>
""" 
            elif res[0]['usertype']=='reception':
                re = "select * from receptions where login_id='%s'"%(session['lid'])
                r = select(re)
                if r:
                    session['res_id']=r[0]['reception_id']
                    return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/loading.gif" alt="Smiley Image" style="width: 200px; height: 300px;border-radius: 20px;">
        <h3 style="color: red;">Loading......</h3>
    </div>
    <script>
        setTimeout(function() {
            window.location.href = 'reception_home';
        }, 4000); // Redirect after 2 seconds
    </script>
"""


    return render_template('login.html')


@public.route('/patient_reg',methods=['get','post'])
def patient_reg():
    if 'submit' in request.form:
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        email = request.form['email']
        housename = request.form['housename']
        place = request.form['place']
        gender = request.form['gender']
        blood = request.form['blood']
        date = request.form['dob']
        username = request.form['username']
        password = request.form['password']

        qa="select * from login where username='%s' and password='%s'"%(username,password)
        res=select(qa)
        if res:
            return render_template('pop_log.html')
        else:
            f = "insert into login values(null,'%s','%s','patients')"%(username, password)
            t = insert(f)
            g = "insert into patients values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(t, fname, lname, phone, email, housename, place, gender, blood, date)
            insert(g)
            return """
                    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
                        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
                        <h3 style="color:red;">Added Successfully 😄</h3>
                    </div>
                    <script>
                        setTimeout(function() {
                            window.location.href = 'login_all';
                        }, 2000); // Redirect after 2 seconds
                       </script>
                    """
        
    return render_template('patient_reg.html')


@public.route('/forgotpassword', methods=['GET', 'POST'])
def forgotpassword():
    data = {}
    if 'next' in request.form:
        ph = request.form['ph']
        uname = request.form['uname']
        q = """SELECT login_id, patient_id, username, email, phone FROM login 
               INNER JOIN patients USING(login_id) WHERE username='%s' AND phone='%s'
               UNION
               SELECT login_id, doctor_id, username, email, phone FROM login 
               INNER JOIN doctors USING(login_id) WHERE username='%s' AND phone='%s'
               UNION
               SELECT login_id, lab_id, username, email, phone FROM login 
               INNER JOIN laboratory USING(login_id) WHERE username='%s' AND phone='%s'
               UNION
               SELECT login_id, pharmacy_id, username, email, phone FROM login 
               INNER JOIN pharmacy USING(login_id) WHERE username='%s' AND phone='%s'
               UNION
               SELECT login_id, reception_id, username, email, phone FROM login 
               INNER JOIN receptions USING(login_id) WHERE username='%s' AND phone='%s'
               UNION
               SELECT login_id, dept_id, username, email, phone FROM login 
               INNER JOIN departments USING(login_id) WHERE username='%s' AND phone='%s'
            """ % (uname, ph, uname, ph, uname, ph, uname, ph, uname, ph, uname, ph)
        print(q)
        res = select(q)
        print(res)
        if res:
            session['lid'] = res[0]['login_id']
            print(res)
            session['uname'] = res[0]['username']
            email = res[0]['email']
            print(email)
            rd = random.randrange(1000, 9999, 4)
            msg = str(rd)
            data['rd'] = rd
            print(rd)
            try:
                gmail = smtplib.SMTP('smtp.gmail.com', 587)
                gmail.ehlo()
                gmail.starttls()
                gmail.login('projectsriss2020@gmail.com', 'vroiyiwujcvnvade')
            except Exception as e:
                print("Couldn't setup email!!" + str(e))

            msg = MIMEText(msg)
            msg['Subject'] = 'OTP FOR PASSWORD RECOVERY'
            msg['To'] = email
            msg['From'] = 'projectsriss2020@gmail.com'

            try:
                gmail.send_message(msg)
                print(msg)
                flash("EMAIL SENT SUCCESSFULLY")
                session['rd'] = rd
                return redirect(url_for('public.enterotp'))
            except Exception as e:
                print("COULDN'T SEND EMAIL", str(e))
                return redirect(url_for('public.forgotpassword'))
        else:
            flash("INVALID DETAILS")
            return redirect(url_for('public.forgotpassword'))
    return render_template("forgotpassword.html", data=data)




@public.route('/enterotp', methods=['get', 'post'])
def enterotp():
    rd = session['rd']
    ids = session['lid']
    data = {}

    if "otp" in request.form:
        otp = request.form['otp']
        if int(otp) == int(rd):
            print('hello')
            data['chp'] = session['uname']
        else:
            flash("invalid otp")
            return redirect(url_for('public.forgotpassword'))

    if 'update' in request.form:
        uname = request.form['uname']
        p = request.form['pwd']
        cp = request.form['pwds']
        if p == cp:
            print("+++++++++++")
            q = "update login set password='%s' where login_id='%s'" % (p, ids)
            update(q)
            flash("UPDATED SUCCESSFULLY")
            return redirect(url_for('public.login_all'))
        else:
            flash("PASSWORD MISMATCH")
            data['chp'] = uname

    return render_template("enterotp.html", data=data)

