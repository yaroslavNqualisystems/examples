from threading import Thread
from cloudshell.cli.helper.singleton import Singleton


class FF(Singleton):
    def __init__(self):
        print('init FF')

class DD(Singleton):
    pass

def do():
    print(FF())
    print(DD())








if __name__ == '__main__':
    Thread(target=do).start()
    Thread(target=do).start()
    Thread(target=do).start()
    Thread(target=do).start()