
from google.protobuf.service import RpcChannel

from services.world import WorldServiceImpl

class WorldChannel(RpcChannel):

    def __init__(self):
        self.world_service = WorldServiceImpl()

    def CallMethod(self, method_descriptor, controller,
                   request, response_class, callback):
        return self.world_service.CallMethod(method_descriptor, controller,
                request, callback)
