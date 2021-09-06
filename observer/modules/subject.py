from observer.observer import Observer

class Subject:

    def __init__(self, directory, Destination: Observer):
        self.directory = directory
        self.Destination = Destination


    def notify(self):
        self.Destination.get(self.directory)

    def monitor(self):
        pass


    def set_con(self):
        con_info ={
            'directory': self.directory,
            'destination': self.Destination
        }
        return con_info
