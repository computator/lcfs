import errno
import stat

class OpError(Exception):
	def __init__(self, errno):
		assert isinstance(errno, int)
		self.errno = errno

class OpMapper:
	'''Maps filesystem operations to a `LayerStack`.'''
	def __init__(self, stack):
		self.stack = stack

	def getattr(self, path, fh=None):
		if path != '/':
			raise OpError(errno.ENOENT)
		return dict(st_mode=stat.S_IFDIR|0o755, st_nlink=2)