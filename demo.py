from riker.rkclient import RikerClient
from plugins import DebugPlugin, ReConnect, EchoPacket, Gravity, AntiAFK, ChatMessage
#from login import username, password

username = "ownspock"
password = ""

plugins = [DebugPlugin.DebugPlugin, ChatMessage.ChatMessagePlugin]
client = RikerClient(plugins = plugins)
client.start()