import configparser

config = configparser.ConfigParser()
config.read('./config.ini')


def get_host():
    return config.get('default', 'host')


def get_port():
    return config.getint('default', 'port')


def get_websocket_url():
    return config.get('default', 'websocket_url')
