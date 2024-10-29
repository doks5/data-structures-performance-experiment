from typing import TypedDict


class TestTypedDict(TypedDict):
    pass


def access_dict_elements(data_struct: dict) -> None:
    data_struct["key12"]
    data_struct["key1"]
    data_struct.get("key21")

    "key15" in data_struct.keys()
    "nonexistent_key" in data_struct.keys()
    "nonexistent_value" in data_struct.values()
