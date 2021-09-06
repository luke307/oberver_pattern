class Observer:

    def __init__(self, address, username, password):
        self.address = address
        self.username = username
        self.password = password


    def get(self, filepath):
        self.filepath = filepath
        self._upload(filepath)

    def _upload(self):
        pass