from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Answer(_message.Message):
    __slots__ = ("question", "options")
    QUESTION_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    question: str
    options: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, question: _Optional[str] = ..., options: _Optional[_Iterable[str]] = ...) -> None: ...

class ExtractAnswerSheetRequest(_message.Message):
    __slots__ = ("test_result_id", "images", "template", "test_answers")
    class ANSWER_SHEET_TEMPLATE(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CLASS_EXAM: _ClassVar[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE]
        CLASS_EXAM_SEPARATED: _ClassVar[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE]
        CLASS_PERIODIC: _ClassVar[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE]
        CLASS_PERIODIC_SEPARATED: _ClassVar[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE]
        SCHOOL_ENTRANCE_EXAM: _ClassVar[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE]
        SCHOOL_ENTRANCE_EXAM_SEPARATED: _ClassVar[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE]
        UNI_ENTRANCE_EXAM: _ClassVar[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE]
        UNI_ENTRANCE_EXAM_SEPARATED: _ClassVar[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE]
        TOEIC: _ClassVar[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE]
    CLASS_EXAM: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    CLASS_EXAM_SEPARATED: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    CLASS_PERIODIC: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    CLASS_PERIODIC_SEPARATED: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    SCHOOL_ENTRANCE_EXAM: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    SCHOOL_ENTRANCE_EXAM_SEPARATED: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    UNI_ENTRANCE_EXAM: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    UNI_ENTRANCE_EXAM_SEPARATED: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    TOEIC: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    TEST_RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    TEST_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    test_result_id: str
    images: _containers.RepeatedScalarFieldContainer[bytes]
    template: ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE
    test_answers: _containers.RepeatedCompositeFieldContainer[Answer]
    def __init__(self, test_result_id: _Optional[str] = ..., images: _Optional[_Iterable[bytes]] = ..., template: _Optional[_Union[ExtractAnswerSheetRequest.ANSWER_SHEET_TEMPLATE, str]] = ..., test_answers: _Optional[_Iterable[_Union[Answer, _Mapping]]] = ...) -> None: ...

class ExtractAnswerSheetResponse(_message.Message):
    __slots__ = ("test_result_id", "images", "user_answers")
    TEST_RESULT_ID_FIELD_NUMBER: _ClassVar[int]
    IMAGES_FIELD_NUMBER: _ClassVar[int]
    USER_ANSWERS_FIELD_NUMBER: _ClassVar[int]
    test_result_id: str
    images: _containers.RepeatedScalarFieldContainer[bytes]
    user_answers: _containers.RepeatedCompositeFieldContainer[Answer]
    def __init__(self, test_result_id: _Optional[str] = ..., images: _Optional[_Iterable[bytes]] = ..., user_answers: _Optional[_Iterable[_Union[Answer, _Mapping]]] = ...) -> None: ...
