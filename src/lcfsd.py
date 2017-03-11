#!/usr/bin/env python3
import sys, os.path
srcdir = os.path.dirname(os.path.abspath(__file__))
sys.path[1:1] = map(os.path.abspath, [os.path.join(srcdir, x) for x in [
		'../lib/fusepy'
	]])

import lcfs
from lcfs.stack import LayerStack, LayerGroup
from lcfs.layers.dummy import DummyBackingLayer
from sys import argv
import logging

logging.basicConfig(level=logging.DEBUG)

args = dict([arg.split('=', 1) if '=' in arg else [arg, True] for arg in argv[2:]])

stack = LayerStack()
stack.add(
		LayerGroup().add(DummyBackingLayer())
	)

fs = lcfs.LCFS(argv[1], stack)
fs.setArgs(args)

fs.run()