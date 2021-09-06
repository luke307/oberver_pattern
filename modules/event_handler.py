from watchdog.events import LoggingEventHandler

from observer.subject import Subject


class Event(LoggingEventHandler):

    def on_created(self, event):
        Subject.notify()
        
