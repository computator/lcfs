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
    pass

class LayerGroup:
    '''
    A group of one or more caching layers.

    Block writes are sent to the last layer in a group that will accept it
    based on each layer's policies. Block reads are sent to the first layer in
    a group that has the requested block. Reads and writes may not match any
    layer in a group, in which case they will be handled by one or more other
    groups in the stack.
    '''
    pass