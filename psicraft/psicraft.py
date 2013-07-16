import socket
from bottle import route, run, template, static_file
import json
import time
import datetime

layers = 16 # 4 layers equal 1kb that are transferred to the webinterface




@route('/query_chunk')
def query_chunk():
	ip = 'localhost'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, 50050))
	message = "query_chunk"
	s.send(message.encode())
	data = ""
	while True:
		data1 = s.recv(4)

		if not data1:
			s.close()
			break
		data += data1.decode()

	chunk = json.loads(data)

	web_chunk = [[[[0, 0] for i in range(16)] for j in range(256)] for k in range(16)]

	for x in range(16):
		for y in range(256):
			for z in range(16):
				web_chunk[x][y][z] = chunk[x][y][z]


	print("got it! block_type 8 28 8 is: %s" % chunk[8][200][8])
	s.close()

	return json.dumps([web_chunk, 1, layers])

@route('/connect/<command>')
def connect_to_bot(command):
	ip = 'localhost'
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, 50042))
	message = command
	s.send(message.encode())
	s.close()


@route('/bot')
def commence_webinterface():
    return template('psicraft_webinterface')


@route('/button/<command>')
def button(command):
    tel = telnetlib.Telnet("localhost", 9393)
    tel.write("%s\r\n" % command)
    bots_answer = tel.read_until("\r\n\r")
    tel.close()
    time_now = time.time()
    format_time = datetime.datetime.fromtimestamp(time_now).strftime('%Y-%m-%d %H:%M:%S')
    return "Bot <'{0}'> : '{1}'".format(format_time, bots_answer)


#@route('/query_chunk')
#def query_chunk():
#    tel = telnetlib.Telnet("localhost", 9393)
#    tel.write("q9bl\r\n")
#    text = tel.read_until("\r\n\r") #command does currently not get displayed for queries
#
#    bot_block = json.loads(tel.read_until("\r\n\r").strip())
#
#    chunk_list = list()
#    for i in range(0, 128):
#        next_chunk_part = tel.read_until("\r\n\r")
#        next_chunk_part = next_chunk_part.strip()
#        chunk_list.extend(json.loads(next_chunk_part))
#
#    tel.close()
#
#    chunk = [[[[0, 0] for i in range(16)] for j in range(256)] for k in range(16)]
#
#    for x in range(16):
#        for y in range(256):
#            for z in range(16):
#                chunk[x][y][z] = chunk_list[y * 16 * 16 + z * 16 + x]
#
#    bot_height = bot_block[1]
#
#    web_chunk = [[[[0, 0] for i in range(16)] for j in range(layers)] for k in range(16)]
#
#    for x in range(16):
#        for y in range(layers):
#            for z in range(16):
#                web_chunk[x][y][z] = chunk[x][bot_height - ((layers - 1) / 2) + y][z]
#
#    return json.dumps([web_chunk, bot_block, layers])

@route('/query_bot')
def query_bot():
    tel = telnetlib.Telnet("localhost", 9393)
    tel.write("send_bot_position\r\n")
    text = tel.read_until("\r\n\r") #command does currently not get displayed for queries

    bot_block = json.loads(tel.read_until("\r\n\r").strip())

    return json.dumps([bot_block, layers])


@route('/fewer_layers')
def fewer_layers():
    global layers
    layers = layers - 1
    return str(layers)

@route('/more_layers')
def more_layers():
    global layers
    layers = layers + 1
    return str(layers)




@route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename, root='./')


run(host='localhost', port=8080, debug=True)