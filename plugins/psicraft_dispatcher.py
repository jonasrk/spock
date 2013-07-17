__author__ = 'jonas'
from spock.mcp.mcpacket import Packet
import json


def dispatch_psicraft_command(antwort, client, komm):
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

	elif antwort.decode() == "x+":
		print("old coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))
		client.push(Packet(ident = 0x0B, data = {
						'x': client.position['x'] + 1,
						'y': client.position['y'],
						'z': client.position['z'],
						'on_ground': False,
						'stance': client.position['y'] + 0.11
						}))
		print("new coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))

	elif antwort.decode() == "z-":
		print("old coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))
		client.push(Packet(ident = 0x0B, data = {
						'x': client.position['x'],
						'y': client.position['y'],
						'z': client.position['z'] - 1,
						'on_ground': False,
						'stance': client.position['y'] + 0.11
						}))
		print("new coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))

	elif antwort.decode() == "z+":
		print("old coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))
		client.push(Packet(ident = 0x0B, data = {
						'x': client.position['x'],
						'y': client.position['y'],
						'z': client.position['z'] + 1,
						'on_ground': False,
						'stance': client.position['y'] + 0.11
						}))
		print("new coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))

	elif antwort.decode() == "query_chunk":
		print("trying to send chunk do webinterface")

		x_chunk = client.position['x'] // 16
		z_chunk = client.position['z'] // 16

		block_types_json = [[[0 for i in range(16)] for i in range(256)] for j in range(16)]

		for i in range (0,16):
				for x in range (0,16):
					for y in range (0,16):
						for z in range (0,16):
							if client.world.columns[(x_chunk, z_chunk)].chunks[i] != None:
								block_types_json[x][y+(16*i)][z] = client.world.columns[(x_chunk, z_chunk)].chunks[i]['block_data'].get(x,y,z)



		bot_block = [client.position['x'], client.position['y'], client.position['z']]

		komm.send(("%s\r\n\r" % json.dumps([bot_block, block_types_json])).encode())