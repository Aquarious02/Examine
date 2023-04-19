"""Проверки прибора."""
import pytest
from loguru import logger

from pygen.device import Device


@pytest.fixture()
def device():
    device_ = Device(0x12)

    yield device_


def test_version(device):
    version = device.get_tm(device.TmId.version)
    logger.info(f'Actual version: {version}')
    assert version.minor > 0
