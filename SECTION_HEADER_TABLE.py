from typing import BinaryIO


class SH_NAME:
    s_name_off: int  # 偏移
    s_name_str: str  # 值


class SECTION_TABLE_ELEMENT:
    sh_name: SH_NAME
    sh_type: int
    sh_flags: int
    sh_addr: int
    sh_offset: int
    sh_size: int
    sh_link: int
    sh_info: int
    sh_addralign: int
    sh_entsize: int
    ss_data: str


def handle_program_header_table(binfile: BinaryIO) -> SECTION_TABLE_ELEMENT():
    table = SECTION_TABLE_ELEMENT()

    sh_name = SH_NAME()
    s_name_data = binfile.read(4)
    sh_name.s_name_off = int.from_bytes(s_name_data, 'little')
    sh_name.s_name_str = "tesym str"
    table.sh_name = sh_name

    sh_type_data = binfile.read(4)
    table.sh_type = int.from_bytes(sh_type_data, 'little')

    sh_flags_data = binfile.read(4)
    table.sh_flags = int.from_bytes(sh_flags_data, 'little')

    sh_addr_data = binfile.read(4)
    table.sh_addr = int.from_bytes(sh_addr_data, 'little')

    sh_offset_data = binfile.read(4)
    table.sh_offset = int.from_bytes(sh_offset_data, 'little')

    sh_size_data = binfile.read(4)
    table.sh_size = int.from_bytes(sh_size_data, 'little')

    sh_link_data = binfile.read(4)
    table.sh_link = int.from_bytes(sh_link_data, 'little')

    sh_info_data = binfile.read(4)
    table.sh_info = int.from_bytes(sh_info_data, 'little')

    sh_addralign_data = binfile.read(4)
    table.sh_addralign = int.from_bytes(sh_addralign_data, 'little')

    sh_entsize_data = binfile.read(4)
    table.sh_entsize = int.from_bytes(sh_entsize_data, 'little')

    table.ss_data = get_p_data(table.sh_offset, table.sh_size)

    return table


def get_p_data(p_offset: int, p_memsz: int) -> str:
    filepath = "C:\\Users\\zhend\\Desktop\\ELF\\user"
    binfile = open(filepath, 'rb')
    binfile.read(p_offset)
    p_data_data = binfile.read(p_memsz)
    p_data = p_data_data.hex()
    binfile.close()
    return p_data


def handle_section_header_tables(filepath: str, shoff: int, shentsize: int, shnum: int) -> []:
    tables = []
    binfile = open(filepath, 'rb')  # 打开二进制文件
    binfile.read(shoff)
    for i in range(shentsize):
        table = handle_program_header_table(binfile)
        tables.append(table)
    binfile.close()
    return tables
