import multiprocessing
from observer.ftp_server import FTPserver
from observer.observed_dir import ObservedDir


if __name__ == '__main__':
    server_1 = FTPserver('127.0.0.1', 'trainee', 'trainee')
    observed_dir_1 = ObservedDir('c/dir', server_1)
    n1 = multiprocessing.Process(target=observed_dir_1.monitor)
