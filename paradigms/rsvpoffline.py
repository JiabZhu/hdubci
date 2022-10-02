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

        self.__url = config.get_local_url()
        self.__device = []
        self.__show_stimulus_thread = None

        self.target_proportion = -1
        self.non_target_proportion = -1
        self.trial_num = -1

        self.target_mark = -1
        self.non_target_mark = -1

        self.fixation_duration = -1
        self.pic_duration = -1

        self.fixation_pic = ''
        self.end_pic = ''
        self.target_pic_list = []
        self.non_target_pic_list = []

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
        # print(study_info)
        self.target_proportion = study_info['target_proportion']
        self.non_target_proportion = study_info['non_target_proportion']

        self.trial_num = study_info['trial_num']

        self.target_mark = study_info['target_mark']
        self.non_target_mark = study_info['non_target_mark']

        self.fixation_duration = study_info['fixation_duration']
        self.pic_duration = study_info['pic_duration']

        self.fixation_pic = study_info['fixation_pic']
        self.end_pic = study_info['end_pic']
        self.target_pic_list = study_info['target_pic_list']
        self.non_target_pic_list = study_info['non_target_pic_list']

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

        cnt_trial = 0
        while cnt_trial < self.trial_num:
            # 图片列表加入目标与非目标刺激，并打乱顺序
            pic_list = [[random.randint(0, len(self.target_pic_list) - 1), self.target_mark]
                        for _ in range(self.target_proportion)]
            pic_list.extend([[random.randint(0, len(self.non_target_pic_list) - 1), self.non_target_mark]
                             for _ in range(self.non_target_proportion)])
            np.random.shuffle(pic_list)

            for i in range(len(pic_list)):
                for dv_id in range(len(self.__device)):
                    self.__device[dv_id].add_mark([time.time(), pic_list[i][1]])
                self.__request_show_sti_pic(pic=self.__get_pic_name_mark(pic_list[i]))  # 向前端指定需要发送的刺激图片
                print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), pic_list[i])
                time.sleep(self.pic_duration)

                cnt_trial += 1
                if not cnt_trial < self.trial_num:
                    break

        # self.__request_show_end_pic()
        self.__request_show_sti_pic(pic={'pic': self.end_pic, 'mark': -1})

        # 保存数据，断开连接
        for i in range(len(self.__device)):
            self.__device[i].stop_send_data()
            self.__device[i].save_data()
            self.__device[i].disconnect()

    # def __request_show_fixation_pic(self, pic):
    #     requests.get(url=self.__url + 'sendfixpic')
    #
    # def __request_show_end_pic(self, pic):
    #     requests.get(url=self.__url + 'sendendpic')

    def __request_show_sti_pic(self, pic):
        requests.post(url=self.__url + 'sendstipic', json=json.dumps(pic))

    def __get_pic_name_mark(self, pic_info):
        idx = pic_info[0]
        mark = pic_info[1]
        if mark == self.target_mark:
            return {'pic': self.target_pic_list[idx], 'mark': mark}
        elif mark == self.non_target_mark:
            return {'pic': self.non_target_pic_list[idx], 'mark': mark}
