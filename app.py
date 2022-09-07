from flask import Flask, request
from flask_socketio import SocketIO

import util.config as config
import paradigms.rsvpoffline as rsvp_offline

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


exp_paradigm = rsvp_offline.RsvpOffline()


@app.route('/rsvp_offline', methods=['GET'])
def rsvp_paradigm_offline():
    """
    选择离线RSVP实验范式
    :return:
    """
    global exp_paradigm
    exp_paradigm = rsvp_offline.RsvpOffline()
    return 'rsvp study paradigm'


@app.route('/rsvp_offline/adddevice', methods=['POST'])
def rsvp_offline_add_device():
    """
    添加设备
    :return:
    """
    device_info = request.get_json()
    print(device_info)
    exp_paradigm.add_device(device_info)
    return "rsvp paradigm add device"


@app.route('/rsvp_offline/setstudy', methods=['POST'])
def rsvp_offline_set_study():
    """
    设置实验参数
    :return:
    """
    study_info = request.get_json()
    exp_paradigm.set_study(study_info)
    return "rsvp paradigm set study"


@app.route('/rsvp_offline/readystudy', methods=['GET'])
def rsvp_offline_ready_study():
    """
    实验设置完毕准备实验，倒计时结束后正式开始实验
    :return:
    """
    exp_paradigm.ready_study()
    return 'study ready'


@app.route('/rsvp_offline/startstudy', methods=['GET'])
def rsvp_offline_start_study():
    """
    正式开始实验
    :return:
    """
    exp_paradigm.start_study()
    return 'study starting'


@app.route('/sendstipic', methods=['POST'])
def send_sti_pic():
    """
    要求前端展示相应的刺激图片
    :return:
    """
    socketio.emit('sti pic', request.get_json())
    return "send sti pic success"


@app.route('/sendfixpic', methods=['GET'])
def send_fix_pic():
    """
    要求前端展示fixation阶段的图片
    :return:
    """
    socketio.emit('fixation pic', 'show fixation pic')
    return "send fixation pic success"


@app.route('/sendendpic', methods=['GET'])
def send_end_pic():
    """
    要求前端展示结束实验的图片
    :return:
    """
    socketio.emit('end pic', 'show end pic')
    return "send end pic success"


# @socketio.on('my event')
# def test_connect(json):
#     print('received json:' + str(json))


if __name__ == '__main__':
    socketio.run(app, host=config.get_host(), port=config.get_port())
