import time
import socket
import struct
import threading
import numpy as np


class NeuroScan:
    def __init__(self):
        super(NeuroScan, self).__init__()
        self.basic_info = {}

        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__packet_header = {}
        self.__f_recvData = False
        self.__EEG_data = np.array([])
        self.__recv_data_thread = None

    def __setPacketHead(self, tuple):
        self.__packet_header = {'m_chId': tuple[0], 'm_wCode': tuple[1],
                                'm_wRequest': tuple[2], 'm_dwSize': tuple[3]}

    def __setBasicInfo(self, tuple):
        self.basic_info = {'dwSize': tuple[0], 'nEegChan': tuple[1], 'nEvtChan': tuple[2],
                           'nBlockPnts': tuple[3], 'nRate': tuple[4], 'nDataSize': tuple[5],
                           'fResolution': tuple[6]}

    def sendCmd(self, m_chId, m_wCode, m_wRequest):
        header = struct.pack(">4sHHI", m_chId, m_wCode, m_wRequest, 0)
        self.__sock.send(header)

    def connect(self, ip, port):
        self.__sock.connect((ip, port))
        self.getEDFHeader()

    def disconnect(self):
        self.sendCmd(b'CTRL', 1, 2)
        self.__sock.close()

    def startAcquisition(self):
        self.sendCmd(b'CTRL', 2, 1)

    def stopAcquisition(self):
        self.sendCmd(b'CTRL', 2, 2)

    def startImpedance(self):
        self.sendCmd(b'CTRL', 2, 3)

    def startSendData(self):
        self.sendCmd(b'CTRL', 3, 3)
        self.__f_recvData = True
        self.__recv_data_thread = threading.Thread(target=self.recvEEGData)
        self.__recv_data_thread.start()

    def stopSendData(self):
        self.__f_recvData = False
        time.sleep(0.2)
        self.sendCmd(b'CTRL', 3, 4)

    def getEDFHeader(self):
        self.sendCmd(b'CTRL', 3, 5)
        buffer = self.__sock.recv(12)
        self.__setPacketHead(struct.unpack('>4sHHI', buffer))

        buffer = b''
        body_len = self.__packet_header['m_dwSize']
        if body_len > 0:
            while (len(buffer) < body_len):
                buffer += self.__sock.recv(body_len - len(buffer))
        self.__setBasicInfo(struct.unpack('<6If', buffer))

    def recvEEGData(self):
        while self.__f_recvData:
            buffer = self.__sock.recv(12)

            self.__setPacketHead(struct.unpack('!4sHHI', buffer))

            buffer = b''
            body_len = self.__packet_header['m_dwSize']
            if body_len > 0:
                while (len(buffer) < body_len):
                    buffer += self.__sock.recv(body_len - len(buffer))
                data_len = body_len / self.basic_info['nDataSize']

                data = np.array(list(struct.unpack('<%di' % data_len, buffer)))
                data = data.astype(float) * self.basic_info['fResolution']
                data = data.reshape(self.basic_info['nBlockPnts'],
                                    self.basic_info['nEegChan'] + self.basic_info['nEvtChan'])
                if len(self.__EEG_data) == 0:
                    self.__EEG_data = data
                else:
                    self.__EEG_data = np.append(self.__EEG_data, data, axis=0)
        self.__EEG_data = self.__EEG_data.transpose()
