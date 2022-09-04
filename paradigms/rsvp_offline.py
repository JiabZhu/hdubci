from devices.neuroscan import NeuroScan

class RSVP_Offline:
    def __init__(self, exp_settiing):
        super(RSVP_Offline, self).__init__()
        self.__device = []

        self.start_time = -1

        self.target_mark = -1
        self.non_target_mark = -1

        self.fixation_duration = -1
        self.target_pic_duration = -1
        self.non_target_pic_duration = -1

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
            self.__device[i].connect(deviceInfo['ip'], deviceInfo['port'])
            # NeuroScan设备连接完毕后开始播放
            if deviceInfo['type'][i] == 'neuroscan':
                self.__device[i].startAcquisition()

    def setStudy(self, studyInfo):
        '''
        设置实验范式
        :param studyInfo: 实验设置信息
        :return:
        '''
        self.target_mark = studyInfo['target_mark']
        self.non_target_mark = studyInfo['non_target_mark']

        self.fixation_duration = studyInfo['fixation_duration']
        self.target_pic_duration = studyInfo['target_pic_duration']
        self.non_target_pic_duration = studyInfo['non_target_pic_duration']

        self.fixation_pic = studyInfo['fixation_pic']
        self.rest_pic = studyInfo['rest_pic']
        self.end_pic = studyInfo['end_pic']
        self.target_pic_list = studyInfo['target_pic_list']
        self.non_target_pic_list = studyInfo['non_target_pic_list']
