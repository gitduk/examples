from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/t')
def hello_world():
    return 'test'


if __name__ == '__main__':
    app.run(debug=True)
