import sys
import time
import zmq

ctx = zmq.Context()
xpub = ctx.socket(zmq.XPUB)
xpub.bind('tcp://127.0.0.1:24000')
xsub = ctx.socket(zmq.XSUB)
xsub.bind('tcp://127.0.0.1:23000')
zmq.proxy(xpub, xsub)
