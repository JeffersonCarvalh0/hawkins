#!/usr/bin/env python

from cefpython3 import cefpython as cef
from multiprocessing import Process
import manage, sys, subprocess

# Creates the browser window which will show django's server

class Server:
    def __init__(self, process):
        self.server = process

    def myExceptHook(self, type, value, traceback):
        self.server.terminate()
        cef.ExceptHook(type, value, traceback)

def call():
    subprocess.call(['python', 'manage.py', 'runserver'])

def main():
    process = Process(target=call, name='django_server')
    serverInstance = Server(process)
    sys.excepthook = serverInstance.myExceptHook
    serverInstance.server.start()

    cef.Initialize()
    cef.CreateBrowserSync(url='localhost:8000', window_title='Hawkings')
    cef.MessageLoop()
    cef.Shutdown()

    serverInstance.server.terminate()


if __name__ == '__main__':
    main()
