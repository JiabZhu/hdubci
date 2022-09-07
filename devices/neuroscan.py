import time
import socket
import struct
import scipy.io
import numpy as np
from threading import Thread


class NeuroScan:
    def __init__(self):
        super(NeuroScan, self).__init__()
        self.basic_info = {}

        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__packet_header = {}
        self.__f_recvData = False
        self.__EEG_data = np.array([])
        self.__recv_data_thread = None

    def __set_packet_head(self, header_info):
        self.__packet_header = {'m_chId': header_info[0], 'm_wCode': header_info[1],
                                'm_wRequest': header_info[2], 'm_dwSize': header_info[3]}

    def __set_basic_info(self, basis_info):
        self.basic_info = {'dwSize': basis_info[0], 'nEegChan': basis_info[1], 'nEvtChan': basis_info[2],
                           'nBlockPnts': basis_info[3], 'nRate': basis_info[4], 'nDataSize': basis_info[5],
                           'fResolution': basis_info[6]}

    def send_cmd(self, m_chid, m_wcode, m_wrequest):
        header = struct.pack(">4sHHI", m_chid, m_wcode, m_wrequest, 0)
        self.__sock.send(header)

    def connect(self, ip, port):
        self.__sock.connect((ip, port))
        self.get_edf_header()

    def disconnect(self):
        time.sleep(0.1)
        self.send_cmd(b'CTRL', 1, 2)
        self.__sock.close()

    def start_acquisition(self):
        self.send_cmd(b'CTRL', 2, 1)

    def stop_acquisition(self):
        self.send_cmd(b'CTRL', 2, 2)

    def start_impedance(self):
        self.send_cmd(b'CTRL', 2, 3)

    def start_send_data(self):
        self.send_cmd(b'CTRL', 3, 3)
        self.__f_recvData = True
        self.__recv_data_thread = Thread(target=self.__recv_data)
        self.__recv_data_thread.start()

    def stop_send_data(self):
        self.__f_recvData = False
        time.sleep(0.2)
        self.send_cmd(b'CTRL', 3, 4)
        time.sleep(0.1)
        self.stop_acquisition()

    def get_edf_header(self):
        self.send_cmd(b'CTRL', 3, 5)
        buffer = self.__sock.recv(12)

        self.__set_packet_head(struct.unpack('>4sHHI', buffer))

        buffer = b''
        body_len = self.__packet_header['m_dwSize']
        if body_len > 0:
            while len(buffer) < body_len:
                buffer += self.__sock.recv(body_len - len(buffer))
        self.__set_basic_info(struct.unpack('<6If', buffer))

    def __recv_data(self):
        while self.__f_recvData:
            buffer = self.__sock.recv(12)

            self.__set_packet_head(struct.unpack('!4sHHI', buffer))

            buffer = b''
            body_len = self.__packet_header['m_dwSize']
            if body_len > 0:
                while len(buffer) < body_len:
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

    def save_data(self, mark):
        time_stamps = (mark[:, 0] * self.basic_info['nRate']).astype(int)
        tag = mark[:, 1]
        print(time_stamps[-1])
        self.__EEG_data[self.basic_info['nEegChan']] = 0
        for i in range(len(tag)):
            self.__EEG_data[self.basic_info['nEegChan']][time_stamps[i]] = tag[i]

        scipy.io.savemat('./data/2022-9-7.mat', {'data': self.__EEG_data})
        print('save EEG data finish! EEG data shape: ', self.__EEG_data.shape)
