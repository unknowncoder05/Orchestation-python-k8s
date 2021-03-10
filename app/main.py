import time
import threading

class effective_worker():
    name:str = ""
    main_number:int = 1
    effectiveness:float = 1
    working:bool = False
    debug:bool = False

    _last_multiple = 0
    _threads = []
    def __init__(self,name:str,main_number:int, effectiveness:float = 1, **kwargs):
        self.main_number = main_number
        self.name = name
        self.effectiveness = effectiveness
        self.debug=kwargs.get("debug",False)
        if(self.debug):
            print(f"New Worker! {name} job {main_number}")
    def start_work(self):
        self.working = True
        while True:
            time.sleep(self.effectiveness)
            self._last_multiple += self.main_number
            if(self.debug):
                print(self._last_multiple,self.working)
            if(self.working == False):
                break
    def thread_work(self):
        t=threading.Thread(target=w.start_work)
        self._threads.append(t)
        t.start()
    def thread_stop(self):
        self.working = False
        for t in self._threads:
            t.join()
jobs = [2,4,7,10]
workers = []
w = effective_worker("karl",jobs[0],debug = True)
workers.append(w)


workers[0].thread_work()
time.sleep(5)
#workers[0].thread_stop()