from threading import Thread


class EyeTracker:
    def __init__(self):
        super(EyeTracker, self).__init__()
        self.__recv_data_thread = None

    def connect(self):
        pass

    def disconnect(self):
        pass

    def start_send_data(self):
        self.__recv_data_thread = Thread(target=self.__recv_data)
        self.__recv_data_thread.start()

    def stop_send_data(self):
        pass

    def save_data(self, mark):
        pass

    def __recv_data(self):
        pass
