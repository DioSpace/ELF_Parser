class E_Ident:
    file_identification: str
    e_class: int
    e_data: int
    e_version: int
    os_abi: int
    abi_version: int
    pad: str
    nident_size: int


class ELF_Header:
    e_ident: E_Ident  #magic魔数
    e_type: str  #类别
    e_machine: str  #系统架构：3(Intel 80386)
    e_version: str  #版本：2(可执行文件)
    e_entry: int  #入口点地址
    e_phoff: int  #程序头部表
    e_shoff: int  #节区头部表
    e_flags: int  #标志
    e_ehsize: int  #本头的大小
    e_phentsize: int  #程序头大小
    e_phnum: int  #程序头数量
    e_shentsize: int  #节头大小
    e_shnum: int  #节头数量
    e_shstrndx: int  #字符串表索引节头


def handle_elf_header(filepath):
    binfile = open(filepath, 'rb')  # 打开二进制文件

    # 初始化E_Ident
    e_ident = E_Ident()
    ident_data: bytes = binfile.read(4)
    e_ident.file_identification = str(ident_data, "utf-8")
    e_class_data: bytes = binfile.read(1)
    e_ident.e_class = int.from_bytes(e_class_data, 'little')
    ei_data_data = binfile.read(1)
    e_ident.e_data = int.from_bytes(ei_data_data, 'little')
    ei_version_data = binfile.read(1)
    e_ident.e_version = int.from_bytes(ei_version_data, 'little')
    ei_osabi_data = binfile.read(1)
    e_ident.os_abi = int.from_bytes(ei_osabi_data, 'little')
    ei_abiversion_data = binfile.read(1)
    e_ident.abi_version = int.from_bytes(ei_abiversion_data, 'little')
    ei_pad_data: bytes = binfile.read(6)
    e_ident.pad = ei_pad_data.hex()
    ei_nident_size_data = binfile.read(1)
    e_ident.nident_size = int.from_bytes(ei_nident_size_data, 'little')

    # print('\n'.join(['%s:%s' % item for item in e_ident.__dict__.items()]))

    elf_header = ELF_Header()
    elf_header.e_ident = e_ident  # 把e_ident 给ELF_Header
    e_type_data = binfile.read(2)
    elf_header.e_type = int.from_bytes(e_type_data, 'little')
    e_machine_data = binfile.read(2)
    elf_header.e_machine = int.from_bytes(e_machine_data, 'little')
    e_version_data = binfile.read(4)
    elf_header.e_version = int.from_bytes(e_version_data, 'little')
    e_entry_data = binfile.read(4)
    elf_header.e_entry = int.from_bytes(e_entry_data, 'little')
    e_phoff_data = binfile.read(4)
    elf_header.e_phoff = int.from_bytes(e_phoff_data, 'little')
    e_shoff_data = binfile.read(4)
    elf_header.e_shoff = int.from_bytes(e_shoff_data, 'little')
    e_flags_data = binfile.read(4)
    elf_header.e_flags = int.from_bytes(e_flags_data, 'little')
    e_ehsize_data = binfile.read(2)
    elf_header.e_ehsize = int.from_bytes(e_ehsize_data, 'little')
    e_phentsize_data = binfile.read(2)
    elf_header.e_phentsize = int.from_bytes(e_phentsize_data, 'little')
    e_phnum_data = binfile.read(2)
    elf_header.e_phnum = int.from_bytes(e_phnum_data, 'little')
    e_shentsize_data = binfile.read(2)
    elf_header.e_shentsize = int.from_bytes(e_shentsize_data, 'little')
    e_shnum_data = binfile.read(2)
    elf_header.e_shnum = int.from_bytes(e_shnum_data, 'little')
    e_shstrndx_data = binfile.read(2)
    elf_header.e_shstrndx = int.from_bytes(e_shstrndx_data, 'little')

    # print('\n'.join(['%s:%s' % item for item in elf_header.__dict__.items()]))
    binfile.close()

    return elf_header
