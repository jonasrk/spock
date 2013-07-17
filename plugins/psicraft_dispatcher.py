__author__ = 'jonas'
from spock.mcp.mcpacket import Packet
import json


def dispatch_psicraft_command(antwort, client, komm):
	if antwort.decode() == "x-":
		psicraft_xminus(client, komm)
	elif antwort.decode() == "x+":
		psicraft_xplus(client, komm)
	elif antwort.decode() == "z-":
		psicraft_zminus(client, komm)
	elif antwort.decode() == "z+":
		psicraft_zplus(client, komm)
	elif antwort.decode() == "query_chunk":
		psicraft_query_chunk(client, komm)
	elif antwort.decode() == "query_bot":
		psicraft_query_bot(client, komm)

def psicraft_xminus(client, komm):
	print("old coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))
	client.push(Packet(ident = 0x0B, data = {
					'x': client.position['x'] - 1,
					'y': client.position['y'],
					'z': client.position['z'],
					'on_ground': False,
					'stance': client.position['y'] + 0.11
					}))
	print("new coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))

def psicraft_xplus(client, komm):
	print("old coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))
	client.push(Packet(ident = 0x0B, data = {
					'x': client.position['x'] + 1,
					'y': client.position['y'],
					'z': client.position['z'],
					'on_ground': False,
					'stance': client.position['y'] + 0.11
					}))
	print("new coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))

def psicraft_zminus(client, komm):
	print("old coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))
	client.push(Packet(ident = 0x0B, data = {
					'x': client.position['x'],
					'y': client.position['y'],
					'z': client.position['z'] - 1,
					'on_ground': False,
					'stance': client.position['y'] + 0.11
					}))
	print("new coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))

def psicraft_zplus(client, komm):
	print("old coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))
	client.push(Packet(ident = 0x0B, data = {
					'x': client.position['x'],
					'y': client.position['y'],
					'z': client.position['z'] + 1,
					'on_ground': False,
					'stance': client.position['y'] + 0.11
					}))
	print("new coords -> x: %s y: %s z: %s" % (client.position['x'], client.position['y'], client.position['z']))

def psicraft_query_chunk(client, komm):
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

	komm.send(json.dumps([bot_block, block_types_json]).encode())

def psicraft_query_bot(client, komm):
	print("trying to send bot_block do webinterface")

	bot_block = [client.position['x'], client.position['y'], client.position['z']]

	komm.send(json.dumps(bot_block).encode())