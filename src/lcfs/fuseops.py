from .operations import OpError
from fuse import Operations, LoggingMixIn, FuseOSError

class FuseOps(LoggingMixIn, Operations):
	def __init__(self, op_mapper):
		self.op_mapper = op_mapper

	def getattr(self, path, fh=None):
		try:
			return self.op_mapper.getattr(path, fh)
		except OpError as e:
			raise FuseOSError(e.errno)