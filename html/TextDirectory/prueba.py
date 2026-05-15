from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola():
    return 'Hola mundo'

app.run(debug=True)
