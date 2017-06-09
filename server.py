import socket
import threading
from common import send_msg, recv_msg

class Server:
    def __init__(self, host=None, port=None):
        self.msg_size = 1024
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            client, address = self.sock.accept()
            client.settimeout(60)
            ct = threading.Thread(target = self.listen_client, args = (client, address))
            ct.start()

    def listen_client(self, client, address):

        while True:
            request = self._get_request(client)
            print("request: {}".format(request))

            if request:
                response = self._generate_responce(request)
                send_msg(client, response)
            else:
                client.close()
                return False

    def _generate_responce(self, request):
        return "adsasdfsdf"


    def _get_request(self, client):
        return recv_msg(client)

if __name__ == "__main__":

    Server("", 9999).listen()