SMS MO and DLR Server in Python
-------------------------------

To run the example, first install all dependencies with

```shell script
$ pip install --user -r requirements.txt
```

Afterwards, run the flask server to accept the POST requests with

```shell script
$ export FLASK_APP=sms_server.py
$ flask run --host=0.0.0.0
```
