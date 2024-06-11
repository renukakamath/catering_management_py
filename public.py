from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
        username=request.form['name']
        password=request.form['password']

        print(username,password)
        q="select * from login where username='%s' and password='%s' "%(username,password)
        res=select(q)
        print("test1")
        if res:
            session['Username']=res[0]['Username']
            Username=session['Username']

            print("f")
            if res[0]['User_type']=="admin":
                return redirect(url_for('admin.adminhome'))
            elif res[0]['User_type']=="staff":
                return redirect(url_for('staff.staffhome'))
            elif res[0]['User_type']=="customer":
                print("t")
                q="select * from tbl_customer where Email='%s'"%(Username)
                res=select(q)
                if res:
                    session['cus_id']=res[0]['cus_id']
                    cus_id=session['cus_id']
                return redirect(url_for('customer.customerhome'))

    return render_template("login.html")
   

@public.route('/registration',methods=['get','post'])
def registration():
    if 'submit' in request.form:
        email=request.form['Email']
        fname=request.form['Firstname']
        lname=request.form['Lastname']
        phone=request.form['Phone_number']  
        housename=request.form['House_name']
        state=request.form['State']
        district=request.form['District']
        pincode=request.form['Pincode']
        password=request.form['Password']
      
   

        
        q="insert into login values('%s','%s','customer')"%(email,password)
        insert(q)

        q="insert into tbl_customer values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s',1)"%(email,fname,lname,phone,housename,state,district,pincode,password)
        insert(q)
        return redirect(url_for('public.login'))

    return render_template("reg.html")