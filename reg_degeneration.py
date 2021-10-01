from pyuvm import uvm_reg_field


def get_access(ipyxact_field):
    assert ipyxact_field.access == 'read-write'
    # TODO Implement handling of oll accesses
    return 'RW'


def get_volatility(ipyxact_field):
    # TODO Implement Handling of volatility
    return False


def add_uvm_reg_field(reg, ipyxact_field):
    field = uvm_reg_field(ipyxact_field.name)
    setattr(reg, ipyxact_field.name, field)
    field.configure(reg,
                    ipyxact_field.bitWidth,
                    ipyxact_field.bitOffset,
                    get_access(ipyxact_field),
                    get_volatility(ipyxact_field),
                    ipyxact_field.resets.reset.value)


def main():
    print('Degenerating regs')
