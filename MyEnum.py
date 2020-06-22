from enum import Enum


class ELFCLASS(Enum):
    ELFCLASSNONE = 0
    ELFCLASS32 = 1
    ELFCLASS64 = 2
    ELFCLASSNUM = 3
