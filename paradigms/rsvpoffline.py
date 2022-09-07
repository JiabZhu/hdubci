import json
import time
import random
import requests
import numpy as np
from threading import Thread

import util.config as config
from devices.neuroscan import NeuroScan


class RsvpOffline:
    def __init__(self):
        super(RsvpOffline, self).__init__()

        self.__websocket_url = config.get_websocket_url()

        self.__mark = []
        self.__device = []
        self.__show_stimulus_thread = None

        self.start_time = -1

        self.target_proportion = -1
        self.non_target_proportion = -1
        self.trial_num = -1
        # self.rest_trial_num = -1

        self.target_mark = -1
        self.non_target_mark = -1

        self.fixation_duration = -1
        self.pic_duration = -1
        # self.rest_duration = -1

        self.fixation_pic = ''
        # self.rest_pic = ''
        self.end_pic = ''
        self.target_pic_list = []
        self.non_target_pic_list = []

    def add_device(self, device_info):
        """
        添加设备
        :param device_info: 设备信息
        :return:
        """

        # 清空设备，清除前一次设备添加失败的影响
        self.__device = []

        # 添加设备
        for i in range(device_info['num']):
            if device_info['type'][i] == 'neuroscan':
                self.__device.append(NeuroScan())

        # 连接设备
        for i in range(device_info['num']):
            self.__device[i].connect(device_info['ip'][i], device_info['port'][i])
            # NeuroScan设备连接完毕后开始播放
            if device_info['type'][i] == 'neuroscan':
                self.__device[i].start_acquisition()

    def set_study(self, study_info):
        """
        设置实验范式
        :param study_info: 实验设置信息
        :return:
        """
        print(study_info)
        self.target_proportion = study_info['target_proportion']
        self.non_target_proportion = study_info['non_target_proportion']

        self.trial_num = study_info['trial_num']
        # self.rest_trial_num = studyInfo['rest_trial_num']

        self.target_mark = study_info['target_mark']
        self.non_target_mark = study_info['non_target_mark']

        self.fixation_duration = study_info['fixation_duration']
        self.pic_duration = study_info['pic_duration']
        # self.rest_duration = studyInfo['rest_duration']

        self.fixation_pic = study_info['fixation_pic']
        # self.rest_pic = studyInfo['rest_pic']
        self.end_pic = study_info['end_pic']
        self.target_pic_list = study_info['target_pic_list']
        self.non_target_pic_list = study_info['non_target_pic_list']

    def ready_study(self):
        self.start_time = time.time()
        print('start time: ', time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
        for i in range(len(self.__device)):
            self.__device[i].start_send_data()

    def start_study(self):
        self.__show_stimulus_thread = Thread(target=self.show_stimulus)
        self.__show_stimulus_thread.start()

    def show_stimulus(self):
        print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), self.fixation_pic)
        self.__request_show_fixation_pic()
        time.sleep(self.fixation_duration)

        cnt_trial = 0
        while cnt_trial < self.trial_num:
            # 图片列表加入目标与非目标刺激，并打乱顺序
            pic_list = [[random.randint(0, len(self.target_pic_list) - 1), self.target_mark]
                        for _ in range(self.target_proportion)]
            pic_list.extend([[random.randint(0, len(self.non_target_pic_list) - 1), self.non_target_mark]
                             for _ in range(self.non_target_proportion)])
            np.random.shuffle(pic_list)

            for i in range(len(pic_list)):
                self.__mark.append([time.time(), pic_list[i][1]])
                self.__request_show_sti_pic(pic=self.__get_pic_name_mark(pic_list[i]))
                print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), pic_list[i])
                time.sleep(self.pic_duration)

                cnt_trial += 1
                if not cnt_trial < self.trial_num:
                    break

                # if cnt_trial % self.rest_trial_num == 0:
                #     print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), self.rest_pic)
                #     time.sleep(self.rest_duration)

        self.__request_show_end_pic()
        # print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), self.end_pic)
        for i in range(len(self.__mark)):
            self.__mark[i][0] = self.__mark[i][0] - self.start_time
        # print(self.__mark)

        # 保存数据，断开连接
        for i in range(len(self.__device)):
            self.__device[i].stop_send_data()
            self.__device[i].save_data(mark=self.__mark)
            self.__device[i].disconnect()


    def __request_show_fixation_pic(self):
        requests.get(url=self.__websocket_url + 'sendfixpic')

    def __request_show_end_pic(self):
        requests.get(url=self.__websocket_url + 'sendendpic')

    def __request_show_sti_pic(self, pic):
        requests.post(url=self.__websocket_url + 'sendstipic', json=json.dumps(pic))

    def __get_pic_name_mark(self, pic_info):
        idx = pic_info[0]
        mark = pic_info[1]
        if mark == self.target_mark:
            return {'pic': self.target_pic_list[idx], 'mark': mark}
        elif mark == self.non_target_mark:
            return dict({'pic': self.non_target_pic_list[idx], 'mark': mark})
