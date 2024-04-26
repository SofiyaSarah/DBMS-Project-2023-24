from flask import Flask, render_template, request, redirect, url_for, session,make_response
from flask_cors import CORS
from flask_mysqldb import MySQL
from pytz import timezone
from datetime import datetime
from dateutil import parser 
import pytz
import json
from json import JSONEncoder
from werkzeug.utils import secure_filename




app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'lms'
CORS(app) 
 
app.secret_key = 'your secret key'
mysql = MySQL(app)
now_utc = datetime.now(timezone('UTC'))
now_asia = now_utc.astimezone(timezone('Asia/Kolkata'))

@app.route('/sreg',methods=['GET', 'POST'])
def userreg():
    return render_template('register.html')

import hashlib
@app.route('/sregister', methods=['GET','POST'])
def register():
    name=request.form.get('name')
    uname=request.form.get('uname')
    email=request.form.get('email')
    branch=request.form.get('branch')
    pno=request.form.get('pno')
    pwd=request.form.get('pwd')
    
    
    cursor=mysql.connection.cursor()
    #pwd = hashlib.md5(pwd.encode('utf-8')).digest()
    cursor.execute(''' INSERT INTO student(name,uname,email,branch,pno,pwd) VALUES(%s,%s,%s,%s,%s,MD5(%s))''',(name,uname,email,branch,pno,pwd))
    mysql.connection.commit()
    cursor.close()
    return "success"


@app.route('/ireg',methods=['GET', 'POST'])
def usereg():
    return render_template('userreg.html')

import hashlib
@app.route('/iregister', methods=['GET','POST'])
def iiregister():
    name=request.form.get('name')
    email=request.form.get('email')
    pwd=request.form.get('pwd')
    qual=request.form.get('qual')
    pno=request.form.get('pno')
    
    
    cursor=mysql.connection.cursor()
    #pwd = hashlib.md5(pwd.encode('utf-8')).digest()
    cursor.execute(''' INSERT INTO instructor(name,email,pwd,qual,pno) VALUES(%s,%s,MD5(%s),%s,%s)''',(name,email,pwd,qual,pno))
    mysql.connection.commit()
    cursor.close()
    return "success"

@app.route('/inslogin', methods=['GET', 'POST'])

def inslogin():
    email=request.form.get('email')
    pwd=request.form.get('pwd')
    cursor=mysql.connection.cursor()
    cursor.execute(''' SELECT * FROM instructor WHERE email=%s and pwd=MD5(%s)''',(email,pwd))
    row=cursor.fetchone()
    cursor.close()
    iid=str(row[5])
    if row:
            response = make_response("successfully logged") # We can also render new page with render_template
            response.set_cookie('iid',iid)
            return response
            return ("successfully logged")
        
        
    else:
        return "Failed to login"

@app.route('/lgn', methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/idash', methods=['GET','POST'])
def idash():
    return render_template('instrdash.html')
@app.route('/ilgn', methods=['GET'])
def ilogin():
    return render_template('login2.html')


@app.route('/admin', methods =['GET', 'POST'])
def admin():
    
    username = request.form.get('uname')
    password = request.form.get('psw')
    print(username, password)
    if username == 'admin' and password == 'ppp':
        #return redirect(url_for('adminlogin', username=username))
        return ('success')
    else:
        return ('Login failed')
    
@app.route('/hpage', methods=['GET'])
def hpage():
    return render_template('hpage.html')
    
@app.route('/cinsert', methods =['GET', 'POST'])
def cinsert():
    
    cname = request.form.get('cname')
    cid = request.form.get('cid')
    credits= request.form.get('credits')
    
    #date_object = parser.parse(sdate)
    #sdate = date_object.astimezone(pytz.timezone('Asia/Kolkata')) 
    #print(date_object)
    cursor = mysql.connection.cursor()
    cursor.execute(''' INSERT INTO course(cname,cid,credits) VALUES(%s,%s,%s)''',(cname,cid,credits))
    mysql.connection.commit()
    cursor.close()
    return "Inserted successfully"

@app.route('/tinsert', methods =['GET', 'POST'])

def tinsert():
    tname=request.form.get('tname')
    tid=request.form.get('tid')
    tdes=request.form.get('tdes')

    cursor=mysql.connection.cursor()
    cursor.execute(''' INSERT INTO learning_type(t_id,t_name,tdes) VALUES(%s,%s,%s)''',(tid,tname,tdes))
    mysql.connection.commit()
    cursor.close()
    return "Inserted successfully"

@app.route('/minsert', methods =['GET', 'POST'])
def minsert():
    
    mid = request.form.get('mid')
    mname = request.form.get('mname')
    mc=request.form.get('mc')
    mcid=request.form.get('mcid')
    mtid=request.form.get('mtid')

    #ravalue=request.form.get('ravalue')
    #rstatus=request.form.get('rstatus')
    f = request.files['mfile']       
    filename = secure_filename(f.filename)
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    rimg=dt_string+"_"+filename
    f.save("static/resources/" + rimg)
    iid=request.cookies.get('iid')
    cursor = mysql.connection.cursor()
    print(iid)
    cursor.execute(''' INSERT INTO learning_module(module_name,module_content,mid,tid,cid,mfile,iid) VALUES(%s,%s,%s,%s,%s,%s,%s)''',(mname,mc,mid,mtid,mcid,rimg,iid))
    mysql.connection.commit()
    cursor.close()
    return "Inserted successfully"


@app.route('/cupdate', methods =['GET', 'POST'])
def cupdate():
    
    did=request.form.get('did')
    cname = request.form.get('cname')
    credits = request.form.get('credits')
   
    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE course SET cname=%s,credits=%s WHERE cid=%s''',(cname,credits,did))
    mysql.connection.commit()
    cursor.close()
    return "Updated successfully"

@app.route('/tupdate', methods =['GET', 'POST'])
def tupdate():
    
    tid=request.form.get('rtid')
    tname = request.form.get('tname')
    tdes = request.form.get('tdes')
    
    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE learning_type SET t_name=%s,tdes=%s WHERE t_id=%s''',(tname,tdes,tid))
    mysql.connection.commit()
    cursor.close()
    return "Updated successfully"


@app.route('/cdelete', methods =['GET', 'POST'])
def cdelete():
    
    did=request.form.get('did')
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM course WHERE cid=%s''',(did,))
    mysql.connection.commit()
    cursor.close()
    return "Deleted successfully"

@app.route('/tdelete', methods =['GET', 'POST'])
def tdelete():
    
    tid=request.form.get('rtid')
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM learning_type WHERE t_id=%s''',(tid,))
    mysql.connection.commit()
    cursor.close()
    return "Deleted successfully"

@app.route('/mdelete', methods =['GET', 'POST'])
def mdelete():
    
    rid=request.form.get('rid')
    cursor = mysql.connection.cursor()
    cursor.execute(''' DELETE FROM learning_module WHERE mid=%s''',(rid,))
    mysql.connection.commit()
    cursor.close()
    return "Deleted successfully"

@app.route('/getcoursenames', methods =['GET', 'POST'])

def getcoursenames():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM course")
    DBData = cursor.fetchall() 
    cursor.close()
    
    rtnames=''
    for result in DBData:
        print(result)
        rtnames+="<option value="+str(result[1])+">"+result[0]+"</option>"
    return rtnames    

@app.route('/gettypenames', methods =['GET', 'POST'])

def gettypenames():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM learning_type")
    DBData = cursor.fetchall() 
    cursor.close()
    
    rtnames=''
    for result in DBData:
        print(result)
        rtnames+="<option value="+str(result[0])+">"+result[1]+"</option>"
    return rtnames   
           
@app.route('/cshow', methods =['GET', 'POST'])
def cshow():
    
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT cid,cname,credits FROM course")
    row_headers=[x[0] for x in cursor.description] 
    DBData = cursor.fetchall() 
    cursor.close()
    json_data=[]
    rstr="<table border><tr>"
    for r in row_headers:
        rstr=rstr+"<th>"+r+"</th>"
    rstr=rstr+"<th>Update</th><th>Delete</th></tr>"
    cnt=0
    did=-1
    for result in DBData:
        cnt=0
        ll=['A','B','C','D','E','F','G','H','I','J','K']
        for row in result:
            if cnt==0:
                did=row
                rstr=rstr+"<td>"+str(row)+"</td>" 
            elif cnt==3:
                rstr=rstr+"<td>"+"<input type=date id=C"+str(ll[cnt])+str(did)+" value="+str(row)+"></td>"  
            else:
                rstr=rstr+"<td>"+"<input type=text id=C"+str(ll[cnt])+str(did)+" value=\""+str(row)+"\"></td>"     
            cnt+=1
            
        rstr+="<td><a ><i class=\"fa fa-edit\" aria-hidden=\"true\" onclick=update('"+str(did)+"')></i></a></td>"
        rstr+="<td><a ><i class=\"fa fa-trash\" aria-hidden=\"true\" onclick=del('"+str(did)+"')></i></a></td>"
        
        rstr=rstr+"</tr>"
    
    rstr=rstr+"</table>"
    rstr=rstr+'''
    <script type=\"text/javascript\">
    function update(did)
    {
       cname=$("#CB"+did).val();
       credits=$("#CC"+did).val();
       
       $.ajax({
        url: \"/cupdate\",
        type: \"POST\",
        data: {did:did,cname:cname,credits:credits},
        success: function(data){    
        alert(data);
        loadcourses();
        }
       });
    }
   
    function del(did)
    {
    $.ajax({
        url: \"/cdelete\",
        type: \"POST\",
        data: {did:did},
        success: function(data){
            alert(data);
            loadcourses();
        }
        });
    }
    function loadcourses(){

       $.ajax({
        url: 'http://127.0.0.1:5000/cshow',
        type: 'POST',
        success: function(data){
          $('#cshow').html(data);
        }
      });
    }
    
    
    </script>

'''
    return rstr


@app.route('/tshow', methods =['GET', 'POST'])
def tshow():
    
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM learning_type")
    row_headers=[x[0] for x in cursor.description] 
    DBData = cursor.fetchall() 
    cursor.close()
    json_data=[]
    rstr="<table border><tr>"
    for r in row_headers:
        rstr=rstr+"<th>"+r+"</th>"
    rstr=rstr+"<th>Update</th><th>Delete</th></tr>"
    cnt=0
    did=-1
    for result in DBData:
        cnt=0
        ll=['A','B','C','D','E','F','G','H','I','J','K']
        for row in result:
            if cnt==0:
                rtid=row
                rstr=rstr+"<td>"+str(row)+"</td>" 
           
            else:
                rstr=rstr+"<td>"+"<input type=text id=T"+str(ll[cnt])+str(rtid)+" value=\""+str(row)+"\"></td>"     
            cnt+=1
            
        rstr+="<td><a ><i class=\"fa fa-edit\" aria-hidden=\"true\" onclick=tupdate("+str(rtid)+")></i></a></td>"
        rstr+="<td><a ><i class=\"fa fa-trash\" aria-hidden=\"true\" onclick=tdel("+str(rtid)+")></i></a></td>"
        
        rstr=rstr+"</tr>"
    
    rstr=rstr+"</table>"
    rstr=rstr+'''
    <script type=\"text/javascript\">
    function tupdate(rtid)
    {
       //alert('aha no');
       tname=$("#TB"+rtid).val();
       tdes=$("#TC"+rtid).val();
       $.ajax({
        url: \"/tupdate\",
        type: \"POST\",
        data: {rtid:rtid,tname:tname,tdes:tdes},
        success: function(data){
       
        alert(data);
        loadtypes();
        }
       });
    }
   
    function tdel(rtid)
    {
    $.ajax({
        url: \"/tdelete\",
        type: \"POST\",
        data: {rtid:rtid},
        success: function(data){
        alert(data);
        loadtypes();
        }
        });
    }
   
    function loadtypes(){
       $.ajax({
        url: 'http://127.0.0.1:5000/tshow',
        type: 'POST',
        success: function(data){
          $('#tshow').html(data);
        }
      });
    }
    
    
    </script>

'''
    return rstr
@app.route('/mupdate', methods=['GET', 'POST'])

def mupdate():
    mid=request.form.get('rid')
    mname=request.form.get('mname')
    mc=request.form.get('mc')
    
    cursor = mysql.connection.cursor()
    cursor.execute(''' UPDATE learning_module SET module_name=%s,module_content=%s WHERE mid=%s''',(mname,mc,mid))
    mysql.connection.commit()
    cursor.close()
    return "Updated successfully"
@app.route('/mshow', methods=['GET', 'POST'])

def mshow():
    cursor = mysql.connection.cursor()

    cursor.execute("SELECT * FROM learning_module")
    row_headers=[x[0] for x in cursor.description] 
    DBData = cursor.fetchall() 
    cursor.close()
    json_data=[]
    rstr="<table border><tr>"
    for r in row_headers:
        rstr=rstr+"<th>"+r+"</th>"
    rstr=rstr+"<th>Update</th><th>Delete</th></tr>"
    cnt=0
    did=-1
    for result in DBData:
        cnt=0
        ll=['A','B','C','D','E','F','G','H','I','J','K']
        for row in result:
            if cnt==0:
                rid=row
                rstr=rstr+"<td>"+str(row)+"</td>" 
            elif cnt==5:
                rfil="http://127.0.0.1:5000/static/resources/"+str(row)
                rstr=rstr+"<td>"+"<a href=\""+str(rfil)+"\" target=_blank>File</a></td>"
            else:
                rstr=rstr+"<td>"+"<input type=text id=M"+str(ll[cnt])+str(rid)+" value=\""+str(row)+"\"></td>"     
            cnt+=1
            
        rstr+="<td><a ><i class=\"fa fa-edit\" aria-hidden=\"true\" onclick=mupdate("+str(rid)+")></i></a></td>"
        rstr+="<td><a ><i class=\"fa fa-trash\" aria-hidden=\"true\" onclick=mdel("+str(rid)+")></i></a></td>"
        
        rstr=rstr+"</tr>"
    
    rstr=rstr+"</table>"
    rstr=rstr+'''
    <script type=\"text/javascript\">
    function mupdate(rid)
    {
       //alert('aha no');

       mname=$("#MB"+rid).val();
       mc=$("#MC"+rid).val();
       mtid=$("#MD"+rid).val();
       mcid=$("#ME"+rid).val();
       
       var fd=new FormData();
       fd.append('mname',mname);
       fd.append('mc',mc);
       fd.append('mtid',mtid);
       fd.append('mcid',mcid);
       
       fd.append('rid',rid); 

       $.ajax({
        url: \"/mupdate\",
        type: \"POST\",
        data: fd,
        processData: false,
        contentType: false,
        success: function(data){
       
        alert(data);
        loadmodules();
        }
       });
    }
   
    function mdel(rid)
    {
    $.ajax({
        url: \"/mdelete\",
        type: \"POST\",
        data: {rid:rid},
        success: function(data){
        alert(data);
        loadmodules();
        }
        });
    }
   
    
    function loadmodules(){
       $.ajax({
        url: 'http://127.0.0.1:5000/mshow',
        type: 'POST',
        success: function(data){
          $('#mshow').html(data);
        }
      });
    }
    
    
    </script>

'''
    return rstr


                              
@app.route('/adminav', methods =['GET', 'POST'])
def adminav():
    return render_template('adminnav.html')


if __name__ == '__main__':
    app.run(debug=True)