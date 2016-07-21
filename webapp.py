from flask import Flask, render_template,url_for,request, redirect
app = Flask(__name__)

from database_setup import Base,Profile
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///crudlab.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':	
		return render_template('log_in.html')
	else:
		loger = session.query(Profile).filter_by(email = request.form['email']).first()
		if request.form['email'] == loger.email :
			print ('after mail')
			if loger.password == request.form['psw'] :
				print ('after password')
				return redirect(url_for('view_profile',pid=loger.id))
				print ('after redirect')
		#	else: 
				#wrong password

		#else:
			#you didnt sign up
#test

@app.route('/profile/<pid>')
def view_profile(pid):
	profile = session.query(Profile).filter_by(id = pid).first()
	return render_template("profile.html",profile=profile)

@app.route('/group')
def group(x):
	return render_template("group.html")



@app.route('/signup', methods=['GET', 'POST'])
def sign_up():
	if request.method == 'GET':	
		return render_template('index.html')
	else:
		new_name = request.form['name']
        	new_email = request.form['email']
        	new_password = request.form['password']
        	new_project = request.form['project']
		new_profile= Profile(name=new_name,email=new_email,password=new_password,project=new_project)
		session.add(new_profile)
		session.commit()
		return redirect(url_for('view_profile',pid=new_profile.id))






if __name__ == "__main__": 
	app.run() 
