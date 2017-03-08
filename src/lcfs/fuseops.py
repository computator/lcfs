from fuse import Operations, LoggingMixIn, FuseOSError

class FuseOps(LoggingMixIn, Operations):
	pass
