from flask_socketio import SocketIO, emit
from flask import Flask, redirect, request, jsonify, url_for

import paradigms.rsvp_offline as rsvp_offline

exp_paradigm = None

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


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


@app.route('/rsvp_offline', methods=['GET'])
def rsvp_paradigm_offline():
    global exp_paradigm
    exp_paradigm = rsvp_offline.RSVP_Offline()
    return 'rsvp study paradigm'


@app.route('/rsvp_offline/adddevice', methods=['POST'])
def rsvp_offline_addDevice():
    deviceInfo = request.get_json()
    print(deviceInfo)
    return "rsvp paradigm add device"


@app.route('/rsvp_offline/setstudy', methods=['POST'])
def rsvp_offline_setStudy():
    studyInfo = request.get_json()
    exp_paradigm.setStudy(studyInfo)

    return "rsvp paradigm set study"


@app.route('/rsvp_offline/readystudy', methods=['GET'])
def rsvp_offline_readyStudy():
    exp_paradigm.readyStudy()
    return 'study ready'


@app.route('/rsvp_offline/startstudy', methods=['GET'])
def rsvp_offline_startStudy():
    exp_paradigm.startStudy()
    return 'study starting'

@app.route('/sendpic')
def send_pic(pic):
    socketio.emit('send pic', pic)

def call_send_pic(pic):
    return url_for("api.send_pic", pic=pic)
@socketio.on('my event')
def test_connect(json):
    print('received json:' + str(json))


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
