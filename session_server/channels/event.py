
from google.protobuf.service import RpcChannel
from services.browserquest_event import BrowserQuestEventService


class EventChannel(RpcChannel):

    def __init__(self):
        self.event_service = BrowserQuestEventService()

    def CallMethod(self, method_descriptor, controller,
            request, response_class, callback):

        self.event_service.CallMethod(method_descriptor, controller, request, callback)
