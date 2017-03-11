from lcfs.stack import LayerStack
from lcfs.operations import OpMapper
from lcfs.fuseops import FuseOps
from fuse import FUSE
import logging

log = logging.getLogger(__name__)

class LCFS:
	'''An instance of a lcfs filesystem.'''

	def __init__(self, mountpoint, stack):
		if not isinstance(stack, LayerStack):
			raise TypeError("stack is not an instance of LayerStack")
		if not stack.valid():
			raise Exception("Invalid LayerStack")
		log.debug("The specified LayerStack is valid")
		self.stack = stack
		self.mp = mountpoint
		log.info("Mountpoint set to %s", mountpoint)
		self.op_mapper = OpMapper(self.mp, self.stack)
		self.fuse_op_handler = FuseOps(self.op_mapper)

	def setArgs(self, fuse_args):
		'''Set the fuse arguments for the filesystem.'''
		log.debug("FUSE args set to %s", fuse_args)
		self.fuse_args = fuse_args

	def run(self):
		'''
		Start the lcfs filesystem.

		This method will not return until the filesystem is unmounted, either
		normally or due to an error.
		'''
		return FUSE(self.fuse_op_handler, self.mp, fsname="lcfs", **self.fuse_args)