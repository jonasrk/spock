import threading
import spock.net.client
from spock.net.cflags import cflags
from spock.net.timer import ThreadedTimer
from spock.smpmap import World
from riker.packet_queue import PacketQueue

class RikerClient(spock.net.client.Client):
	def __init__(self, plugins):
		self.plugins = plugins
		self.world = World()
		spock.net.client.Client.__init__(self, plugins = plugins, world = self.world)
		self.move_queue = PacketQueue()

		self.stop_event = threading.Event()
		self.register_dispatch(self.start_timer, 0x01)
		self.register_handler(self.stop_timer, cflags['SOCKET_ERR'], cflags['SOCKET_HUP'], cflags['KILL_EVENT'])
		#self.register_handler(self.s.close(), cflags['SOCKET_ERR'], cflags['SOCKET_HUP'], cflags['KILL_EVENT'])
		self.register_dispatch(self.stop_timer, 0xFF)

	def start_timer(self, *args):
		ThreadedTimer(self.stop_event, .05, self._send_move, -1).start()

	def stop_timer(self, *args):
		self.stop_event.set()
		self.stop_event = threading.Event()

	def push_move(self, packet):
		self.move_queue.push(packet)

	def _send_move(self):
		if self.move_queue:
			self.push(self.move_queue.pop())

	def move_to(x, y, z):
		pass