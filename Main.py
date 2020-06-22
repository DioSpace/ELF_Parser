import ELF_HEADER
import PROGRAM_HEADER_TABLE
import SECTION_HEADER_TABLE
import DYNAMIC_SYMBOL_TABLE

filepath = "C:\\Users\\zhend\\Desktop\\ELF\\user"

if __name__ == '__main__':
    elf_header = ELF_HEADER.handle_elf_header(filepath)
    print('\n'.join(['%s:%s' % item for item in elf_header.__dict__.items()]))
    program_header_table = PROGRAM_HEADER_TABLE.handle_program_header_tables(filepath, elf_header.e_phoff,
                                                                             elf_header.e_phnum)
    # for i in range(len(program_header_table)):
    #     table = program_header_table[i]
    #     print('\n'.join(['%s:%s' % item for item in table.__dict__.items()]))
    #     print("%d =========================== program_header_table ===========================" % i)

    section_header_table = SECTION_HEADER_TABLE.handle_section_header_tables(filepath, elf_header.e_shoff,
                                                                             elf_header.e_shentsize, elf_header.e_shnum)
    # for i in range(len(section_header_table)):
    #     print("%d =========================== section_header_table symart ===========================" % i)
    #     table = section_header_table[i]
    #     print('\n'.join(['%s:%s' % item for item in table.__dict__.items()]))
    #     print("%d =========================== section_header_table end ===========================" % i)

    dynamic_symbol_tables = DYNAMIC_SYMBOL_TABLE.handle_dynamic_symbol_tables(filepath, 0x148, 16)
    for i in range(len(dynamic_symbol_tables)):
        print("%d =========================== dynamic_symbol_table start ===========================" % i)
        table = dynamic_symbol_tables[i]
        print('\n'.join(['%s:%s' % item for item in table.__dict__.items()]))
        print("%d =========================== dynamic_symbol_table end ===========================" % i)
