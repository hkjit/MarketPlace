from flask import Flask
from flask import render_template
from flask import request
from flask import redirect, url_for, session
import MySQLdb


dbc = MySQLdb.connect("localhost","root","123456","practise")


app = Flask(__name__)
app.secret_key = 'EasyPayIITIANS'


def setSessionCredentials(username, usertype):
	session['username'] = username
	session['usertype'] = usertype

def getUserNameInCookies():
	if('username' in session and 'usertype' in session and session['username'] != "" and session['usertype'] == "user"):
		return session['username']
	return ""

def getIsUserLoggedin():
	if('username' in session and 'usertype' in session and session['username'] != "" and session['usertype'] == "user"):
		return True
	return False

def getIsMerchantLoggedin():
	if('username' in session and 'usertype' in session and session['username'] != "" and session['usertype'] == "merchant"):
		return True
	return False

def getMerchantNameInCookies():
	if('username' in session and 'usertype' in session and session['username'] != "" and session['usertype'] == "merchant"):
		return session['username']
	return ""

def getErrorString():
	if('errorString' in session ):
		return session['errorString']
	return ""

def setErrorString(error):
	session['errorString'] = error


@app.route('/login', methods=['POST', 'GET'])
def loginscreen():
	setErrorString("")
	setSessionCredentials("", "")
	print request
	if request.method=='POST':
		username = request.form["username"]
		password = request.form['password']
		usertype = request.form['usertype']
		if(usertype == "buyer"):
			#setSessionCredentials(username, usertype)
			cr = dbc.cursor()
			ss = "select * from users where username='"+username+ "' and password='"+password+"';"
			print ss
			cr.execute(ss)
			n = len(cr.fetchall())
			if n==1:
				return "login success"
			else:
				return "login failed"
			# check for user in db
		elif(usertype == "seller"):
			return "nothign"
			# check for user in db
	else:
		return "got"
		#get method



# if __name__ == '__main__':
#     app.run(debug=True)
