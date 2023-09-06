from threading import Thread

class MoverThread(Thread):
    def __init__(self, callback):
        self.__thread = Thread(target=callback)
        self.__callback = callback
    
    def is_running(self) -> bool:
        if self.__thread and self.__thread.is_alive():return True
            
    def run(self):
        self.__thread = Thread(target=self.__callback)
        self.__thread.daemon = True
        self.__thread.start()