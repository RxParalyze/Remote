import samsungctl
import runController

with samsungctl.Remote(runController.config) as remote:
    #remote.connection.connect()
    remote.control("KEY_POWER")
