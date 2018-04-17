import sys
import time
import zmq

ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.setsockopt(zmq.CONFLATE, 1)
sub.connect('tcp://127.0.0.1:24000')
sub.subscribe('hello-')

while 1:
    while sub.poll(0):
        msg = sub.recv_string()
        print(f'received "{msg}"')
        # simulate a busy receiver here
        time.sleep(1)
    time.sleep(2)
