# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import service
from google.protobuf import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import entity_pb2
import world_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='world_service.proto',
  package='',
  serialized_pb='\n\x13world_service.proto\x1a\x0c\x65ntity.proto\x1a\x0bworld.proto\"\x15\n\x06IDList\x12\x0b\n\x03ids\x18\x01 \x03(\x05\"+\n\rChangedGroups\x12\x1a\n\x12has_changed_groups\x18\x01 \x01(\x08\"&\n\x11PlayerJoinRequest\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\"P\n\x12PlayerJoinResponse\x12\x11\n\tplayer_id\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\x12\x11\n\thitpoints\x18\x04 \x01(\x05\"6\n\x0bMoveRequest\x12\x11\n\tentity_id\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\"\x0e\n\x0cMoveResponse\" \n\x0bZoneRequest\x12\x11\n\tentity_id\x18\x01 \x01(\x05\"\x0e\n\x0cZoneResponse\":\n\x0fTeleportRequest\x12\x11\n\tentity_id\x18\x01 \x01(\x05\x12\t\n\x01x\x18\x02 \x01(\x05\x12\t\n\x01y\x18\x03 \x01(\x05\"\x12\n\x10TeleportResponse\"5\n\x0c\x43heckRequest\x12\x11\n\tentity_id\x18\x01 \x01(\x05\x12\x12\n\ncheckpoint\x18\x02 \x01(\x05\"\x0f\n\rCheckResponse\"5\n\rAttackRequest\x12\x11\n\tattack_id\x18\x01 \x01(\x05\x12\x11\n\ttarget_id\x18\x02 \x01(\x05\"6\n\x0e\x41ttackResponse\x12\x11\n\tattack_id\x18\x01 \x01(\x05\x12\x11\n\ttarget_id\x18\x02 \x01(\x05\"5\n\rDamageRequest\x12\x11\n\tattack_id\x18\x01 \x01(\x05\x12\x11\n\ttarget_id\x18\x02 \x01(\x05\"F\n\x0e\x44\x61mageResponse\x12\x11\n\tattack_id\x18\x01 \x01(\x05\x12\x11\n\ttarget_id\x18\x02 \x01(\x05\x12\x0e\n\x06\x64\x61mage\x18\x03 \x01(\x05\x32\x85\x04\n\x0cWorldService\x12\x35\n\nPlayerJoin\x12\x12.PlayerJoinRequest\x1a\x13.PlayerJoinResponse\x12#\n\x04Move\x12\x0c.MoveRequest\x1a\r.MoveResponse\x12#\n\x04Zone\x12\x0c.ZoneRequest\x1a\r.ZoneResponse\x12&\n\x05\x43heck\x12\r.CheckRequest\x1a\x0e.CheckResponse\x12/\n\x08Teleport\x12\x10.TeleportRequest\x1a\x11.TeleportResponse\x12)\n\x06\x41ttack\x12\x0e.AttackRequest\x1a\x0f.AttackResponse\x12)\n\x06\x44\x61mage\x12\x0e.DamageRequest\x1a\x0f.DamageResponse\x12\x14\n\x06\x41\x64\x64Mob\x12\x04.Mob\x1a\x04.Mob\x12)\n\x15GetAdjacentPlayerList\x12\x07.Player\x1a\x07.IDList\x12)\n\x15GetRelevantEntityList\x12\x07.Entity\x1a\x07.IDList\x12\x32\n\x1eGetRecentlyLeftGroupPlayerList\x12\x07.Player\x1a\x07.IDList\x12%\n\x12GetWorldPlayerList\x12\x06.World\x1a\x07.IDListB\x03\x90\x01\x01')




_IDLIST = descriptor.Descriptor(
  name='IDList',
  full_name='IDList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='ids', full_name='IDList.ids', index=0,
      number=1, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=50,
  serialized_end=71,
)


_CHANGEDGROUPS = descriptor.Descriptor(
  name='ChangedGroups',
  full_name='ChangedGroups',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='has_changed_groups', full_name='ChangedGroups.has_changed_groups', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=73,
  serialized_end=116,
)


_PLAYERJOINREQUEST = descriptor.Descriptor(
  name='PlayerJoinRequest',
  full_name='PlayerJoinRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='player_id', full_name='PlayerJoinRequest.player_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=118,
  serialized_end=156,
)


_PLAYERJOINRESPONSE = descriptor.Descriptor(
  name='PlayerJoinResponse',
  full_name='PlayerJoinResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='player_id', full_name='PlayerJoinResponse.player_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='x', full_name='PlayerJoinResponse.x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='PlayerJoinResponse.y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='hitpoints', full_name='PlayerJoinResponse.hitpoints', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=158,
  serialized_end=238,
)


_MOVEREQUEST = descriptor.Descriptor(
  name='MoveRequest',
  full_name='MoveRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='entity_id', full_name='MoveRequest.entity_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='x', full_name='MoveRequest.x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='MoveRequest.y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=240,
  serialized_end=294,
)


_MOVERESPONSE = descriptor.Descriptor(
  name='MoveResponse',
  full_name='MoveResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=296,
  serialized_end=310,
)


_ZONEREQUEST = descriptor.Descriptor(
  name='ZoneRequest',
  full_name='ZoneRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='entity_id', full_name='ZoneRequest.entity_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=312,
  serialized_end=344,
)


_ZONERESPONSE = descriptor.Descriptor(
  name='ZoneResponse',
  full_name='ZoneResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=346,
  serialized_end=360,
)


_TELEPORTREQUEST = descriptor.Descriptor(
  name='TeleportRequest',
  full_name='TeleportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='entity_id', full_name='TeleportRequest.entity_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='x', full_name='TeleportRequest.x', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='y', full_name='TeleportRequest.y', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=362,
  serialized_end=420,
)


_TELEPORTRESPONSE = descriptor.Descriptor(
  name='TeleportResponse',
  full_name='TeleportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=422,
  serialized_end=440,
)


_CHECKREQUEST = descriptor.Descriptor(
  name='CheckRequest',
  full_name='CheckRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='entity_id', full_name='CheckRequest.entity_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='checkpoint', full_name='CheckRequest.checkpoint', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=442,
  serialized_end=495,
)


_CHECKRESPONSE = descriptor.Descriptor(
  name='CheckResponse',
  full_name='CheckResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=497,
  serialized_end=512,
)


_ATTACKREQUEST = descriptor.Descriptor(
  name='AttackRequest',
  full_name='AttackRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attack_id', full_name='AttackRequest.attack_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_id', full_name='AttackRequest.target_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=514,
  serialized_end=567,
)


_ATTACKRESPONSE = descriptor.Descriptor(
  name='AttackResponse',
  full_name='AttackResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attack_id', full_name='AttackResponse.attack_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_id', full_name='AttackResponse.target_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=569,
  serialized_end=623,
)


_DAMAGEREQUEST = descriptor.Descriptor(
  name='DamageRequest',
  full_name='DamageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attack_id', full_name='DamageRequest.attack_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_id', full_name='DamageRequest.target_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=625,
  serialized_end=678,
)


_DAMAGERESPONSE = descriptor.Descriptor(
  name='DamageResponse',
  full_name='DamageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='attack_id', full_name='DamageResponse.attack_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='target_id', full_name='DamageResponse.target_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='damage', full_name='DamageResponse.damage', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=680,
  serialized_end=750,
)

DESCRIPTOR.message_types_by_name['IDList'] = _IDLIST
DESCRIPTOR.message_types_by_name['ChangedGroups'] = _CHANGEDGROUPS
DESCRIPTOR.message_types_by_name['PlayerJoinRequest'] = _PLAYERJOINREQUEST
DESCRIPTOR.message_types_by_name['PlayerJoinResponse'] = _PLAYERJOINRESPONSE
DESCRIPTOR.message_types_by_name['MoveRequest'] = _MOVEREQUEST
DESCRIPTOR.message_types_by_name['MoveResponse'] = _MOVERESPONSE
DESCRIPTOR.message_types_by_name['ZoneRequest'] = _ZONEREQUEST
DESCRIPTOR.message_types_by_name['ZoneResponse'] = _ZONERESPONSE
DESCRIPTOR.message_types_by_name['TeleportRequest'] = _TELEPORTREQUEST
DESCRIPTOR.message_types_by_name['TeleportResponse'] = _TELEPORTRESPONSE
DESCRIPTOR.message_types_by_name['CheckRequest'] = _CHECKREQUEST
DESCRIPTOR.message_types_by_name['CheckResponse'] = _CHECKRESPONSE
DESCRIPTOR.message_types_by_name['AttackRequest'] = _ATTACKREQUEST
DESCRIPTOR.message_types_by_name['AttackResponse'] = _ATTACKRESPONSE
DESCRIPTOR.message_types_by_name['DamageRequest'] = _DAMAGEREQUEST
DESCRIPTOR.message_types_by_name['DamageResponse'] = _DAMAGERESPONSE

class IDList(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _IDLIST
  
  # @@protoc_insertion_point(class_scope:IDList)

class ChangedGroups(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHANGEDGROUPS
  
  # @@protoc_insertion_point(class_scope:ChangedGroups)

class PlayerJoinRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PLAYERJOINREQUEST
  
  # @@protoc_insertion_point(class_scope:PlayerJoinRequest)

class PlayerJoinResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PLAYERJOINRESPONSE
  
  # @@protoc_insertion_point(class_scope:PlayerJoinResponse)

class MoveRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MOVEREQUEST
  
  # @@protoc_insertion_point(class_scope:MoveRequest)

class MoveResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MOVERESPONSE
  
  # @@protoc_insertion_point(class_scope:MoveResponse)

class ZoneRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ZONEREQUEST
  
  # @@protoc_insertion_point(class_scope:ZoneRequest)

class ZoneResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ZONERESPONSE
  
  # @@protoc_insertion_point(class_scope:ZoneResponse)

class TeleportRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TELEPORTREQUEST
  
  # @@protoc_insertion_point(class_scope:TeleportRequest)

class TeleportResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _TELEPORTRESPONSE
  
  # @@protoc_insertion_point(class_scope:TeleportResponse)

class CheckRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHECKREQUEST
  
  # @@protoc_insertion_point(class_scope:CheckRequest)

class CheckResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHECKRESPONSE
  
  # @@protoc_insertion_point(class_scope:CheckResponse)

class AttackRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ATTACKREQUEST
  
  # @@protoc_insertion_point(class_scope:AttackRequest)

class AttackResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _ATTACKRESPONSE
  
  # @@protoc_insertion_point(class_scope:AttackResponse)

class DamageRequest(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DAMAGEREQUEST
  
  # @@protoc_insertion_point(class_scope:DamageRequest)

class DamageResponse(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _DAMAGERESPONSE
  
  # @@protoc_insertion_point(class_scope:DamageResponse)


_WORLDSERVICE = descriptor.ServiceDescriptor(
  name='WorldService',
  full_name='WorldService',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=753,
  serialized_end=1270,
  methods=[
  descriptor.MethodDescriptor(
    name='PlayerJoin',
    full_name='WorldService.PlayerJoin',
    index=0,
    containing_service=None,
    input_type=_PLAYERJOINREQUEST,
    output_type=_PLAYERJOINRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='Move',
    full_name='WorldService.Move',
    index=1,
    containing_service=None,
    input_type=_MOVEREQUEST,
    output_type=_MOVERESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='Zone',
    full_name='WorldService.Zone',
    index=2,
    containing_service=None,
    input_type=_ZONEREQUEST,
    output_type=_ZONERESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='Check',
    full_name='WorldService.Check',
    index=3,
    containing_service=None,
    input_type=_CHECKREQUEST,
    output_type=_CHECKRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='Teleport',
    full_name='WorldService.Teleport',
    index=4,
    containing_service=None,
    input_type=_TELEPORTREQUEST,
    output_type=_TELEPORTRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='Attack',
    full_name='WorldService.Attack',
    index=5,
    containing_service=None,
    input_type=_ATTACKREQUEST,
    output_type=_ATTACKRESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='Damage',
    full_name='WorldService.Damage',
    index=6,
    containing_service=None,
    input_type=_DAMAGEREQUEST,
    output_type=_DAMAGERESPONSE,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='AddMob',
    full_name='WorldService.AddMob',
    index=7,
    containing_service=None,
    input_type=entity_pb2._MOB,
    output_type=entity_pb2._MOB,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='GetAdjacentPlayerList',
    full_name='WorldService.GetAdjacentPlayerList',
    index=8,
    containing_service=None,
    input_type=entity_pb2._PLAYER,
    output_type=_IDLIST,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='GetRelevantEntityList',
    full_name='WorldService.GetRelevantEntityList',
    index=9,
    containing_service=None,
    input_type=entity_pb2._ENTITY,
    output_type=_IDLIST,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='GetRecentlyLeftGroupPlayerList',
    full_name='WorldService.GetRecentlyLeftGroupPlayerList',
    index=10,
    containing_service=None,
    input_type=entity_pb2._PLAYER,
    output_type=_IDLIST,
    options=None,
  ),
  descriptor.MethodDescriptor(
    name='GetWorldPlayerList',
    full_name='WorldService.GetWorldPlayerList',
    index=11,
    containing_service=None,
    input_type=world_pb2._WORLD,
    output_type=_IDLIST,
    options=None,
  ),
])

class WorldService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _WORLDSERVICE
class WorldService_Stub(WorldService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _WORLDSERVICE

# @@protoc_insertion_point(module_scope)
