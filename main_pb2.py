# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nmain.proto\x12\x16\x61nswer_sheet_extractor\"+\n\x06\x41nswer\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x0f\n\x07options\x18\x02 \x03(\t\"\xcb\x03\n\x19\x45xtractAnswerSheetRequest\x12\x16\n\x0etest_result_id\x18\x01 \x01(\t\x12\x0e\n\x06images\x18\x02 \x03(\x0c\x12Y\n\x08template\x18\x03 \x01(\x0e\x32G.answer_sheet_extractor.ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE\x12\x34\n\x0ctest_answers\x18\x04 \x03(\x0b\x32\x1e.answer_sheet_extractor.Answer\"\xf4\x01\n\x15\x41NSWER_SHEET_TEMPLATE\x12\x0e\n\nCLASS_EXAM\x10\x00\x12\x18\n\x14\x43LASS_EXAM_SEPARATED\x10\x01\x12\x12\n\x0e\x43LASS_PERIODIC\x10\x02\x12\x1c\n\x18\x43LASS_PERIODIC_SEPARATED\x10\x03\x12\x18\n\x14SCHOOL_ENTRANCE_EXAM\x10\x04\x12\"\n\x1eSCHOOL_ENTRANCE_EXAM_SEPARATED\x10\x05\x12\x15\n\x11UNI_ENTRANCE_EXAM\x10\x06\x12\x1f\n\x1bUNI_ENTRANCE_EXAM_SEPARATED\x10\x07\x12\t\n\x05TOEIC\x10\x08\"z\n\x1a\x45xtractAnswerSheetResponse\x12\x16\n\x0etest_result_id\x18\x01 \x01(\t\x12\x0e\n\x06images\x18\x02 \x03(\x0c\x12\x34\n\x0cuser_answers\x18\x03 \x03(\x0b\x32\x1e.answer_sheet_extractor.Answer2\x9e\x01\n\x1b\x41nswerSheetExtractorService\x12\x7f\n\x12\x65xtractAnswerSheet\x12\x31.answer_sheet_extractor.ExtractAnswerSheetRequest\x1a\x32.answer_sheet_extractor.ExtractAnswerSheetResponse\"\x00(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'main_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_ANSWER']._serialized_start=38
  _globals['_ANSWER']._serialized_end=81
  _globals['_EXTRACTANSWERSHEETREQUEST']._serialized_start=84
  _globals['_EXTRACTANSWERSHEETREQUEST']._serialized_end=543
  _globals['_EXTRACTANSWERSHEETREQUEST_ANSWER_SHEET_TEMPLATE']._serialized_start=299
  _globals['_EXTRACTANSWERSHEETREQUEST_ANSWER_SHEET_TEMPLATE']._serialized_end=543
  _globals['_EXTRACTANSWERSHEETRESPONSE']._serialized_start=545
  _globals['_EXTRACTANSWERSHEETRESPONSE']._serialized_end=667
  _globals['_ANSWERSHEETEXTRACTORSERVICE']._serialized_start=670
  _globals['_ANSWERSHEETEXTRACTORSERVICE']._serialized_end=828
# @@protoc_insertion_point(module_scope)
