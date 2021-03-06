import sys
import time
import logging
from watchdog.observers import Observer

from observer.event_handler import Event
from observer.subject import Subject


class ObservedDir(Subject):

    def monitor(self):
        event_handler = Event()
        observer = Observer()

        logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

        observer.schedule(event_handler, self.directory)
        
        observer.start()

        try:
            while True:
                time.sleep(1)
        finally:

            observer.join()
