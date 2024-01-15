from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestIntegers(_message.Message):
    __slots__ = ("num1", "num2")
    NUM1_FIELD_NUMBER: _ClassVar[int]
    NUM2_FIELD_NUMBER: _ClassVar[int]
    num1: int
    num2: int
    def __init__(self, num1: _Optional[int] = ..., num2: _Optional[int] = ...) -> None: ...

class ResponseInteger(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: int
    def __init__(self, result: _Optional[int] = ...) -> None: ...

class ResponseFloat(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: float
    def __init__(self, result: _Optional[float] = ...) -> None: ...
