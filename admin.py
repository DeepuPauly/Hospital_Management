import uuid
from django.http import JsonResponse
from flask import *
from database import *

admin=Blueprint ('admin',__name__)

@admin.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@admin.route('/admin_manage_department',methods=['get','post'])
def admin_manage_department():
    data={}
    if 'submit' in request.form:
        departmentname=request.form['departmentname']
        phone=request.form['phone']
        email=request.form['email']
        description=request.form['description']
        username=request.form['username']
        password=request.form['password']

        f="insert into login values(null,'%s','%s','department')"%(username,password)
        t=insert(f)
        g="insert into departments values(null,'%s','%s','%s','%s','%s')"%(t,departmentname,phone,email,description)
        insert(g)   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Added 😄</h3>
        </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_department';
        }, 4000); // Redirect after 1 seconds
    </script>"""

    d="select * from departments"
    data['department']=select(d)

    
    if 'action' in request.args:
        action=request.args['action']
        deptid=request.args['deptid']
    else:
        action=None
    
    
    if action=='update':
        fu="select * from departments where dept_id='%s'"%(deptid)
        data['updates']=select(fu)

    if 'update' in request.form:
        departmentname=request.form['departmentname']
        phone=request.form['phone']
        email=request.form['email']
        description=request.form['description']
        yy="update departments set dept_name='%s',phone='%s',email='%s',description='%s' where dept_id='%s'"%(departmentname,phone,email,description,deptid)
        update(yy)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_department';
        }, 2000); // Redirect after 2 seconds
        </script>
        """
    
    if action=='delete':
        pu="delete from departments where dept_id='%s'"%(deptid)
        delete(pu)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_department';
        }, 2000); // Redirect after 2 seconds
        </script>
            """
    return render_template('admin_manage_department.html',data=data)

@admin.route('/dept_search',methods=['get'])
def dept_search():
    if request.is_ajax():

        query = request.GET.get('query', '')
        results ="select * from departments where dept_name like '%s'"%(query)
        select(results)

        data = [
            {
                'dept_name': member.dept_name, 
                'phone': member.phone,
                'email': member.email,
                'dob': member.dob,
                'description': member.description,
            }
            for member in results
        ]

        return JsonResponse({'data': data})

    return JsonResponse({'error': 'Invalid request'})

@admin.route('/admin_manage_reception',methods=['get','post'])
def admin_manage_reception():
    data={}
    if 'submit' in request.form:
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        phone=request.form['phone']
        floor=request.form['floor']
        username=request.form['username']
        password=request.form['password']

        j="insert into login values(null,'%s','%s','reception')"%(username,password)
        l=insert(j)
        p="insert into receptions values(null,'%s','%s','%s','%s','%s','%s')"%(l,firstname,lastname,phone,email,floor)
        insert(p)   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Added 😄</h3>
        </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_reception';
        }, 4000); // Redirect after 1 seconds
    </script>"""

    x="select * from receptions"
    data['receptions']=select(x)

    if 'action' in request.args:
        action=request.args['action']
        recpid=request.args['recpid']
    else:
        action=None
    
    
    if action=='update':
        u="select * from receptions where reception_id='%s'"%(recpid)
        data['updatess']=select(u)

    if 'update' in request.form:
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        email=request.form['email']
        phone=request.form['phone']
        floor=request.form['floor']
        y="update receptions set first_name='%s',last_name='%s',phone='%s',email='%s',floor='%s' where reception_id='%s'"%(firstname,lastname,phone,email,floor,recpid)
        update(y )
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_reception';
        }, 2000); // Redirect after 2 seconds
        </script>
        """
    
    if action=='delete':
        p="delete from receptions where reception_id='%s'"%(recpid)
        delete(p)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_reception';
        }, 2000); // Redirect after 2 seconds
        </script>
            """

    return render_template('admin_manage_reception.html',data=data)

@admin.route('/recp_search',methods=['get'])
def recp_search():
    if request.is_ajax():

        query = request.GET.get('query', '')
        resultss ="select * from receptions where first_name like '%s'"%(query)
        select(resultss)

        data = [
            {
                'dept_name': member.dept_name, 
                'phone': member.phone,
                'email': member.email,
                'dob': member.dob,
                'description': member.description,
            }
            for member in resultss
        ]

        return JsonResponse({'data': data})

    return JsonResponse({'error': 'Invalid request'})

@admin.route('/admin_manage_pharmacy',methods=['get','post'])
def admin_manage_pharmacy():
    data={}
    if 'submit' in request.form:
        pharmacyname=request.form['pharmacyname']
        email=request.form['email']
        phone=request.form['phone']
        floor=request.form['floor']
        username=request.form['username']
        password=request.form['password']

        lk="insert into login values(null,'%s','%s','pharmacy')"%(username,password)
        o=insert(lk)
        a="insert into pharmacy values(null,'%s','%s','%s','%s','%s')"%(o,pharmacyname,phone,email,floor)
        insert(a)   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Added 😄</h3>
        </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_pharmacy';
        }, 4000); // Redirect after 1 seconds
    </script>"""

    bv="select * from pharmacy"
    data['pharmacy']=select(bv)

    if 'action' in request.args:
        action=request.args['action']
        phar=request.args['pharid']
    else:
        action=None
    
    
    if action=='update':
        u="select * from pharmacy where pharmacy_id='%s'"%(phar)
        data['updat']=select(u)

    if 'update' in request.form:
        pharmacyname=request.form['pharmacyname']
        email=request.form['email']
        phone=request.form['phone']
        floor=request.form['floor']
        y="update pharmacy set pharmacy_name='%s',phone='%s',email='%s',floor='%s' where pharmacy_id='%s'"%(pharmacyname,phone,email,floor,phar)
        update(y )
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_pharmacy';
        }, 2000); // Redirect after 2 seconds
        </script>
        """
    
    if action=='delete':
        p="delete from pharmacy where pharmacy_id='%s'"%(phar)
        delete(p)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_pharmacy';
        }, 2000); // Redirect after 2 seconds
        </script>
            """

    return render_template('admin_manage_pharmacy.html',data=data)

@admin.route('/admin_manage_laboratary',methods=['get','post'])
def admin_manage_laboratary():
    data={}
    if 'submit' in request.form:
        labname=request.form['labname']
        email=request.form['email']
        phone=request.form['phone']
        category=request.form['category']
        username=request.form['username']
        password=request.form['password']

        bg="insert into login values(null,'%s','%s','laboratory')"%(username,password)
        pa=insert(bg)
        b="insert into laboratory values(null,'%s','%s','%s','%s','%s')"%(pa,labname,category,phone,email)
        insert(b)   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Added 😄</h3>
        </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_laboratary';
        }, 4000); // Redirect after 1 seconds
    </script>"""

    bj="select * from laboratory"
    data['laboratory']=select(bj)

    if 'action' in request.args:
        action=request.args['action']
        lab=request.args['labid']
    else:
        action=None
    
    
    if action=='update':
        u="select * from laboratory where lab_id='%s'"%(lab)
        data['updat']=select(u)

    if 'update' in request.form:
        laborataryname=request.form['labname']
        category=request.form['category']
        email=request.form['email']
        phone=request.form['phone']
        d="update laboratory set lab_name='%s',category='%s',phone='%s',email='%s' where lab_id='%s'"%(laborataryname,category,phone,email,lab)
        update(d)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_laboratary';
        }, 2000); // Redirect after 2 seconds
        </script>
        """
    
    if action=='delete':
        j="delete from laboratory where lab_id='%s'"%(lab)
        delete(j)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_laboratary';
        }, 2000); // Redirect after 2 seconds
        </script>
            """

    return render_template('admin_manage_laboratary.html',data=data)

@admin.route('/admin_manage_patients',methods=['get','post'])
def admin_manage_patients():
    data={}

    dd="select * from patients"
    data['patients']=select(dd)

    return render_template('admin_manage_patients.html',data=data)

@admin.route('/admin_view_payment',methods=['get','post'])
def admin_view_payment():
    data={}

    uy="SELECT * FROM `payments` INNER JOIN `booking` USING (`booking_id`)INNER JOIN `patients` USING (`patient_id`)"
    data['payment']=select(uy)

    return render_template('admin_view_payment.html',data=data)

@admin.route('/admin_manage_ambulances',methods=['get','post'])
def admin_manage_ambulances():
    data={}
    if 'submit' in request.form:
        ambulancenumber=request.form['ambulancenumber']
        typee=request.form['type']
        capacity=request.form['capacity']
        equipments=request.form.getlist('equipments')
        drivername=request.form['drivername']
        username=request.form['username']
        password=request.form['password']
        eqi=', '.join(equipments)

        ij="insert into login values(null,'%s','%s','ambulance')"%(username,password)
        pk=insert(ij)
        o="insert into ambulances values(null,'%s','%s','%s','%s','%s','active','%s')"%(pk,ambulancenumber,typee,capacity,eqi,drivername)
        print(o,'///')
        insert(o)   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Added 😄</h3>
        </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_ambulances';
        }, 4000); // Redirect after 1 seconds
    </script>"""

    sn="select * from ambulances"
    data['ambulances']=select(sn)

    if 'action' in request.args:
        action=request.args['action']
        ambu=request.args['ambuid']
    else:
        action=None
    
    
    if action=='update':
        u="select * from ambulances where ambulance_id='%s'"%(ambu)
        data['updat']=select(u)

    if 'update' in request.form:
        ambulancenumber=request.form['ambulancenumber']
        typee=request.form['type']
        capacity=request.form['capacity']
        equipments=request.form.getlist('equipments')
        drivername=request.form['drivername']
        eqi=', '.join(equipments)
        df="update ambulances set ambulance_number='%s',type='%s',capacity='%s',equipments='%s',status='pending',driver_name='%s' where ambulance_id='%s'"%(ambulancenumber,typee,capacity,eqi,drivername,ambu)
        update(df)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_ambulances';
        }, 2000); // Redirect after 2 seconds
        </script>
        """
    
    if action=='delete':
        j="delete from ambulances where ambulance_id='%s'"%(ambu)
        delete(j)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_ambulances';
        }, 2000); // Redirect after 2 seconds
        </script>
            """
    if action=='active':
        hy="update ambulances set status='active' where ambulance_id='%s'"%(ambu)
        update(hy)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Actived 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_ambulances';
        }, 2000); // Redirect after 2 seconds
        </script>
        """
    if action=='inactive':
        xc="update ambulances set status='inactive' where ambulance_id='%s'"%(ambu)
        update(xc)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully inactived 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_ambulances';
        }, 2000); // Redirect after 2 seconds
        </script>
            """


    return render_template('admin_manage_ambulances.html',data=data)

@admin.route('/admin_manage_specialist',methods=['get','post'])
def admin_manage_specialist():
    data={}
    if 'submit' in request.form:
        doctor=request.form['doctor']
        speciality=request.form['speciality']
        certifications=request.form['certification']
        experience=request.form['experience']
        username=request.form['username']
        password=request.form['password']

        gt="insert into login values(null,'%s','%s','specialist')"%(username,password)
        i=insert(gt)
        p="insert into specialist values(null,'%s','%s','%s','%s','%s')"%(i,doctor,speciality,certifications,experience)
        insert(p)   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Added 😄</h3>
        </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_specialist';
        }, 4000); // Redirect after 1 seconds
    </script>"""

    x="SELECT * FROM `specialist` INNER JOIN `doctors` USING(`doctor_id`)"
    data['specialist']=select(x)

    g="select * from doctors"
    data['doctor']=select(g)

    if 'action' in request.args:
        action=request.args['action']
        splid=request.args['splid']
    else:
        action=None
    
    
    if action=='update':
        po="select * from specialist INNER JOIN `doctors` USING(`doctor_id`) where specialist_id='%s'"%(splid)
        data['updatess']=select(po)

    if 'update' in request.form:
        doctor=request.form['doctor']
        speciality=request.form['speciality']
        certifications=request.form['certification']
        experience=request.form['experience']
        y="update specialist set doctor_id='%s',speciality='%s',certifications='%s',experience='%s' where specialist_id='%s'"%(doctor,speciality,certifications,experience,splid)
        update(y )
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_specialist';
        }, 2000); // Redirect after 2 seconds
        </script>
        """
    
    if action=='delete':
        p="delete from specialist where specialist_id='%s'"%(splid)
        delete(p)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_specialist';
        }, 2000); // Redirect after 2 seconds
        </script>
            """

    return render_template('admin_manage_specialist.html',data=data)

@admin.route('/admin_manage_doctor',methods=['get','post'])
def admin_manage_doctor():
    data={}
    if 'submit' in request.form:
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        phone=request.form['phone']
        email=request.form['email']
        place=request.form['place']
        qualification=request.form['qualification']
        image=request.files['image']
        username=request.form['username']
        password=request.form['password']
        path="static/"+str(uuid.uuid4())+image.filename
        image.save(path)

        pti="insert into login values(null,'%s','%s','doctor')"%(username,password)
        d=insert(pti)
        kun="insert into doctors values(null,'%s','%s','%s','%s','%s','%s','%s','%s')"%(d,firstname,lastname,phone,email,place,qualification,path)
        insert(kun)   
        return """
    <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Added 😄</h3>
        </div>
    <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_doctor';
        }, 4000); // Redirect after 2 seconds
    </script>"""

    z="SELECT * FROM `doctors`"
    data['doctor']=select(z)

    if 'action' in request.args:
        action=request.args['action']
        docid=request.args['docid']
    else:
        action=None
    
    
    if action=='update':
        pod="select * from doctors where doctor_id='%s'"%(docid)
        data['updatess']=select(pod)

    if 'update' in request.form:
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        phone=request.form['phone']
        email=request.form['email']
        place=request.form['place']
        qualification=request.form['qualification']
        image=request.files['image']
        path="static/"+str(uuid.uuid4())+image.filename
        image.save(path)
        pez="update doctors set first_name='%s',last_name='%s',phone='%s',email='%s',place='%s',qualification='%s',image='%s' where doctor_id='%s'"%(firstname,lastname,phone,email,place,qualification,path,docid)
        update(pez)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/success.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Updated 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_doctor';
        }, 2000); // Redirect after 2 seconds
        </script>
        """
    
    if action=='delete':
        po="delete from doctors where doctor_id='%s'"%(docid)
        delete(po)
        return """
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);  color: white; padding: 20px; text-align: center; border-radius: 20px;">
        <img src="/static/delete.gif" alt="Smiley Image" style="width: 100px; height: 100px;border-radius: 20px;">
        <h3 style="color:red;">Successfully Deleted 😄</h3>
        </div>
        <script>
        setTimeout(function() {
            window.location.href = 'admin_manage_doctor';
        }, 2000); // Redirect after 2 seconds
        </script>
            """

    return render_template('admin_manage_doctor.html',data=data)



