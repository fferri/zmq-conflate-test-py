import sys
import time
import zmq

ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.connect('tcp://127.0.0.1:23000')
#pub.setsockopt(zmq.CONFLATE, 1)

i = 0
while 1:
    msg = f'hello-{i}'
    print(f'sending "{msg}"...')
    pub.send_string(msg)
    time.sleep(0.02)
    i += 1
