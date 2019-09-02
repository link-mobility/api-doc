#!env python3

from argparse import ArgumentParser
from collections import namedtuple

from requests import post
from requests.auth import HTTPBasicAuth


class SmsSender(object):

    def __init__(self, server, user, password, msisdns):
        self.server = server
        self.auth = HTTPBasicAuth(user, password)
        self.msisdns = msisdns

    def do_request(self, path, data):
        response = post(self.server + path, json=data, auth=self.auth)
        print(response)

    def send_single_sms(self):
        self.do_request('/sms/send', {
            "source": "LINK",
            "destination": self.msisdns[0],
            "userData": "Hello world",
            "platformId": "0",
            "platformPartnerId": "0",
            "useDeliveryReport": False})

    def send_bulk_sms(self):
        pass

    def send_payment_sms(self):
        pass

    def execute(self, command):
        commands = {
        'send': self.send_single_sms,
        'send_bulk': self.send_bulk_sms,
        'send_payment': self.send_payment_sms
        }
        commands[command]()


def main():
    parser = ArgumentParser()

    parser.add_argument('command',
                        choices=['send', 'send_bulk', 'send_payment'],
                        metavar='COMMAND',
                        help='Available commands: %(choices)s')
    parser.add_argument('msisdns',
                        nargs='+',
                        metavar='MSISDNS',
                        help='One or more MSISDNs to test sending with')

    args = parser.parse_args()


    try:
        with open('./server_settings.txt') as server_settings:
            config = [l.strip() for l in server_settings.readlines()]
    except FileNotFoundError:
        print('File server_settings.txt not found!')

    sms_sender = SmsSender(config[0], config[1], config[2], args.msisdns)
    sms_sender.execute(args.command)


if __name__ == '__main__':
    main()
