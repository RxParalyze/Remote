import samsungctl

config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "68:27:37:2F:A5:3A",
    "host": "192.168.1.42",
    "port": 1515,
    "method": "websocket",
    "timeout": 0,
}

with samsungctl.Remote(config) as remote:
    remote.connection.connect()
    remote.control("KEY_POWER")