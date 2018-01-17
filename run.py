#!/usr/bin/env python

from cefpython3 import cefpython as cef
from subprocess import Popen
import sys

# Creates the browser window which will show django's page

def main():
    cef.Initialize()
    sys.excepthook = cef.ExceptHook

    args = ['python', 'manage.py', 'runserver']
    with Popen(args) as subprocess:
        cef.CreateBrowserSync(url='localhost:8000', window_title='Hawkings')
        cef.MessageLoop()
        cef.Shutdown()

if __name__ == '__main__':
    main()
