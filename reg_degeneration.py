import argparse
from ipyxact.ipyxact import Component
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
    # TODO Handle reg block name
    block = uvm_reg_block('regs')
    default_map = uvm_reg_map('default_map')
    setattr(block, 'default_map', default_map)
    for ipyxact_reg in ipyxact_address_block.register:
        reg = add_uvm_reg_to_block(block, ipyxact_reg)
        default_map.add_reg(reg, ipyxact_reg.addressOffset)
    return block


# TODO Replace with 'reg_block.print()', once implemented in 'pyuvm'
def print_reg_block(reg_block):
    print(f'reg_block: {reg_block.get_name()}')
    for reg in reg_block.get_registers():
        print(f'  reg: {reg.get_name()}')
        #for field in reg.get_fields()[::-1]:
        for field in reversed(reg.get_fields()):
            lower = field.get_lsb_pos()
            upper = lower + field.get_n_bits() - 1
            print(f'    field: {field.get_name()} [{upper}:{lower}]')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ipxact', metavar='IP-XACT-FILE', type=argparse.FileType())
    args = parser.parse_args()
    print(f'Degenerating regs from {args.ipxact.name}')

    component = Component()
    component.load(args.ipxact.name)
    print(f'Component: {component.name}')

    assert len(component.memoryMaps.memoryMap) == 1
    memory_map = component.memoryMaps.memoryMap[0]
    assert memory_map.addressBlock
    assert len(memory_map.addressBlock) == 1
    address_block = memory_map.addressBlock[0]
    print(f'Handling address block "{address_block.name}" of memory map "{memory_map.name}"')

    reg_block = new_uvm_reg_block(address_block)
    print("Built the following 'uvm_reg_block':")
    print_reg_block(reg_block)
