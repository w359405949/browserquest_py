import json
from geventwebsocket import WebSocketApplication
from controllers.controller import Controller
from services.browserquest import BrowserQuestImpl

class BrowserQuestApplication(WebSocketApplication):
    browserquest = BrowserQuestImpl()

    def __init__(self, *args, **kwargs):
        super(BrowserQuestApplication, self).__init__(*args, **kwargs)
        self.connection = None
        self.environ = {}

    def on_open(self):
        self.ws.send("go")
        self.connection = self.ws

    def on_message(self, message):
        if message is None:
            return
        print "data:", message
        request_data = json.loads(message)
        method_descriptor = self.browserquest.DESCRIPTOR.methods[request_data[0]]
        request_class = self.browserquest.GetRequestClass(method_descriptor)
        request = request_class()
        for index in xrange(1, len(request_data)):
            field_descriptor = request_class.DESCRIPTOR.fields_by_number[index]
            if field_descriptor.label == 3: # repeated TODO: only WHO enter this
                field = getattr(request, field_descriptor.name)
                field.extend(request_data[index:])
                break
            else:
                setattr(request, field_descriptor.name, request_data[index])

        controller = Controller()
        controller.connection = self.connection
        controller.environ = self.environ
        self.browserquest.CallMethod(method_descriptor, controller, request, None)

    def on_close(self, reason):
        self.connection = None
        print reason
