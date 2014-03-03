import channels

from entity_pb2 import Entity
from entity_pb2 import Player
from world_pb2 import World

from browserquest_broadcast_pb2 import SpawnRequest
from browserquest_broadcast_pb2 import ListRequest
from browserquest_broadcast_pb2 import MoveRequest
from browserquest_broadcast_pb2 import AttackRequest
from browserquest_broadcast_pb2 import KillRequest
from browserquest_broadcast_pb2 import DespawnRequest
from browserquest_broadcast_pb2 import PopulationRequest
from browserquest_broadcast_pb2 import DestroyRequest


from event_service_pb2 import EventService
from browserquest_pb2 import BrowserQuest_Stub
from world_service_pb2 import WorldService_Stub
from entity_service_pb2 import EntityService_Stub


class BrowserQuestEventService(EventService):

    def PlayerLogined(self, controller, event, callback):
        entity_service = EntityService_Stub(channels.entity_channel)

        player = Player()
        player.id = event.player_id
        player = entity_service.GetPlayer(controller, player)

    def EntityJoinWorld(self, controller, event, callback):
        entity_service = EntityService_Stub(channels.entity_channel)
        entity = Entity()
        entity.id = event.entity_id
        entity = entity_service.GetEntity(controller, entity)

    def PopulationUpdate(self, controller, event, callback):
        world_service = WorldService_Stub(channels.world_channel)
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)

        world = World()
        world.id = event.world_id
        id_list = world_service.GetWorldPlayerList(controller, world)

        population = PopulationRequest()
        population.world = event.world_id
        population.total = event.population
        controller.player_ids = id_list.ids
        browserquest_stub.population(controller, population)

    def EntityGroupChanged(self, controller, event, callback):
        entity_service = EntityService_Stub(channels.entity_channel)
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)
        world_service = WorldService_Stub(channels.world_channel)

        entity = Entity()
        entity.id = event.entity_id
        entity = entity_service.GetEntity(controller, entity)

        list_request = ListRequest()
        id_list = world_service.GetRelevantEntityList(controller, entity)
        list_request.entity_ids.extend(id_list.ids)
        controller.player_ids = [entity.id]
        browserquest_stub.list(controller, list_request)

        spawn = SpawnRequest()
        spawn.entity_id = entity.id
        spawn.kind = entity.kind
        spawn.x = entity.x
        spawn.y = entity.y
        spawn.name = entity.name
        spawn.orientation = 1
        spawn.armor = entity.armor
        spawn.weapon = entity.weapon
        id_list = world_service.GetAdjacentPlayerList(controller, entity)
        controller.player_ids = id_list.ids
        browserquest_stub.spawn(controller, spawn)

        destroy = DestroyRequest()
        destroy.entity_id = entity.id
        id_list = world_service.GetRecentlyLeftGroupPlayerList(controller, entity)
        controller.player_ids = id_list.ids
        browserquest_stub.destroy(controller, destroy)

    def EntityMove(self, controller, event, callback):
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)
        world_service = WorldService_Stub(channels.world_channel)

        move_request = MoveRequest()
        move_request.entity_id = event.entity_id
        move_request.entity_x = event.x
        move_request.entity_y = event.y
        entity = Entity()
        entity.id = event.entity_id
        id_list = world_service.GetAdjacentPlayerList(controller, entity)
        controller.player_ids = id_list.ids
        browserquest_stub.move(controller, move_request)

    def Attack(self, controller, event, callback):
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)
        world_service = WorldService_Stub(channels.world_channel)

        attack_request = AttackRequest()
        attack_request.attacker_id = event.attack_id
        attack_request.target_id = event.target_id
        entity = Entity()
        entity.id = event.attack_id
        id_list = world_service.GetAdjacentPlayerList(controller, entity)
        controller.player_ids = id_list.ids
        browserquest_stub.attack(controller, attack_request)

    def Damage(self, controller, event, callback):
        pass

    def Kill(self, controller, event, callback):
        world_service = WorldService_Stub(channels.world_channel)
        entity_service = EntityService_Stub(channels.entity_channel)
        browserquest_stub = BrowserQuest_Stub(channels.browserquest_channel)

        killed_entity = Entity()
        killed_entity.id = event.killed_id
        killed_entity = entity_service.GetEntity(controller, killed_entity)

        kill_request = KillRequest()
        kill_request.mob_kind = killed_entity.kind
        controller.player_ids = [event.killer_id]
        browserquest_stub.kill(controller, kill_request)

        despawn_request = DespawnRequest()
        despawn_request.entity_id = event.killed_id
        id_list = world_service.GetAdjacentPlayerList(controller, killed_entity)
        controller.player_ids = id_list.ids
        browserquest_stub.despawn(controller, despawn_request)
