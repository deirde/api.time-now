# API.TIMER.WEBFORYOU.TV #

Specs
-----
This API aims to print out a timestamp on which the external systems can relay to be synchronized.

Update dependecies
-----
```pip3 install setuptools```

```pip3 install -r requirements```

--OR--

```python3.5 -m pip install setuptools```

```python3.5 -m pip install -r requirements```

Run with output in console
-----
```python3.5 bootstrap.py```

Run as background process with output appended to file
-----
```nohup python3.5 bootstrap.py &```

Usage
-----
Call Type API: GET
<br/>
Url: http://1.2.3.4:8080/secret/qwerty/
<br/>
<br/>
API answer:
```json
{
    "posix": {
        "millis": 1508452082764,
        "timestamp": 1508452083
    },
    "timezone": "UTC"
}
```