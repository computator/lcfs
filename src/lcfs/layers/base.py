class CacheLayer:
    '''
    Base class for all caching layers.

    Cache layer implementations should not directly inherit from this class.
    Instead, they should inherit one of the strategy based subclasses.
    '''

    def __init__(self, config = []):
        self.config = config

class FullCacheLayer(CacheLayer):
    '''
    Base class for layers that cache everything.

    The bottom layer of the layer stack must be an instance of this layer type
    so that data is not lost due to only storing part of a file.
    '''
    pass

class PolicyCacheLayer(CacheLayer):
    '''
    Base class for layers that only cache some data based on a policy.

    Cache layer implementations should not directly inherit from this class.
    Instead, they should inherit one of the strategy based subclasses.
    '''
    pass

class FileCacheLayer(PolicyCacheLayer):
    '''
    Base class for layers that cache entire files.
    '''
    pass

class PartialCacheLayer(PolicyCacheLayer):
    '''
    Base class for layers that cache partial files or individual blocks.

    Layers based on this cache are allowed to cache whole files, but they can
    also choose to only cache parts of files or individual blocks.
    '''
    pass