from typing import BinaryIO


class SYM_NAME:
    sym_name_off: int  # 偏移
    sym_name_str: str  # 值


class Sym_Info:
    sym_info_type: int
    sym_info_bind: int


class DYNAMIC_SYMBOL_TABLE:
    sym_name: SYM_NAME
    sym_value: int
    sym_size: int
    sym_info: int
    sym_other: int
    sym_shndx: int


def handle_dynamic_symbol_table(binfile: BinaryIO) -> DYNAMIC_SYMBOL_TABLE():
    table = DYNAMIC_SYMBOL_TABLE()

    sym_name = SYM_NAME()
    sym_name_off_data = binfile.read(4)
    sym_name.sym_name_off = int.from_bytes(sym_name_off_data, 'little')
    sym_name.sym_name_str = "sym_name"
    table.sym_name = sym_name

    sym_value_data = binfile.read(4)
    table.sym_value = int.from_bytes(sym_value_data, 'little')

    sym_size_data = binfile.read(4)
    table.sym_size = int.from_bytes(sym_size_data, 'little')

    sym_info_data = binfile.read(1)
    table.sym_info = int.from_bytes(sym_info_data, 'little')

    sym_other_data = binfile.read(1)
    table.sym_other = int.from_bytes(sym_other_data, 'little')

    sym_shndx_data = binfile.read(2)
    table.sym_shndx = int.from_bytes(sym_shndx_data, 'little')

    return table


def handle_dynamic_symbol_tables(filepath: str, shoff: int, shentsize: int) -> []:
    tables = []
    binfile = open(filepath, 'rb')  # 打开二进制文件
    binfile.read(shoff)
    for i in range(shentsize):
        table = handle_dynamic_symbol_table(binfile)
        tables.append(table)
    binfile.close()
    return tables
