from http import HTTPStatus

from flask import Flask, request

app = Flask(__name__)


@app.route("/sms_mo", methods=['POST'])
def sms_mo():
    sms = request.json

    print('Received an SMS from', sms['source'])
    print('Operator:', sms['operator'])
    print('Type:', sms['content']['type'])
    print('Data:', sms['content']['userData'])

    return '', HTTPStatus.NO_CONTENT


@app.route('/dlr', methods=['POST'])
def dlr():
    dr = request.json

    print('Received DLR for message ID', dr['id'])
    print('Result code:', dr['resultCode'])
    print('Operator:', dr['operator'])

    return '', HTTPStatus.NO_CONTENT
