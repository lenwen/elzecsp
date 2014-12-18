__author__ = 'lennie'
import  time
import threading


class testThread (threading.Thread):
    def __init__(self, threadID, name, counter, settings):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.running = False
        self.settings = settings


    def run(self):
        self.running = True
        while(self.running):
            time.sleep(5)
            if self.settings.screenEnable:
                self.settings.screenEnable = False
            else:
                self.settings.screenEnable = True





