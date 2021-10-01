from pyuvm import uvm_reg_field


def add_uvm_reg_field(reg, ipyxact_field):
    field = uvm_reg_field(ipyxact_field.name)
    setattr(reg, ipyxact_field.name, field)
    field.configure(reg,
                    ipyxact_field.bitWidth,
                    ipyxact_field.bitOffset,
                    'RW',  # TODO Handle access
                    False,  # TODO Handle volatility
                    ipyxact_field.resets.reset.value)


def main():
    print('Degenerating regs')
