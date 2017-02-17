from .layers.base import CacheLayer

class LayerStack:
    '''
    A stack of one or more `LayerGroup`s that a lcfs filesystem maps to.

    Normally a lcfs filesystem will have multiple layer groups in which each
    group corresponds to a specific capacity/latency level. Each group can have
    multiple caching layers to implement multiple caching strategies at each
    capacity/latency level.

    Blocks will be written to every group in a stack, and read from the first
    group that has the requested block.
    '''

    def __init__(self):
        self._groups = []

    def add(self, group):
        '''Add a new group to the stack'''
        assert isinstance(group, LayerGroup)
        assert group not in self._groups
        self._groups.append(group)
        return self

class LayerGroup:
    '''
    A group of one or more caching layers.

    Block writes are sent to the last layer in a group that will accept it
    based on each layer's policies. Block reads are sent to the first layer in
    a group that has the requested block. Reads and writes may not match any
    layer in a group, in which case they will be handled by one or more other
    groups in the stack.
    '''

    def __init__(self):
        self._layers = []

    def add(self, layer):
        '''Add a new layer to the group'''
        assert isinstance(layer, CacheLayer)
        assert layer not in self._layers
        self._layers.append(layer)
        return self