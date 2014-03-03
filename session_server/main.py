from geventwebsocket import WebSocketServer, Resource
#from servers.ai import AIServer
#from servers.tick import TickServer
from servers.application import BrowserQuestApplication

if __name__ == "__main__":
    #AIServer().start()
    #TickServer().start()
    WebSocketServer(('', 8000), Resource({'/': BrowserQuestApplication})).serve_forever()
