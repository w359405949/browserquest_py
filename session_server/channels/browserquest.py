import json

from google.protobuf.service import RpcChannel


class BrowserQuestChannel(RpcChannel):
    def __init__(self):
        self.connections = {}

    def CallMethod(self, method_descriptor, controller,
                   request, response_class, done=None):
        request_data = []
        request_data.append(method_descriptor.index)
        for field_descriptor in request.DESCRIPTOR.fields:
            value = getattr(request, field_descriptor.name)
            if field_descriptor.label == 3: # repeated
                request_data.extend(value)
            else:
                request_data.append(getattr(request, field_descriptor.name))
        request_data = json.dumps(request_data)
        for player_id in controller.player_ids:
            print 'send:', request_data, 'to', player_id
            connection = self.connections.get(player_id, None)
            if connection:
                try:
                    connection.send(request_data)
                except: # TODO: do some any other thing
                    print "failed"
