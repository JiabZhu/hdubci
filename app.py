from flask import Flask, request
from flask_socketio import SocketIO

import paradigms.rsvp_offline as rsvp_offline

exp_paradigm = None

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/rsvp_offline', methods=['GET'])
def rsvp_paradigm_offline():
    global exp_paradigm
    exp_paradigm = rsvp_offline.RSVP_Offline()
    return 'rsvp study paradigm'


@app.route('/rsvp_offline/adddevice', methods=['POST'])
def rsvp_offline_addDevice():
    deviceInfo = request.get_json()
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


@app.route('/sendstipic', methods=['POST'])
def send_sti_pic():
    socketio.emit('sti pic', request.get_json())
    return "send sti pic success"


@app.route('/sendfixpic', methods=['GET'])
def send_fix_pic():
    socketio.emit('fixation pic', 'show fixation pic')
    return "send fixation pic success"


@app.route('/sendendpic', methods=['GET'])
def send_end_pic():
    socketio.emit('end pic', 'show end pic')
    return "send end pic success"


@socketio.on('my event')
def test_connect(json):
    print('received json:' + str(json))


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
