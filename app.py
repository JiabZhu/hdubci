from flask import Flask, redirect, request, jsonify
from paradigms.rsvp_offline import RSVP_Offline

exp_paradigm = None

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/hey/<username>')
def hey(username):
    return "hey %s" % username


@app.route('/baidu/')
def baidu():
    return redirect('https://www.baidu.com')


@app.route('/test/my/first', methods=['POST'])
def first_post():
    my_json = request.get_json()
    print(my_json)
    name = my_json.get("name")
    age = my_json.get("age")
    return jsonify(name=name, age=age, code=200)


@app.route('/test/rsvp_offline', methods=['POST'])
def rsvp_offline():
    global exp_paradigm

    json = request.get_json()
    print(json)
    rsvp = RSVP_Offline()

    exp_paradigm = rsvp
    return "success"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10087)
