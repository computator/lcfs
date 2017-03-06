# base classes
class BaseLayer:
    '''
    Base class for all caching layers.

    Cache layer implementations must inherit from a subclass of `BaseLayerType`
    and a subclass of `BaseDataStrategy` in addition to inheriting from this
    class (or a subclass of this class).
    '''

    def __init__(self, config = []):
        # require this instance to inherit from a subclass of BaseLayerType
        assert isinstance(self, BaseLayerType) and BaseLayerType not in type(self).__bases__
        # require this instance to inherit from a subclass of BaseDataStrategy
        assert isinstance(self, BaseDataStrategy) and BaseDataStrategy not in type(self).__bases__
        self.config = config

class BaseLayerType:
    '''Base class for layer types.'''
    pass

class BaseDataStrategy:
    '''Base class for layer data strategies.'''
    pass

# Storage types
class BackingLayerType(BaseLayerType):
    '''Base class for layers that store data long term.'''
    pass

class CacheLayerType(BaseLayerType):
    '''Base class for layers that cache data temporarily.'''
    pass

# Strategy types
class FullDataStrategy(BaseDataStrategy):
    '''Base class for layers that store entire files.'''
    pass

class PartialDataStrategy(BaseDataStrategy):
    '''
    Base class for layers that store partial files or individual blocks.

    Layers based on this type are allowed to store whole files, but they can
    also choose to only store parts of files or individual blocks.
    '''
    pass

# Layer variations
class PolicyLayer(BaseLayer):
    '''
    Base class for layers that only store data for some files based on a policy.
    '''
    pass