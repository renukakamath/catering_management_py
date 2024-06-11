from flask import *
from database import *

customer=Blueprint('customer',__name__)

@customer.route('/customerhome')
def customerhome():
      data={}

      return render_template('customer_home.html',data=data)



@customer.route('/viewproducts',methods=['get','post'])
def viewproducts():
      data={}
     
      q="select * from tbl_item inner join tbl_category using(cat_id) "
      res=select(q)
      data['res']=res
      
      return render_template('productview.html',data=data)




@customer.route('/cart',methods=['get','post'])
def cart():
      data={}
      id=request.args['id']
      q="select * from tbl_item where item_id='%s'"%(id)
      res=select(q)
      data['price']=res[0]['Price']
      data['name']=res[0]['Iname']


      q="select * from tbl_event"
      res=select(q)
      data['evet']=res
      
      if 'add' in request.form:
            item=request.form['item']
            price=request.form['price']
            qty=request.form['qty']
            total=request.form['total_amt']
            event=request.form['event']
            cus_id=session['cus_id']
            q="select * from tbl_cart_master where cus_id='%s' and status='pending'"%(cus_id)
            res=select(q)
            if res:
                  omid=res[0]['cartM_id']
            else:
                  q="insert into tbl_cart_master values(null,'%s','%s','0','pending')"%(cus_id,event)
                  omid=insert(q)
            q="select * from tbl_cart_child where item_id='%s' and cartM_id='%s'"%(id,omid)
            res=select(q)
            if res:
                  odid=res[0]['cartC_id']
                  q="update tbl_cart_child set qty=qty+'%s' , price=price+'%s' where cartC_id='%s'"%(qty,total,odid)
                  update(q)
            else:
                  q="insert into tbl_cart_child values(null,'%s','%s','%s','%s',curdate())"%(omid,id,qty,total)
                  insert(q)
            q="update tbl_cart_master set total_price=total_price+'%s' where cartM_id='%s'"%(total,omid)
            update(q)

            flash('successfully')
            return redirect(url_for('customer.customerviewcart'))
            
            
      return render_template('cart.html',data=data)


@customer.route('/customerviewcart',methods=['get','post'])
def customerviewcart():
      data={}
      cus_id=session['cus_id']



      q="SELECT * FROM `tbl_cart_master` INNER JOIN `tbl_cart_child` USING (`cartM_id`) INNER JOIN `tbl_item` USING (`item_id`) INNER JOIN `tbl_event` USING (`event_id`) INNER JOIN `tbl_customer` USING (`cus_id`) where tbl_cart_master.status='pending' and tbl_cart_master.cus_id='%s'"%(cus_id)
      res=select(q)
      data['len']=len(res)
      data['view']=res

      for i in range(1,len(res)+1):
            if 'btn'+str(i) in request.form:
                  oid=request.form['oid'+str(i)]
                  pid=request.form['pid'+str(i)]

                  q="update tbl_cart_master set total_price=total_price-(select price from tbl_cart_child where item_id='%s' and cartM_id='%s') where cartM_id='%s'"%(pid,oid,oid)
                  print(q)
                  update(q)
                  q="delete from tbl_cart_child where cartM_id='%s' and item_id='%s'"%(oid,pid)
                  delete(q)
                  q=" select * from tbl_cart_master where cartM_id='%s' and total_price='0'"%(oid)
                  ves=select(q)
                  if ves:
                        q="delete from tbl_cart_master where cartM_id='%s'"%(oid)
                        delete(q)


                  flash('successfully')
                  
                  return redirect(url_for("customer.customerviewcart"))

      return render_template('customerviewcart.html',data=data)


@customer.route('/customer_makepayment',methods=['post','get'])
def customer_makepayment():
      data={}

      omid=request.args['omid']
      data['omid']=omid
      amt=request.args['ttamount']
      data['ttamount']=amt
      

      
      cid=session['cus_id']
      q="select * from tbl_card where cus_id='%s'"%(cid)
      res=select(q)
      data['card']=res



      if "confirm_order" in request.form:
            
            omid=request.args['omid']
            amt=request.args['ttamount']
            cnum=request.form['cnum']
            cname=request.form['cname']
            cid=session['cus_id']
            
            d=request.form['date']


            from datetime import date,datetime

            d1=datetime.strptime(d,'%Y-%m')
            print(type(d1))


            today = datetime.today()
            print("Today's date:", type(today))

            print(d,")))))))))))")

            print(today)
            if d1 < today:


                  flash('expired')




            else:
                    q="UPDATE `tbl_cart_master` SET `status`='paid' WHERE `cartM_id`='%s'"%(omid)
                    update(q)
                    q2="INSERT INTO `tbl_payment` VALUES(NULL,'%s',CURDATE())"%(omid)
                    insert(q2);
                    q="select * from tbl_cart_child where cartM_id='%s'"%(omid)
                    select(q)
                    
                    q="SELECT * FROM `tbl_card` WHERE `card_no`='%s' AND `card_name`='%s'  and `cus_id`='%s'"%(cnum,cname,cid)
                    res=select(q)
                    if len(res) == 0:
                        q3="INSERT INTO `tbl_card` VALUES(NULL,'%s','%s','%s','%s','paid')"%(cid,cnum,cname,d)
                        insert(q3);
                        return redirect(url_for('customer.customerviewcart'))
                    
                  
            


      if "action" in request.args:
            action=request.args['action']
            choose=request.args['choose']

            if action=='choose':
                  qx="SELECT * FROM `tbl_card`  WHERE `card_id`='%s'"%(choose)
                  rx=select(qx);
                  data['chooses']=rx
      return render_template('customer_makepayment.html',data=data)



@customer.route('/customer_viewmybookings')
def customer_viewmybookings():
      data={}
      cus_id=session['cus_id']

      q="SELECT * FROM `tbl_cart_master` INNER JOIN `tbl_cart_child` USING (`cartM_id`) INNER JOIN `tbl_item` USING (`item_id`) INNER JOIN `tbl_event` USING (`event_id`) INNER JOIN `tbl_customer` USING (`cus_id`) where tbl_cart_master.status='paid' and tbl_cart_master.cus_id='%s'"%(cus_id)
      res=select(q)
      
      data['view']=res

      return render_template('customer_viewmybookings.html',data=data)