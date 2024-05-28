from flask import Flask, flash,render_template,request,url_for,redirect,session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash,check_password_hash
import mysql.connector

app=Flask(__name__)
app.secret_key ='course'

# app.config["MYSQL_HOST"]="localhost"
# app.config["MYSQL_USER"]="root"
# app.config["MYSQL_PASSWORD"]="kGISL"
# app.config["MYSQL_DB"]="fkiteissue"
# app.config["MYSQL_CURSORCLASS"]="DictCursor"
# conn=MySQL(app)
# for restoring database


@app.route('/',methods = ['GET','POST'])
def index():
   return render_template('index.html')


@app.route('/course',methods = ['GET','POST'])
def course():
   return render_template('course.html')

@app.route('/test',methods = ['GET','POST'])
def test():
   return render_template('test.html')

@app.route('/gindex',methods = ['GET','POST'])
def gindex():
   return render_template('gindex.html')
@app.route('/detail',methods = ['GET','POST'])
def detail():
   return render_template('detail.html')

# @app.route('/about',methods = ['GET','POST'])
# def about():
#    return render_template('about.html')

# @app.route('/contact',methods = ['GET','POST'])
# def contact():
#    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True)