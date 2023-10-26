from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class LookUpRequest(_message.Message):
    __slots__ = ["stockName"]
    STOCKNAME_FIELD_NUMBER: _ClassVar[int]
    stockName: str
    def __init__(self, stockName: _Optional[str] = ...) -> None: ...

class LookUpResponse(_message.Message):
    __slots__ = ["stockPrice", "stockVol"]
    STOCKPRICE_FIELD_NUMBER: _ClassVar[int]
    STOCKVOL_FIELD_NUMBER: _ClassVar[int]
    stockPrice: float
    stockVol: int
    def __init__(self, stockPrice: _Optional[float] = ..., stockVol: _Optional[int] = ...) -> None: ...

class TradeRequest(_message.Message):
    __slots__ = ["stockName", "stockQuantity", "stockType"]
    STOCKNAME_FIELD_NUMBER: _ClassVar[int]
    STOCKQUANTITY_FIELD_NUMBER: _ClassVar[int]
    STOCKTYPE_FIELD_NUMBER: _ClassVar[int]
    stockName: str
    stockQuantity: int
    stockType: str
    def __init__(self, stockName: _Optional[str] = ..., stockQuantity: _Optional[int] = ..., stockType: _Optional[str] = ...) -> None: ...

class TradeResponse(_message.Message):
    __slots__ = ["tradeStatus"]
    TRADESTATUS_FIELD_NUMBER: _ClassVar[int]
    tradeStatus: int
    def __init__(self, tradeStatus: _Optional[int] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ["stockName", "stockPrice"]
    STOCKNAME_FIELD_NUMBER: _ClassVar[int]
    STOCKPRICE_FIELD_NUMBER: _ClassVar[int]
    stockName: str
    stockPrice: float
    def __init__(self, stockName: _Optional[str] = ..., stockPrice: _Optional[float] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ["updateStatus"]
    UPDATESTATUS_FIELD_NUMBER: _ClassVar[int]
    updateStatus: int
    def __init__(self, updateStatus: _Optional[int] = ...) -> None: ...
