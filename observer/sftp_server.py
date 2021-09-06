import pysftp
from observer.subject import Subject

class FTPserver(Subject):
    
    def upload(self, filepath):
        with pysftp.Connection(self.address, username=self.username, password=self.password) as sftp:
            sftp.put(filepath)