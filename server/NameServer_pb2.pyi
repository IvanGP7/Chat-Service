from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class testResponse(_message.Message):
    __slots__ = ("mesnsaje",)
    MESNSAJE_FIELD_NUMBER: _ClassVar[int]
    mesnsaje: str
    def __init__(self, mesnsaje: _Optional[str] = ...) -> None: ...

class GetChatParametersRequest(_message.Message):
    __slots__ = ("chat_id",)
    CHAT_ID_FIELD_NUMBER: _ClassVar[int]
    chat_id: str
    def __init__(self, chat_id: _Optional[str] = ...) -> None: ...

class GetChatParametersResponse(_message.Message):
    __slots__ = ("address", "port")
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    address: str
    port: int
    def __init__(self, address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class RegisterClientRequest(_message.Message):
    __slots__ = ("username", "ip_address", "port")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    username: str
    ip_address: str
    port: int
    def __init__(self, username: _Optional[str] = ..., ip_address: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class RegisterClientResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
