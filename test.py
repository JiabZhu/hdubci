import time
import numpy as np
from devices.neuroscan import NeuroScan

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    a.extend(b)
    print(a)
    np.random.shuffle(a)
    print(a)

    # n = NeuroScan()
    # n.connect("10.1.125.103", 4000)
    # print(n.basic_info)
    #
    # print("开始播放")
    # n.startAcquisition()
    # time.sleep(10)
    # print("请求发送数据")
    # n.startSendData()
    # time.sleep(10)
    #
    # n.stopSendData()
    # time.sleep(0.1)
    # n.stopAcquisition()
    # time.sleep(0.1)
    # n.disconnect()
