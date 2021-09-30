import xml.etree.ElementTree as ET
from ipyxact.ipyxact import Component


def test_read_uart_16550():
    uart_16550 = Component()
    uart_16550.load('uart_16550.xml')
    print(uart_16550.name)
