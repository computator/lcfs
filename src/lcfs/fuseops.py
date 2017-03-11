from fuse import Operations, LoggingMixIn, FuseOSError

class FuseOps(LoggingMixIn, Operations):
	def __init__(self, op_mapper):
		self.op_mapper = op_mapper