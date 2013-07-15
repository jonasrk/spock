from riker.rkclient import RikerClient
from plugins import DebugPlugin, ReConnect, EchoPacket, Gravity, AntiAFK
#from login import username, password

username = "ownspock"
password = ""

plugins = [DebugPlugin.DebugPlugin]
client = RikerClient(plugins = plugins)
client.start()