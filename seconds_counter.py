import threading
import time

class SecondCounter(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/1000 of a second
    '''
    def __init__(self, interval=0.001):
        # init the thread
        threading.Thread.__init__(self)
        self.interval = interval  # seconds
        # initial value
        self.value = 0
        # controls the while loop in method run
        self.alive = False
        self.valuetoupdate = self.interval
    def run(self):
        '''
        this will run in its own thread via self.start()
        '''
        self.alive = True
        while self.alive:
            time.sleep(self.interval)
            # update count value
            self.value += self.valuetoupdate

    def pause(self):
        self.valuetoupdate = 0

    def resume(self):
        self.valuetoupdate = self.interval

    def peek(self):
        '''
        return the current value
        '''
        return self.value
    def finish(self):
        '''
        close the thread, return final value
        '''
        # stop the while loop in method run
        self.alive = False
        return self.value

##
##https://www.daniweb.com/programming/software-development/code/485072/count-seconds-in-the-background-python
##