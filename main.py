from flask import Flask,request,render_template,redirect,url_for,session
import pymysql
import smtplib
import ast
from functools import wraps

#Copyright by Mitul & Jay !

app = Flask(__name__)
app.secret_key = "AllrightItsFckinOKDude"
db = pymysql.connect(
	                     host = "localhost",
	                     user = "root",
	                     password = "",
	                     db = "fruit_stole"
	                 )
	                     
@app.route("/signup", methods=['GET','POST'])
def signup():
	if request.method == 'POST':
		name = request.form['name']
		username = request.form['username']
		email = request.form['email']
		contact = request.form['contact']
		address = request.form['address']
		password = request.form['password']
		cursor = db.cursor()
		danzer = "true"
		if name !="" and username !="" and email !="" and contact !="" and address !="" and password !="":
			
			

			cursor.execute("select username from regester")
			numrow = cursor.rowcount
			for i in range(numrow):
				user_input = cursor.fetchone()
				if user_input[0] == username:
					res_msg = "username is already in the database. so type other username ! ThankYou"
					danzer = "true"
					return render_template("signup.html",res_msg=res_msg,title="signup",danzer=danzer)
			cursor.execute("select email from regester")
			numrow_email = cursor.rowcount
			for i in range(numrow_email):
				user_input_email = cursor.fetchone()
				if user_input_email[0] == email:
					res_msg = "Email is already in the database. so type other username ! ThankYou "
					danzer = "true"
					return render_template("signup.html",res_msg=res_msg,title="signup",danzer=danzer)

			query = "INSERT INTO regester(name,username,email,contact,address,password) VALUES(%s,%s,%s,%s,%s,%s)"
			try:
				cursor.execute(query,(name,username,email,contact,address,password))
				new_user_query = """CREATE TABLE IF NOT EXISTS {}(
															order_id INT AUTO_INCREMENT,
															order_date DATE,
															item_list TEXT,
															total_pay VARCHAR(255),
															PRIMARY KEY (order_id)
														)""".format(username)
				cursor.execute(new_user_query)
				db.commit()
				cursor.close()
				# preparing Message for New User and send A Email
				email_message = '''
						Hello {},

						Welcome To The UVPCE Fruit Store. ! 
						Happy To see you

						Thank you, from UVPCE Fruit Store.
				'''.format(name)
				res_msg = "Regestration Successfully Done !"
				send_data(email,email_message)	
				danzer = "false"
				return render_template("signup.html",res_msg=res_msg,title="signup",danzer=danzer)
			except:
				db.rollback()
				cursor.close()
				res_msg = "Something Was Wrong !"
				danzer = "true"
				return render_template("signup.html",res_msg=res_msg,title="signup",danzer=danzer)
		else:
			cursor.close()
			res_msg = "Please Enter All Informations ! "
			danzer = "true"
			return render_template("signup.html",res_msg=res_msg,title="signup",danzer=danzer)		
	else:
		return render_template("signup.html",title="signup")	

@app.route("/")
@app.route("/login", methods=['GET','POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		cursor = db.cursor()
		if username != "" and password !="":
			
			query = 'select username from regester where username = "'+str(username)+'"'
			cursor.execute(query)
			numrow = cursor.rowcount
			if numrow >= 1 :
				cursor.execute('select password from regester where username = "'+str(username)+'"')
				fetched_pass = cursor.fetchone()
				if fetched_pass[0] == password:
					cursor.execute('select * from regester where username = "'+str(username)+'"')
					data = cursor.fetchone()
					session['logged_in'] = True
					session['username'] = username
					cursor.close()
					return  redirect('dashboard/'+session['username'])
				else:
					message = "password Does Not Match  ! "
					cursor.close()
					return render_template("login.html",message=message,title="login")	
			else:
				message = "No such username Exiist  ! "
				cursor.close()
				return render_template("login.html",message=message,title="login")
		else:
				message = "Please Enter Unsername And Password "
				cursor.close()
				return render_template("login.html",message=message,title="login")	
	else:
		if 'logged_in' in session:
			return redirect("dashboard/"+session['username'])
		else:
			return render_template("login.html",title="login")	

@app.route("/logout", methods=['GET','POST'])
def logout():
	session.clear()
	return redirect(url_for("login"))

def send_data(reciver,message):
	s = smtplib.SMTP('smtp.gmail.com', 587) 
	s.starttls() 
	s.login("Enter Your Email Here", "Enter Your Password Here") 
	s.sendmail("Enter Your Email Here",reciver, message) 
	s.quit()


@app.route("/dashboard/<username>/<total_prise>/<bill>")
def done(username,total_prise,bill):
	cursor = db.cursor()
	query = "INSERT INTO {}(order_date,item_list,total_pay) values(CURDATE(),%s,%s)".format(username)
	cursor.execute('select * from regester where username = "'+str(username)+'"')
	data = cursor.fetchone()
	email = data[3]
	address = data[5]
	order_dict = ast.literal_eval(bill)
	list_str = ""
	for k,v in order_dict.items():
		list_str = list_str +  k +" : " +v+" ,"
	
	email_msg = '''
	Hello {},
	Your iteam is :  {}
	Total price is :  {} /-
	your order will reach you in 1 hour !
	your Address is : {}
	Happy to Help you ! Thank you, from UVPCE Fruit Store.
	'''.format(username,list_str,total_prise,address)
	tablelist = order_dict
	try:
		send_data(email,email_msg)
		cursor.execute(query,(bill,total_prise))
		db.commit()
		cursor.close()	
		
		return render_template('thankyou.html',username = username,list_str=list_str,total_prise=total_prise,address=address,tablelist=tablelist)
	except:
		db.rollback()
		cursor.close()	
		return "problem"
	

@app.route("/admin", methods=['GET','POST'])
def admin():	
	query="select * from regester"
	cursor = db.cursor()
	cursor.execute(query)
	data = cursor.fetchall()
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username == "admin" and password == "admin":
			session['admin'] = username
			cursor.close()
			return render_template("admin_data.html",data=data,title="admin")
		else:
			message = "Username or Password Does Not Match !"
			danzer = "true"
			cursor.close()
			return render_template("admin_login.html",message=message,danzer=danzer,title="admin")	
	else:
		if 'admin' in session:
			cursor.close()
			return render_template("admin_data.html",data=data,title="admin")
		else:
			cursor.close()
			return render_template("admin_login.html",title="admin")

@app.route("/ChangePassword", methods=['GET','POST'])
def change_password():
	if request.method == 'POST':
		username = session['username']
		old_password = request.form['old_password']
		new_password = request.form['new_password']
		danzer = "false"
		cursor = db.cursor()
		query = 'select * from regester where username = "'+str(username)+'"'+' AND password = "'+str(old_password)+'"'
		
		cursor.execute(query)
		numrow = cursor.rowcount
		
		if numrow >=1 :
			data = cursor.fetchone()
			email = data[3]
			query1 = "UPDATE regester SET password=%s where username=%s"
			
			if cursor.execute(query1,(new_password,username)):
				db.commit()
				message = "Password Successfully Changed !"
				email_message = '''
                    Hello {},
                    Password Successfully Changed ! 

                    				Thank you, from UVPCE Fruit Store.
						'''.format(data[1])

				send_data(email,email_message)
				cursor.close()
				return render_template("change_password.html",message=message,title="change password",danzer=danzer)
			else:	

				message = "Something Was Wrong ! Please Try Again"
				danzer = "true"
				cursor.close()
				return render_template("change_password.html",message=message,title="change password",danzer=danzer)
		else:
			message = "Something Was Wrong ! Please Try Again"
			danzer = "true"
			cursor.close()
			return render_template("change_password.html",message=message,title="change password",danzer=danzer)
	else:
		
		if 'logged_in' in session:
			return render_template("change_password.html",title="change password")
		else:
			return redirect("login")					
		
@app.route("/ForgotPassword", methods=['GET','POST'])
def recovery():
	if request.method == 'POST':
		email = request.form['email']
		cursor = db.cursor()
		query = 'select * from regester where email = "'+str(email)+'"'
		cursor.execute(query)
		numrow_recovery = cursor.rowcount
		if numrow_recovery >=1 :
			cursor.execute('select * from regester where email = "'+str(email)+'"')
			data = cursor.fetchone()
			email_message = '''
                    Hello {},
                        Your username : {}
                        	 password : {} 

                    				Thank you, from UVPCE Fruit Store.
						'''.format(data[1],data[2],data[6])
			send_data(data[3],email_message)
			message = "Username and Password Are Send To Your Email ! "
			cursor.close()
			return render_template("forgot_password.html",message=message,title="recovery")
		else:
			message = "Something Was Wrong ! Please Try Again"
			cursor.close()
			return render_template("forgot_password.html",message=message,title="recovery")
	else:
		return render_template("forgot_password.html",title="recovery")	


@app.route("/dashboard/<username>", methods=['GET','POST'])
#@login_required
def dashboard(username):
	cursor = db.cursor()
	cursor.execute('SELECT * FROM fruits')
	data = cursor.fetchall()
	total_fruit = len(data)
	if request.method == 'POST' :
		
		checkbox = []
		checked_name = []
		checked_prise = []
		checked_select = []
		for i in range(len(data)):
			try:
				temp = request.form[data[i][1]]

			except:
				temp = "off"	

			checkbox.append(temp)
			checked_name.append(data[i][1])
			checked_prise.append(data[i][2])
			checked_select.append(request.form[str(data[i][1])+"_select"])
		bill = {}
		total_prise = 0
		for i in range(len(data)):
			if checkbox[i] == "on":
				total_prise = total_prise + (float(checked_prise[i])*float(checked_select[i]))
				bill.update({checked_name[i]:str(checked_prise[i])+" ( "+checked_select[i]+"Kg ) = "+str(float(checked_select[i])*float(checked_prise[i]))})

				
		if total_prise>0:
			bill_str = str(bill)
			total_prise_str = str(total_prise)
			cursor.close()		
			return render_template("test.html",checkbox=checkbox,checked_name=checked_name,checked_prise=checked_prise,bill=bill,total_prise=total_prise,bill_str=bill_str,total_prise_str=total_prise_str)
		else:
			message = "Please select at least one iteam ! "
			cursor.close()
			return render_template("dashboard.html",data=data,total_fruits=total_fruit,message=message)
	else : 
		cursor.close()
		if 'logged_in' in session:
			return render_template("dashboard.html",data=data,total_fruits=total_fruit)
		else:
			return redirect("login")
		#return render_template("dashboard.html",data=data,total_fruits=total_fruit)	

	return "something was wrong ! try again! "

@app.route("/shopkeeper_auth", methods=['GET','POST'])
def shopkeeper_auth():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username == "shop" and password == "shop":
			session['shopkeeper'] = username
			return redirect("shopkeeper")
		else:
			message = "Username or Password Does Not Match !"
			danzer = "true"
			return render_template("shopkeeper_login.html",message=message,danzer=danzer,title="shopkeeper")	
	else:
		if 'shopkeeper' in session:
			return redirect("shopkeeper")
		else:
			return render_template("shopkeeper_login.html",title="shopkeeper")



@app.route("/shopkeeper", methods=['GET','POST'])
def shopkeeper():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM fruits')
	data = cursor.fetchall()
	total_fruit = len(data)
	
	if request.method == 'POST':

		

		iteam_name = request.form['iteam_name']
		iteam_prise = request.form['iteam_prise']
		if iteam_name != "" and iteam_prise != "":
			cursor = db.cursor()
			query = "insert into fruits(fruit_name,fruit_prise) values(%s,%s)"
			cursor.execute(query,(iteam_name,iteam_prise))
			db.commit()	
			# for fetching  updated data
			cursor.execute('SELECT * FROM fruits')
			data = cursor.fetchall()
			total_fruit = len(data) 
			cursor.close()
			message = iteam_name+" successfully added ! "
			danzer = "flase"
			return render_template("shopkeeper.html",message = message,data = data,total_fruit=total_fruit,danzer=danzer)
		else:
			message = "Please Enter Valid Information ! "
			danzer = "true"
			return render_template("shopkeeper.html",message = message,data = data,total_fruit=total_fruit,danzer=danzer)	
	else:
		if 'shopkeeper' in session:
			return render_template("shopkeeper.html",data=data,total_fruit=total_fruit)
		else:
			return redirect("shopkeeper_auth")

@app.route("/operation/<id_code>")
def operation(id_code):
	if 'shopkeeper' in session:
		cursor = db.cursor()
		cursor.execute("select fruit_id from fruits")
		numrow1 = cursor.rowcount
		ids = cursor.fetchall()
	
		x = str(id_code)
		query = "DELETE FROM fruits WHERE fruit_id=%s"
		cursor.execute(query,(x))
		db.commit()
		return redirect("/shopkeeper_auth")
	else:
		return redirect("/shopkeeper_auth")	

					
	


@app.route("/profile/<username>", methods=['GET','POST'])
def profile(username):
	if 'logged_in' in session:
		cursor = db.cursor()
		username = session['username']
		query0 = "select id from regester where username = %s"
		cursor.execute(query0,(username))
		user_id = cursor.fetchone()
		query = "select * from regester where username = %s"
		cursor.execute(query,(username))		
		data = cursor.fetchall()
		email_fetched = data[0][3]
		if request.method == 'POST':
			name = request.form['name']
			#username_form = request.form['username']
			email = request.form['email']
			contact = request.form['contact']
			address = request.form['address']

			if name !="" and  email !="" and contact !="" and address !="":

				'''if username_form != username:
					query_username_check = "select username from regester"
					cursor.execute(query_username_check)
					numrow = cursor.rowcount
					for i in range(numrow):
						fetched_username = cursor.fetchone()
						if fetched_username[0] == username:
							res_msg = "{} username is already in the database. so type other username ! ThankYou".format(username_form)
							return render_template("profile.html",data=data,res_msg=res_msg,title="profile")'''

				if email_fetched != email:
					query_email_check = "select email from regester"
					cursor.execute(query_email_check)
					numrow = cursor.rowcount
					for i in range(numrow):
						fetched_email = cursor.fetchone()
						if fetched_email[0] == email:
							res_msg = " '{}' is already in the database. so type other Email ! ThankYou".format(email)
							return render_template("profile.html",res_msg=res_msg,title="profile",data=data)

				query1 = "UPDATE regester SET name = %s,email = %s,contact = %s,address = %s where username = %s"
				try:
					cursor.execute(query1,(name,email,contact,address,username))
					db.commit()
					query = "select * from regester where username = %s"
					cursor.execute(query,(username))		
					data = cursor.fetchall()
					res_msg = "Data Updated ! Thank You !"
					return render_template("profile.html",res_msg=res_msg,title="profile",data=data)
				except:
					res_msg = "Something Was Wrong ! Please Try Again"
					return render_template("profile.html",res_msg=res_msg,title="profile",data=data)
			else:
				res_msg = "Invalid Information ! Please try Agian !"	
				return render_template("profile.html",res_msg=res_msg,title="profile",data=data)
		else:
			
			res_msg = ""
			return render_template("profile.html",res_msg=res_msg,data=data)
	else:
		return redirect("login")	

@app.route("/my_order/<username>")
def my_order(username):
	if 'logged_in' in session:
		cursor = db.cursor()
		username = session['username']
		query = "select * from {}".format(username)
		try:
			cursor.execute(query)		
			data = cursor.fetchall()
		except:
			return "tabLe not found ! "
		print(data)
		data_length = len(data)
		return render_template("myorder.html",title="myorder",data=data,data_length=data_length)	
	else:
		return redirect("login")	

@app.route("/about")
def about():

    return render_template("about.html")



if __name__ == '__main__':
	app.run(debug=True)
