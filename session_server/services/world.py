import json
from random import randint

import entity_pb2
from world_pb2 import World
from world_pb2 import Group
from world_pb2 import MobArea
from world_pb2 import ChestArea
from entity_pb2 import Mob
from entity_pb2 import Player
from entity_pb2 import Entity

from controllers.controller import Controller
from world_service_pb2 import WorldService
from world_service_pb2 import PlayerJoinResponse
from world_service_pb2 import MoveResponse
from world_service_pb2 import ZoneResponse
from world_service_pb2 import AttackResponse
from world_service_pb2 import TeleportResponse
from world_service_pb2 import CheckResponse
from world_service_pb2 import DamageResponse
from world_service_pb2 import IDList

from entity_service_pb2 import EntityService_Stub
from event_service_pb2 import EventService_Stub
from event_service_pb2 import EntityJoinWorldEvent
from event_service_pb2 import PopulationUpdateEvent
from event_service_pb2 import EntityGroupChangedEvent
from event_service_pb2 import EntityMoveEvent
from event_service_pb2 import AttackEvent
from event_service_pb2 import DamageEvent
from event_service_pb2 import KillEvent

from world_map import WorldMap

import channels

class WorldServiceImpl(WorldService):
    max_world = 1
    world_map = WorldMap("data/map.json")
    mob_properties = json.loads(open('data/properties.json').read())

    def __init__(self):
        self.worlds = {}
        self.groups = {} # key: %s-%s-%s % (world.id, entity.x, entity.y)
        self.areas = {}
        self.chest_areas = {}
        self.mob_areas = {}
        self.auto_id = 1
        self.auto_area_id = 1

    def GetRelevantEntityList(self, controller, entity, callback):
        entity_service = EntityService_Stub(channels.entity_channel)

        entity = entity_service.GetEntity(controller, entity)
        id_list = IDList()
        group = self.groups.get('%s-%s' % (entity.world_id, entity.group_id))
        id_list.ids.extend(group.entity_ids)
        if entity.id in id_list.ids:
            id_list.ids.remove(entity.id)
        return id_list

    def GetWorldPlayerList(self, controller, world, callback):
        world = self.worlds.get(world.id, None)
        if world:
            id_list = IDList()
            id_list.ids.extend(world.player_ids)
            return id_list

    def GetAdjacentPlayerList(self, controller, entity, callback):
        entity_service = EntityService_Stub(channels.entity_channel)

        entity = entity_service.GetEntity(controller, entity)
        id_list = IDList()
        for position in self.world_map.get_adjacent_group_positions(entity.group_id):
            group_index = "%s-%s-%s" % (entity.world_id, position['x'], position['y'])
            group = self.groups.get(group_index, None)
            if group:
                id_list.ids.extend(group.player_ids)

        if entity.id in id_list.ids:
            id_list.ids.remove(entity.id)
        return id_list

    def GetRecentlyLeftGroupPlayerList(self, controller, entity, callback):
        id_list = IDList()
        for group_index in entity.recently_left_groups:
            group = self.groups.get(group_index, None)
            if group:
                id_list.ids.extend(group.player_ids)
        return id_list

    def PlayerJoin(self, controller, request, callback):
        # service list
        entity_service = EntityService_Stub(channels.entity_channel)
        event_service = EventService_Stub(channels.event_channel)

        # model
        player = Player()
        player.id = request.player_id
        player = entity_service.GetPlayer(controller, player)
        player.kind = 1 # Wariior
        checkpoint = self.world_map.checkpoints.get(player.last_check_point, None)
        world = self.get_random_world()
        entity_service.UpdateEntity(controller, player)

        # event list
        event_controller = Controller()
        entity_join_world_event = EntityJoinWorldEvent()
        population_update_event = PopulationUpdateEvent()
        entity_group_changed_event = EntityGroupChangedEvent()

        # pre
        entity_join_world_event.entity_id = player.id
        entity_group_changed_event.entity_id = player.id
        entity_group_changed_event.pre_group_id = player.group_id
        population_update_event.world_id = world.id
        population_update_event.pre_population = len(world.player_ids)

        #
        if not checkpoint:
            random_start = randint(0, len(self.world_map.starting_areas) - 1)
            checkpoint_id = self.world_map.starting_areas[random_start]
            checkpoint = self.world_map.checkpoints[checkpoint_id]
        player.world_id = world.id
        player.x = checkpoint.x
        player.y = checkpoint.y
        player.hitpoints = 100
        world.player_ids.append(player.id)

        self.handle_entity_group_membership(world, player)
        entity_service.UpdateEntity(controller, player)

        # post
        entity_join_world_event.world_id = player.world_id
        entity_group_changed_event.group_id = player.group_id
        population_update_event.population = len(world.player_ids)

        # broadcast event
        event_service.EntityJoinWorld(event_controller, entity_join_world_event)
        event_service.PopulationUpdate(event_controller, population_update_event)
        event_service.EntityGroupChanged(event_controller, entity_group_changed_event)

        response = PlayerJoinResponse()
        response.player_id = player.id
        response.x = player.x
        response.y = player.y
        response.hitpoints = player.hitpoints
        return response

    def Move(self, controller, request, callback):
        # service
        entity_service = EntityService_Stub(channels.entity_channel)
        event_service = EventService_Stub(channels.event_channel)

        # model
        entity = Entity()
        entity.id = request.entity_id
        entity = entity_service.GetEntity(controller, entity)

        # event
        entity_move_event = EntityMoveEvent()

        # pre
        event_controller = Controller()
        entity_move_event.entity_id = entity.id
        entity_move_event.pre_x = entity.x
        entity_move_event.pre_y = entity.y

        #
        entity.x = request.x
        entity.y = request.y
        entity_service.UpdateEntity(controller, entity)

        # post
        entity_move_event.x = entity.x
        entity_move_event.y = entity.y

        # broadcast event
        event_service.EntityMove(event_controller, entity_move_event)

        response = MoveResponse()
        return response

    def Zone(self, controller, request, callback):
        # service
        entity_service = EntityService_Stub(channels.entity_channel)
        event_service = EventService_Stub(channels.event_channel)

        # model
        entity = Entity()
        entity.id = request.entity_id
        entity = entity_service.GetEntity(controller, entity)
        world = self.worlds.get(entity.world_id, None)

        # event
        event_controller = Controller()
        entity_group_changed_event = EntityGroupChangedEvent()

        # pre
        entity_group_changed_event.entity_id = entity.id
        entity_group_changed_event.pre_group_id = entity.group_id

        #
        has_changed_groups = self.handle_entity_group_membership(world, entity)
        entity_service.UpdateEntity(controller, entity)
        if has_changed_groups:
            # post
            entity_group_changed_event.group_id = entity.group_id

            # broadcast event
            event_service.EntityGroupChanged(event_controller, entity_group_changed_event)

        response = ZoneResponse()
        return response

    def Check(self, controller, request, callback):
        entity_service = EntityService_Stub(channels.entity_channel)
        event_service = EventService_Stub(channels.event_channel)

        entity = Entity()
        entity.id = request.entity_id
        entity = entity_service.GetEntity(controller, entity)

        entity.last_check_point = request.checkpoint
        entity_service.UpdateEntity(controller, entity)

        response = CheckResponse()
        return response

    def Teleport(self, controller, request, callback):
        # service
        entity_service = EntityService_Stub(channels.entity_channel)
        event_service = EventService_Stub(channels.event_channel)

        # model
        entity = Entity()
        entity.id = request.entity_id
        entity = entity_service.GetEntity(controller, entity)
        world = self.worlds[entity.world_id]

        # event
        event_controller = Controller()
        entity_group_changed_event = EntityGroupChangedEvent()

        # pre
        entity_group_changed_event.entity_id = entity.id
        entity_group_changed_event.pre_group_id = entity.group_id

        #
        entity.x = request.x
        entity.y = request.y
        self.handle_entity_group_membership(world, entity)
        entity_service.UpdateEntity(controller, entity)

        # post
        entity_group_changed_event.group_id = entity.group_id

        # broadcast event
        event_service.EntityGroupChanged(event_controller, entity_group_changed_event)

        response = TeleportResponse()
        return response

    def Attack(self, controller, request, callback):
        entity_service = EntityService_Stub(channels.entity_channel)
        event_service = EventService_Stub(channels.event_channel)

        attack = Entity()
        attack.id = request.attack_id
        target = Entity()
        target.id = request.target_id
        attack = entity_service.GetEntity(controller, attack)
        target = entity_service.GetEntity(controller, target)

        event_controller = Controller()
        attack_event = AttackEvent()
        attack_event.attack_id = request.attack_id
        attack_event.target_id = request.target_id
        event_service.Attack(event_controller, attack_event)

        response = AttackResponse()
        response.attack_id = request.attack_id
        response.target_id = request.target_id
        return response

    def Damage(self, controller, request, callback):
        entity_service = EntityService_Stub(channels.entity_channel)
        event_service = EventService_Stub(channels.event_channel)

        attack = Entity()
        attack.id = request.attack_id
        target = Entity()
        target.id = request.target_id
        attack = entity_service.GetEntity(controller, attack)
        target = entity_service.GetEntity(controller, target)

        event_controller = Controller()
        damage_event = DamageEvent()
        kill_event = KillEvent()
        damage_event.attack_id = attack.id
        damage_event.attack_weapon = attack.weapon
        damage_event.target_armor = target.armor
        damage_event.pre_target_hitpoints = target.hitpoints
        kill_event.killer_id = attack.id
        kill_event.killed_id = target.id

        damage = randint(0, 3)
        dealt = attack.weapon * randint(5, 10)
        absorbed = target.armor * randint(1, 3)
        if dealt - absorbed > 0:
            damage = dealt - absorbed

        target.hitpoints -= damage
        if target.hitpoints <= 0:
            target.is_dead = True
        entity_service.UpdateEntity(controller, target)

        damage_event.target_hitpoints = target.hitpoints

        event_service.Damage(event_controller, damage_event)
        if target.hitpoints <= 0:
            event_service.Kill(event_controller, kill_event)

        response = DamageResponse()
        response.attack_id = request.attack_id
        response.target_id = request.target_id
        response.damage = damage
        return response

    def get_random_world(self):
        id = randint(1, self.max_world)
        world = self.worlds.get(id, None)
        if not world:
            world = World()
            world.id = id
            self.worlds[world.id] = world
            self.initial(world)
        return world

    def handle_entity_group_membership(self, world, entity):
        new_group_id = self.world_map.get_group_id_from_position(entity.x, entity.y)
        if entity.group_id == new_group_id: # changed groups
            return False

        old_groups = set()
        new_groups = set()

        # remove from old groups
        old_group_index = '%s-%s' % (world.id, entity.group_id)
        group = self.groups.get(old_group_index, None)
        if group:
            assert entity.id in group.entity_ids and 'entity not in group'
            group.entity_ids.remove(entity.id)
            if isinstance(entity, Player):
                group.player_ids.remove(entity.id)
            for position in self.world_map.get_adjacent_group_positions(entity.group_id):
                old_group_index = '%s-%s-%s' % (world.id, position['x'], position['y'])
                if old_group_index in self.groups.keys():
                    old_groups.add(old_group_index)

        # add to new groups
        for position in self.world_map.get_adjacent_group_positions(new_group_id):
            new_group_index = '%s-%s-%s' % (world.id, position['x'], position['y'])
            if new_group_index in self.groups.keys():
                new_groups.add(new_group_index)

        new_group_index = '%s-%s' % (world.id, new_group_id)
        group = self.groups.get(new_group_index, None)
        group.entity_ids.append(entity.id)
        if isinstance(entity, Player):
            group.player_ids.append(entity.id)
        entity.group_id = new_group_id
        entity.ClearField('recently_left_groups')
        entity.recently_left_groups.extend(old_groups - new_groups)
        return True

    def _auto_id(self):
        id = self.auto_id
        self.auto_id += 1
        return id

    def _auto_area_id(self):
        id = self.auto_area_id
        self.auto_area_id += 1
        return id

    def initial(self, world):
        for group_id in self.world_map.groups:
            group = Group()
            group.id = group_id
            group.world_id = world.id
            group_index = "%s-%s" % (world.id, group_id)
            self.groups[group_index] = group

        for area in self.world_map.mob_areas:
            mob_area = MobArea(**area)
            mob_area.id = self._auto_area_id()
            mob_area.world_id = world.id
            self.spawn_mobs(world, mob_area)
            self.areas[mob_area.id] = mob_area
            self.mob_areas[mob_area.id] = mob_area
            world.mob_area_ids.append(mob_area.id)

        for area in self.world_map.chest_areas:
            chest_area = ChestArea()
            chest_area.id = self._auto_area_id()
            chest_area.width = area['w']
            chest_area.height = area['h']
            chest_area.world_id = world.id
            self.areas[chest_area.id] = chest_area
            self.chest_areas[chest_area.id] = chest_area
            world.chest_area_ids.append(chest_area.id)

    def spawn_mobs(self, world, mob_area):
        entity_service = EntityService_Stub(channels.entity_channel)
        controller = Controller()
        mob_property = self.mob_properties[mob_area.type]
        for i in xrange(mob_area.nb):
            position = self.get_random_position_inside_area(mob_area)
            mob = Mob()
            mob.x = position['x']
            mob.y = position['y']
            mob.kind = self.get_entity_number_by_name(mob_area.type)
            mob.area_id = mob_area.id
            mob.world_id = mob_area.world_id
            mob.hitpoints = mob_property['hp']
            mob.weapon = mob_property['weapon']
            mob.armor = mob_property['armor']
            mob_area.entity_ids.append(mob.id)
            mob = entity_service.CreateMob(controller, mob)
            world.entity_ids.append(mob.id)
            self.handle_entity_group_membership(world, mob)

    def get_random_position_inside_area(self, area): # check outside
        x = area.x + randint(0, area.width + 1)
        y = area.y + randint(0, area.height + 1)
        position = {'x': x, 'y': y}
        return position

    def get_entity_number_by_name(self, name):
        return entity_pb2._ENTITIES.values_by_name[name.upper()].number
