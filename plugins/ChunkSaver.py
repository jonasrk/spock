import sys
from spock.mcp.mcdata import structs
from spock.net.cflags import cflags

class ChunkSaverPlugin:
	def __init__(self, client):
		self.client = client
		client.register_dispatch(self.savechunk, 0x38)


	def savechunk(self, packet):
		pass
'''
			#Map Chunk Bulk
	0x38: (
		("short", "chunk_column_count"),
		("int", "data_size"),
		("bool", "sky_light")),
'''