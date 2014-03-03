
from google.protobuf.service import RpcChannel

from services.entity import EntityServiceImp

class EntityChannel(RpcChannel):

    def __init__(self):
        self.entity_service = EntityServiceImp()

    def CallMethod(self, method_descriptor, controller,
                   request, response_class, callback):
        return self.entity_service.CallMethod(method_descriptor, controller,
                request, callback)
