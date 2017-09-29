import socket
import SMTP
import traceback
from threading import *

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)

        self.sock = socket
        self.addr = address
        self.start()

    def connect(self):
        pass
    def run(self):
        pass

def connect():
    HOST = 'smtp.naver.com'
    PORT = 465
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return client(sock, HOST)

class SMTPClient():
    def __init__(self, sock, server):
        self.sock = sock
        self.smtp = SMTP.SMTP(server)

    def helo(self):
        self.sock.sendall(bytes(self.smtp.helo(), 'utf-8'))

    def sendData(self, subject, content):
        data = self.smtp.data(subject, content)
        self.sock.sendall(bytes(data, 'utf-8'))

