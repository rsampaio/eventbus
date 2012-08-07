import zmq

reply_addr = "tcp://*:7890"
pubsub_addr = "tcp://*:7891"

class Main(Object):
    def __init__(self):
        self.context = zmq.Context()
        self.rep_socket = self.context.socket(zmq.REP)
        self.rep_socket.bind(reply_addr)

        
