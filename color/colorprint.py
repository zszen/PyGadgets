class cc:
    black = '\033[0;30m'
    red = '\033[0;31m'
    green = '\033[0;32m'
    yellow = '\033[0;33m'
    blue = '\033[0;34m'
    purple = '\033[0;35m'
    cyan = '\033[0;36m'
    white = '\033[0;37m'
    org = '\033[0m'
    def __init__(self):
        pass

    @staticmethod
    def print(str, color):
        print(f'{color}{str}{cc.org}')
