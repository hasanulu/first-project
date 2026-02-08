from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Merhaba DevOps Dünyasi!</h1><p>Ben geldim herkes ayağini denk alsin.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)