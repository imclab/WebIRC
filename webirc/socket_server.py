from txwebsockets import BasicOperations
import json

class SocketServer(BasicOperations):
    def on_read(self, line):
        data = json.loads(line[1:])
        self.bot_factory.send_msg(data['message'])
    
    def on_connect(self):
        print "connected. writeHandler is ", self.writeHandler  

    def on_close(self, r):
        self.bot_factory.close_connections()
        print "connection closed: ", r 

    def after_connection(self):
        self._out('out!after_connection')
        
    def send(self, data):
        self._out(str(json.dumps(data)))
