import json
import time
import requests
from threading import Thread

import util.config as config
from devices.neuroscan import NeuroScan

from model.model import Net


class RsvpOnline:
    def __init__(self):
        super(RsvpOnline, self).__init__()

        self.__url = config.get_local_url()

        self.__websocket_url = config.get_websocket_url()

        self.__device = []
        self.__show_stimulus_thread = None
        self.__model = Net()

        self.fixation_duration = -1
        self.pic_duration = -1

        self.fixation_pic = ''
        self.end_pic = ''
        self.pic_list = []

        self.time_window = 1

        self.__total_predict = 0

    # noinspection DuplicatedCode
    def add_device(self, device_info):
        """
        添加设备
        :param device_info: 设备信息
        :return:
        """
        print(device_info)

        device = None

        # 添加设备
        if device_info['type'] == 'neuroscan':
            device = NeuroScan()

        # 连接设备
        device.connect(device_info['ip'], device_info['port'])
        # NeuroScan设备连接完毕后开始播放
        if device_info['type'] == 'neuroscan':
            device.start_acquisition()

        self.__device.append(device)

    def set_study(self, study_info):
        """
        设置实验范式
        :param study_info: 实验设置信息
        :return:
        """
        print(study_info)

        self.fixation_duration = study_info['fixation_duration']
        self.pic_duration = study_info['pic_duration']

        self.fixation_pic = study_info['fixation_pic']
        self.end_pic = study_info['end_pic']
        self.pic_list = study_info['pic_list']

        self.time_window = study_info['time_window']
        # 加载模型
        # .......

    def ready_study(self):
        print('start time: ', time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
        for i in range(len(self.__device)):
            self.__device[i].start_send_data()

    def start_study(self):
        self.__show_stimulus_thread = Thread(target=self.show_stimulus)
        self.__show_stimulus_thread.start()

    def show_stimulus(self):
        print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), self.fixation_pic)
        # self.__request_show_fixation_pic()
        self.__request_show_sti_pic(pic={'pic': self.fixation_pic, 'mark': -1})
        time.sleep(self.fixation_duration)

        for i in range(len(self.pic_list)):
            for dv_id in range(len(self.__device)):
                self.__request_show_sti_pic(pic={'pic': self.pic_list[i], 'mark': -1})  # 向前端发送刺激图片
                # 预测该刺激图片属于哪一类
                __predict_thread = Thread(target=self.__model_predict, args=(self.pic_list[i], time.time(),))
                __predict_thread.start()

                print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), self.pic_list[i])
                time.sleep(self.pic_duration)

        # self.__request_show_end_pic()
        self.__request_show_sti_pic(pic={'pic': self.end_pic, 'mark': -1})

        while(self.__total_predict < len(self.pic_list)):
            pass

        # 断开设备连接
        for i in range(len(self.__device)):
            self.__device[i].stop_send_data()
            self.__device[i].disconnect()

    # def __request_show_fixation_pic(self):
    #     requests.get(url=self.__websocket_url + 'sendfixpic')
    #
    # def __request_show_end_pic(self):
    #     requests.get(url=self.__websocket_url + 'sendendpic')

    def __request_show_sti_pic(self, pic):
        requests.post(url=self.__url + 'sendstipic', json=json.dumps(pic))

    def __model_predict(self, pic, timestamp):
        # 获取数据
        data = []
        for i in range(len(self.__device)):
            if isinstance(self.__device[i], NeuroScan):
                data.append(self.__device[i].get_eeg_by_time(timestamp, self.time_window))

        res = {}
        # 模型预测
        for i in range(len(data)):
            res = {'pic': pic, 'predict': self.__model(data[i])}

        self.__total_predict += 1

        requests.post(url=self.__url + 'sendpredict', json=json.dumps(res))
