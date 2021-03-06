# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: job.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import types_pb2 as types__pb2
from . import errors_pb2 as errors__pb2

from .errors_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='job.proto',
  package='descarteslabs.workflows',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\tjob.proto\x12\x17\x64\x65scarteslabs.workflows\x1a\x0btypes.proto\x1a\x0c\x65rrors.proto\"M\n\x08JobError\x12\x30\n\x04\x63ode\x18\x01 \x01(\x0e\x32\".descarteslabs.workflows.ErrorCode\x12\x0f\n\x07message\x18\x02 \x01(\t\"P\n\x0bJobProgress\x12\x0f\n\x07waiting\x18\x01 \x01(\r\x12\r\n\x05ready\x18\x02 \x01(\r\x12\x0f\n\x07running\x18\x03 \x01(\r\x12\x10\n\x08\x66inished\x18\x04 \x01(\r\"\xb6\x01\n\x05\x45ntry\x12\x11\n\ttimestamp\x18\x01 \x01(\x03\x12\x30\n\x05stage\x18\x02 \x01(\x0e\x32!.descarteslabs.workflows.JobStage\x12\x30\n\x05\x65rror\x18\x03 \x01(\x0b\x32!.descarteslabs.workflows.JobError\x12\x36\n\x08progress\x18\x04 \x01(\x0b\x32$.descarteslabs.workflows.JobProgress\"\x97\x04\n\x03Job\x12\n\n\x02id\x18\x01 \x01(\t\x12\x19\n\x11\x63reated_timestamp\x18\x02 \x01(\x03\x12\x19\n\x11updated_timestamp\x18\x03 \x01(\x03\x12\x30\n\x05stage\x18\x04 \x01(\x0e\x32!.descarteslabs.workflows.JobStage\x12\x32\n\x06status\x18\x05 \x01(\x0e\x32\".descarteslabs.workflows.JobStatus\x12\x30\n\x05\x65rror\x18\x06 \x01(\x0b\x32!.descarteslabs.workflows.JobError\x12\x12\n\nterminated\x18\x07 \x01(\x08\x12\x0f\n\x07\x63hannel\x18\x08 \x01(\t\x12\x12\n\nparameters\x18\n \x01(\t\x12\x31\n\x04type\x18\x11 \x01(\x0e\x32#.descarteslabs.workflows.ResultType\x12\x13\n\x0bworkflow_id\x18\x12 \x01(\t\x12+\n\x03log\x18\x13 \x03(\x0b\x32\x1e.descarteslabs.workflows.Entry\x12\x36\n\x08progress\x18\x14 \x01(\x0b\x32$.descarteslabs.workflows.JobProgress\x12\x18\n\x10serialized_graft\x18\x15 \x01(\t\x12\x1b\n\x13serialized_typespec\x18\x16 \x01(\t\x12\x0c\n\x04user\x18\x17 \x01(\t\x12\x0b\n\x03org\x18\x18 \x01(\t\"\xb6\x01\n\x10\x43reateJobRequest\x12\x12\n\nparameters\x18\x02 \x01(\t\x12\x13\n\x0bworkflow_id\x18\x03 \x01(\t\x12\x31\n\x04type\x18\x04 \x01(\x0e\x32#.descarteslabs.workflows.ResultType\x12\x18\n\x10serialized_graft\x18\x05 \x01(\t\x12\x1b\n\x13serialized_typespec\x18\x06 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x07 \x01(\t\"\x1b\n\rGetJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1e\n\x10\x43\x61ncelJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\x1d\n\x0fWatchJobRequest\x12\n\n\x02id\x18\x01 \x01(\t\"T\n\x0fListJobsRequest\x12\x13\n\x0bworkflow_id\x18\x01 \x01(\t\x12\x16\n\x0estart_datetime\x18\x02 \x01(\t\x12\x14\n\x0c\x65nd_datetime\x18\x03 \x01(\t*G\n\tJobStatus\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x00\x12\x12\n\x0eSTATUS_SUCCESS\x10\x01\x12\x12\n\x0eSTATUS_FAILURE\x10\x02*\x8d\x01\n\x08JobStage\x12\x11\n\rSTAGE_UNKNOWN\x10\x00\x12\x11\n\rSTAGE_PENDING\x10\x01\x12\x13\n\x0fSTAGE_PREPARING\x10\x02\x12\x11\n\rSTAGE_RUNNING\x10\x03\x12\x10\n\x0cSTAGE_SAVING\x10\x04\x12\x0e\n\nSTAGE_DONE\x10\x05\x12\x11\n\rSTAGE_EXPIRED\x10\x06\x32\xba\x03\n\x06JobAPI\x12V\n\tCreateJob\x12).descarteslabs.workflows.CreateJobRequest\x1a\x1c.descarteslabs.workflows.Job\"\x00\x12V\n\x08ListJobs\x12(.descarteslabs.workflows.ListJobsRequest\x1a\x1c.descarteslabs.workflows.Job\"\x00\x30\x01\x12P\n\x06GetJob\x12&.descarteslabs.workflows.GetJobRequest\x1a\x1c.descarteslabs.workflows.Job\"\x00\x12V\n\tCancelJob\x12).descarteslabs.workflows.CancelJobRequest\x1a\x1c.descarteslabs.workflows.Job\"\x00\x12V\n\x08WatchJob\x12(.descarteslabs.workflows.WatchJobRequest\x1a\x1c.descarteslabs.workflows.Job\"\x00\x30\x01P\x01\x62\x06proto3')
  ,
  dependencies=[types__pb2.DESCRIPTOR,errors__pb2.DESCRIPTOR,],
  public_dependencies=[errors__pb2.DESCRIPTOR,])

_JOBSTATUS = _descriptor.EnumDescriptor(
  name='JobStatus',
  full_name='descarteslabs.workflows.JobStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATUS_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_SUCCESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATUS_FAILURE', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1312,
  serialized_end=1383,
)
_sym_db.RegisterEnumDescriptor(_JOBSTATUS)

JobStatus = enum_type_wrapper.EnumTypeWrapper(_JOBSTATUS)
_JOBSTAGE = _descriptor.EnumDescriptor(
  name='JobStage',
  full_name='descarteslabs.workflows.JobStage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STAGE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGE_PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGE_PREPARING', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGE_RUNNING', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGE_SAVING', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGE_DONE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STAGE_EXPIRED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1386,
  serialized_end=1527,
)
_sym_db.RegisterEnumDescriptor(_JOBSTAGE)

JobStage = enum_type_wrapper.EnumTypeWrapper(_JOBSTAGE)
STATUS_UNKNOWN = 0
STATUS_SUCCESS = 1
STATUS_FAILURE = 2
STAGE_UNKNOWN = 0
STAGE_PENDING = 1
STAGE_PREPARING = 2
STAGE_RUNNING = 3
STAGE_SAVING = 4
STAGE_DONE = 5
STAGE_EXPIRED = 6



_JOBERROR = _descriptor.Descriptor(
  name='JobError',
  full_name='descarteslabs.workflows.JobError',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='descarteslabs.workflows.JobError.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='descarteslabs.workflows.JobError.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=142,
)


_JOBPROGRESS = _descriptor.Descriptor(
  name='JobProgress',
  full_name='descarteslabs.workflows.JobProgress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='waiting', full_name='descarteslabs.workflows.JobProgress.waiting', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ready', full_name='descarteslabs.workflows.JobProgress.ready', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='running', full_name='descarteslabs.workflows.JobProgress.running', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finished', full_name='descarteslabs.workflows.JobProgress.finished', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=224,
)


_ENTRY = _descriptor.Descriptor(
  name='Entry',
  full_name='descarteslabs.workflows.Entry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='descarteslabs.workflows.Entry.timestamp', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage', full_name='descarteslabs.workflows.Entry.stage', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='descarteslabs.workflows.Entry.error', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='descarteslabs.workflows.Entry.progress', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=227,
  serialized_end=409,
)


_JOB = _descriptor.Descriptor(
  name='Job',
  full_name='descarteslabs.workflows.Job',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.Job.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_timestamp', full_name='descarteslabs.workflows.Job.created_timestamp', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_timestamp', full_name='descarteslabs.workflows.Job.updated_timestamp', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage', full_name='descarteslabs.workflows.Job.stage', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='descarteslabs.workflows.Job.status', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='error', full_name='descarteslabs.workflows.Job.error', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='terminated', full_name='descarteslabs.workflows.Job.terminated', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='descarteslabs.workflows.Job.channel', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parameters', full_name='descarteslabs.workflows.Job.parameters', index=8,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='descarteslabs.workflows.Job.type', index=9,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='descarteslabs.workflows.Job.workflow_id', index=10,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='log', full_name='descarteslabs.workflows.Job.log', index=11,
      number=19, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='progress', full_name='descarteslabs.workflows.Job.progress', index=12,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_graft', full_name='descarteslabs.workflows.Job.serialized_graft', index=13,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_typespec', full_name='descarteslabs.workflows.Job.serialized_typespec', index=14,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='descarteslabs.workflows.Job.user', index=15,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org', full_name='descarteslabs.workflows.Job.org', index=16,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=412,
  serialized_end=947,
)


_CREATEJOBREQUEST = _descriptor.Descriptor(
  name='CreateJobRequest',
  full_name='descarteslabs.workflows.CreateJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='parameters', full_name='descarteslabs.workflows.CreateJobRequest.parameters', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='descarteslabs.workflows.CreateJobRequest.workflow_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='descarteslabs.workflows.CreateJobRequest.type', index=2,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_graft', full_name='descarteslabs.workflows.CreateJobRequest.serialized_graft', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialized_typespec', full_name='descarteslabs.workflows.CreateJobRequest.serialized_typespec', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel', full_name='descarteslabs.workflows.CreateJobRequest.channel', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=950,
  serialized_end=1132,
)


_GETJOBREQUEST = _descriptor.Descriptor(
  name='GetJobRequest',
  full_name='descarteslabs.workflows.GetJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.GetJobRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1134,
  serialized_end=1161,
)


_CANCELJOBREQUEST = _descriptor.Descriptor(
  name='CancelJobRequest',
  full_name='descarteslabs.workflows.CancelJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.CancelJobRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1163,
  serialized_end=1193,
)


_WATCHJOBREQUEST = _descriptor.Descriptor(
  name='WatchJobRequest',
  full_name='descarteslabs.workflows.WatchJobRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='descarteslabs.workflows.WatchJobRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1195,
  serialized_end=1224,
)


_LISTJOBSREQUEST = _descriptor.Descriptor(
  name='ListJobsRequest',
  full_name='descarteslabs.workflows.ListJobsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workflow_id', full_name='descarteslabs.workflows.ListJobsRequest.workflow_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_datetime', full_name='descarteslabs.workflows.ListJobsRequest.start_datetime', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_datetime', full_name='descarteslabs.workflows.ListJobsRequest.end_datetime', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1226,
  serialized_end=1310,
)

_JOBERROR.fields_by_name['code'].enum_type = errors__pb2._ERRORCODE
_ENTRY.fields_by_name['stage'].enum_type = _JOBSTAGE
_ENTRY.fields_by_name['error'].message_type = _JOBERROR
_ENTRY.fields_by_name['progress'].message_type = _JOBPROGRESS
_JOB.fields_by_name['stage'].enum_type = _JOBSTAGE
_JOB.fields_by_name['status'].enum_type = _JOBSTATUS
_JOB.fields_by_name['error'].message_type = _JOBERROR
_JOB.fields_by_name['type'].enum_type = types__pb2._RESULTTYPE
_JOB.fields_by_name['log'].message_type = _ENTRY
_JOB.fields_by_name['progress'].message_type = _JOBPROGRESS
_CREATEJOBREQUEST.fields_by_name['type'].enum_type = types__pb2._RESULTTYPE
DESCRIPTOR.message_types_by_name['JobError'] = _JOBERROR
DESCRIPTOR.message_types_by_name['JobProgress'] = _JOBPROGRESS
DESCRIPTOR.message_types_by_name['Entry'] = _ENTRY
DESCRIPTOR.message_types_by_name['Job'] = _JOB
DESCRIPTOR.message_types_by_name['CreateJobRequest'] = _CREATEJOBREQUEST
DESCRIPTOR.message_types_by_name['GetJobRequest'] = _GETJOBREQUEST
DESCRIPTOR.message_types_by_name['CancelJobRequest'] = _CANCELJOBREQUEST
DESCRIPTOR.message_types_by_name['WatchJobRequest'] = _WATCHJOBREQUEST
DESCRIPTOR.message_types_by_name['ListJobsRequest'] = _LISTJOBSREQUEST
DESCRIPTOR.enum_types_by_name['JobStatus'] = _JOBSTATUS
DESCRIPTOR.enum_types_by_name['JobStage'] = _JOBSTAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

JobError = _reflection.GeneratedProtocolMessageType('JobError', (_message.Message,), {
  'DESCRIPTOR' : _JOBERROR,
  '__module__' : 'job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.JobError)
  })
_sym_db.RegisterMessage(JobError)

JobProgress = _reflection.GeneratedProtocolMessageType('JobProgress', (_message.Message,), {
  'DESCRIPTOR' : _JOBPROGRESS,
  '__module__' : 'job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.JobProgress)
  })
_sym_db.RegisterMessage(JobProgress)

Entry = _reflection.GeneratedProtocolMessageType('Entry', (_message.Message,), {
  'DESCRIPTOR' : _ENTRY,
  '__module__' : 'job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Entry)
  })
_sym_db.RegisterMessage(Entry)

Job = _reflection.GeneratedProtocolMessageType('Job', (_message.Message,), {
  'DESCRIPTOR' : _JOB,
  '__module__' : 'job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.Job)
  })
_sym_db.RegisterMessage(Job)

CreateJobRequest = _reflection.GeneratedProtocolMessageType('CreateJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEJOBREQUEST,
  '__module__' : 'job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.CreateJobRequest)
  })
_sym_db.RegisterMessage(CreateJobRequest)

GetJobRequest = _reflection.GeneratedProtocolMessageType('GetJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETJOBREQUEST,
  '__module__' : 'job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.GetJobRequest)
  })
_sym_db.RegisterMessage(GetJobRequest)

CancelJobRequest = _reflection.GeneratedProtocolMessageType('CancelJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _CANCELJOBREQUEST,
  '__module__' : 'job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.CancelJobRequest)
  })
_sym_db.RegisterMessage(CancelJobRequest)

WatchJobRequest = _reflection.GeneratedProtocolMessageType('WatchJobRequest', (_message.Message,), {
  'DESCRIPTOR' : _WATCHJOBREQUEST,
  '__module__' : 'job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.WatchJobRequest)
  })
_sym_db.RegisterMessage(WatchJobRequest)

ListJobsRequest = _reflection.GeneratedProtocolMessageType('ListJobsRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTJOBSREQUEST,
  '__module__' : 'job_pb2'
  # @@protoc_insertion_point(class_scope:descarteslabs.workflows.ListJobsRequest)
  })
_sym_db.RegisterMessage(ListJobsRequest)



_JOBAPI = _descriptor.ServiceDescriptor(
  name='JobAPI',
  full_name='descarteslabs.workflows.JobAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1530,
  serialized_end=1972,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateJob',
    full_name='descarteslabs.workflows.JobAPI.CreateJob',
    index=0,
    containing_service=None,
    input_type=_CREATEJOBREQUEST,
    output_type=_JOB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ListJobs',
    full_name='descarteslabs.workflows.JobAPI.ListJobs',
    index=1,
    containing_service=None,
    input_type=_LISTJOBSREQUEST,
    output_type=_JOB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetJob',
    full_name='descarteslabs.workflows.JobAPI.GetJob',
    index=2,
    containing_service=None,
    input_type=_GETJOBREQUEST,
    output_type=_JOB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CancelJob',
    full_name='descarteslabs.workflows.JobAPI.CancelJob',
    index=3,
    containing_service=None,
    input_type=_CANCELJOBREQUEST,
    output_type=_JOB,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='WatchJob',
    full_name='descarteslabs.workflows.JobAPI.WatchJob',
    index=4,
    containing_service=None,
    input_type=_WATCHJOBREQUEST,
    output_type=_JOB,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_JOBAPI)

DESCRIPTOR.services_by_name['JobAPI'] = _JOBAPI

# @@protoc_insertion_point(module_scope)
