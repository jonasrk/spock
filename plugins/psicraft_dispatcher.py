__author__ = 'jonas'
from spock.mcp.mcpacket import Packet

def dispatch_psicraft_command(antwort, client):
	if antwort.decode() == "x-":
		print("old coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))
		client.push(Packet(ident = 0x0B, data = {
						'x': client.position['x'] - 1,
						'y': client.position['y'],
						'z': client.position['z'],
						'on_ground': False,
						'stance': client.position['y'] + 0.11
						}))
		print("new coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))

		pass