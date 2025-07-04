# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: quiz.proto
# Protobuf Python Version: 6.31.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    31,
    0,
    '',
    'quiz.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nquiz.proto\x12\x04quiz\"\'\n\x10StartQuizRequest\x12\x13\n\x0bplayer_name\x18\x01 \x01(\t\"(\n\x12GetQuestionRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"?\n\x13SubmitAnswerRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x14\n\x0c\x61nswer_index\x18\x02 \x01(\x05\"\'\n\x11\x46inishQuizRequest\x12\x12\n\nsession_id\x18\x01 \x01(\t\"Q\n\x11StartQuizResponse\x12\x12\n\nsession_id\x18\x01 \x01(\t\x12\x17\n\x0ftotal_questions\x18\x02 \x01(\x05\x12\x0f\n\x07message\x18\x03 \x01(\t\"\x8b\x01\n\x13GetQuestionResponse\x12\x15\n\rquestion_text\x18\x01 \x01(\t\x12\x0f\n\x07options\x18\x02 \x03(\t\x12\x17\n\x0fquestion_number\x18\x03 \x01(\x05\x12\x17\n\x0ftotal_questions\x18\x04 \x01(\x05\x12\x1a\n\x12has_more_questions\x18\x05 \x01(\x08\"p\n\x14SubmitAnswerResponse\x12\x12\n\nis_correct\x18\x01 \x01(\x08\x12\x10\n\x08\x66\x65\x65\x64\x62\x61\x63k\x18\x02 \x01(\t\x12\x1b\n\x13\x63orrect_explanation\x18\x03 \x01(\t\x12\x15\n\rcurrent_score\x18\x04 \x01(\x05\"\xa3\x01\n\x12\x46inishQuizResponse\x12\x13\n\x0b\x66inal_score\x18\x01 \x01(\x05\x12\x17\n\x0ftotal_questions\x18\x02 \x01(\x05\x12\x12\n\npercentage\x18\x03 \x01(\x01\x12\x1b\n\x13performance_message\x18\x04 \x01(\t\x12.\n\x10question_results\x18\x05 \x03(\x0b\x32\x14.quiz.QuestionResult\"d\n\x0eQuestionResult\x12\x10\n\x08question\x18\x01 \x01(\t\x12\x13\n\x0buser_answer\x18\x02 \x01(\t\x12\x16\n\x0e\x63orrect_answer\x18\x03 \x01(\t\x12\x13\n\x0bwas_correct\x18\x04 \x01(\x08\x32\x97\x02\n\x0bQuizService\x12<\n\tStartQuiz\x12\x16.quiz.StartQuizRequest\x1a\x17.quiz.StartQuizResponse\x12\x42\n\x0bGetQuestion\x12\x18.quiz.GetQuestionRequest\x1a\x19.quiz.GetQuestionResponse\x12\x45\n\x0cSubmitAnswer\x12\x19.quiz.SubmitAnswerRequest\x1a\x1a.quiz.SubmitAnswerResponse\x12?\n\nFinishQuiz\x12\x17.quiz.FinishQuizRequest\x1a\x18.quiz.FinishQuizResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'quiz_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STARTQUIZREQUEST']._serialized_start=20
  _globals['_STARTQUIZREQUEST']._serialized_end=59
  _globals['_GETQUESTIONREQUEST']._serialized_start=61
  _globals['_GETQUESTIONREQUEST']._serialized_end=101
  _globals['_SUBMITANSWERREQUEST']._serialized_start=103
  _globals['_SUBMITANSWERREQUEST']._serialized_end=166
  _globals['_FINISHQUIZREQUEST']._serialized_start=168
  _globals['_FINISHQUIZREQUEST']._serialized_end=207
  _globals['_STARTQUIZRESPONSE']._serialized_start=209
  _globals['_STARTQUIZRESPONSE']._serialized_end=290
  _globals['_GETQUESTIONRESPONSE']._serialized_start=293
  _globals['_GETQUESTIONRESPONSE']._serialized_end=432
  _globals['_SUBMITANSWERRESPONSE']._serialized_start=434
  _globals['_SUBMITANSWERRESPONSE']._serialized_end=546
  _globals['_FINISHQUIZRESPONSE']._serialized_start=549
  _globals['_FINISHQUIZRESPONSE']._serialized_end=712
  _globals['_QUESTIONRESULT']._serialized_start=714
  _globals['_QUESTIONRESULT']._serialized_end=814
  _globals['_QUIZSERVICE']._serialized_start=817
  _globals['_QUIZSERVICE']._serialized_end=1096
# @@protoc_insertion_point(module_scope)
