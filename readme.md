# API-TIME-NOW

## Specs

This API aims to print out a timestamp on which the external systems can relay to be synchronized.

## Usage

Call Type API: GET
<br/>
Url: http://1.2.3.4:8080/secret/qwerty/
<br/>

```json
{
  "posix": {
    "millis": 1508452082764,
    "timestamp": 1508452083
  },
  "timezone": "UTC"
}
```
