from flask import Flask
import mysql.connector
from mysql.connector import errorcode


config = {
  'host':'mysql789.mysql.database.azure.com',
  'user':'mysqluser',
  'password':'jyPassw.rd1234',
  'database':'movies'
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

@app.route('/pong')
def pong():
    msg = ""
    try:
        conn = mysql.connector.connect(**config)
        msg = "Connection established"
        #print("Connection established")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            msg = "Something is wrong with the user name or password"
            #print("Something is wrong with the user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            msg = "Database does not exist"
            #print("Database does not exist")
        else:
            print(err)
            msg = err
    else:
        cursor = conn.cursor()
        msg = "cusor = conn.cursor()"
    
    # Read data
    cursor.execute("SELECT * FROM movies;")
    rows = cursor.fetchall()
    print("Read",cursor.rowcount,"row(s) of data.")

    # Print all rows
    for row in rows:
        print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

    # Cleanup
    conn.commit()
    cursor.close()
    conn.close()
    print("Done.")

    return msg


if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)
    
    #msg = ""
    
