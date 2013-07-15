from spock.mcp.mcdata import structs
from spock.mcp.mcpacket import Packet

class ChatMessagePlugin:
	def __init__(self, client):
		self.client = client
		client.register_dispatch(self.chatmessage, 0x03)

	def chatmessage(self, packet):
		if packet.data['text'] == "[Server] u there?":
			self.client.push(Packet(ident = 0x03, data = {
						'text': "is this real life?"
						}))