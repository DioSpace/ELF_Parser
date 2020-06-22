from typing import BinaryIO


class PROGRAM_HEADER_TABLE:
    p_type: int  # *segment type *
    p_offset: int  # p_data 位置偏移
    p_vaddr: int  # *virtual
    p_paddr: int #填充
    p_filesz: int  # p_data 大小
    p_memsz: int  # p_data 大小
    p_flags: int  # flags
    p_align: int  # memory alignment
    p_data: str


def handle_program_header_table(binfile: BinaryIO, filepath: str) -> PROGRAM_HEADER_TABLE():
    table = PROGRAM_HEADER_TABLE()
    p_type_data = binfile.read(4)
    table.p_type = int.from_bytes(p_type_data, 'little')
    p_offset_data = binfile.read(4)
    table.p_offset = int.from_bytes(p_offset_data, 'little')
    p_vaddr_data = binfile.read(4)
    table.p_vaddr = int.from_bytes(p_vaddr_data, 'little')
    p_paddr_data = binfile.read(4)
    table.p_paddr = int.from_bytes(p_paddr_data, 'little')
    p_filesz_data = binfile.read(4)
    table.p_filesz = int.from_bytes(p_filesz_data, 'little')
    p_memsz_data = binfile.read(4)
    table.p_memsz = int.from_bytes(p_memsz_data, 'little')
    p_flag_data = binfile.read(4)
    table.p_flags = int.from_bytes(p_flag_data, 'little')
    p_align_data = binfile.read(4)
    table.p_align = int.from_bytes(p_align_data, 'little')
    # 获取字符串
    table.p_data = get_p_data(table.p_offset, table.p_memsz, filepath)
    return table


def get_p_data(p_offset: int, p_memsz: int, filepath: str) -> str:
    binfile = open(filepath, 'rb')
    binfile.read(p_offset)
    p_data_data = binfile.read(p_memsz)
    p_data = p_data_data.hex()
    binfile.close()
    return p_data


def handle_program_header_tables(filepath: str, symartAddr: int, size: int) -> []:
    # table = PROGRAM_HEADER_TABLE()
    tables = []
    binfile = open(filepath, 'rb')  # 打开二进制文件
    binfile.read(symartAddr)
    for i in range(size):
        table = handle_program_header_table(binfile, filepath)
        tables.append(table)
    binfile.close()
    return tables
