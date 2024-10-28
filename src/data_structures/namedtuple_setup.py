from collections import namedtuple
from typing import NamedTuple


BasicNamedTuple = namedtuple("BasicNamedTuple", f"{' '.join([f'key{i}' for i in range(1, 26)])}")

TypedNamedTuple = NamedTuple("TypedNamedTuple", [(f'key{i}', str) for i in range(1, 26)])


def access_namedtuple_elements(data_struct: tuple):
    data_struct.key5
    data_struct.key15
    data_struct.key25

    "key12" in data_struct._fields
    "nonexistent_field" in data_struct._fields
    "nonexistent_value" in data_struct
