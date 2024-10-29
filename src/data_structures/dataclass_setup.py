from dataclasses import make_dataclass, fields


TestDataclass = make_dataclass(
    'TestDataclass',
    [(f"key{i}", str) for i in range(1, 26)]
)

ImmutableDataclass = make_dataclass(
    'ImmutableDataclass',
    [(f"key{i}", str) for i in range(1, 26)],
    frozen=True
)


def field_present(data_class: TestDataclass | ImmutableDataclass, field_name: str) -> bool:
    return any(field.name == field_name for field in fields(data_class))


def access_dataclass_elements(data_struct: TestDataclass | ImmutableDataclass) -> None:
    data_struct.key1
    data_struct.key15
    data_struct.key25

    field_present(data_struct, "key20")
    field_present(data_struct, "nonexistent_field")
