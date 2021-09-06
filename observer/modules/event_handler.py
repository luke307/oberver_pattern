from watchdog.events import LoggingEventHandler

class Event(LoggingEventHandler):

    def on_created(self, event):
        pass
