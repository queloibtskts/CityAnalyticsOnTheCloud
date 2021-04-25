from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/scenarios', methods=['GET'])
def get_scenarios():
    return 'There are some scenarios!'


if __name__ == '__main__':
    app.run()
