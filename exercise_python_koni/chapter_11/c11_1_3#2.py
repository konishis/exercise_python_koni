import threading


def hello(arg):
    print(arg)


threading.Thread(target=hello, args=("world",)).start()