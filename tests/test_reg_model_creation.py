import reg_degeneration
from pyuvm import uvm_reg, uvm_reg_block


class Object:
    pass


def test_add_uvm_reg_field():
    reg = uvm_reg('REG')

    field = Object()
    field.name = 'FIELD'
    field.bitOffset = 8
    field.bitWidth = 2
    field.access = 'read-write'
    field.resets = Object()
    field.resets.reset = Object()
    field.resets.reset.value = 1

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

    added_reg = reg_degeneration.add_uvm_reg_to_block(block, reg)

    assert block.REG
    assert block.REG.get_name() == 'REG'
    assert block.get_registers() == [block.REG]
    assert added_reg == block.REG


def test_convert_address_block():
    address_block = Object()
    address_block.register = []

    reg0 = Object()
    reg0.name = 'REG0'
    reg0.addressOffset = 0
    address_block.register.append(reg0)
    reg1 = Object()
    reg1.name = 'REG1'
    reg1.addressOffset = 128
    address_block.register.append(reg1)

    reg_block = reg_degeneration.new_uvm_reg_block(address_block)

    assert reg_block

    assert reg_block.default_map
    assert reg_block.default_map.get_name() == 'default_map'

    assert len(reg_block.get_registers()) == 2
    assert reg_block.get_registers()[0].get_name() == 'REG0'
    assert reg_block.get_registers()[1].get_name() == 'REG1'
