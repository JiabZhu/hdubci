import time
import random
import numpy as np
from threading import Thread

import app
from devices.neuroscan import NeuroScan

class RSVP_Offline:
    def __init__(self):
        super(RSVP_Offline, self).__init__()

        self.__mark = []
        self.__device = []
        self.__show_stimulus_thread = None

        self.start_time = -1

        self.target_proportion = -1
        self.non_target_proportion = -1
        self.trial_num = -1
        self.rest_trial_num = -1

        self.target_mark = -1
        self.non_target_mark = -1

        self.fixation_duration = -1
        self.pic_duration = -1
        self.rest_duration = -1

        self.fixation_pic = ''
        self.rest_pic = ''
        self.end_pic = ''
        self.target_pic_list = []
        self.non_target_pic_list = []

    def addDevice(self, deviceInfo):
        '''
        添加设备
        :param deviceInfo: 设备信息
        :return:
        '''

        # 清空设备，清除前一次设备添加失败的影响
        self.__device = []

        # 添加设备
        for i in range(deviceInfo['num']):
            if deviceInfo['type'][i] == 'neuroscan':
                self.__device.append(NeuroScan())

        # 连接设备
        for i in range(deviceInfo['num']):
            self.__device[i].connect(deviceInfo['ip'][i], deviceInfo['port'][i])
            # NeuroScan设备连接完毕后开始播放
            if deviceInfo['type'][i] == 'neuroscan':
                self.__device[i].startAcquisition()

    def setStudy(self, studyInfo):
        '''
        设置实验范式
        :param studyInfo: 实验设置信息
        :return:
        '''
        print(studyInfo)
        self.target_proportion = studyInfo['target_proportion']
        self.non_target_proportion = studyInfo['non_target_proportion']

        self.trial_num = studyInfo['trial_num']
        self.rest_trial_num = studyInfo['rest_trial_num']

        self.target_mark = studyInfo['target_mark']
        self.non_target_mark = studyInfo['non_target_mark']

        self.fixation_duration = studyInfo['fixation_duration']
        self.pic_duration = studyInfo['pic_duration']
        self.rest_duration = studyInfo['rest_duration']

        self.fixation_pic = studyInfo['fixation_pic']
        self.rest_pic = studyInfo['rest_pic']
        self.end_pic = studyInfo['end_pic']
        self.target_pic_list = studyInfo['target_pic_list']
        self.non_target_pic_list = studyInfo['non_target_pic_list']

    def readyStudy(self):
        self.start_time = time.time()
        print('start time: ', time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
        # for i in range(len(self.__device)):
        #     self.__device[i].startSendData()

    def startStudy(self):
        self.__show_stimulus_thread = Thread(target=self.showStimulus)
        self.__show_stimulus_thread.start()

    def showStimulus(self):
        print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), self.fixation_pic)
        time.sleep(self.fixation_duration)

        cnt_trial = 0
        while (cnt_trial < self.trial_num):
            pic_list = [[random.randint(0, len(self.target_pic_list) - 1), self.target_mark]
                        for _ in range(self.target_proportion)]
            pic_list.extend([[random.randint(0, len(self.non_target_pic_list) - 1), self.non_target_mark]
                             for _ in range(self.non_target_proportion)])
            np.random.shuffle(pic_list)

            for i in range(len(pic_list)):
                self.__mark.append([time.time(), pic_list[i][1]])
                app.call_send_pic(21232)
                # app.sendPic(123)
                print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), pic_list[i])
                time.sleep(self.pic_duration)

                cnt_trial += 1
                if not cnt_trial < self.trial_num:
                    break

                if cnt_trial % self.rest_trial_num == 0:
                    print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), self.rest_pic)
                    time.sleep(self.rest_duration)

        print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()), self.end_pic)
        for i in range(len(self.__mark)):
            self.__mark[i][0] = self.__mark[i][0] - self.start_time
        print(self.__mark)

        # 保存数据
        # for i in range(len(self.__device)):
        #     self.__device[i].saveData(mark=self.__mark)

