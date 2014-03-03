from random import randint
from gevent import sleep
from gevent.greenlet import Greenlet

from services.browserquest_broadcast_pb2 import MoveRequest

from controllers.controller import Controller

from models import entity as Entity
from models import world as World
import services as Service


class AIServer(Greenlet):

    def run(self):
        while True:
            sleep(5)
            self.mob_active()

    def mob_active(self):
        for mob_id in Entity.objects.mobs:
            if randint(0, 1):
                continue
            mob = Entity.objects.entities.get(mob_id, None)
            if not mob or mob.is_dead:
                continue
            mob_area = World.objects.mob_areas.get(mob.area_id, None)
            if not mob_area:
                continue
            world = World.objects.worlds.get(mob_area.world_id, None)
            if not world:
                continue
            position = World.objects.get_random_position_inside_area(mob_area)
            mob.x = position['x']
            mob.y = position['y']
            move_request = MoveRequest()
            move_request.entity_id = mob.id
            move_request.entity_x = mob.x
            move_request.entity_y = mob.y
            controller = Controller()
            controller.player_ids = World.objects.get_adjacent_player_ids(world, mob)
            Service.objects.browserquest_stub.move(controller, move_request)
