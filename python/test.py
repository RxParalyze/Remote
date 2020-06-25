import samsungctl

config = {
    "name": "samsungctl",
    "description": "PC",
    "id": "D8:E0:E1:51:F3:F1",
    "host": "192.168.1.42",
    "port": 1515,
    "method": "legacy",
    "timeout": 0,
}

with samsungctl.Remote(config) as remote:
    remote.control("KEY_POWEROFF")