#!/usr/bin/env python

from cefpython3 import cefpython as cef
from subprocess import Popen
import sys, os, signal

# Creates the browser window which will show django's server

SIGNAL = signal.CTRL_C_EVENT if os.name == 'nt' else signal.SIGINT

class Server:
    def __init__(self, process):
        self.server = process

    def myExceptHook(self, type, value, traceback):
        os.kill(self.server.pid, SIGNAL)
        cef.ExceptHook(type, value, traceback)

def main():
    args = ['python', 'manage.py', 'runserver']
    process = Popen(args)
    serverInstance = Server(process)
    sys.excepthook = serverInstance.myExceptHook

    cef.Initialize()
    cef.CreateBrowserSync(url='localhost:8000', window_title='Hawkings')
    cef.MessageLoop()
    cef.Shutdown()

    os.kill(serverInstance.server.pid, SIGNAL)


if __name__ == '__main__':
    main()
