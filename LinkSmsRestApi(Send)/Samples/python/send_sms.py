#!env python3

from argparse import ArgumentParser

from requests import post
from requests.auth import HTTPBasicAuth

server = None
user = None
password = None


def do_request(path, data):
    url = f'{server}{path}'
    print('sending to ', url)
    print(post(url, json=data, auth=HTTPBasicAuth(user, password)))


def send_single_sms(msisdns):
    do_request('/sms/send', {
        "source": "LINK",
        "destination": msisdns[0],
        "userData": "Hello world",
        "platformId": "0",
        "platformPartnerId": "0",
        "useDeliveryReport": False})


def send_bulk_sms(msisdns):
    pass


def send_payment_sms(msisdns):
    pass


commands = {
    'send': send_single_sms,
    'send_bulk': send_bulk_sms,
    'send_payment': send_payment_sms
}


def main():
    parser = ArgumentParser()

    parser.add_argument('command', choices=commands.keys(), metavar='COMMAND',
                        help='Available commands: %(choices)s')
    parser.add_argument('msisdns', nargs='+', metavar='MSISDNS',
                        help='One or more MSISDNs to test sending with')

    args = parser.parse_args()

    try:
        with open('./server_settings.txt') as server_settings:
            global server
            global user
            global password
            server, user, password = [l.strip() for l in server_settings.readlines()]
    except FileNotFoundError:
        print('File server_settings.txt not found!')

    commands[args.command](args.msisdns)


if __name__ == '__main__':
    main()
