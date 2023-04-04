from dataclasses import dataclass
from enum import IntEnum

from utils.pygen import Command, AttrDict, Caller


class Device(Caller):
    def __init__(self, device_id: int):
        super().__init__('localhost')
        self.device_id = device_id

    class CmdId(IntEnum):
        set_active_bus = 0x6315111b
        set_serial = 0x18feb9c5c
        set_time = 0x1dc4734ff
        get_tm = 0x151db77ae

    class TmId(IntEnum):
        active_bus = 0x129a6bf7
        temperature = 0x7cc02234
        consumption = 0x19a87e6d
        version = 0x251d1696c
        serial = 0x2457c7116
        current_time = 0x6b13fac9

    class ActiveBus(IntEnum):
        main = 0
        reserve = 1

    @dataclass
    class OperatingTimeInfo:
        reboot_count: int
        operating_time: float
        total_time: float

    @dataclass
    class Version:
        major: int
        minor: int
        patch: int
        build: int

    class ResultCode(IntEnum):
        ok = 0
        ParamTooMany = 1
        NotEnoughData = 2
        BadArg = 3
        TmUnknown = 4
        NotImplemented = 5
        UnknownError = 6

    set_active_bus = Command(cmd_id=CmdId.set_active_bus, return_type=ResultCode)
    """Установка приоритетной шины обмена"""

    get_tm = Command(cmd_id=CmdId.get_tm, return_type=AttrDict)
    """Запрос ТМ сообщения"""

    set_time = Command(cmd_id=CmdId.set_time, return_type=ResultCode)
    """Установка времени"""


if __name__ == '__main__':
    my_device = Device(0x12)
    result = my_device.set_time(1)  # ResultCode.ok
    active_bus = my_device.get_tm(my_device.TmId.active_bus)  # ActiveBus
