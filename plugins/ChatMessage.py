from spock.mcp.mcdata import structs
from spock.mcp.mcpacket import Packet
import socket

class ChatMessagePlugin:
	def __init__(self, client):
		self.client = client
		client.register_dispatch(self.chatmessage, 0x03)

	def chatmessage(self, packet):
		if packet.data['text'] == "[Server] u there?":
			self.client.push(Packet(ident = 0x03, data = {
						'text': "is this real life?"
						}))

		if packet.data['text'] == "<moejoe> do something!":
			print("x : ", self.client.position['x'])
			self.client.push(Packet(ident = 0x03, data = {
						'text': "I'll try!"
						}))
			self.client.push(Packet(ident = 0x0C, data = {
						'yaw': 75,
						'pitch': 45,
						'on_ground': False
						}))
			self.client.push(Packet(ident = 0x0B, data = {
						'x': self.client.position['x'] + 1,
						'y': self.client.position['y'],
						'z': self.client.position['z'],
						'on_ground': False,
						'stance': self.client.position['y'] + 0.11
						}))
			ip = 'localhost'
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip, 50000))

			nachricht = "psicraft? can you read me?"
			s.send(nachricht.encode())
			antwort = s.recv(1024)
			print("[%s] %s" % (ip,antwort.decode()))
			s.close()