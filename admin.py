from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
    return render_template('adminhome.html')



@admin.route('/staffadd',methods=['POST','GET'])
def staffadd():
    if 'submit' in request.form:
        username=request.form['Email']
        password=request.form['Password']
        fname=request.form['Firstname']
        lname=request.form['Lastname']
        phone=request.form['Phone_number']
        housename=request.form['House_name']
        state=request.form['State']
        district=request.form['District']
        pincode=request.form['Pincode']
        date=request.form['Date']
        q="insert into login values('%s','%s','staff')"%(username,password)
        insert(q)
        q="insert into tbl_staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s',1)"%(username,fname,lname,phone,housename,state,district,pincode,date)
        insert(q)
       

   
        return redirect(url_for("admin.staffadd"))

        

        
    data={}
    q="select * from tbl_staff"
    res=select(q)
    data['view']=res

    
        
    if 'action' in request.args:
        action=request.args['action']
        sid=request.args['sid']
    else:
        action=None

    if action=="inactive":
          q="update tbl_staff set Status='0' where staff_id='%s'"%(sid)
          update(q)
          return redirect(url_for("admin.staffadd"))
    if action=="active":
          s="update tbl_staff set Status='1' where staff_id='%s'"%(sid)
          update(s)
          return redirect(url_for("admin.staffadd"))

    if action == "update":
        q="select * from tbl_staff where staff_id='%s'"%(sid)
        val=select(q)
        data['staff']=val

        if 'update' in request.form:
            # email=request.form['Email']
            # password=request.form['Password']
            fname=request.form['Firstname']
            lname=request.form['Lastname']
            phone=request.form['Phone_number']
            housename=request.form['House_name']
            state=request.form['State']
            district=request.form['District']
            pincode=request.form['Pincode']
            date=request.form['Date']

            q="update tbl_staff set Firstname='%s', Lastname='%s',Phone_number='%s',House_name='%s',State='%s',District='%s',Pincode='%s',Date='%s' where staff_id='%s' "%(fname,lname,phone,housename,state,district,pincode,date,sid)
            update(q)
            return redirect(url_for("admin.staffadd"))
       

    return render_template('staffadd.html',data=data)




@admin.route('/eventadd',methods=['POST','GET'])
def eventadd():
    
    if 'submit' in request.form:
        name=request.form['Name']
        description=request.form['Description']
        q="insert into tbl_event values(null,'%s','%s')"%(name,description)
        insert(q)
        return redirect(url_for("admin.eventadd"))

    
    data={}
    q="select * from tbl_event"
    res=select(q)
    data ['view']=res
    if 'action' in request.args:
        action=request.args['action']
        eid=request.args['eid']
    else:
        action=None

    if action == "update":
        q="select * from tbl_event where event_id='%s'"%(eid)
        val=select(q)
        data['event']=val

        if 'update' in request.form:
           
            name=request.form['Name']
            description=request.form['Description']
           

            q="update tbl_event set Name='%s', Description='%s' where event_id='%s'"%(name,description,eid)
            update(q)
            return redirect(url_for("admin.eventadd"))
       




    return render_template('eventadd.html',data=data)
@admin.route('/categoryadd',methods=['POST','GET'])
def categoryadd():

    if 'submit' in request.form:
        name=request.form['Name']
        description=request.form['Description']
        q="insert into tbl_category values(null,'%s','%s')"%(name,description)
        insert(q)
        return redirect(url_for("admin.categoryadd"))

    data={}
    q="select * from tbl_category"
    res=select(q)
    data ['view']=res
    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

    if action == "update":
        q="select * from tbl_category where cat_id='%s'"%(cid)
        val=select(q)
        data['category']=val

        if 'update' in request.form:
    
            name=request.form['Name']
            description=request.form['Description']
           

            q="update tbl_category set Name='%s', Description='%s' where cat_id='%s'"%(name,description,cid)
            update(q)
            return redirect(url_for("admin.categoryadd"))
        
    return render_template('categoryadd.html',data=data)
    
    


@admin.route("/adcus")
def adcus():
    data={}
    q="select * from tbl_customer"
    res=select(q)
    data["view"]=res
    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

   
    
    if action=="inactive":
          q="update tbl_customer set Status='0' where cus_id='%s'"%(cid)
          update(q)
          return redirect(url_for("admin.adcus"))
    if action=="active":
          s="update tbl_customer set Status='1' where cus_id='%s'"%(cid)
          update(s)
          return redirect(url_for("admin.adcus"))
    return render_template('adcus.html',data=data)    

@admin.route('/itemadd',methods=['get','post'])
def itemadd():
    data={}    
    q="select * from tbl_category"
    res=select(q)
    data['category']=res

    
    
    if 'submit' in request.form:
        category=request.form['category']
        itemname=request.form['Iname']
        des=request.form['Description']
        img=request.files['Image']
        path='static/uploads/'+str(uuid.uuid4())+img.filename 
        img.save(path)
        print(path)
        price=request.form['Price']
        q="insert into tbl_item values(null,'%s','%s','%s','%s','%s','1')"%(category,itemname,des,path,price)
        insert(q)   
        return redirect(url_for("admin.itemadd"))
    q="select * from tbl_item inner join tbl_category using(cat_id)"
    res=select(q)
    data['view']=res

    if "action" in request.args:
       action=request.args['action']
       sid=request.args['sid']
    else:
     action=None

    if action=="inactive":
        q="update tbl_item set Status='0' where item_id='%s'"%(sid)
        print(q)
        update(q)
        return redirect(url_for("admin.itemadd"))
    if action=="active":
        s="update tbl_item set Status='1' where item_id='%s'"%(sid)
        update(s)
        return redirect(url_for("admin.itemadd"))
        
    if action=='update':
        q="select * from tbl_item inner join category using(cat_id) where item_id='%s'"%(sid)
        data['iup']=res

    if 'edit' in request.form:
        category=request.form['category']
        itemname=request.form['Iname']
        des=request.form['Description']
        img=request.files['Image']
       
        price=request.form['Price']
        print(img)
        if img==" ":
            q="update tbl_item set cat_id='%s',Iname='%s',Description='%s',Price='%s' where item_id='%s'"%(category,itemname,des,price,sid)
            update(q)
        else:
            path='static/uploads/'+str(uuid.uuid4())+img.filename 
            img.save(path)
            print(path)
            q="update tbl_item set cat_id='%s',Iname='%s',Description='%s',Price='%s',Image='%s' where item_id='%s'"%(category,itemname,des,price,path,sid)
            update(q)
        return redirect (url_for('admin.itemadd'))
    
    return render_template('itemadd.html',data=data)



@admin.route('/viewbookings',methods=['get','post'])
def viewbookings():
    data={}
    q="SELECT * FROM `tbl_cart_master` INNER JOIN `tbl_cart_child` USING (`cartM_id`) INNER JOIN tbl_customer USING (cus_id) where tbl_cart_master.status<>'pending'"
    data['view']=select(q)
    return render_template('admin_view_booking.html',data=data)



@admin.route('/viewsales',methods=['get','post'])
def viewsales():
    data={}
    q="SELECT * FROM `tbl_cart_master` INNER JOIN `tbl_cart_child` USING (`cartM_id`) INNER JOIN tbl_customer USING (cus_id) where tbl_cart_master.status<>'pending'"
    data['view']=select(q)
    return render_template('admin_view_sales.html',data=data)