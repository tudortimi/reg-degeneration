import reg_degeneration
from pyuvm import uvm_reg, uvm_reg_block


class Object:
    pass


def new_ipyxact_reg_field(name, offset, width, reset=0):
    field = Object()
    field.name = name
    field.bitOffset = offset
    field.bitWidth = width
    field.access = 'read-write'
    field.resets = Object()
    field.resets.reset = Object()
    field.resets.reset.value = reset
    return field


def test_add_uvm_reg_field():
    reg = uvm_reg('REG')
    field = new_ipyxact_reg_field('FIELD', 8, 2, 1)

    reg_degeneration.add_uvm_reg_field(reg, field)

    assert reg.FIELD
    assert reg.FIELD.get_name() == 'FIELD'
    assert reg.get_fields() == [reg.FIELD]
    assert reg.FIELD.get_lsb_pos() == 8
    assert reg.FIELD.get_n_bits() == 2
    assert reg.FIELD.get_access() == 'RW'
    assert not reg.FIELD.is_volatile()
    assert reg.FIELD.get_reset() == 1


def test_add_uvm_reg_to_block():
    block = uvm_reg_block()

    reg = Object()
    reg.name = 'REG'
    reg.field = []

    added_reg = reg_degeneration.add_uvm_reg_to_block(block, reg)

    assert block.REG
    assert block.REG.get_name() == 'REG'
    assert block.get_registers() == [block.REG]
    assert added_reg == block.REG


def test_add_uvm_reg_to_block_including_fields():
    block = uvm_reg_block()

    reg = Object()
    reg.name = 'REG'
    reg.field = []
    reg.field.append(new_ipyxact_reg_field('FIELD0', 1, 0))
    reg.field.append(new_ipyxact_reg_field('FIELD1', 1, 1))

    added_reg = reg_degeneration.add_uvm_reg_to_block(block, reg)

    assert len(block.REG.get_fields()) == 2


def test_convert_address_block():
    address_block = Object()
    address_block.register = []

    reg0 = Object()
    reg0.name = 'REG0'
    reg0.addressOffset = 0
    reg0.field = []
    address_block.register.append(reg0)
    reg1 = Object()
    reg1.name = 'REG1'
    reg1.addressOffset = 128
    reg1.field = []
    address_block.register.append(reg1)

    reg_block = reg_degeneration.new_uvm_reg_block(address_block)

    assert reg_block

    assert reg_block.default_map
    assert reg_block.default_map.get_name() == 'default_map'

    assert len(reg_block.get_registers()) == 2
    assert reg_block.get_registers()[0].get_name() == 'REG0'
    assert reg_block.get_registers()[1].get_name() == 'REG1'

    assert reg_block.default_map.get_reg_by_offset(0) == reg_block.REG0
    assert reg_block.default_map.get_reg_by_offset(128) == reg_block.REG1
