import ftplib
import os
from observer.subject import Subject

class FTPserver(Subject):
    
    def upload(self, filepath):
        file = os.path.basename(filepath)
        with ftplib.FTP(self.address) as ftp:
            ftp.login("Benutzername", "Passwort")
            ftp.login(self.username,self.password)
            ftp.storbinary(f'STOR {file}', open(filepath,'rb'))
