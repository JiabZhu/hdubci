from devices.neuroscan import NeuroScan

class RSVP_Offline:
    def __init__(self, exp_settiing):
        super(RSVP_Offline, self).__init__()
        self.__device = []

        self.start_time = -1

        self.target_mark = exp_settiing['target_mark']
        self.non_target_mark = exp_settiing['non_target_mark']

        self.fixation_duration = exp_settiing['fixation_duration']
        self.target_pic_duration = exp_settiing['target_pic_duration']
        self.non_target_pic_duration = exp_settiing['non_target_pic_duration']

        self.target_pic_list = exp_settiing['target_pic_list']
        self.non_target_pic_list = exp_settiing['non_target_pic_list']

    def addDevice(self, deviceInfo):
        # 清空设备，清除前一次设备添加失败的影响
        self.__device = []

        # 添加设备
        for i in range(deviceInfo['num']):
            if deviceInfo['type'][i] == 'neuroscan':
                self.__device.append(NeuroScan())

        # 连接设备
        for i in range(deviceInfo['num']):
            self.__device[i].connect(deviceInfo['ip'], deviceInfo['port'])
            # NeuroScan设备连接完毕就开始播放
            if deviceInfo['type'][i] == 'neuroscan':
                self.__device[i].startAcquisition()
