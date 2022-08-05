from flask import Flask
import mysql.connector
from mysql.connector import errorcode


config = {
  'host':'mysql789.mysql.database.azure.com',
  'user':'mysqluser',
  'password':'jyPassw.rd1234',
  'database':'mysql789'
}


app = Flask(__name__)
host_addr = "0.0.0.0"
host_port = 80

@app.route('/')
def hello():
    #return msg
    return "try `/ping!"

@app.route('/ping')
def ping():
    return {'response': 'pong'}

if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)
    
    #msg = ""
    try:
        conn = mysql.connector.connect(**config)
        print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            #msg = "err"
    else:
        cursor = conn.cursor()
        print("cusor = conn.cursor()")
