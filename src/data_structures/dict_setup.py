from typing import TypedDict


BasicTypedDict = TypedDict("BasicTypedDict", {f"key{i}":str for i in range(1, 26)})


def access_dict_elements(data_struct: dict) -> None:
    data_struct.get("key12")
    data_struct.get("key1")
    data_struct.get("key21")

    "key15" in data_struct.keys()
    "nonexistent_key" in data_struct.keys()
