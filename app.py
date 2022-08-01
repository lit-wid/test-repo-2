from flask import Flask

app = Flask(__name__)
host_addr = "0.0.0.0"
host_port = 80

@app.route('/')
def hello():
    return "try twelveth `/ping!"

@app.route('/ping')
def ping():
    return {'response': 'pong'}

if __name__ == "__main__":
    app.run(debug=True,
            host=host_addr,
            port=host_port)
