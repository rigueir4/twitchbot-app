import socket
import requests
import logging
from datetime import date


class TwitchBot:
    def __init__(self):
        self.server = 'irc.chat.twitch.tv'
        self.port = 6667
        self.nickname = 'o_bot_da_livemode'
        self.token = 'oauth:tmrtfxymh0sd1etr60syk5jrpjh88p'
        self.channel = '#casimito'
        self.isRunning = False
        self.mustRun = False


    def runthebot(self):
        while self.mustRun == True:
            self.isRunning = True
            resp = self.sock.recv(2048).decode('utf-8')
            if resp.startswith('PING'):
                self.sock.send("PONG\n".encode('utf-8'))

            elif len(resp) > 0:
                logging.info(resp)

    def start_bot(self):
        self.mustRun=True
        self.sock = socket.socket()
        sock = self.sock
        sock.connect((self.server, self.port))

        sock.send(f"PASS {self.token}\n".encode('utf-8'))
        sock.send(f"NICK {self.nickname}\n".encode('utf-8'))
        sock.send(f"JOIN {self.channel}\n".encode('utf-8'))
        self.sock = sock 
        #2048 é o tamanho do buffer em bytes
        resp = sock.recv(2048).decode('utf-8')
        hoje = date.today().strftime("%b-%d-%Y")
        logging.basicConfig(level=logging.DEBUG,
                            format = '%(asctime)s - %(message)s',
                            datefmt = '%Y-%m-%d_%H:%M:%S',
                            handlers = [logging.FileHandler(f'twitchchat-{hoje}.log', encoding='utf-8')])

        return self.runthebot()

    def stop_bot(self):
        self.mustRun = False
        if self.isRunning == True:
            print('deu alguma merda ai')
            self.mustRun = False

    def check_bot(self):
        return str(self.isRunning)

if __name__ == '__main__':
    TwitchBot()
