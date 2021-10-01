import reg_degeneration
from pyuvm import uvm_reg


def test_add_uvm_reg_field():
    reg = uvm_reg('REG')

    class Object:
        pass

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