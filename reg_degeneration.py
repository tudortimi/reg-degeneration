from pyuvm import uvm_reg_field, uvm_reg, uvm_reg_block, uvm_reg_map


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


def add_uvm_reg_to_block(block, ipyxact_reg):
    reg = uvm_reg(ipyxact_reg.name)
    setattr(block, ipyxact_reg.name, reg)
    reg.configure(block)
    for field in ipyxact_reg.field:
        add_uvm_reg_field(reg, field)
    return reg


def new_uvm_reg_block(ipyxact_address_block):
    block = uvm_reg_block()
    default_map = uvm_reg_map('default_map')
    setattr(block, 'default_map', default_map)
    for ipyxact_reg in ipyxact_address_block.register:
        reg = add_uvm_reg_to_block(block, ipyxact_reg)
        default_map.add_reg(reg, ipyxact_reg.addressOffset)
    return block


def main():
    print('Degenerating regs')
