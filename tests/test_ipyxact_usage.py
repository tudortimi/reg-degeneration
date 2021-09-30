import xml.etree.ElementTree as ET
import reg_degeneration


def test_read_uart_16550():
    tree = ET.parse('uart_16550.xml')
    root = tree.getroot()
    print(root)
