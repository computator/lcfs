class OpMapper:
	'''Maps filesystem operations from a mountpoint to a `LayerStack`.'''
	def __init__(self, mountpoint, stack):
		self.mp = mountpoint
		self.stack = stack