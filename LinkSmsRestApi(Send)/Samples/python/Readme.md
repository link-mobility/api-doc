Python SMS Samples
------------------

To retrieve all dependencies, either create a venv or install directly
using

```bash
$ pip install -r requirements.txt
```

Afterwards, configure the parameters of your account in `server_settings.json`.
See `server_settings_example.json` for an example on how to format the configuration.


Run using `./send_sms.py COMMAND MSISDNS`, for example `./send_sms.py send +49123123123`.
For more details, run `./send_sms.py -h`.
