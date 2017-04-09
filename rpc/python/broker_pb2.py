# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: broker.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
import agent_pb2 as agent__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='broker.proto',
  package='jiji.rpc',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x62roker.proto\x12\x08jiji.rpc\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x0b\x61gent.proto\"&\n\x0fGetPairsRequest\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\"1\n\x10GetPairsResponse\x12\x1d\n\x05pairs\x18\x01 \x03(\x0b\x32\x0e.jiji.rpc.Pair\"w\n\x04Pair\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0binternal_id\x18\x02 \x01(\t\x12\x0b\n\x03pip\x18\x03 \x01(\x01\x12\x17\n\x0fmax_trade_units\x18\x04 \x01(\x04\x12\x11\n\tprecision\x18\x05 \x01(\x01\x12\x13\n\x0bmargin_rate\x18\x06 \x01(\x01\"%\n\x0eGetTickRequest\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\"\xae\x01\n\x14RetrieveRatesRequest\x12\x13\n\x0binstance_id\x18\x01 \x01(\t\x12\x11\n\tpair_name\x18\x02 \x01(\t\x12\x10\n\x08interval\x18\x03 \x01(\t\x12.\n\nstart_time\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"&\n\x05Rates\x12\x1d\n\x05rates\x18\x01 \x03(\x0b\x32\x0e.jiji.rpc.Rate\"\xe3\x01\n\x04Rate\x12\x0c\n\x04pair\x18\x01 \x01(\t\x12\"\n\x04open\x18\x02 \x01(\x0b\x32\x14.jiji.rpc.Tick.Value\x12#\n\x05\x63lose\x18\x03 \x01(\x0b\x32\x14.jiji.rpc.Tick.Value\x12\"\n\x04high\x18\x04 \x01(\x0b\x32\x14.jiji.rpc.Tick.Value\x12!\n\x03low\x18\x05 \x01(\x0b\x32\x14.jiji.rpc.Tick.Value\x12-\n\ttimestamp\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06volume\x18\x07 \x01(\x04\x32\xcf\x01\n\rBrokerService\x12\x43\n\x08GetPairs\x12\x19.jiji.rpc.GetPairsRequest\x1a\x1a.jiji.rpc.GetPairsResponse\"\x00\x12\x35\n\x07GetTick\x12\x18.jiji.rpc.GetTickRequest\x1a\x0e.jiji.rpc.Tick\"\x00\x12\x42\n\rRetrieveRates\x12\x1e.jiji.rpc.RetrieveRatesRequest\x1a\x0f.jiji.rpc.Rates\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_empty__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,agent__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_GETPAIRSREQUEST = _descriptor.Descriptor(
  name='GetPairsRequest',
  full_name='jiji.rpc.GetPairsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='jiji.rpc.GetPairsRequest.instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=101,
  serialized_end=139,
)


_GETPAIRSRESPONSE = _descriptor.Descriptor(
  name='GetPairsResponse',
  full_name='jiji.rpc.GetPairsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pairs', full_name='jiji.rpc.GetPairsResponse.pairs', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=141,
  serialized_end=190,
)


_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='jiji.rpc.Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='jiji.rpc.Pair.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='internal_id', full_name='jiji.rpc.Pair.internal_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pip', full_name='jiji.rpc.Pair.pip', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_trade_units', full_name='jiji.rpc.Pair.max_trade_units', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precision', full_name='jiji.rpc.Pair.precision', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='margin_rate', full_name='jiji.rpc.Pair.margin_rate', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=311,
)


_GETTICKREQUEST = _descriptor.Descriptor(
  name='GetTickRequest',
  full_name='jiji.rpc.GetTickRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='jiji.rpc.GetTickRequest.instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=313,
  serialized_end=350,
)


_RETRIEVERATESREQUEST = _descriptor.Descriptor(
  name='RetrieveRatesRequest',
  full_name='jiji.rpc.RetrieveRatesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='instance_id', full_name='jiji.rpc.RetrieveRatesRequest.instance_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pair_name', full_name='jiji.rpc.RetrieveRatesRequest.pair_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='interval', full_name='jiji.rpc.RetrieveRatesRequest.interval', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='jiji.rpc.RetrieveRatesRequest.start_time', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='jiji.rpc.RetrieveRatesRequest.end_time', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=353,
  serialized_end=527,
)


_RATES = _descriptor.Descriptor(
  name='Rates',
  full_name='jiji.rpc.Rates',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rates', full_name='jiji.rpc.Rates.rates', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=567,
)


_RATE = _descriptor.Descriptor(
  name='Rate',
  full_name='jiji.rpc.Rate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pair', full_name='jiji.rpc.Rate.pair', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='open', full_name='jiji.rpc.Rate.open', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='close', full_name='jiji.rpc.Rate.close', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='high', full_name='jiji.rpc.Rate.high', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='low', full_name='jiji.rpc.Rate.low', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='jiji.rpc.Rate.timestamp', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='volume', full_name='jiji.rpc.Rate.volume', index=6,
      number=7, type=4, cpp_type=4, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=570,
  serialized_end=797,
)

_GETPAIRSRESPONSE.fields_by_name['pairs'].message_type = _PAIR
_RETRIEVERATESREQUEST.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RETRIEVERATESREQUEST.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_RATES.fields_by_name['rates'].message_type = _RATE
_RATE.fields_by_name['open'].message_type = agent__pb2._TICK_VALUE
_RATE.fields_by_name['close'].message_type = agent__pb2._TICK_VALUE
_RATE.fields_by_name['high'].message_type = agent__pb2._TICK_VALUE
_RATE.fields_by_name['low'].message_type = agent__pb2._TICK_VALUE
_RATE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['GetPairsRequest'] = _GETPAIRSREQUEST
DESCRIPTOR.message_types_by_name['GetPairsResponse'] = _GETPAIRSRESPONSE
DESCRIPTOR.message_types_by_name['Pair'] = _PAIR
DESCRIPTOR.message_types_by_name['GetTickRequest'] = _GETTICKREQUEST
DESCRIPTOR.message_types_by_name['RetrieveRatesRequest'] = _RETRIEVERATESREQUEST
DESCRIPTOR.message_types_by_name['Rates'] = _RATES
DESCRIPTOR.message_types_by_name['Rate'] = _RATE

GetPairsRequest = _reflection.GeneratedProtocolMessageType('GetPairsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETPAIRSREQUEST,
  __module__ = 'broker_pb2'
  # @@protoc_insertion_point(class_scope:jiji.rpc.GetPairsRequest)
  ))
_sym_db.RegisterMessage(GetPairsRequest)

GetPairsResponse = _reflection.GeneratedProtocolMessageType('GetPairsResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETPAIRSRESPONSE,
  __module__ = 'broker_pb2'
  # @@protoc_insertion_point(class_scope:jiji.rpc.GetPairsResponse)
  ))
_sym_db.RegisterMessage(GetPairsResponse)

Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), dict(
  DESCRIPTOR = _PAIR,
  __module__ = 'broker_pb2'
  # @@protoc_insertion_point(class_scope:jiji.rpc.Pair)
  ))
_sym_db.RegisterMessage(Pair)

GetTickRequest = _reflection.GeneratedProtocolMessageType('GetTickRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTICKREQUEST,
  __module__ = 'broker_pb2'
  # @@protoc_insertion_point(class_scope:jiji.rpc.GetTickRequest)
  ))
_sym_db.RegisterMessage(GetTickRequest)

RetrieveRatesRequest = _reflection.GeneratedProtocolMessageType('RetrieveRatesRequest', (_message.Message,), dict(
  DESCRIPTOR = _RETRIEVERATESREQUEST,
  __module__ = 'broker_pb2'
  # @@protoc_insertion_point(class_scope:jiji.rpc.RetrieveRatesRequest)
  ))
_sym_db.RegisterMessage(RetrieveRatesRequest)

Rates = _reflection.GeneratedProtocolMessageType('Rates', (_message.Message,), dict(
  DESCRIPTOR = _RATES,
  __module__ = 'broker_pb2'
  # @@protoc_insertion_point(class_scope:jiji.rpc.Rates)
  ))
_sym_db.RegisterMessage(Rates)

Rate = _reflection.GeneratedProtocolMessageType('Rate', (_message.Message,), dict(
  DESCRIPTOR = _RATE,
  __module__ = 'broker_pb2'
  # @@protoc_insertion_point(class_scope:jiji.rpc.Rate)
  ))
_sym_db.RegisterMessage(Rate)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class BrokerServiceStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.GetPairs = channel.unary_unary(
          '/jiji.rpc.BrokerService/GetPairs',
          request_serializer=GetPairsRequest.SerializeToString,
          response_deserializer=GetPairsResponse.FromString,
          )
      self.GetTick = channel.unary_unary(
          '/jiji.rpc.BrokerService/GetTick',
          request_serializer=GetTickRequest.SerializeToString,
          response_deserializer=agent__pb2.Tick.FromString,
          )
      self.RetrieveRates = channel.unary_unary(
          '/jiji.rpc.BrokerService/RetrieveRates',
          request_serializer=RetrieveRatesRequest.SerializeToString,
          response_deserializer=Rates.FromString,
          )


  class BrokerServiceServicer(object):

    def GetPairs(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def GetTick(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def RetrieveRates(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_BrokerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'GetPairs': grpc.unary_unary_rpc_method_handler(
            servicer.GetPairs,
            request_deserializer=GetPairsRequest.FromString,
            response_serializer=GetPairsResponse.SerializeToString,
        ),
        'GetTick': grpc.unary_unary_rpc_method_handler(
            servicer.GetTick,
            request_deserializer=GetTickRequest.FromString,
            response_serializer=agent__pb2.Tick.SerializeToString,
        ),
        'RetrieveRates': grpc.unary_unary_rpc_method_handler(
            servicer.RetrieveRates,
            request_deserializer=RetrieveRatesRequest.FromString,
            response_serializer=Rates.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'jiji.rpc.BrokerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaBrokerServiceServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetPairs(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def GetTick(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def RetrieveRates(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaBrokerServiceStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def GetPairs(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetPairs.future = None
    def GetTick(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    GetTick.future = None
    def RetrieveRates(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    RetrieveRates.future = None


  def beta_create_BrokerService_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('jiji.rpc.BrokerService', 'GetPairs'): GetPairsRequest.FromString,
      ('jiji.rpc.BrokerService', 'GetTick'): GetTickRequest.FromString,
      ('jiji.rpc.BrokerService', 'RetrieveRates'): RetrieveRatesRequest.FromString,
    }
    response_serializers = {
      ('jiji.rpc.BrokerService', 'GetPairs'): GetPairsResponse.SerializeToString,
      ('jiji.rpc.BrokerService', 'GetTick'): agent__pb2.Tick.SerializeToString,
      ('jiji.rpc.BrokerService', 'RetrieveRates'): Rates.SerializeToString,
    }
    method_implementations = {
      ('jiji.rpc.BrokerService', 'GetPairs'): face_utilities.unary_unary_inline(servicer.GetPairs),
      ('jiji.rpc.BrokerService', 'GetTick'): face_utilities.unary_unary_inline(servicer.GetTick),
      ('jiji.rpc.BrokerService', 'RetrieveRates'): face_utilities.unary_unary_inline(servicer.RetrieveRates),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_BrokerService_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('jiji.rpc.BrokerService', 'GetPairs'): GetPairsRequest.SerializeToString,
      ('jiji.rpc.BrokerService', 'GetTick'): GetTickRequest.SerializeToString,
      ('jiji.rpc.BrokerService', 'RetrieveRates'): RetrieveRatesRequest.SerializeToString,
    }
    response_deserializers = {
      ('jiji.rpc.BrokerService', 'GetPairs'): GetPairsResponse.FromString,
      ('jiji.rpc.BrokerService', 'GetTick'): agent__pb2.Tick.FromString,
      ('jiji.rpc.BrokerService', 'RetrieveRates'): Rates.FromString,
    }
    cardinalities = {
      'GetPairs': cardinality.Cardinality.UNARY_UNARY,
      'GetTick': cardinality.Cardinality.UNARY_UNARY,
      'RetrieveRates': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'jiji.rpc.BrokerService', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)