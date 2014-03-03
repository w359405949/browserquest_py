from entity_pb2 import *
from entity_service_pb2 import EntityService

class EntityServiceImp(EntityService):

    def __init__(self):
        self.auto_id = 1
        self.entities = {}
        self.players = {}
        self.items = {}
        self.chests = {}
        self.characters = {}
        self.mobs = {}
        self.hates = {}

    def _auto_id(self):
        id = self.auto_id
        self.auto_id += 1
        return id

    def GetPlayer(self, controller, player, callback):
        _player = self.players.get(player.id, None)
        if _player:
            return _player

        for _player in self.players.values():
            if player.name == _player.name:
                return _player

    def GetMob(self, controller, mob, callback):
        mob = self.mobs.get(mob.id, None)
        return mob

    def CreatePlayer(self, controller, player, callback):
        player.id = self._auto_id()
        self.entities[player.id] = player
        self.players[player.id] = player
        return player

    def CreateItem(self, controller, item, callback):
        item.id = self._auto_id()
        self.entities[item.id] = item
        self.items[item.id] = item
        return item

    def CreateChest(self, controller, chest, callback):
        chest.id = self._auto_id()
        self.entities[chest.id] = chest
        self.items[chest.id] = chest
        self.chests[chest.id] = chest
        return chest

    def CreateCharacter(self, controller, character, callback):
        character.id = self._auto_id()
        self.entities[character.id] = character
        self.characters[character.id] = character
        return character

    def CreateMob(self, controller, mob, callback):
        mob.id = self._auto_id()
        self.entities[mob.id] = mob
        self.characters[mob.id] = mob
        self.mobs[mob.id] = mob
        return mob

    def GetPlayerIDList(self, controller, request, callback):
        id_list = IDList()
        id_list.ids = self.players.keys()
        return id_list

    def UpdateEntity(self, controller, entity, callback):
        self.entities[entity.id] = entity

    def GetEntity(self, controller, entity, callback):
        entity = self.entities[entity.id]
        return entity
