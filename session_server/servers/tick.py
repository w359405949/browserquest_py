from gevent import sleep
from gevent.greenlet import Greenlet

import channels
from controllers.controller import Controller
from services.browserquest_pb2 import HealthRequest
from services.browserquest_pb2 import BrowserQuest_Stub
from services.entity_pb2 import EntityService_Stub


class TickServer(Greenlet):


    def run(self):
        while True:
            sleep(5)
            self.hit_points_update()

    def hit_points_update(self):
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)
        entity_service = BrowserQuest_Stub(channels.entity_channel)

        request = GetPlayerIDListRequest()
        controller = Controller()
        id_list = entity_service.GetPlayerIDList(controller, request)
        for id in id_list.ids:
            player = Player()
            player.id = id
            player = entity_service.GetPlayer(controller, player)
            if player.hit_points >= 100:
                continue
            player.hit_points += 5
            if player.hit_points >= 100:
                player.hit_points = 100
            health_request = HealthRequest()
            health_request.hit_points = player.hit_points
            controller = Controller()
            controller.player_ids = [player.id]
            browserquest_stub.hitpoints(controller, health_request)
