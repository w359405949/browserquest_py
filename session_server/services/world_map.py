
import json
from world_map_pb2 import Checkpoint

class WorldMap(object):

    def __init__(self, filepath):
        data = open(filepath)
        map_data = json.loads(''.join(data.readlines()))

        self.checkpoints = {}
        self.starting_areas = []
        self.auto_id_checkpoint = 1
        self.init_map(map_data)

    def get_randome_postion(self, checkpoint): # validate outside
        x = checkpoint.x + randint(0, checkpoint.width + 1)
        y = checkpoint.y + randint(0, checkpoint.height + 1)
        position = {'x': x, 'y': y}
        return position

    def create_checkpoint(self, *args, **kwargs):
        kwargs['id'] = self._auto_id_checkpoint()
        checkpoint = Checkpoint(*args, **kwargs)
        self.checkpoints[checkpoint.id] = checkpoint
        if checkpoint.s == 1:
            self.starting_areas.append(checkpoint.id)
        return checkpoint

    def _auto_id_checkpoint(self):
        id = self.auto_id_checkpoint
        self.auto_id_checkpoint += 1
        return id

    def init_map(self, map_data):
        self.width = map_data['width']
        self.height = map_data['height']
        self.collisions = map_data['collisions']
        self.mob_areas = map_data['roamingAreas']
        self.chest_areas = map_data['chestAreas']
        self.static_entities = map_data['staticEntities']
        self.is_loaded = True

        self.zone_width = 28
        self.zone_height = 12
        self.group_width = self.width / self.zone_width
        self.group_height = self.height / self.zone_height

        self.init_connected_groups(map_data['doors'])
        self.init_checkpoints(map_data['checkpoints'])
        self.generate_collision_grid()

    def init_connected_groups(self, doors):
        self.connected_groups = {}
        for door in doors:
            group_id = self.get_group_id_from_position(
                                                    door['x'], door['y'])
            connected_group_id = self.get_group_id_from_position(
                                                    door['tx'], door['ty'])
            connected_position = self.group_id_to_group_position(
                                                    connected_group_id)

            if group_id in self.connected_groups:
                self.connected_groups[group_id].append(connected_position)
            else:
                self.connected_groups[group_id] = [connected_position]

    def init_checkpoints(self, checkpoints):
        for checkpoint in checkpoints:
            self.create_checkpoint(**checkpoint)

    def generate_collision_grid(self):
        self.grid = {}
        tile_index = 0

        for tile in self.collisions:
            i = tile / self.height
            j = tile % self.width
            grid_i = self.grid.setdefault(i, {})
            grid_i[j] = 1

    @property
    def groups(self):
        for x in xrange(0, self.group_width):
            for y in xrange(0, self.group_height):
                yield str(x) + '-' + str(y)

    def get_group_id_from_position(self, x, y):
        w = self.zone_width
        h = self.zone_height
        gx = int((x - 1) / w)
        gy = int((y - 1) / h)
        return str(gx) + '-' + str(gy)

    def group_id_to_group_position(self, id):
        x, y = id.split('-')
        return {"x": int(x), "y": int(y)}

    def get_adjacent_group_positions(self, group_id):
        position = self.group_id_to_group_position(group_id)
        x = position['x']
        y = position['y']
        positions = [
                {'x': x-1, 'y': y-1}, {'x': x, 'y': y-1}, {'x': x+1, 'y': y-1},
                {'x': x-1, 'y': y  }, {'x': x, 'y': y  }, {'x': x+1, 'y': y  },
                {'x': x-1, 'y': y+1}, {'x': x, 'y': y+1}, {'x': x+1, 'y': y+1}]
        positions.extend(position for position in self.connected_groups.get(group_id, []) if position not in positions)
        return positions

    def is_out_of_bounds(self, x, y):
        return x <= 0 or x >= self.width or y <= 0 or y >= self.height

    def is_colliding(self, x, y):
        return not self.is_out_of_bounds(x, y) and self.grid[y][x] == 1
