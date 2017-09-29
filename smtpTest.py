import unittest
import socket
import SMTP
import simpleSMTP

from threading import *
class testServer(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        HOST = "127.0.0.1"
        PORT = 4567
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((HOST,PORT))
            sock.listen(1) # backlog; maximam unaccepted connections
        except:
            pass

        while True:
            clientsocket, address = sock.accept()
            client(clientsocket, address)

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()
    def run(self):
        data = self.sock.recv(4096)
        if not data:
            return

        print()
        print("Received, and will be echoed: " + str(data))
        print()
        self.sock.sendall(data)

class Test(unittest.TestCase):
    def setUp(self):
        self.server = testServer()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.connect(('localhost', 4567))
        print()

    def tearDown(self):
        self.sock.close()

    def testHelo(self):
        sock = self.sock
        client = simpleSMTP.SMTPClient(self.sock, "smtp.naver.com")

        client.helo()
        resp = sock.recv(4096)
        assert "HELO" in resp.decode('utf-8')

    def testData(self):
        sock = self.sock
        client = simpleSMTP.SMTPClient(self.sock, "smtp.naver.com")
        client.smtp.source = "abc@abc.com"
        client.smtp.sourceName = "Sender"
        client.smtp.dest = "abc@bbc.com"
        client.smtp.destName = "Receiver"

        client.sendData("Hello", "Hello World\n")
        resp = sock.recv(4096)
        assert 'From: "Sender" <abc@abc.com>\r\n' in resp.decode('utf-8')
        assert 'To: "Receiver" <abc@bbc.com>\r\n' in resp.decode('utf-8')
        assert "Subject: Hello\r\n" in resp.decode('utf-8')
        assert "\r\nHello World\n" in resp.decode('utf-8')
        assert "\r\n.\r\n" in resp.decode('utf-8')



if __name__ == '__main__':
    unittest.main()