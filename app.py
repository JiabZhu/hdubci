from flask import Flask, redirect, request, jsonify
from paradigms.rsvp_offline import RSVP_Offline

from flask_socketio import SocketIO

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
def rsvp_offline():
    global exp_paradigm
    exp_paradigm = RSVP_Offline()
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


@socketio.on('connect', namespace='/test')  # 有客户端连接会触发该函数
def on_connect():
   print('connect')


@socketio.on('sendPic')
def sendPic(pic):
    socketio.emit('pic', pic)

if __name__ == '__main__':

    # app.run(host="0.0.0.0", port=5000)
    socketio.run(app, host='0.0.0.0', port=9999)
