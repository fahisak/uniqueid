import base64

import random
import qrcode
import time

from Naked.toolshed.system import directory
from flask import Flask, render_template, request, session, jsonify
from DBConnection import Db
from flask_mail import Mail, Message
from enc import AESCipher
app = Flask(__name__)
app.secret_key ="helloo"
#................................................................................................................


filepath_stu_pic = "C:\\Users\\hp\\PycharmProjects\\uniqid\\static\\student_pics\\"
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'uniqueid005@gmail.com'  # enter your email here
app.config['MAIL_DEFAULT_SENDER'] = 'uniqueid005@gmail.com' # enter your email here
app.config['MAIL_PASSWORD'] = 'jubi1997' # enter your password here
mail = Mail(app)

@app.route('/')
def login():
    return render_template("login1.html")


@app.route('/login_post', methods=['post'])
def login_post():
    db = Db()
    username = request.form['username']
    password = request.form['password']
    # btn = request.form['button']
    # if (btn == 'LOGIN'):
    qry = "select * from login where user_name='" + username + "' and password='" + password + "'"
    res = db.selectOne(qry)
    if (res is not None):

        if res['type'] == "admin":
            session['lid'] = res['id']
            return render_template("index-1.html")
        elif res['type'] == "subadmin":
            session['lid'] = res['id']
            return render_template("index-2.html")
        elif res['type'] == "college":
            session['lid'] = res['id']
            return render_template("index-3.html")
        elif res['type'] == "staff":
            session['lid'] = res['id']
            # print(str(session['lid']))
            return render_template("index-4.html")
        else:
            return "<script>alert('Student and verifier has no acces to web');window.location='/'</script>"
    else:
        return '''<script>alert("please enter valid username and password ")
                window.location='/'</script>'''
    # else:
    #     # qry = "select * from login where user_name='" + username + "'"
    #     # res = db.selectOne(qry)
    #     # if(res is None):
    #     #     return '''<script>alert("please enter valid username")
    #     #                         window.location='/'</script>'''
    #     # else:
    #         return render_template("forget_password.html")



@app.route('/forget_password')
def forget_password():
    return render_template("forget_password.html")

@app.route('/forget_password_post',methods=['post'])
def forget_password_post():
    db=Db()
    email= request.form['textfield']
    # type=request.form['type']
    # uname=request.form['uname']
    qry = "select * from login where user_name='" +email + "'"
    res = db.selectOne(qry)
    if(res is not None):
        passwd=res['password']
        msg = Message(subject="Your password",
                      sender=app.config.get("uniqueid005@gmail.com"),
                      recipients=[email],  # replace with your email for testing
                      body="Password:"+passwd)
        mail.send(msg)
        return '''<script>alert("sucessfully")
                            window.location='/'</script>'''
    else:
        return '''<script>alert("please enter valid email")
        window.location='/'</script>'''


@app.route('/change_password')
def change_password():
    return render_template("change_password.html")

@app.route('/change_password_post',methods=['post'])
def change_password_post():
    db=Db()
    cpass=request.form['textfield4']
    npass=request.form['textfield']
    confirmpass=request.form['textfield5']
    qry="update login set password='"+confirmpass+"' where id='"+str(session['lid'])+"' "
    res=db.update(qry)
    return '''<script>alert("chnge password sucessfully")
    window.location='/'</script>'''

@app.route('/change_passwor')
def change_passwor():
    return render_template("change_passwor.html")

@app.route('/change_passwor_post',methods=['post'])
def change_passwor_post():
    db=Db()
    cpass=request.form['textfield4']
    npass=request.form['textfield']
    confirmpass=request.form['textfield5']
    qry="update login set password='"+confirmpass+"' where id='"+str(session['lid'])+"' "
    res=db.update(qry)
    return '''<script>alert("chnge password sucessfully")
    window.location='/'</script>'''

@app.route('/change_passwo')
def change_passwo():
    return render_template("change_passwo.html")

@app.route('/change_passwo_post',methods=['post'])
def change_passwo_post():
    db=Db()
    cpass=request.form['textfield4']
    npass=request.form['textfield']
    confirmpass=request.form['textfield5']
    qry="update login set password='"+confirmpass+"' where id='"+str(session['lid'])+"' "
    res=db.update(qry)
    return '''<script>alert("chnge password sucessfully")
    window.location='/'</script>'''

@app.route('/change_passw')
def change_passw():
    return render_template("change_passw.html")

@app.route('/change_passw_post',methods=['post'])
def change_passw_post():
    db=Db()
    cpass=request.form['textfield4']
    npass=request.form['textfield']
    confirmpass=request.form['textfield5']
    qry="update login set password='"+confirmpass+"' where id='"+str(session['lid'])+"' "
    res=db.update(qry)
    return '''<script>alert("chnge password sucessfully")
    window.location='/'</script>'''










# ........................admin......................................................................









@app.route('/ad_homepage')
def ad_homepage():
   return render_template("admin/admin_homepage.html")



@app.route('/ad_add_subadmin')
def ad_add_subadmin():
    return render_template('admin/add_subadmin.html')


@app.route('/add_subadmin', methods=["post"])
def add_subadmin():
    db = Db()
    name = request.form['textfield']
    dob = request.form['textfield2']
    designation = request.form['textfield3']
    house_name = request.form['textfield4']
    place = request.form['textfield5']
    pin = request.form['textfield9']
    post = request.form['textfield6']
    gender = request.form['radio']
    mail_id = request.form['textfield7']
    phone_no = request.form['textfield8']

    qry = "insert into login(user_name,password,type)values('" + mail_id + "','" + phone_no + "','subadmin')"
    res = db.insert(qry)
    qry1 = "insert into university_staff(U_name,house_name,place,post,pin,gender,dob,designation,mail_id,phone_number,login_id) value('" + name + "','" + house_name + "','" + place + "','" + post + "','" + pin + "','" + gender + "','" + dob + "','" + designation + "','" + mail_id + "','" + phone_no + "','" + str(res) + "')"
    res1 = db.insert(qry1)
    return '<script>alert("sucessfully");window.location="/ad_add_subadmin"</script>'


@app.route('/ad_view_subadmin')
def ad_view_subadmin():
    db = Db()
    qry = "select * from university_staff"
    res = db.select(qry)
    return render_template('admin/view_subadmin.html', data=res)


@app.route('/ad_edit_subadmin/<id>')
def ad_edit_subadmin(id):
    db = Db()
    qry = "select U_name,house_name,post,place,pin,dob,gender,designation,phone_number,mail_id,id from university_staff where id='" + id + "'"
    res = db.selectOne(qry)
    return render_template('admin/edit_subadmin.html', data=res)




@app.route('/edit_subadmin_post',methods=["post"])
def edit_subadmin_post():
    db = Db()
    name = request.form['textfield']
    house_name = request.form['textfield2']
    post = request.form['textfield3']
    place = request.form['textfield4']
    pin = request.form['textfield9']
    dob=request.form['textfield5']
    designation=request.form['textfield6']
    gender = request.form['radio']
    mail_id = request.form['textfield8']
    phone_no = request.form['textfield7']
    hid = request.form['hid']
    #print(hid)
    qry1= "UPDATE university_staff set U_name='"+name+"',dob='"+dob+"',designation='"+designation+"',house_name='"+house_name+"',post='"+post+"',place='"+ place+"',pin='"+pin+"',gender='"+gender+"',mail_id='"+mail_id+"',phone_number='"+ phone_no+"' where id='"+hid+"'"
    print(qry1)
    res1=db.update(qry1)
    return '''<script>
        alert("Updated successfully")
        window.location='/ad_view_subadmin'

        </script>'''


@app.route('/ad_delete_subadmin/<id>')
def ad_delete_subadmin(id):
    db = Db()
    qry = "delete from university_staff where login_id='" + id + "'"
    db.delete(qry)
    qry2 = "delete from login where login_id='" + id + "'"
    db.delete(qry2)
    return '<script>alert("delition successfully");window.location="/ad_view_subadmin"</script>'


@app.route('/ad_college')
def ad_college():
    return render_template('admin/add_college.html')


@app.route('/ad_add_college',methods=["post"])
def ad_add_college():
    db=Db()
    college=request.form['textfield']
    # state=request.form['select']
    district=request.form['select2']
    place=request.form['textfield2']
    post=request.form['textfield3']
    pin=request.form['textfield4']
    mail_id=request.form['textfield5']
    phone_no=request.form['textfield6']
    qry2="select * from college where college=college "
    res1=db.selectOne(qry2)
    if(res1 is not None):
        ci=Db()
        qry = "insert into login(user_name,password,type)values('" + mail_id + "','" + phone_no + "','college')"
        print(qry)
        res=ci.insert(qry)
        print("resss",res)
        qry1="insert into college(college,district,place,pincode,post,phone_no,mail_id,login_id)values('"+college+"','"+district+"','"+place+"','"+pin+"','"+post+"','"+phone_no+"','"+mail_id+"','"+str(res)+"')"
        res2=ci.insert(qry1)
        return '<script>alert("sucessfully");window.location="/ad_college"</script>'


@app.route('/ad_view_college')
def ad_view_college():
    db=Db()
    qry="select * from college"
    res=db.select(qry)

    return render_template('admin/view_college.html',data=res)

# @app.route('/ad_view_search_colleges',methods=['post'])
# def ad_view_search_colleges():
#     db=Db()
#     serch = request.form['textfield']
#     qry = "select * from college where college like '%" + serch + "%' or district like '%" + serch + "%'"
#     res = db.select(qry)
#     return render_template('admin/view_college.html',)
#




@app.route('/ad_edit_college/<id>')
def ad_edit_college(id):
    db = Db()
    qry = "select college,district,place,post,pincode,mail_id,phone_no,id from college where login_id='" + id + "'"
    res=db.selectOne(qry)
    return render_template('admin/edit_college.html',data=res)

# @app.route('/edit_college')
# def edit_college():
#     return render_template('admin/edit_college.html')

@app.route('/edit_college_post',methods=["post"])
def edit_college_post():
    db=Db()
    college=request.form['textfield']
    # state=request.form['select']
    dist=request.form['select2']
    place = request.form['textfield2']
    post = request.form['textfield3']
    pin = request.form['textfield4']
    mail_id = request.form['textfield5']
    phone_no = request.form['textfield6']
    id=request.form['id']
    qry="update college set college='"+college+"',district='"+dist+"',place='"+place+"',post='"+post+"',pincode='"+pin+"',mail_id='"+mail_id+"',phone_no='"+phone_no+"' where login_id='"+id+"'"
    db.update(qry)
    return '''<script>
            alert("Updated successfully")
            window.location='/ad_view_college'

            </script>'''


@app.route('/ad_delete_college/<id>')
def ad_delete_college(id):

    db=Db()
    qry="delete from college where login_id='"+id+"'"
    db.delete(qry)
    qry2="delete from login where id='"+id+"'"

    db.delete(qry2)
    return '<script>alert("delition successfully");window.location="/ad_view_college"</script>'



@app.route('/add_dept')
def add_dept():
    db=Db()
    qry="select * from college"
    res=db.select(qry)
    return render_template('admin/add_dept.html',data=res)


@app.route('/ad_add_dept',methods=['post'])
def ad_add_dept():
    db=Db()
    dep=request.form['textfield']
    qry1="select department from department where department='"+dep+"'"
    res1=db.select(qry1)
    if(res1 is  None):
        qry="insert into department(department)values('"+dep+"')"
        res=db.insert(qry)
        return '<script>alert("sucessfully");window.location="/add_dept"</script>'
    return '<script>alert("Alredy exits");window.location="/add_dept"</script>'   # return render_template('admin/add_dept.html')

@app.route('/ad_view_dept')
def ad_view_dept():
    db=Db()
    qry="select * from department "
    res=db.select(qry)
    return render_template('admin/view_dept.html',data=res)


@app.route('/ad_edit_dept/<iid>')
def ad_edit_dept(iid):
    db=Db()
    qry="select * from department where department.id='"+iid+"' "
    res = db.selectOne(qry)

    return render_template('admin/edit_dept.html', data=res)

    #return render_template('admin/edit_dept.html')



@app.route('/edit_dept_post',methods=['post'])
def edit_dept_post():
    db=Db()
    dept=request.form['textfield']
    id=request.form['id']

    qry="update department set department='"+dept+"' where id='"+id+"' "
    res=db.update(qry)
    return'''<script>alert("update sucessfully")
    window.location='/ad_view_dept'</script>'''


@app.route('/delete_dept/<id>')
def delete_dept(id):
    db=Db()
    qry="delete from department where id='"+id+"'"
    qry1="delete from course where department_id='"+id+"'"
    res1 = db.delete(qry1)
    res=db.delete(qry)
    return '''<script>alert("deletion sucessfully")
        window.location='/ad_view_dept'</script>'''



@app.route('/add_course')
def add_course():
    db=Db()
    qry="select department,id from department"
    res = db.select(qry)
    return render_template('admin/add_course.html',data=res)

@app.route('/ad_add_course',methods=['post'])
def ad_add_course():
    db=Db()
    course=request.form['textfield']
    dept=request.form['select']
    course_code=request.form['textfield2']
    qry="select course.* from course where course.department_id='"+dept+"' and course='"+course+"' "
    res=db.selectOne(qry)
    if(res is None):
        qry = "insert into course(department_id,course,course_code)values('" + dept + "','" + course + "','" + course_code + "')"
        db.insert(qry)
        return '''<script>alert("sucessfully")
        window.location='/add_course'</script>'''
    return '''<script>alert("Alredy exist")
    window.location='/add_course'</script>'''

@app.route('/ad_view_course')
def ad_view_course():
    db=Db()
    qry="select course.*,department.department from course INNER JOIN department on course.department_id=department.id"
    res=db.select(qry)
    return render_template('admin/view_course.html',data=res)


@app.route('/ad_edit_course/<id>')
def ad_edit_course(id):
    db=Db()
    qry="select course.*,department.department from course inner join department on course.department_id=department.id where course.id='"+id+"'"
    res=db.selectOne(qry)

    qry1="select department,id from department"
    res1=db.select(qry1)
    return render_template('admin/edit_course.html',data=res,data1=res1)

@app.route('/edit_course_post',methods=['post'])
def edit_course_post():
    db=Db()
    course=request.form['textfield']
    coursecode = request.form['textfield2']
    dept=request.form['select']
    id=request.form['id']
    qry="select course.* from course where course.department_id='"+dept+"' and course='"+course+"' "
    res = db.selectOne(qry)
    if (res is None):
        qry = "update course set course='" + course + "',department_id='" + dept + "',course_code='" + coursecode + "' where id='" + id + "'"
        res = db.update(qry)

        return '''<script>alert("update sucessfully")
            window.location='/ad_view_course'</script>'''
    return '''<script>alert("Alredy exit")
        window.location='/ad_view_course'</script>'''

@app.route('/delete_course/<id>')
def delete_course(id):
    db=Db()
    qry1="delete from course where id='"+id+"'"
    res1 = db.delete(qry1)
    return '''<script>alert("deletion sucessfully")
        window.location='/ad_view_course'</script>'''



@app.route('/ad_add_course_college')
def ad_add_course_college():
    db=Db()
    qry="select * from college"
    qry1="select * from course"
    res=db.select(qry)
    res1=db.select(qry1)
    return render_template('admin/add_course_college.html',data=res,data1=res1)

@app.route('/ad_add_course_college_post',methods=['post'])
def ad_add_course_college_post():
    db=Db()
    college=request.form['select']
    course=request.form['select2']
    qry="insert into college_course(course_id,college_id)values('"+course+"','"+college+"')"
    res=db.insert(qry)
    return '''<script>alert("sucessfully")
    window.location='/ad_add_course_college'</script>'''

@app.route('/view_course_college')
def view_course_college():
    db=Db()
    qry="select college_course.*,course.course,course.id as ccid,department.department,college.college,college.login_id from college_course inner join course on course.id=college_course.course_id inner join department on course.department_id=department.id inner join college on college_course.college_id=college.login_id order by college.college"
    res=db.select(qry)
    print(res)
    qry1="select * from college"
    res1=db.select(qry1)
    return render_template('admin/view_course_collegewise.html', data=res,data1=res1)

@app.route('/view_course_college_search',methods=['post'])
def view_course_college_search():
    db=Db()
    college_id=request.form['select']
    if college_id!='select':
        qry="select college_course.*,course.course,course.id as ccid,department.department,college.college,college.login_id from college_course inner join course on course.id=college_course.course_id inner join department on course.department_id=department.id inner join college on college_course.college_id=college.login_id where college_course.college_id='"+college_id+"' order by college.college"
    else:
        qry = "select college_course.*,course.course,course.id as ccid,department.department,college.college,,college.login_id from college_course inner join course on course.id=college_course.course_id inner join department on course.department_id=department.id inner join college on college_course.college_id=college.login_id order by college.college"

    # print(qry)
    res=db.select(qry)
    # print(res)
    qry1="select * from college"
    res1=db.select(qry1)
    return render_template('admin/view_course_collegewise.html', data=res,data1=res1)


@app.route('/edit_course_college/<id>')
def edit_course_college(id):
    db=Db()
    qry = "select college.college,college.id,college.login_id from college inner join college_course where college_course.college_id=college.login_id and college_course.id='"+id+"' "
    qry1 = "select course.course,course.id from course inner join college_course on college_course.course_id=course.id and college_course.id='"+id+"' "
    # qry2 = "select college_course.*,course.course,department.department,college.college from college_course inner join course on course.id=college_course.course_id inner join department on course.department_id=department.id inner join college on college_course.college_id=college.id where college_course.id='"+id+"'"
    qry2="select course.course,course.id as ccid,college.college,college.login_id,college_course.* from college_course,course,college where college_course.id='"+id+"' and college_course.college_id=college.login_id and college_course.course_id=course.id"
    print(qry2)
    res2=db.select(qry2)
    res = db.select(qry)
    res1 = db.select(qry1)
    print("fffffff",res2)
    print("ggg",res)
    print("kkk",res1)
    return render_template('admin/edit_college_course.html',clg=res,course=res1,data2=res2)


@app.route('/edit_course_college_post',methods=['post'])
def edit_course_college_post():
    db=Db()
    id=request.form['id']
    college=request.form['select']
    course=request.form['select2']
    qry="update college_course set college_id='"+college+"',course_id='"+course+"' where id='"+id+"'"
    res=db.update(qry)
    return'''<script>alert("update sucessfully")
    window.location='/view_course_college'</script>'''

@app.route('/delete_college_course/<id>')
def delete_college_course(id):
    db=Db()
    qry1="delete from college_course where id='"+id+"'"
    res1 = db.delete(qry1)
    return '''<script>alert("deletion sucessfully")
        window.location='/view_course_college'</script>'''

@app.route('/ad_add_batch')
def ad_add_batch():
    db=Db()
    qry="select * from course"
    res=db.select(qry)
    return render_template('admin/add_batch.html',data=res)

@app.route('/add_batch_post',methods=['post'])
def add_batch_post():
    db=Db()
    fro =request.form['textfield']
    to=request.form['textfield2']
    course=request.form['select2']
    qry1="insert into batch(from_year,course_id,to_year) values('"+fro+"','"+course+"','"+to+"')"
    print(qry1)
    res=db.insert(qry1)
    return '''<script>alert("sucessfully")
    window.location='/ad_add_batch'</script>'''

@app.route('/ad_view_batch')
def ad_view_batch():
    db=Db()
    qry="select batch.*,course.course from batch INNER JOIN course on batch.course_id=course.id "
    res=db.select(qry)
    return render_template('admin/view_batch.html',data=res)

@app.route('/delete_batch/<id>')
def delete_batch(id):
    db=Db()
    qry="delete from batch where id='"+id+"'"
    db.delete(qry)
    return '''<script>alert("deletion sucessfully")
    window.location='/ad_view_batch'</script>'''

@app.route('/ad_edit_batch/<id>')
def ad_edit_batch(id):
    db=Db()
    qry="select * from course"
    res=db.select(qry)
    qry1 = "select batch.*,course.course from batch INNER JOIN course on batch.course_id=course.id where batch.id='"+id+"' "
    res1 = db.selectOne(qry1)
    return render_template('admin/edit_batch.html',data=res,data1=res1)

@app.route('/edit_batch_post',methods=['post'])
def edit_batch_post():
    db=Db()
    fro=request.form['textfield']
    to=request.form['textfield2']
    course=request.form['select2']
    id=request.form['id']
    qry="update batch set from_year='"+fro+"',to_year='"+to+"',course_id='"+course+"' where id='"+id+"'"
    db.update(qry)
    return '''<script>alert("updation sucessfully")
    window.location='/ad_view_batch'</script>'''


@app.route('/ad_add_subject')
def ad_add_subject():
    db=Db()
    qry="select * from course"
    res=db.select(qry)
    return render_template('admin/add_subject.html',data=res)

@app.route('/add_subject_post',methods=['post'])
def add_subject_post():
    db=Db()
    sub=request.form['textfield']
    subcode=request.form['textfield2']
    course=request.form['select']
    sem=request.form['select2']
    qry="insert into subject(subject,subject_code,course_id,semester) values('"+sub+"','"+subcode+"','"+course+"','"+sem+"')"
    res=db.insert(qry)
    return'''<script>alert("sucessfully")
    window.location='/ad_add_subject'</script>'''


@app.route('/ad_view_subject')
def ad_view_subject():
    db=Db()
    qry="select subject.*,course.course,department.department from subject inner join course on course.id=subject.course_id inner join department on department.id=course.department_id"
    res=db.select(qry)
    qry1="select * from course"
    res1=db.select(qry1)
    return render_template('admin/view_subject_coursewise.html',data=res,data1=res1)

@app.route('/view_subject_post',methods=['post'])
def view_subject_post():
    db=Db()
    course=request.form['select2']
    sem=request.form['select3']
    qry = "select subject.*,course.course,department.department from subject inner join course on course.id=subject.course_id inner join department on department.id=course.department_id where course_id='"+course+"' and semester='"+sem+"'"
    print(qry)
    res = db.select(qry)
    return render_template('admin/view_subject_coursewise.html', data=res)


@app.route('/ad_edit_subject/<id>')
def ad_edit_subject(id):
    db=Db()
    qry="select subject.*,course.course from subject inner join course on course.id=subject.course_id where subject.id='"+id+"'"

    res=db.selectOne(qry)
    print(qry)
    qry1="select * from course"
    res1=db.select(qry1)
    return render_template('admin/edit_subject.html',sub=res,crs=res1)

@app.route('/edit_subject_post',methods=['post'])
def edit_subject_post():
    db=Db()
    sub=request.form['textfield']
    subcode=request.form['textfield2']
    course=request.form['select']
    sem=request.form['select2']
    id=request.form['id']
    qry="update subject set subject='"+sub+"',subject_code='"+subcode+"',course_id='"+course+"',semester='"+sem+"' where id='"+id+"' "
    data=db.update(qry)
    return'''<script>alert("updation sucessfully")
    window,location='/ad_view_subject'</script>'''



@app.route('/delete_subject/<id>')
def delete_subject(id):
    db=Db()
    qry="delete from subject where id='"+id+"'"
    db.delete(qry)
    return'''<script>alert("deletion sucessfully")
    window.location='/ad_view_subject'</script>'''


@app.route('/ad_sent_notification')
def ad_sent_notification():
    return render_template('admin/sent_notification.html')

@app.route('/sent_notification_post',methods=['post'])
def sent_notification_post():
    db=Db()
    notification=request.form['textarea']
    qry="insert into notification(notification,date)values('"+notification+"',curdate())"
    res=db.insert(qry)
    return'''<script>alert("sucessfully")
    window.location='/ad_sent_notification'</script>'''


@app.route('/view_notification')
def view_notification():
    db=Db()
    qry="select * from notification"
    res=db.select(qry)
    return render_template("admin/view_notification.html", data=res)

@app.route('/delete_notification/<id>')
def delete_notification(id):
    db=Db()
    qry="delete from notification where id='"+id+"' "
    res=db.delete(qry)
    return '''<script>alert("delete sucessfully")
    window.location='/view_notification'</script>'''


@app.route('/ad_view_complient')
def ad_view_complient():
    db=Db()
    qry="select complient.*,login.type from complient inner join login on complient.login_id=login.id"
    res=db.select(qry)
    return render_template('admin/view_complient.html',data=res)


@app.route('/ad_sent_complient_replay/<id>')
def ad_sent_complient_replay(id):
    db=Db()
    qry="select complient,id,replay from complient where id='"+id+"'"
    res=db.selectOne(qry)
    return render_template('admin/sent_complient_replay.html',data=res)

@app.route('/sent_complient_replay_post',methods=['post'])
def sent_complient_replay_post():
    db=Db()
    id=request.form['id']
    replay=request.form['textarea']
    qry="update complient set  rep_date=curdate(),replay='"+replay+"',status= 'replied' where id='"+id+"'"
    db.insert(qry)
    return '''<script>alert("sending replay")
    window.location='/ad_view_complient'</script>'''


@app.route('/ad_view_search_students')
def ad_view_search_students():
    db=Db()
    qry = "select college_course.*,course.course from college_course inner join course on college_course.course_id=course.id"
    res = db.select(qry)
    qry1 = "select * from batch "
    res1 = db.select(qry1)
    qry3 = "select * from college"
    res3 = db.select(qry3)
    qry2 = "select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id "
    res2 = db.select(qry2)
    return render_template('admin/view_serch_students.html', course=res, batch=res1, std=res2, clg=res3)


@app.route('/ad_view_search_students_post',methods=['post'])
def ad_view_search_students_post():
    db=Db()
    college = request.form['select']
    course = request.form['select2']
    batch = request.form['select3']
    if college == "select" and batch == "select" and course == "select":
        qry2 = "select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id "
    elif college != "select" and batch == "select" and course == "select":
        qry2 = "select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where college.login_id='" + college + "'"
    elif batch != "select" and college == "select" and course == "select":
        qry2 = "select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.batch_id='" + batch + "'  "
    elif course != "select" and batch == "select" and college == "select":
        qry2 = "select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.course='" + course + "'"
    elif college != "select" and course != "select" and batch == "select":
        qry2 = "select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where college.login_id='" + college + "' and student.course='" + course + "'"
    elif college != "select" and batch != "select" and course == "select":
        qry2 = "select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id where college.login_id='" + college + "' and student.batch_id='" + batch + "' "
    elif batch != "select" and course != "select" and college == "select":
        qry2 = "select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.batch_id='" + batch + "' and student.course='" + course + "'"
    else:
        qry2 = "select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id where student.batch_id='" + batch + "'  and student.course='" + course + "' and college.login_id='" + college + "'"

    res2 = db.select(qry2)
    qry = "select college_course.*,course.course from college_course inner join course on college_course.course_id=course.id"
    res = db.select(qry)
    qry1 = "select * from batch "
    res1 = db.select(qry1)
    qry3 = "select * from college"
    res3 = db.select(qry3)
    return render_template('admin/view_serch_students.html', course=res, batch=res1, std=res2, clg=res3)

@app.route('/view_mark/<id>')
def view_mark(id):
    db=Db()
    session['id']=id
    return render_template('admin/marks.html')


@app.route('/view_markk',methods=['post'])
def view_markk():
    db=Db()
    mark=[]
    mark1=[]
    sem=request.form['select3']
    qry2="select student.course,subject.subject,subject.id as sub_id,course.course from student,subject,college_course,course where student.id='"+str(session['id'])+"' and student.course=college_course.id and course.id=college_course.course_id and subject.semester='"+sem+"' and course.id=subject.course_id"
    sub=db.select(qry2)
    print(sub)
    print("mmm",mark)
    # qry1="select subject.id as subid,subject.subject,subject.semester,external_mark.mark1,internal_mark.mark from subject left join external_mark on external_mark.student_id='"+str(session['id'])+"' left join internal_mark on internal_mark.student_id='"+str(session['id'])+"' where subject.semester='"+sem+"' and subject.id=external_mark.subject_id   "
    for i in sub:
        subid=i['sub_id']
        # qry1="select external_mark.mark1,internal_mark.mark from external_mark,internal_mark where external_mark.student_id='"+str(session['id'])+"' and  external_mark.subject_id='"+str(subid)+"' and  internal_mark.subject_id='"+str(subid)+"'"
        qry1="select mark1,subject_id from external_mark where student_id='"+str(session['id'])+"'  and subject_id='"+str(subid)+"' "

        qry2="select mark, subject_id from internal_mark where student_id='"+str(session['id'])+"'  and subject_id='"+str(subid)+"' "
        print(qry1)
        res1=db.selectOne(qry1)
        res2=db.selectOne(qry2)
        if res1 is not None:
            mark.append(str(res1['mark1']))
        else:
            mark.append('nil')

        if res2 is not None:
            mark1.append(str(res2['mark']))
        else:
            mark1.append('nil')

    print("after ...",mark)
    print(mark1)

    return render_template('admin/marks.html',sub=sub,mark=mark,len1=len(sub),mark1=mark1)
############################!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



@app.route('/view_external_mark')
def view_external_mark():
    db=Db()
    qry="select * from college"
    res=db.select(qry)
    qry1="select college_course.*,course.course from college_course,course where college_course.course_id=course.id"
    res1=db.select(qry1)
    qry2="select * from batch"
    res2=db.select(qry2)
    return render_template("view_external_mark.html",clg=res,course=res1,batch=res2,ln=0)

@app.route('/view_external_mark1',methods=['post'])
def view_external_mark1():
    db=Db()
    clg=request.form['cid']
    qry="select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+clg+"'"
    print(qry)
    res=db.select(qry)
    return jsonify(res)

@app.route('/view_external_mark2',methods=['post'])
def view_external_mark2():
    db=Db()
    course=request.form['cid']
    qry = "select batch.*,college_course.course_id,course.id as cid from batch,college_course,course where college_course.course_id=course.id and college_course.id='" +course+ "'"
    print(qry)
    res = db.select(qry)
    return jsonify(res)

@app.route('/vview_external',methods=['post'])
def vview_external():
    db=Db()
    qry3 = "select * from college"
    res3 = db.select(qry3)
    qry4 = "select college_course.*,course.course from college_course,course where college_course.course_id=course.id"
    res4 = db.select(qry4)
    qry2 = "select * from batch"
    res2 = db.select(qry2)
    course=request.form['select']
    clg=request.form['select2']
    batch=request.form['select4']
    sem=request.form['select3']
    qry = "select DISTINCT student.id,student.name,student.regno from student,college_course,course,subject where college_course.id='" + course + "' and college_course.course_id=course.id and subject.semester='" + sem + "' and subject.course_id=course.id and student.batch_id='" + batch + "'and  student.college_lid='" + clg + "' and student.course=college_course.id "


    res = db.select(qry)

    subject1 = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
    sub1 = db.select(subject1)

    print(res)

    # head=[0,0]
    # marks = []

    allstds=[]
    for i in res:

        std=[i['name'],i['regno']]
        stid=i['id']
        subject = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
        sub = db.select(subject)
        for j in sub:
            qry1="select mark1 from external_mark where student_id='"+str(stid)+"' and  subject_id='"+str(j['id'])+"'"
            # print(qry1)
            mark=db.selectOne(qry1)
            if mark is not None:
                std.append(mark['mark1'])
            else:
                std.append('not available')
        allstds.append(std)


        print(allstds)




    return render_template("view_external_mark.html",sub1=sub1,allstds=allstds,sln=len(sub1),clg=res3, course=res4, batch=res2)






@app.route('/view_internal_mark')
def view_internal_mark():
    db=Db()
    qry="select * from college"
    res=db.select(qry)
    qry1="select college_course.*,course.course from college_course,course where college_course.course_id=course.id"
    res1=db.select(qry1)
    qry2="select * from batch"
    res2=db.select(qry2)
    return render_template("view_internal_mark.html",clg=res,course=res1,batch=res2)

@app.route('/view_internal_mark1',methods=['post'])
def view_internal_mark1():
    db=Db()
    clg=request.form['cid']
    qry="select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+clg+"'"
    print(qry)
    res=db.select(qry)
    return jsonify(res)

@app.route('/view_internal_mark2',methods=['post'])
def view_internal_mark2():
    db=Db()
    course=request.form['cid']
    qry = "select batch.*,college_course.course_id,course.id as cid from batch,college_course,course where college_course.course_id=course.id and college_course.id='" +course+ "'"
    print(qry)
    res = db.select(qry)
    return jsonify(res)



@app.route('/vview_internal_mark')
def vview_internal_mark():
    db = Db()
    qry3 = "select * from college"
    res3 = db.select(qry3)
    qry4 = "select college_course.*,course.course from college_course,course where college_course.course_id=course.id"
    res4 = db.select(qry4)
    qry2 = "select * from batch"
    res2 = db.select(qry2)
    course = request.form['select']
    clg = request.form['select2']
    batch = request.form['select4']
    sem = request.form['select3']
    qry = "select DISTINCT student.id,student.name,student.regno from student,college_course,course,subject where college_course.id='" + course + "' and college_course.course_id=course.id and subject.semester='" + sem + "' and subject.course_id=course.id and student.batch_id='" + batch + "'and  student.college_lid='" + clg + "' and student.course=college_course.id "

    res = db.select(qry)

    subject1 = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
    sub1 = db.select(subject1)

    print(res)

    # head=[0,0]
    # marks = []

    allstds = []
    for i in res:

        std = [i['name'], i['regno']]
        stid = i['id']
        subject = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
        sub = db.select(subject)
        for j in sub:
            qry1 = "select mark from internal_mark where student_id='" + str(stid) + "' and  subject_id='" + str(j['id']) + "'"
            # print(qry1)
            mark = db.selectOne(qry1)
            if mark is not None:
                std.append(mark['mark1'])
            else:
                std.append('not available')
        allstds.append(std)

        print(allstds)

    return render_template("view_external_mark.html", sub1=sub1, allstds=allstds, sln=len(sub1), clg=res3, course=res4,
                           batch=res2)



@app.route('/ad_view_verifier_details')
def ad_view_verifier_details():
    db=Db()
    res=db.select("select * from verifier")
    return render_template('admin/view_verifier_details.html',data=res)




@app.route('/ad_certificate_generate')
def ad_certificate_generate():
    db = Db()
    res = db.select("select * from college")
    return render_template('admin/certificate_generate.html', data = res)











@app.route('/ajax_dept_by_clg',methods=['post'])
def ajax_dept_by_clg():
    c = Db()
    clg = request.form['clgid']
    ce = "select distinct(department.id),department.department from college_course,course,department where college_course.course_id=course.id and course.department_id=department.id and college_course.college_id='" + clg + "'"

    print(ce)

    res = c.select(ce)

    print(res)

    return jsonify(res)


@app.route("/adm_ajax_course_call_internal",methods=['post'])
def call_adm_ajax_course_call_internalintern():
    ci=Db()
    clg=request.form['clgid']
    dep=request.form['dptid']
    session['dep']=dep
    session['clg']=clg
    de="select course.id,course.course from course inner join college_course on course.id=college_course.course_id where course.department_id='"+dep+"' and college_course.college_id='"+clg+"'"
    res=ci.select(de)
    return jsonify(res)


@app.route("/adm_ajax_batch",methods=['post'])
def adm_ajax_batch():
    ci=Db()
    clg=request.form['clgid']
    course_id=request.form['course_id']
    session['course_id']= course_id
    de="select batch.* from batch inner join course on batch.course_id = course.id and course.id = '"+course_id+"'"
    res=ci.select(de)
    return jsonify(res)


@app.route("/adm_ajax_studdd",methods=['post'])
def adm_ajax_studdd():
    ci=Db()
    clg=session['clg']
    dep=session['dep']
    cou = session['course_id']
    batch_id = request.form['batch']

    print(clg)
    print(cou)
    print(batch_id)
    clgg="select * from college"
    college=ci.select(clgg)
    # batch=ci.select("select * from batch")
    # dep=ci.select("select * from department")
    # course=ci.select("select * from course")



    de="select student.*,department.department,course.course,college.college,batch.from_year,batch.to_year,cert_generation.status from student,cert_generation,college,course,department,college_course,batch where student.college_lid=college.login_id and student.course=college_course.id and course.id = college_course.course_id and batch.course_id = course.id and batch.id = student.batch_id  and course.department_id = department.id  and student.college_lid='"+clg+"' and course.id ='"+str(cou)+"' and  course.department_id ='"+str(dep)+"' and student.batch_id = '"+batch_id+"'and cert_generation.regno=student.regno"
    print(de)
    res=ci.select(de)
    per = []
    imgg=[]
    certificate=[]
    if res:

        for i in res:

            image=[i['image']]

            certificate = [ i['name'],i['regno'], i['department'], i['course'],i['from_year']+"-"+i['to_year'],i['id'],i['status']]
            # i['name'], i['image'], i['regno'], i['department'], i['course']
            sub_total = ci.selectOne("select count(external_mark.subject_id) as ext_sub,count(internal_mark.subject_id) as int_sub from external_mark inner join internal_mark on external_mark.subject_id = internal_mark.subject_id and internal_mark.student_id = external_mark.student_id and external_mark.student_id = '"+str(i['id'])+"'  ")
            flag = 0

            if sub_total:
                ext_sub = sub_total['ext_sub']
                int_sub = sub_total['int_sub']

                if ext_sub == None:
                    ext_sub = 0
                elif int_sub == None:
                    int_sub = 0


                if ext_sub == int_sub:

                    flag = 1

                    print("select sum(external_mark.mark1) as ext_sum,sum(internal_mark.mark) as int_sum from external_mark inner join internal_mark on external_mark.student_id = internal_mark.student_id and external_mark.subject_id = internal_mark.subject_id and external_mark.student_id = '"+str(i['id'])+"'")

                    tot_mrk = ci.selectOne("select sum(external_mark.mark1) as ext_sum,sum(internal_mark.mark) as int_sum from external_mark inner join internal_mark on external_mark.student_id = internal_mark.student_id and external_mark.subject_id = internal_mark.subject_id and external_mark.student_id = '"+str(i['id'])+"'")

                    if tot_mrk:
                        print("====mark=====",tot_mrk)

                        ext_sum = tot_mrk['ext_sum']
                        int_sum = tot_mrk['int_sum']

                        if ext_sum == None:

                            ext_sum = 0.0

                        elif int_sum == None:

                            int_sum = 0.0

                        mrk = ext_sum + int_sub
                        totalmark =  int(ext_sub) * 100

                        if totalmark != 0:

                            percentage = float((mrk * 100) / totalmark)
                            certificate.append(percentage)
                            if percentage>=90:
                                clas="First Class  with distinction"
                                grade="A+"
                            elif percentage>=80:
                                clas="First Class with distinction"
                                grade = "A"
                            elif percentage>=70:
                                clas="First Class"
                                grade = "B"
                            elif percentage>=60:
                                clas="First Class"
                                grade = "C"
                            elif percentage>=50:
                                clas="Second Class"
                                grade = "D"
                            elif percentage>=40:
                                clas="Third Class"
                                grade = "E"
                            else:
                                clas="fail"
                                grade = "F"

                            certificate.append(clas)
                            certificate.append(grade)


                        else:
                            # prcentage
                            certificate.append('---')
                            # grade
                            certificate.append('---')
                            # class
                            certificate.append('---')
            # per.append(image)
            per.append(certificate)
            imgg.append(image)
            print("kkkk",imgg)
    print("cert",certificate)
    print("percentage", per)
    print(res)
    return render_template('admin/certificate_generate.html',percentage=per,res=res,image=imgg,data=college)


    # return jsonify(percentage=per )
# result = res,ln=len(res)



@app.route("/adm_cert_gen/<stid>/<cls>/<grade>/<regno>")
def adm_cert_gen(stid,cls,grade,regno):
    db = Db()
    qryy="update cert_generation set status='generated'  where regno='"+regno+"'"
    db.update(qryy)
    clss=cls
    grade=grade
    print("clsss", cls)
    # r1=random.randint(00,99)
    # r2=random.randint(00,99)
    # r3 = random.randint(00, 99)
    # r4 = random.randint(00, 99)
    # s=str(r1)+"#"+str(r2)+"#"+str(stid)+"#"+str(r3)+"#"+str(r4)+"#"
    # print("gg")
    # print(s)

    # c=conn()
    # import pyqrcode
    # # Generate QR code
    # url = pyqrcode.create(s)
    # # Create and save the png file naming "myqr.png"

    key = "123456789"
    aes = AESCipher(key)



    image = db.selectOne("select image from student where id = '"+stid+"'")
    print()

    # filepath = "C:\\Users\\hp\\PycharmProjects\\uniqid\\static\\student_pics\\"+image['image']
    filepath = "C:\\Users\\hp\\PycharmProjects\\uniqid\\static\\student_pics\\"+str(image)

    face_id = faceid(filepath)

    featurs = str(face_id)

    encrypt_data = aes.encrypt(featurs)
    print("encryptdta", encrypt_data, "type=====", type(encrypt_data))

    qr = qrcode.QRCode(
        version=1,

        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4, )

    qr.add_data(encrypt_data.decode("utf-8"))
    qr.make(fit=True)
    img = qr.make_image()

    img.save("C:\\Users\\hp\\PycharmProjects\\uniqid\\static\\qr\\" + stid + ".jpg")

    # img.svg("C:\\Users\\hp\\PycharmProjects\\uniqid\\static\\qr\\"+stid+".svg", scale=8)
    qr_path = "/static/qr/" + stid + ".jpg"


    qry="select department.department,student.name,student.regno,batch.to_year,student.gender,course.course,cert_generation.status from cert_generation,batch,department,course,student,college_course where student.course = college_course.id and college_course.course_id = course.id and   course.department_id = department.id  and batch.id=student.batch_id and student.id = '"+stid+"' and cert_generation.regno='"+regno+"'"
    print(qry)
    res=db.selectOne(qry)
    print(res)
    if(res['gender']=='male'):
        g="he"
        h="him"
    else:
        g="she"
        h="her"
    # cls=request.form['cls']
    # print(cls)
    timestr = time.strftime("%Y/%m/%d  %H:%M:%S")
    timestr1 = time.strftime("%Y/%m/%d")
    print(timestr)



    # res1=c.selectall("select distinct(subject.sub_id) from subject,student where student.c_id=subject.c_id and student.login_id='"+stid+"'")
    # print(res1[0])
    return render_template("admin/adm_cert.html",res=res,data2=qr_path,gender=g,h=h,clss=clss,grade=grade,time=timestr,date=timestr1)


def faceid(filepath):
    try:
        import requests
        # 7 days trial face api......search try cognitive face api...microsoft azura
        subscription_key ="98dcf2ccd2224618adcea6f5b4eee35c"
        assert subscription_key
        face_api_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/detect'

        headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion'
        }
        data = open(filepath, 'rb')
        response = requests.post(face_api_url, headers=headers, data=data, params=params)
        faces = response.json()

        face_id = faces[0]['faceId']

        print("===face",face_id)

        return face_id

    except Exception as e:

        print(e)





@app.route('/ad_view_certificate_fraud')
def ad_view_certificate_fraud():
    db=Db()
    qry="select certificate_fraud.*,verifier.name,verifier.mail_id,verifier.phone_no from certificate_fraud,verifier where verifier.verifier_lid=certificate_fraud.verifier_lid"
    res=db.select(qry)
    return render_template('admin/view_certificate_fraud.html',data=res)


# ...........................admin end....................................................................................



#.....................college............................................................................

@app.route('/c_homepage')
def c_homepage():
   return render_template("college/college_homepage.html")


@app.route('/c_view_profile')
def c_view_profile():
    db=Db()
    qry="select college.*,login.id from college inner join login on college.login_id=login.id"
    res=db.selectOne(qry)
    return render_template('college/view_profile.html',data=res)



@app.route('/c_add_staff')
def c_add_staff():
    db=Db()
    qry="select * from department"
    res=db.select(qry)
    return render_template('college/add_staff.html',data=res)

@app.route('/add_staff_post',methods=['post'])
def add_staff_post():
    db=Db()
    name=request.form['textfield']
    dob=request.form['textfield2']
    gender=request.form['radio']
    housename=request.form['textfield3']
    post=request.form['textfield4']
    place=request.form['textfield5']
    pin=request.form['textfield6']
    dep=request.form['select']
    mailid=request.form['textfield8']
    phoneno=request.form['textfield9']
    qry1="insert into login(user_name,password,type) values('"+mailid+"','"+phoneno+"','staff')"
    res=db.insert(qry1)
    qry="insert into college_staff(name,house_name,post,place,pin_code,gender,dob,mail_id,phone_no,login_id,department_id,college_lid) values('"+name+"','"+housename+"','"+post+"','"+place+"','"+pin+"','"+gender+"','"+dob+"','"+mailid+"','"+phoneno+"','"+str(res)+"','"+dep+"','"+str(session['lid'])+"')"
    print(qry)
    res1=db.insert(qry)

    return'''<script>alert("sucessfully")
    window.location='/c_add_staff'</script>'''

@app.route('/c_view_staff')
def c_view_staff():
    db=Db()
    qry="select * from department"
    qry1="select college_staff.*,department.department from college_staff inner join department on college_staff.department_id=department.id where college_staff.college_lid='"+str(session['lid'])+"'"
    res=db.select(qry)
    res1=db.select(qry1)
    return render_template('college/view_staff.html',dep=res,staff=res1)

@app.route('/c_edit_staff/<id>')
def c_edit_staff(id):
    db=Db()
    qry1="select college_staff.*,department.department from college_staff inner join department on college_staff.department_id=department.id  where college_staff.id='"+id+"'"
    res1 = db.selectOne(qry1)
    qry="select * from department"
    res=db.select(qry)
    print(qry)
    print(qry1)
    return render_template('college/edit_staff.html',dep=res,data=res1)

@app.route('/edit_staff_post',methods=['post'])
def edit_staff_post():
    db=Db()
    name=request.form['textfield']
    dob=request.form['textfield2']
    gender=request.form['radio']
    housename=request.form['textfield4']
    post=request.form['textfield5']
    place=request.form['textfield6']
    pin=request.form['textfield7']
    dep=request.form['select']
    mail=request.form['textfield9']
    phoneno=request.form['textfield10']
    id=request.form['id']
    qry="update college_staff set name='"+name+"',dob='"+dob+"',gender='"+gender+"',house_name='"+housename+"',post='"+post+"',place='"+place+"',pin_code='"+pin+"',department_id='"+dep+"',mail_id='"+mail+"',phone_no='"+phoneno+"',college_lid='"+str(session['lid'])+"' where id='"+id+"'"
    print(qry)
    db.update(qry)

    return '''<script>alert("update sucessfully")
    window.location='/c_view_staff'</script>'''



@app.route('/c_delete_staff/<id>')
def delete_staff(id):
    db=Db()
    qry="delete from college_staff where id='"+id+"'"
    db.delete(qry)
    return '''<script>alert("deleted sucessfully")
    window.location='/c_view_staff'</script>'''



@app.route('/c_add_student')
def c_add_student():
    db=Db()
    qry="select * from batch"
    res=db.select(qry)
    #qry1="select college_course.course_id,course.course from college_course inner join course on course.id=college_course.course_id"
    #qry1="select * from college_course"
    qry1="select course.*,college_course.* from college_course,course where course.id=college_course.course_id and college_course.college_id='"+str(session['lid'])+"'"
    res1=db.select(qry1)
    print(qry1)
    return render_template('college/add_student.html',batch=res,course=res1)

@app.route('/student_add', methods=['post'])

def student_add():
    db = Db()
    course = request.form['cid']
    qry = "select batch.* from batch,college_course,course where college_course.id='"+course+"'and batch.course_id=course.id and college_course.course_id=course.id"
    print(qry)
    res = db.select(qry)
    return jsonify(res)


@app.route('/add_student',methods=['post'])
def add_student():
    db=Db()
    try:
        image=request.files['filefield']
        name=request.form['textfield']
        regno=request.form['textfield2']
        dob=request.form['textfield3']
        post=request.form['textfield4']
        housename=request.form['textfield5']
        place=request.form['textfield6']
        gender=request.form['radio']
        pin=request.form['textfield8']
        admission=request.form['textfield11']
        mail=request.form['textfield13']
        phone=request.form['textfield14']
        state=request.form['select']
        dist=request.form['select2']
        course=request.form['select3']
        # fro=request.form['select4']
        batch=request.form['select5']

        # key="123456789"
        # aes=AESCipher(key)
        image.save(filepath_stu_pic+image.filename)
        # img=image.open('')
        # featurs=str(123456)
        # encrypt_data=aes.encrypt(featurs)
        # print("encryptdta",encrypt_data,"type=====",type(encrypt_data))
        #
        # qr = qrcode.QRCode(
        #     version=1,
        #
        #     error_correction=qrcode.constants.ERROR_CORRECT_L,
        #     box_size=10,
        #     border=4, )
        # qr.add_data(encrypt_data.decode("utf-8"))
        # qr.make(fit=True)
        # img = qr.make_image()
        #
        # img.save("C:\\Users\\hp\\PycharmProjects\\uniqid\\static\\qr\\" + name + ".jpg")

        qry="insert into student(name,regno,house_name,post,place,pin,dob,gender,admission_date,course,mail_id,phone_no,image,state,district,batch_id,college_lid)VALUES ('"+name+"','"+regno+"','"+housename+"','"+post+"','"+place+"','"+pin+"','"+dob+"','"+gender+"','"+admission+"','"+course+"','"+mail+"','"+phone+"','"+image.filename+"','"+state+"','"+dist+"','"+batch+"','"+str(session['lid'])+"')"
        res=db.insert(qry)
        qry1 = "insert into cert_generation(regno,status)VALUES('" + regno + "','pending')"
        db.insert(qry1)

        if res>0:
            return '''<script>alert("Added sucessfully")
                window.location='/c_add_student'</script>'''
        else:
            return "no"
    except Exception as e:
        print(str(e))


@app.route('/c_view_student')
def c_view_student():
    db=Db()
    qry="select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.college_lid='"+str(session['lid'])+"'"
    res=db.select(qry)
    qry1="select * from batch "
    res1=db.select(qry1)
    qry2="select college_course.*,course.course from college_course inner join course on college_course.course_id=course.id where college_course.college_id='"+str(session['lid'])+"'"
    res2=db.select(qry2)
   # print(qry)
    return render_template('college/view_student.html',data=res,batch=res1,course=res2)


@app.route('/view_student_post',methods=['post'])
def view_student_post():
    db=Db()
    course=request.form['select']
    batch=request.form['select2']
    if course=="select" and batch=="select":
        qry = "select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  "
    elif course!="select" and batch=="select":
        qry="select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on  student.batch_id=batch.id where student.course='"+course+"'"
    elif batch!="select" and course=="select":
        qry = "select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.batch_id='"+batch+"' "
    else:
        qry = "select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on  student.batch_id=batch.id where student.course='" + course + "'and student.batch_id='"+batch+"'  "


    # print(qry)
    res=db.select(qry)

    qry1="select * from batch"
    res1=db.select(qry1)
    qry2="select college_course.*,course.course from college_course inner join course on college_course.course_id=course.id where college_course.college_id='"+str(session['lid'])+"'"
    res2=db.select(qry2)

    return render_template('college/view_student.html',data=res,batch=res1,course=res2)



@app.route('/delete_student/<id>')
def delete_student(id):
    db=Db()
    qry="delete from student where id='"+id+"'"
    db.delete(qry)
    return render_template('college/view_student.html')


@app.route('/c_edit_student/<id>')
def c_edit_student(id):
    db = Db()
    qry = "select * from batch"
    res = db.select(qry)
    # qry1=" select course.course as cname,college_course.*,student.course as courseid,student.id from college_course inner join course on course.id=college_course.course_id  inner join student on student.course=college_course.id  where college_course.college_id='"+str(session['lid'])+"' "
    # res1 = db.select(qry1)
    qry2 = "select * from student where id='"+id+"'"
    res2 = db.selectOne(qry2)
    qry3="select college_course.course_id,college_course.id,college_course.college_id,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+str(session['lid'])+"'"
    print(qry3)
    res3=db.select(qry3)
    print(res3)
    print(res2)
    return render_template('college/edit_student.html',batch=res,std=res2,data=res3)
# ,data=res1

@app.route('/edit_student',methods=['post'])
def edit_student():
    db = Db()
    name=request.form['textfield']
    regno=request.form['textfield2']
    dob=request.form['textfield3']
    housename=request.form['textfield4']
    gender=request.form['radio']
    post=request.form['textfield5']
    place=request.form['textfield6']
    pin=request.form['textfield7']
    state=request.form['select']
    dist=request.form['select2']
    course=request.form['select3']
    batchfrom=request.form['select4']
    # batchto=request.form['select5']
    admission=request.form['textfield10']
    mail=request.form['textfield12']
    phone=request.form['textfield13']
    id=request.form['id']
    if request.files is not None:

        if "pic" in request.files:

            if request.files['pic'].filename!='':

                image = request.files['pic']
                image.save(filepath_stu_pic + image.filename)
                qry="update student set image='"+image.filename+"',name='"+name+"',regno='"+regno+"',dob='"+dob+"',house_name='"+housename+"',gender='"+gender+"',post='"+post+"',place='"+place+"',pin='"+pin+"',state='"+state+"',district='"+dist+"',course='"+course+"',admission_date='"+admission+"',batch_id='"+batchfrom+"',mail_id='"+mail+"',phone_no='"+phone+"' where id='"+id+"'"
                db.update(qry)
            else:
                qry="update student set name='"+name+"',regno='"+regno+"',dob='"+dob+"',house_name='"+housename+"',gender='"+gender+"',post='"+post+"',place='"+place+"',pin='"+pin+"',state='"+state+"',district='"+dist+"',course='"+course+"',admission_date='"+admission+"',batch_id='"+batchfrom+"',mail_id='"+mail+"',phone_no='"+phone+"' where id='"+id+"'"
                db.update(qry)
        else:
            qry = "update student set name='" + name + "',regno='" + regno + "',dob='" + dob + "',house_name='" + housename + "',gender='" + gender + "',post='" + post + "',place='" + place + "',pin='" + pin + "',state='" + state + "',district='" + dist + "',course='" + course + "',admission_date='" + admission + "',batch_id='" + batchfrom + "',mail_id='" + mail + "',phone_no='" + phone + "' where id='" + id + "'"
            db.update(qry)

    else:
        qry = "update student set name='" + name + "',regno='" + regno + "',dob='" + dob + "',house_name='" + housename + "',gender='" + gender + "',post='" + post + "',place='" + place + "',pin='" + pin + "',state='" + state + "',district='" + dist + "',course='" + course + "',admission_date='" + admission + "',batch_id='" + batchfrom + "',mail_id='" + mail + "',phone_no='" + phone + "' where id='" + id + "'"
        db.update(qry)
    return'''<script>alert("update sucessfully")
    window.location='/c_view_student'</script>'''


@app.route('/c_view_notificationn')
def view_notificationn():
    db=Db()
    qry="select * from notification"
    res=db.select(qry)
    return render_template('view_notifica.html',data=res)



@app.route('/c_view_course')
def c_view_course():
    db = Db()
    qry = "select course.*,department.department from course inner JOIN department on department.id=course.department_id"
    res=db.select(qry)
    qry1="select * from college"
    res1=db.select(qry1)
    return render_template('college/view_course.html',data=res,clg=res1)

@app.route('/view_course_post',methods=['post'])
def view_course_post():
    db=Db()
    college=request.form['select']
    print(college)
    qry1 = "select * from college"
    res1 = db.select(qry1)
    if college=="select":
        qry = "select course.*,department.department from course inner JOIN department on department.id=course.department_id"
    else:
        qry = "select college_course.*,course.course,department.department from college_course inner join course on course.id=college_course.course_id inner join department on course.department_id=department.id where college_course.college_id='" +college + "' "
    res = db.select(qry)
    return render_template('college/view_course.html',data=res,clg=res1)

@app.route('/sent_complient')
def sent_complient ():
    return render_template('sent_complient.html')

@app.route('/sent_complient_post',methods=['post'])
def sent_complient_post ():
    db=Db()
    comp=request.form['textarea']
    qry="insert into complient(comp_date,complient,status,login_id,replay,rep_date)values(curdate(),'"+comp+"','pending','"+str(session['lid'])+"','pending','pending') "
    db.insert(qry)
    print(qry)
    return'''<script>alert("sent complient sucessfully")
    window.location='/sent_complient'</script>'''

@app.route('/view_complient')
def view_complient ():
    db=Db()
    qry="select complient.*,college.college,college.login_id from complient inner join college on complient.login_id=college.login_id where complient.login_id='"+str(session['lid'])+"'"
    res=db.select(qry)
    return render_template('college/clg_view_complient.html',data=res)

@app.route('/vview_replay/<id>')
def vview_replay(id):
    db=Db()
    qry="select complient,status,replay,rep_date from complient where id='"+id+"' "
    res=db.selectOne(qry)
    return render_template('view_replay.html',data=res)

@app.route('/ddelete_complient/<id>')
def delete_complient(id):
    db=Db()
    qry="delete from complient where id='"+id+"' "
    res=db.delete(qry)
    return'''<script>alert("delete sucessfully")
    window.locationm='/view_complient'</script>'''

@app.route('/clg_view_external_mark')
def clg_view_external_mark():
    db=Db()
    # qry="select * from college"
    # res=db.select(qry)
    qry1="select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+str(session['lid'])+"'"
    print(qry1)
    res1=db.select(qry1)
    qry2="select * from batch"
    res2=db.select(qry2)
    return render_template("college/clg_view_external.html",course=res1,batch=res2)

# @app.route('/clg_view_external_mark1',methods=['post'])
# def view_external_mark1():
#     db=Db()
#     clg=request.form['cid']
#     qry="select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+clg+"'"
#     print(qry)
#     res=db.select(qry)
#     return jsonify(res)

@app.route('/clg_view_external_mark2',methods=['post'])
def clg_view_external_mark2():
    db=Db()
    course=request.form['cid']
    # qry = "select batch.*,college_course.course_id,course.id as cid from batch,college_course,course where college_course.course_id=course.id and college_course.id='" +course+ "'"
    qry="select  distinct batch.* from batch,college_course,course where college_course.course_id=course.id and batch.course_id='"+course+"' and course.id=batch.course_id"
    print(qry)

    res = db.select(qry)
    return jsonify(res)

@app.route('/clg_vview_external',methods=['post'])
def clg_vview_external():
    db=Db()
    # qry3 = "select * from college"
    # res3 = db.select(qry3)
    qry4 = "select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+str(session['lid'])+"'"
    res4 = db.select(qry4)
    qry2 = "select * from batch"
    res2 = db.select(qry2)
    course=request.form['select']
    # clg=request.form['select2']
    batch=request.form['select4']
    sem=request.form['select3']
    # qry = "select DISTINCT student.id,student.name,student.regno from student,college_course,course,subject where college_course.id='" + course + "' and college_course.course_id=course.id and subject.semester='" + sem + "' and subject.course_id=course.id and student.batch_id='" + batch + "'and  student.college_lid='" +str(session['lid']) + "' and student.course=college_course.id "
    qry="select distinct student.id,student.name,student.regno from student,college_course,course,subject where college_course.course_id='"+course+"' and student.course=college_course.id and college_course.course_id=course.id and subject.semester='"+sem+"' and subject.course_id=course.id and student.batch_id='"+batch+"'and  student.college_lid='"+str(session['lid'])+"' "
    print(qry)
    res = db.select(qry)
    # subject1 = "select distinct subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.course_id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
    subject1="select * from subject where course_id='"+course+"' and semester='"+sem+"'"

    print(subject1)
    sub1 = db.select(subject1)
    print("sub",sub1)
    print(res)

    # head=[0,0]
    # marks = []

    allstds=[]
    for i in res:

        std=[i['name'],i['regno']]
        stid=i['id']
        # subject = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
        subject="select * from subject where course_id='"+course+"' and semester='"+sem+"'"
        sub = db.select(subject)
        for j in sub:
            qry1="select mark1 from external_mark where student_id='"+str(stid)+"' and  subject_id='"+str(j['id'])+"'"
            # print(qry1)
            mark=db.selectOne(qry1)
            if mark is not None:
                std.append(mark['mark1'])
            else:
                std.append('not available')
        allstds.append(std)


        print(allstds)




    return render_template("college/clg_view_external.html",sub1=sub1,allstds=allstds,sln=len(sub1), course=res4, batch=res2)








@app.route('/clg_view_internal_mark')
def clg_view_internal_mark():
    db=Db()
    # qry="select * from college"
    # res=db.select(qry)
    qry1="select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+str(session['lid'])+"'"
    print(qry1)
    res1=db.select(qry1)
    qry2="select * from batch"
    res2=db.select(qry2)
    return render_template("college/clg_view_internal.html",course=res1,batch=res2)

# @app.route('/clg_view_internal_mark1',methods=['post'])
# def clg_view_internal_mark1():
#     db=Db()
#     clg=request.form['cid']
#     qry="select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+clg+"'"
#     print(qry)
#     res=db.select(qry)
#     return jsonify(res)

@app.route('/clg_view_internal_mark2',methods=['post'])
def clg_view_internal_mark2():
    db=Db()
    course=request.form['cid']
    # qry = "select batch.*,college_course.course_id,course.id as cid from batch,college_course,course where college_course.course_id=course.id and college_course.id='" +course+ "'"
    qry="select  distinct batch.* from batch,college_course,course where college_course.course_id=course.id and batch.course_id='"+course+"' and course.id=batch.course_id"
    print(qry)

    res = db.select(qry)
    return jsonify(res)



@app.route('/clg_vview_internal_mark',methods=['post'])
def clg_vview_internal_mark():
    db = Db()
    # qry3 = "select * from college"
    # res3 = db.select(qry3)
    qry4 = "select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+str(session['lid'])+"'"
    res4 = db.select(qry4)
    qry2 = "select * from batch"
    res2 = db.select(qry2)
    course=request.form['select']
    # clg=request.form['select2']
    batch=request.form['select4']
    sem=request.form['select3']
    # qry = "select DISTINCT student.id,student.name,student.regno from student,college_course,course,subject where college_course.id='" + course + "' and college_course.course_id=course.id and subject.semester='" + sem + "' and subject.course_id=course.id and student.batch_id='" + batch + "'and  student.college_lid='" +str(session['lid']) + "' and student.course=college_course.id "
    qry="select distinct student.id,student.name,student.regno from student,college_course,course,subject where college_course.course_id='"+course+"' and student.course=college_course.id and college_course.course_id=course.id and subject.semester='"+sem+"' and subject.course_id=course.id and student.batch_id='"+batch+"'and  student.college_lid='"+str(session['lid'])+"' "
    print(qry)
    res = db.select(qry)
    # subject1 = "select distinct subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.course_id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
    subject1="select * from subject where course_id='"+course+"' and semester='"+sem+"'"
    sub1 = db.select(subject1)
    print("sub", sub1)
    print(res)

    # head=[0,0]
    # marks = []

    allstds = []
    for i in res:

        std = [i['name'], i['regno']]
        stid = i['id']
        # subject = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
        subject = "select * from subject where course_id='" + course + "' and semester='" + sem + "'"
        sub = db.select(subject)
        for j in sub:
            qry1 = "select mark from internal_mark where student_id='" + str(stid) + "' and  subject_id='" + str(j['id']) + "'"
            # print(qry1)
            mark = db.selectOne(qry1)
            if mark is not None:
                std.append(mark['mark'])
            else:
                std.append('not available')
        allstds.append(std)

        print(allstds)


    return render_template("college/clg_view_internal.html", sub1=sub1, allstds=allstds, sln=len(sub1),  course=res4,
                           batch=res2)













#........college  end..............................................................................
#.......staff......................................................................................................

@app.route('/st_homepage')
def st_homepage():
   return render_template("staff/staff_homepage.html")


@app.route('/st_view_profile')
def st_view_profile():
    db=Db()
    qry=" select college_staff.*,department.department,college.college from college_staff inner join department on department.id=college_staff.department_id inner join college on college.login_id=college_staff.college_lid where college_staff.login_id='"+str(session['lid'])+"'"
    res=db.selectOne(qry)
    return render_template('staff/view_profile.html',data=res)

@app.route('/st_view_notification')
def st_view_notification():
    db = Db()
    qry = "select * from notification"
    res = db.select(qry)
    return render_template('view_notificatio.html', data=res)


@app.route('/st_view_studentinfo')
def st_view_studentinfo():
    db=Db()
    qry2="  select college_course.*,college_staff.college_lid,course.course from college_course,college_staff,course where college_course.college_id=college_staff.college_lid and college_course.course_id=course.id"
    res2=db.select(qry2)
    qry1="select * from batch"
    res1=db.select(qry1)
    qry = "select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id"
    res=db.select(qry)
    return render_template('staff/view_studentinfo.html',course=res2,batch=res1,data=res)

@app.route('/st_view_studentinfo_post',methods=['post'])
def st_view_studentinfo_post():
    db=Db()
    course=request.form['select4']
    batch=request.form['select3']
    if course == "select" and batch == "select":
        qry = "select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  "
    elif course != "select" and batch == "select":
        qry = "select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.course='" + course + "'"
    elif batch != "select" and course == "select":
        qry = "select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.batch_id='" + batch + "' "
    else:
        qry = "select student.*,course.course,batch.from_year,batch.to_year from student inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id where student.course='" + course + "'and student.batch_id='" + batch + "' "
    res=db.select(qry)
    return render_template('staff/view_studentinfo.html',data=res)


@app.route('/st_add_internal_mark')
def st_add_internal_mark():
    db=Db()
    qry3 = "select college.*,college_staff.college_lid from college,college_staff where college_staff.login_id='" + str(session['lid']) + "' and college.login_id=college_staff.college_lid "
    res3 = db.selectOne(qry3)
    qry=" select college_course.*,course.course,college_staff.college_lid from course,college_course,college_staff where  college_staff.login_id='"+str(session['lid'])+"' and college_staff.college_lid=college_course.college_id and course.id=college_course.course_id"
    # qry="select college_course.*,course.course from course,college_course where college_course.course_id=course.id  "
    res=db.select(qry)

    qry1="select * from subject"
    res1=db.select(qry1)
    qry2="select * from batch "
    res2=db.select(qry2)
    return render_template('staff/add_internal_mark.html',course=res,sub=res1,batch=res2,clg=res3)


@app.route('/internal_mark_post',methods=['post'])
def internal_mark_post():
    db=Db()
    course=request.form['cid']
    sem=request.form['sem']
    #clgid=request.form['clgid']
    qry="select * from subject,course,college_course where course.id=college_course.course_id and  subject.semester='"+sem+"' and college_course.id='"+course+"'"
    res=db.select(qry)
    print(qry)
    return jsonify(res)

@app.route('/internal_mark_post1', methods=['post'])
def internal_mark_post1():
    db = Db()
    course = request.form['cid']
    qry = "select batch.*,college_course.course_id,course.id as cid from batch,college_course,course where college_course.course_id=course.id and college_course.id='" + course + "'"
    print(qry)
    res = db.select(qry)
    return jsonify(res)
#
@app.route('/internal_mark',methods=['post'])
def internal_mark():
    db=Db()
    qry = "select college_course.*,course.course,college_staff.college_lid from course,college_course,college_staff where  college_staff.login_id='"+str(session['lid'])+"' and college_staff.college_lid=college_course.college_id and course.id=college_course.course_id"
    res = db.select(qry)
    qry1 = "select * from subject"
    res1 = db.select(qry1)
    qry2 = "select * from batch "
    res2 = db.select(qry2)
    qry4 = "select college.*,college_staff.college_lid from college,college_staff where college_staff.login_id='" + str(session['lid']) + "' and college.login_id=college_staff.college_lid "
    res4 = db.selectOne(qry4)

    btn=request.form['button']
    if btn=="ADD":
        course = request.form['select3']
        batch = request.form['select2']
        print(batch)
        subject = request.form['select5']
        session['crs']=course
        session['btch']=batch
        session['sub']=subject
        qry3="select *,student.id as sid  from student,college_course,course where course.id=college_course.course_id and college_course.id=student.course and student.course='"+course+"' and student.batch_id='"+batch+"'"
        res3 = db.select(qry3)
        print(qry3)
        return render_template('staff/add_internal_mark.html', data=res3, course=res, sub=res1, batch=res2, subid=subject,clg=res4)

    else:

        sid = request.form.getlist('sid')
        print(sid)
        subid = str(session['sub'])
        mark = request.form.getlist('textfield')
        print(len(sid))
        for i in range(0,len(sid)):
            qry5 = "select * from internal_mark where student_id='" + sid[i] + "' and subject_id='" + subid+ "' "
            print(sid[i]+" "+mark[i])
            res5 = db.selectOne(qry5)
            if(res5 is None):
                qry4="insert into internal_mark(student_id,subject_id,mark,date)values('"+sid[i]+"','"+subid+"','"+mark[i]+"',curdate())"
                db.insert(qry4)
            else:
                if mark[i]=="":
                    continue
                else:
                    qry4="update internal_mark set mark='"+mark[i]+"' where id='"+str(res5['id'])+"'"
                    db.update(qry4)
        return'''<script>alert("sucessfully")
        window.location='/st_add_internal_mark'</script>'''


@app.route('/st_view_internal_mark')
def st_view_internal_mark():
    db = Db()
    # qry="select * from college"
    # res=db.select(qry)
    qry1 = "select college_course.*,course.course from college_course,course,college_staff where college_course.course_id=course.id and college_course.college_id=college_staff.college_lid and college_staff.login_id='" + str(session['lid']) + "'"
    print(qry1)
    res1 = db.select(qry1)
    qry2 = "select * from batch"
    res2 = db.select(qry2)
    return render_template("staff/st_view_internal.html", course=res1, batch=res2)

# @app.route('/clg_view_internal_mark1',methods=['post'])
# def clg_view_internal_mark1():
#     db=Db()
#     clg=request.form['cid']
#     qry="select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+clg+"'"
#     print(qry)
#     res=db.select(qry)
#     return jsonify(res)

@app.route('/st_view_internal_mark2', methods=['post'])
def st_view_internal_mark2():
    db = Db()
    course = request.form['cid']
    # qry = "select batch.*,college_course.course_id,course.id as cid from batch,college_course,course where college_course.course_id=course.id and college_course.id='" +course+ "'"
    qry = "select  distinct batch.* from batch,college_course,course where college_course.course_id=course.id and batch.course_id='" + course + "' and course.id=batch.course_id"
    print(qry)

    res = db.select(qry)
    return jsonify(res)

@app.route('/st_vview_internal_mark', methods=['post'])
def st_vview_internal_mark():
    db = Db()
    # qry3 = "select * from college"
    # res3 = db.select(qry3)
    # qry4 = "select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='" + str(session['lid']) + "'"
    qry4 = "select college_course.*,course.course from college_course,course,college_staff where college_course.course_id=course.id and college_course.college_id=college_staff.college_lid and college_staff.login_id='" + str(session['lid']) + "'"

    res4 = db.select(qry4)
    qry2 = "select * from batch"
    res2 = db.select(qry2)
    course = request.form['select']
    # clg=request.form['select2']
    batch = request.form['select4']
    sem = request.form['select3']
    # qry = "select DISTINCT student.id,student.name,student.regno from student,college_course,course,subject where college_course.id='" + course + "' and college_course.course_id=course.id and subject.semester='" + sem + "' and subject.course_id=course.id and student.batch_id='" + batch + "'and  student.college_lid='" +str(session['lid']) + "' and student.course=college_course.id "
    qry = "select distinct student.id,student.name,student.regno from student,college_course,course,subject,college_staff where college_course.course_id='" + course + "' and student.course=college_course.id and college_course.course_id=course.id and subject.semester='" + sem + "' and subject.course_id=course.id and student.batch_id='" + batch + "'and  student.college_lid=college_staff.college_lid and college_staff.login_id='" + str(session['lid']) + "' "
    print(qry)
    res = db.select(qry)
    # subject1 = "select distinct subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.course_id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
    subject1 = "select * from subject where course_id='" + course + "' and semester='" + sem + "'"
    sub1 = db.select(subject1)
    print("sub", sub1)
    print(res)

    # head=[0,0]
    # marks = []

    allstds = []
    for i in res:

        std = [i['name'], i['regno']]
        stid = i['id']
        # subject = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
        subject = "select * from subject where course_id='" + course + "' and semester='" + sem + "'"
        sub = db.select(subject)
        for j in sub:
            qry1 = "select mark from internal_mark where student_id='" + str(stid) + "' and  subject_id='" + str(j['id']) + "'"
            # print(qry1)
            mark = db.selectOne(qry1)
            if mark is not None:
                std.append(mark['mark'])
            else:
                std.append('not available')
        allstds.append(std)

        print(allstds)

    return render_template("staff/st_view_internal.html", sub1=sub1, allstds=allstds, sln=len(sub1), course=res4,
                           batch=res2)


#.......staff....end...................................................................................................

#........subadmin......................................................................................................

@app.route('/sub_homepage')
def sub_homepage():
   return render_template("subadmin/subadmin homepage.html")

@app.route('/sub_view_profile')
def sub_view_profile():
    db = Db()
    qry = " select * from university_staff where login_id='" + str(session['lid']) + "'"
    res = db.selectOne(qry)
    return render_template('subadmin/view_profile.html',data=res)


@app.route('/sub_view_college')
def sub_view_college():
    db=Db()
    qry="select * from college "
    res=db.select(qry)
    return render_template('subadmin/view_college.html',data=res)

@app.route('/sub_view_college_post',methods=['post'])
def sub_view_college_post():
    db=Db()
    serch=request.form['textfield']
    qry = "select * from college where college like '%"+serch+"%' or district like '%"+serch+"%'"
    res = db.select(qry)
    return render_template('subadmin/view_college.html', data=res)

@app.route('/sub_view_collegecourse/<id>')
def sub_view_collegecourse(id):
    db=Db()
    qry="select course.course,department.department from course INNER join college_course on college_course.course_id=course.id inner join department on department.id=course.department_id where college_course.college_id='"+id+"'"
    res=db.select(qry)
    print(qry)
    return render_template('subadmin/view_course.html',data=res)

@app.route('/sub_view_notification')
def sub_view_notification():
    db=Db()
    qry="select * from notification"
    res=db.select(qry)
    return render_template('view_notificationnn.html',data=res)

@app.route('/sub_sent_complient')
def sub_sent_complient ():
    return render_template('subadmin/sent_complie.html')

@app.route('/sub_sent_complient_post',methods=['post'])
def sub_sent_complient_post ():
    db=Db()
    comp=request.form['textarea']
    qry="insert into complient(comp_date,complient,status,login_id,replay,rep_date)values(curdate(),'"+comp+"','pending','"+str(session['lid'])+"','pending','pending') "
    db.insert(qry)
    return'''<script>alert("sent complient sucessfully")
    window.location='/sub_sent_complient'</script>'''

@app.route('/sub_view_complient')
def sub_view_complient ():
    db=Db()
    qry="select complient.* from complient inner join university_staff on complient.login_id=university_staff.login_id where complient.login_id='"+str(session['lid'])+"'"
    res=db.select(qry)
    return render_template('subadmin/view_complien.html',data=res)

@app.route('/sub_view_replay/<id>')
def sub_view_replay(id):
    db=Db()
    qry="select complient,status,replay,rep_date from complient where id='"+id+"' "
    res=db.selectOne(qry)
    return render_template('subadmin/view_rep.html',data=res)

@app.route('/sub_delete_complient/<id>')
def sub_delete_complient(id):
    db=Db()
    qry="delete from complient where id='"+id+"' "
    res=db.delete(qry)
    return'''<script>alert("delete sucessfully")
    window.location='/sub_view_complient'</script>'''


@app.route('/sub_view_student_details')
def sub_view_student_details():
    db=Db()
    qry="select college_course.*,course.course from college_course inner join course on college_course.course_id=course.id"
    res=db.select(qry)
    qry1="select * from batch "
    res1=db.select(qry1)
    qry3="select * from college"
    res3=db.select(qry3)
    qry2="select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id "
    res2=db.select(qry2)
    return render_template('subadmin/view_student_details.html',course=res,batch=res1,std=res2,clg=res3)


@app.route('/sub_view_student_post',methods=['post'])
def sub_view_student_post():
    db=Db()
    college=request.form['select']
    course=request.form['select3']
    batch=request.form['select2']
    if college=="select" and batch=="select" and course=="select":
        qry2="select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id "
    elif college!="select" and batch=="select" and course=="select":
        qry2="select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where college.login_id='"+college+"'"
    elif batch!="select" and college=="select" and course=="select":
        qry2="select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.batch_id='"+batch+"'  "
    elif course!="select" and batch=="select" and college=="select":
        qry2="select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.course='"+course+"'"
    elif college!="select" and course!="select" and batch=="select":
        qry2="select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where college.login_id='"+college+"' and student.course='"+course+"'"
    elif college!="select" and batch!="select" and course=="select":
        qry2="select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id where college.login_id='"+college+"' and student.batch_id='"+batch+"' "
    elif batch!="select" and course!="select" and college=="select":
        qry2="select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id  where student.batch_id='"+batch+"' and student.course='"+course+"'"
    else:
        qry2="select student.*,college.college,course.course,batch.from_year,batch.to_year from student inner join college on student.college_lid=college.login_id inner join college_course on student.course=college_course.id inner join course on college_course.course_id=course.id inner join batch on student.batch_id=batch.id where student.batch_id='"+batch+"'  and student.course='"+course+"' and college.login_id='"+college+"'"

    res2=db.select(qry2)
    qry = "select college_course.*,course.course from college_course inner join course on college_course.course_id=course.id"
    res = db.select(qry)
    qry1 = "select * from batch "
    res1 = db.select(qry1)
    qry3 = "select * from college"
    res3 = db.select(qry3)
    return render_template('subadmin/view_student_details.html',course=res,batch=res1,std=res2,clg=res3)



@app.route('/sub_add_external_mark')
def sub_add_external_mark():
    db=Db()
    qry="select * from course"
    res=db.select(qry)
    qry1="select * from subject"
    res1=db.select(qry1)
    qry2="select * from batch "
    res2=db.select(qry2)
    return render_template('subadmin/add_external_mark.html',course=res,sub=res1,batch=res2)

# @app.route('/add_external_mark_post',methods=['post'])
# def add_external_mark_post():
#     db=Db()
#
#     qry = "select * from course"
#     res = db.select(qry)
#     qry1 = "select * from subject"
#     res1 = db.select(qry1)
#     qry2 = "select * from batch "
#     res2 = db.select(qry2)
#     return render_template('subadmin/add_external_mark.html',course=res,sub=res1,batch=res2)

@app.route('/external_mark_post',methods=['post'])
def external_mark_post():
    db=Db()
    course=request.form['cid']
    sem=request.form['sem']
    qry="select * from subject where semester='"+sem+"' and course_id='"+course+"'"
    res=db.select(qry)
    return jsonify(res)

@app.route('/external_mark_post1', methods=['post'])
def external_mark_post1():
    db = Db()
    course = request.form['cid']
    qry = "select * from batch where course_id='" + course + "'"
    res = db.select(qry)
    return jsonify(res)


@app.route('/external_mark',methods=['post'])
def external_mark():
    db=Db()
    qry = "select * from course"
    res = db.select(qry)
    qry1 = "select * from subject"
    res1 = db.select(qry1)
    qry2 = "select * from batch "
    res2 = db.select(qry2)
    course=request.form['select3']
    batch=request.form['select6']
    subject=request.form['select5']
    btn=request.form['button']
    if btn=="ADD":
        qry3="select student.* from student,college_course,course where course.id=college_course.course_id and college_course.id=student.course and course.id='"+course+"' and student.batch_id='"+batch+"'"
        res3 = db.select(qry3)
        return render_template('subadmin/add_external_mark.html', data=res3, course=res, sub=res1, batch=res2, sidd=subject)

    else:

        sid = request.form.getlist('lid')
        subid = request.form['sidd']
        mark = request.form.getlist('textfield')
        for i in range(0, len(sid)):
            qry5 = "select * from external_mark where student_id='" + sid[i] + "' and subject_id='" + subid + "' "
            print(qry5)
            res5 = db.selectOne(qry5)
            if (res5 is None):
                qry4="insert into external_mark(student_id,subject_id,mark1,date)values('"+sid[i]+"','"+subid+"','"+mark[i]+"',curdate())"
                db.insert(qry4)
            else:
                if mark[i] == "":
                    continue
                else:
                    qry4 = "update external_mark set mark1='" + mark[i] + "' where id='" + str(res5['id']) + "'"
                    db.update(qry4)


        return'''<script>alert("sucessfully")
        window.location='/sub_add_external_mark'</script>'''




@app.route('/sub_view_external_mark')
def sub_view_external_mark():
    db=Db()
    qry="select * from college"
    res=db.select(qry)
    qry1="select college_course.*,course.course from college_course,course where college_course.course_id=course.id"
    res1=db.select(qry1)
    qry2="select * from batch"
    res2=db.select(qry2)
    return render_template("subadmin/sub_view_external.html",clg=res,course=res1,batch=res2,ln=0)

@app.route('/sub_view_external_mark1',methods=['post'])
def sub_view_external_mark1():
    db=Db()
    clg=request.form['cid']
    qry="select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+clg+"'"
    print(qry)
    res=db.select(qry)
    return jsonify(res)

@app.route('/sub_view_external_mark2',methods=['post'])
def sub_view_external_mark2():
    db=Db()
    course=request.form['cid']
    qry = "select batch.*,college_course.course_id,course.id as cid from batch,college_course,course where college_course.course_id=course.id and college_course.id='" +course+ "'"
    print(qry)
    res = db.select(qry)
    return jsonify(res)

@app.route('/sub_vview_external',methods=['post'])
def sub_vview_external():
    db=Db()
    qry3 = "select * from college"
    res3 = db.select(qry3)
    qry4 = "select college_course.*,course.course from college_course,course where college_course.course_id=course.id"
    res4 = db.select(qry4)
    qry2 = "select * from batch"
    res2 = db.select(qry2)
    course=request.form['select']
    clg=request.form['select2']
    batch=request.form['select4']
    sem=request.form['select3']
    qry = "select DISTINCT student.id,student.name,student.regno from student,college_course,course,subject where college_course.id='" + course + "' and college_course.course_id=course.id and subject.semester='" + sem + "' and subject.course_id=course.id and student.batch_id='" + batch + "'and  student.college_lid='" + clg + "' and student.course=college_course.id "


    res = db.select(qry)

    subject1 = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
    sub1 = db.select(subject1)

    print(res)

    # head=[0,0]
    # marks = []

    allstds=[]
    for i in res:

        std=[i['name'],i['regno']]
        stid=i['id']
        subject = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
        sub = db.select(subject)
        for j in sub:
            qry1="select mark1 from external_mark where student_id='"+str(stid)+"' and  subject_id='"+str(j['id'])+"'"
            # print(qry1)
            mark=db.selectOne(qry1)
            if mark is not None:
                std.append(mark['mark1'])
            else:
                std.append('not available')
        allstds.append(std)


        print(allstds)




    return render_template("subadmin/sub_view_external.html",sub1=sub1,allstds=allstds,sln=len(sub1),clg=res3, course=res4, batch=res2)






@app.route('/sub_view_internal_mark')
def sub_view_internal_mark():
    db=Db()
    qry="select * from college"
    res=db.select(qry)
    qry1="select college_course.*,course.course from college_course,course where college_course.course_id=course.id"
    res1=db.select(qry1)
    qry2="select * from batch"
    res2=db.select(qry2)
    return render_template("subadmin/sub_view_internal.html",clg=res,course=res1,batch=res2)

@app.route('/sub_view_internal_mark1',methods=['post'])
def sub_view_internal_mark1():
    db=Db()
    clg=request.form['cid']
    qry="select college_course.*,course.course from college_course,course where college_course.course_id=course.id and college_course.college_id='"+clg+"'"
    print(qry)
    res=db.select(qry)
    return jsonify(res)

@app.route('/sub_view_internal_mark2',methods=['post'])
def sub_view_internal_mark2():
    db=Db()
    course=request.form['cid']
    qry = "select batch.*,college_course.course_id,course.id as cid from batch,college_course,course where college_course.course_id=course.id and college_course.id='" +course+ "'"
    print(qry)
    res = db.select(qry)
    return jsonify(res)



@app.route('/sub_vview_internal_mark')
def sub_vview_internal_mark():
    db = Db()
    qry3 = "select * from college"
    res3 = db.select(qry3)
    qry4 = "select college_course.*,course.course from college_course,course where college_course.course_id=course.id"
    res4 = db.select(qry4)
    qry2 = "select * from batch"
    res2 = db.select(qry2)
    course = request.form['select']
    clg = request.form['select2']
    batch = request.form['select4']
    sem = request.form['select3']
    qry = "select DISTINCT student.id,student.name,student.regno from student,college_course,course,subject where college_course.id='" + course + "' and college_course.course_id=course.id and subject.semester='" + sem + "' and subject.course_id=course.id and student.batch_id='" + batch + "'and  student.college_lid='" + clg + "' and student.course=college_course.id "

    res = db.select(qry)

    subject1 = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
    sub1 = db.select(subject1)

    print(res)

    # head=[0,0]
    # marks = []

    allstds = []
    for i in res:

        std = [i['name'], i['regno']]
        stid = i['id']
        subject = "select subject.*,college_course.id as ccid,course.id as cid from subject,college_course,course where college_course.id='" + course + "' and college_course.course_id=course.id and semester='" + sem + "'"
        sub = db.select(subject)
        for j in sub:
            qry1 = "select mark from internal_mark where student_id='" + str(stid) + "' and  subject_id='" + str(j['id']) + "'"
            # print(qry1)
            mark = db.selectOne(qry1)
            if mark is not None:
                std.append(mark['mark1'])
            else:
                std.append('not available')
        allstds.append(std)

        print(allstds)

    return render_template("subadmin/sub_view_internal.html", sub1=sub1, allstds=allstds, sln=len(sub1), clg=res3, course=res4,
                           batch=res2)




@app.route('/sub_view_mark/<id>')
def sub_view_mark(id):
    db=Db()
    session['id']=id
    return render_template('subadmin/sub_marks.html')


@app.route('/sub_view_markk',methods=['post'])
def sub_view_markk():
    db=Db()
    mark=[]
    mark1=[]
    sem=request.form['select3']
    qry2="select student.course,subject.subject,subject.id as sub_id,course.course from student,subject,college_course,course where student.id='"+str(session['id'])+"' and student.course=college_course.id and course.id=college_course.course_id and subject.semester='"+sem+"' and course.id=subject.course_id"
    sub=db.select(qry2)
    print(sub)
    print("mmm",mark)
    # qry1="select subject.id as subid,subject.subject,subject.semester,external_mark.mark1,internal_mark.mark from subject left join external_mark on external_mark.student_id='"+str(session['id'])+"' left join internal_mark on internal_mark.student_id='"+str(session['id'])+"' where subject.semester='"+sem+"' and subject.id=external_mark.subject_id   "
    for i in sub:
        subid=i['sub_id']
        # qry1="select external_mark.mark1,internal_mark.mark from external_mark,internal_mark where external_mark.student_id='"+str(session['id'])+"' and  external_mark.subject_id='"+str(subid)+"' and  internal_mark.subject_id='"+str(subid)+"'"
        qry1="select mark1,subject_id from external_mark where student_id='"+str(session['id'])+"'  and subject_id='"+str(subid)+"' "

        qry2na="select mark, subject_id from internal_mark where student_id='"+str(session['id'])+"'  and subject_id='"+str(subid)+"' "
        print(qry1)
        res1=db.selectOne(qry1)
        res2=db.selectOne(qry2)
        if res1 is not None:
            mark.append(str(res1['mark1']))
        else:
            mark.append('nil')

        if res2 is not None:
            mark1.append(str(res2['mark']))
        else:
            mark1.append('nil')

    print("after ...",mark)
    print(mark1)

    return render_template('subadmin/sub_marks.html',sub=sub,mark=mark,len1=len(sub),mark1=mark1)



# ........subadmin......end.........................................................................................


####################    ANDROID    #############################################################################


#...........verifier..............................................###############################..................


@app.route('/v_login',methods=['post'])
def v_login():
    db=Db()
    uname=request.form['user_name']
    pword=request.form['password']

    qry = "select * from login where user_name='" + uname + "' and password='" + pword + "' "
    res = db.selectOne(qry)
    if(res is not None ):
        if res['type'] == "verifier":

            return jsonify(status="ok",lid=res['id'])
        else:
            return jsonify(status="please create account")
    else:
        return jsonify(status="please create account")


@app.route('/v_create_account', methods=['post'])
def v_create_account():
    db = Db()
    # uname=request.form['edittext1']
    pword=request.form['password']
    name=request.form['name']
    dob=request.form['dob']
    house_name=request.form['house_name']
    post=request.form['post']
    place=request.form['place']
    phone_no=request.form['phone_no']
    email=request.form['email']
    gender=request.form['gender']
    district=request.form['dist']
    qry1= "insert into login(user_name,password,type)values('" + email + "','" + pword+ "','verifier')"
    res=db.insert(qry1)
    qry="insert into verifier(name,house_name,post,place,gender,mail_id,phone_no,district,dob,verifier_lid) values('"+name+"','"+house_name+"','"+post+"','"+place+"','"+gender+"','"+email+"','"+phone_no+"','"+district+"','"+dob+"','"+str(res)+"')"
    db.insert(qry)
    return jsonify(status="ok")

# @app.route('/v_forgot_password', methods=['post'])
# def v_forgot_password():
#     db = Db()
#     email = request.form['email']
#
#     qry = "select * from login where user_name='" + email + "'"
#     res = db.selectOne(qry)
#     if (res is not None):
#         passwd = res['password']
#         msg = Message(subject="Your password",
#                       sender=app.config.get("uniqueid005@gmail.com"),
#                       recipients=[email],  # replace with your email for testing
#                       body="Password:" + passwd)
#         mail.send(msg)
#         return jsonify(status="ok",email=res['user_name'])
#
#     else:
#         return  jsonify(status="Enter valid Email")

@app.route('/v_change_password', methods=['post'])
def V_change_password():
    db = Db()
    cpass = request.form['cpass']
    npass = request.form['npass']
    lid=request.form['lid']

    res=db.selectOne("select * from login where id='"+lid+"' and password='"+cpass+"'")
    if res is not None:
        qry = "update login set password='" + npass + "' where id='" + lid + "' "
        res = db.update(qry)
        return jsonify(status="ok")
    else:
        return jsonify(status="invalid")

@app.route('/verification', methods=['post'])
def verification():
    db = Db()
    key1 = request.form['key1']
    capture_image=request.form['capture_image']
    image_name=request.form['image_name']
    print("pp",capture_image)
    print("name",image_name)

    print("kre5tr",key1)
    key="123456789"
    print("type",type(key1))
    aes = AESCipher(key1)

    decryptdata=aes.decrypt(bytes(key1,'utf-8'))
    print("dc",decryptdata)


    timestr = time.strftime("%Y%m%d-%H%M%S")
    print(timestr)


    a = base64.b64decode(capture_image)
    fh = open("C:\\Users\\hp\\PycharmProjects\\uniqid\\static\\reg_photo\\" + timestr + ".jpg", "wb")
    path = "/static/reg_photo/" + timestr + ".jpg"
    print("na...",path)
    fh.write(a)
    fh.close()

    #------------------generate face_id

    filepath = "C:\\Users\\hp\\PycharmProjects\\uniqid\\static\\reg_photo\\" + timestr + ".jpg"

    new_face_id = faceid(filepath)

    print("==faceid====",new_face_id)

    #-------------------compare faces


    import cognitive_face as CF
    print("hhhhh")
    key = "98dcf2ccd2224618adcea6f5b4eee35c"  # Replace with a valid Subscription Key here.
    CF.Key.set(key)

    base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL

    CF.BaseUrl.set(base_url)

    similarity = CF.face.verify(new_face_id, decryptdata)
    print("-----similarity-----",similarity)

    if similarity['isIdentical'] == True:

        print("true=====")
        return jsonify(status="ok")

    else:
        print("false=====")
        return jsonify(status="no")

@app.route('/report_message',methods=['post'])
def report_message():
    print()
    db=Db()
    message=request.form['message']
    print(message)
    vlid=request.form['lid']
    qry="insert into certificate_fraud(date,report_msg,verifier_lid) values(curdate(),'"+message+"','"+vlid+"')"
    res=db.insert(qry)
    print(res)
    return jsonify(status="ok")






# ......verifier end................................................................................................#

# @app.route('/aaa')
# def aaa():
#     import cognitive_face as CF
#
#     key = '2ffd9489920b49b6890b9db39beda43a'  # Replace with a valid Subscription Key here.
#     CF.Key.set(key)
#
#     base_url = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0/'  # Replace with your regional Base URL
#
#     CF.BaseUrl.set(base_url)
#
#     similarity = CF.face.verify(new_face_id, decryptdata)
#     print("-----similarity-----",similarity)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
# ,host='0.0.0.0'