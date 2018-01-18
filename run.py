#!/usr/bin/env python

from cefpython3 import cefpython as cef
from subprocess import Popen
import sys, os, signal

# Creates the browser window which will show django's page

SIGNAL = signal.CTRL_C_EVENT if os.name == 'nt' else signal.SIGINT

class ExceptHookWrapper(object):
    '''
        With this class, the django's server processes will be killed if an
        exception is raised and not caught.
    '''
    def __init__(self, process):
        self.process = process

    def myExceptHook(self, type, value, traceback):
        os.kill(self.process.pid, SIGNAL)
        cef.ExceptHook(type, value, traceback) # leave the rest of the job to cef

class LoadHandler(object):
    '''
        Checks if the page isn't blank after cef window initializes, because it
        usally does before django's server is up and running, then reload the
        page if necessary.
    '''
    def OnLoadingStateChange(self, browser, is_loading, **_):
        if not is_loading:
            if browser.GetUrl() == 'data:text/html,chromewebdata':
                browser.Reload()

def main():
    args = ['python', 'manage.py', 'runserver']
    subprocess = Popen(args)
    exceptHandler = ExceptHookWrapper(subprocess)
    sys.excepthook = exceptHandler.myExceptHook

    cef.Initialize(
        settings={
            'context_menu' : {
                'enabled' : True,
                'navigation' : True,
                'print' : False,
                'view_source' : False,
                'external_browser' : False,
                'devtools' : False,
            }
        }
    )

    browser = cef.CreateBrowserSync(url='localhost:8000', window_title='Hawkings',)
    browser.SetClientHandler(LoadHandler())
    cef.MessageLoop()
    cef.Shutdown()

    os.kill(exceptHandler.process.pid, SIGNAL)

if __name__ == '__main__':
    main()
