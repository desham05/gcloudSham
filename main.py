import os
from flask import Flask,render_template
import pymysql

app = Flask(__name__)

dbServerName    = "35.237.45.39"
dbUser          = "root"
dbPassword      = "root"
dbName          = "sqldb"
charSet         = "utf8mb4"
cusrorType      = pymysql.cursors.DictCursor

 

connectionObject = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,db=dbName, charset=charSet,cursorclass=cusrorType)
   
def randrange():
    cursor = connectionObject.cursor()
    success='SELECT age,fare from titanic'
    cursor.execute(success)
    
    result = cursor.fetchall()
    return render_template('searchearth.html', ci=result)		
		
@app.route('/multiplerun', methods=['GET'])
def randquery():
    return randrange()

@app.route('/')
def hello_world():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080, debug=True)
