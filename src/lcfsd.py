#!/usr/bin/env python3
import sys, os.path
srcdir = os.path.dirname(os.path.abspath(__file__))
sys.path[1:1] = map(os.path.abspath, [os.path.join(srcdir, x) for x in [
		'../lib/fusepy'
	]])

import logging
import lcfs.stack
from lcfs.layers.base import BaseLayer, BackingLayerType, FullDataStrategy
from lcfs.fuseops import FuseOps
from fuse import FUSE
from sys import argv

class MyLayer(BaseLayer, BackingLayerType, FullDataStrategy):
	pass

logging.basicConfig(level=logging.NOTSET)

cache = lcfs.stack.LayerStack()
cache.add(
		lcfs.stack.LayerGroup().add(
				MyLayer()
			)
	)
logging.debug("Valid: {}".format(cache.valid()))

FUSE(FuseOps(), argv[1], fsname='lcfs', **dict([arg.split('=', 1) if '=' in arg else [arg, True] for arg in argv[2:]]))