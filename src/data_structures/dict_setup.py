from typing import TypedDict


class TestTypedDict(TypedDict):
    pass


def access_dict_elements(data_struct: dict) -> None:
    data_struct.get("key12")
    data_struct.get("key1")
    data_struct.get("key21")

    "key15" in data_struct.keys()
    "nonexistent_key" in data_struct.keys()
