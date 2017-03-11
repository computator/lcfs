from .operations import OpError
from fuse import Operations, LoggingMixIn, FuseOSError

def map_err(func):
    def wrap(*args):
        try:
            return func(*args)
        except OpError as e:
            raise FuseOSError(e.errno)

    return wrap

class FuseOps(LoggingMixIn, Operations):
    def __init__(self, op_mapper):
        self.op_mapper = op_mapper

    @map_err
    def getattr(self, path, fh=None):
        return self.op_mapper.getattr(path, fh)

    @map_err
    def readdir(self, path, fh):
        return self.op_mapper.readdir(path, fh)