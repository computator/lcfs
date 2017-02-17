class BaseCache:
    '''
    Base class for all caching layers.

    Cache layer implementations should not directly inherit from this class.
    Instead, they should inherit one of the strategy based subclasses.
    '''

    def __init__(self, config = []):
        self.config = config

class FullCache(BaseCache):
    '''
    Base class for layers that only cache whole files.

    The bottom layer of the layer stack must be an instance of this layer type
    so that data is not lost due to only storing part of a file.
    '''
    pass

class PartialCache(BaseCache):
    '''
    Base class for layers that cache sections of files or individual blocks.

    Layers based on this cache are allowed to cache whole files, but they can
    also choose to only cache parts of files or individual blocks.
    '''
    pass