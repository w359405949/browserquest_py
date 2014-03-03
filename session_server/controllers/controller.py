from google.protobuf.service import RpcController

class Controller(RpcController):

    def __init__(self, *args, **kwargs):
        super(Controller, self).__init__(*args, **kwargs)

        self.is_failed = False
        self.error_text = ""
        self.is_cancelled = False
        self.cancel_callback = None
        self.player_ids = []
        self.connection = None
        self.browserquest_broadcast_stub= None
        self.browserquest_stub = None

    def Reset(self):
        self.is_failed = False
        self.error_text = ""
        self.is_cancelled = False
        self.cancel_callback = None

    def Failed(self):
        return self.is_failed

    def ErrorText(self):
        return self.error_text

    def StartCancel(self):
        self.is_cancelled = True

    def SetFailed(self, reason):
        self.is_failed = True
        self.error_text = reason

    def IsCancelled(self):
        return self.is_cancelled

    def NotifiOnCancel(self, callback):
        self.cancel_callback = callback
