# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld/v1/service.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bhelloworld/v1/service.proto\x12\rhelloworld.v1\"\'\n\x11HelloWorldRequest\x12\x12\n\x04name\x18\x01 \x01(\tR\x04name\",\n\x12HelloWorldResponse\x12\x16\n\x06result\x18\x01 \x01(\tR\x06result2h\n\x11HelloWorldService\x12S\n\nHelloWorld\x12 .helloworld.v1.HelloWorldRequest\x1a!.helloworld.v1.HelloWorldResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helloworld.v1.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOWORLDREQUEST']._serialized_start=46
  _globals['_HELLOWORLDREQUEST']._serialized_end=85
  _globals['_HELLOWORLDRESPONSE']._serialized_start=87
  _globals['_HELLOWORLDRESPONSE']._serialized_end=131
  _globals['_HELLOWORLDSERVICE']._serialized_start=133
  _globals['_HELLOWORLDSERVICE']._serialized_end=237
# @@protoc_insertion_point(module_scope)
