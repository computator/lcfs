from lcfs.layers.base import BaseLayer, BackingLayerType, CacheLayerType, FullDataStrategy

class DummyBackingLayer(BaseLayer, BackingLayerType, FullDataStrategy):
    pass

class DummyCachingLayer(BaseLayer, CacheLayerType, FullDataStrategy):
    pass