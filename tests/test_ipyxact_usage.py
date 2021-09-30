import reg_degeneration


def test_read_uart_16550(tmp_path):
    uart_16550 = tmp_path / 'uart_16550.xml'
    content = 'will be filled with IP-XACT description'
    uart_16550.write_text(content)
    print(uart_16550.resolve())
