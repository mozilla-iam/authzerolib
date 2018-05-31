# authozero library

This is a super simple and basic Auth0 Python client library.

You can also find it here: https://pypi.python.org/pypi/authzerolib

# Quickstart

```
from authzero import AuthZero

config = {'client_id': 'AAAA', 'client_secret': 'BBBB', 'uri': 'localhost'}
az = AuthZero(config)
ret = az.get_rules()
...
```

See `authzerolib.py` for a list of functions.


## Options

- `AuthZero.access_token_auto_renew bool` if true, the library will attempt to automatically renew access_tokens
- `AuthZero.access_token_auto_renew_leeway int` in seconds, will renew the access token before it expires with that
  amount of time buffer
