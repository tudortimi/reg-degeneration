import xml.etree.ElementTree as ET
from ipyxact.ipyxact import Component


def test_read_uart_16550():
    uart_16550 = Component()
    uart_16550.load('uart_16550.xml')
    assert uart_16550.name == 'uart_16550'
    assert uart_16550.memoryMaps
    assert len(uart_16550.memoryMaps.memoryMap) == 1

    register_map = uart_16550.memoryMaps.memoryMap[0]
    assert register_map.name == 'RegisterMap'
    assert register_map.addressBlock
    assert len(register_map.addressBlock) == 1

    sfrs = register_map.addressBlock[0]
    assert sfrs.name == 'Special Function Registers'
    assert sfrs.register
    assert len(sfrs.register) == 2

    lcr = sfrs.register[0]
    assert lcr.name == 'LCR'
    assert lcr.addressOffset == int('0x100c', 0)
    assert lcr.field
    assert len(lcr.field) == 4

    wls = lcr.field[0]
    assert wls.name == 'WLS'
    assert wls.bitWidth == 2
    assert wls.access == 'read-write'
    assert wls.resets
    assert wls.resets.reset
    assert wls.resets.reset.value == 0
