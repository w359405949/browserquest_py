from browserquest_pb2 import WelcomeRequest
from browserquest_pb2 import SpawnRequest
from browserquest_pb2 import DamageRequest
from browserquest_pb2 import ListRequest
from browserquest_pb2 import BrowserQuest
from browserquest_pb2 import BrowserQuest_Stub


from entity_pb2 import Player
from entity_pb2 import Entity

import world_service_pb2
from world_service_pb2 import WorldService_Stub
from entity_service_pb2 import EntityService_Stub

from event_service_pb2 import PlayerLoginedEvent
from event_service_pb2 import EventService_Stub

from controllers.controller import Controller
import channels


class BrowserQuestImpl(BrowserQuest):

    def hello(self, controller, request, callback):
        world_service = WorldService_Stub(channels.world_channel)
        event_service = EventService_Stub(channels.event_channel)
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)
        entity_service = EntityService_Stub(channels.entity_channel)

        _player = Player()
        _player.name = request.name
        player = entity_service.GetPlayer(controller, _player)
        if not player:
            player = entity_service.CreatePlayer(controller, _player)
            player.armor = 1
            player.weapon = 1
            entity_service.UpdateEntity(controller, player)

        # regist connection
        connections = channels.browserquest_channel.connections
        connections[player.id] = controller.connection
        controller.environ['player_id'] = player.id

        event_controller = Controller()
        player_logined_event = PlayerLoginedEvent()
        player_logined_event.player_id = player.id
        event_service.PlayerLogined(event_controller, player_logined_event)

        player_join_request = world_service_pb2.PlayerJoinRequest()
        player_join_request.player_id = player.id
        player_join_response = world_service.PlayerJoin(controller, player_join_request)

        welcome = WelcomeRequest()
        welcome.player_id = player.id
        welcome.name = request.name
        welcome.x = player_join_response.x
        welcome.y = player_join_response.y
        welcome.hitpoints = player_join_response.hitpoints
        controller.player_ids = [player_join_response.player_id]
        browserquest_stub.welcome(controller, welcome)

    def who(self, controller, request, callback):
        entity_service = EntityService_Stub(channels.entity_channel)
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)

        for entity_id in request.entity_ids:
            entity = Entity()
            entity.id = entity_id
            entity = entity_service.GetEntity(controller, entity)
            if entity and not getattr(entity, 'is_dead', False):
                spawn = SpawnRequest()
                spawn.entity_id = entity.id
                spawn.kind = entity.kind
                spawn.x = entity.x
                spawn.y = entity.y
                spawn.orientation = entity.orientation
                spawn.armor = entity.armor
                spawn.weapon = entity.weapon
                spawn.name = getattr(entity, 'name', '')
                controller.player_ids = [controller.environ['player_id']]
                browserquest_stub.spawn(controller, spawn)

    def move(self, controller, request, callback):
        world_service = WorldService_Stub(channels.world_channel)

        move_request = world_service_pb2.MoveRequest()
        move_request.entity_id = controller.environ['player_id']
        move_request.x = request.entity_x
        move_request.y = request.entity_y
        world_service.Move(controller, move_request)

    def check(self, controller, request, callback):
        world_service = WorldService_Stub(channels.world_channel)

        check_request = world_service_pb2.CheckRequest()
        check_request.entity_id = controller.environ['player_id']
        check_request.checkpoint = request.checkpoint
        world_service.Check(controller, check_request)

    def zone(self, controller, request, callback):
        world_service = WorldService_Stub(channels.world_channel)
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)

        zone_request = world_service_pb2.ZoneRequest()
        zone_request.entity_id = controller.environ['player_id']
        world_service.Zone(controller, zone_request)

        player = Player()
        player.id = controller.environ['player_id']
        id_list = world_service.GetRelevantEntityList(controller, player)
        list_request = ListRequest()
        list_request.entity_ids.extend(id_list.ids)
        controller.player_ids = [player.id]
        browserquest_stub.list(controller, list_request)

    def teleport(self, controller, request, callback):
        world_service = WorldService_Stub(channels.world_channel)
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)

        teleport_request = world_service_pb2.TeleportRequest()
        teleport_request.entity_id = controller.environ['player_id']
        teleport_request.x = request.x
        teleport_request.y = request.y
        world_service.Teleport(controller, teleport_request)

        player = Player()
        player.id = controller.environ['player_id']
        list_request = ListRequest()
        id_list = world_service.GetRelevantEntityList(controller, player)
        list_request.entity_ids.extend(id_list.ids)
        controller.player_ids = [player.id]
        browserquest_stub.list(controller, list_request)

    def attack(self, controller, request, callback):
        world_service = WorldService_Stub(channels.world_channel)

        attack_request = world_service_pb2.AttackRequest()
        attack_request.attack_id = controller.environ['player_id']
        attack_request.target_id = request.target_id
        world_service.Attack(controller, attack_request)

    def hurt(self, controller, request, callback):
        world_service = WorldService_Stub(channels.world_channel)
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)
        entity_service = EntityService_Stub(channels.entity_channel)

        damage_request = world_service_pb2.DamageRequest()
        damage_request.attack_id = request.mob_id
        damage_request.target_id = controller.environ['player_id']
        damage_response = world_service.Damage(controller, damage_request)

        player = Player()
        player.id = controller.environ['player_id']
        playerentity_service.GetPlayer(controller, player)

        health_request = HealthRequest()
        health_request.hitpoints = player.hitpoints
        controller.player_ids = [player.id]
        browserquest_stub.health(controller, health_request)

    def hit(self, controller, request, callback):
        world_service = WorldService_Stub(channels.world_channel)
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)

        world_damage_request = world_service_pb2.DamageRequest()
        world_damage_request.attack_id = controller.environ['player_id']
        world_damage_request.target_id = request.mob_id
        damage_response = world_service.Damage(controller, world_damage_request)

        damage_request = DamageRequest()
        damage_request.entity_id = request.mob_id
        damage_request.damage = damage_response.damage
        controller.player_ids = [controller.environ['player_id']]
        browserquest_stub.damage(controller, damage_request)

    def aggro(self, controller, request, callback):
        pass # unused
