from dataclasses import make_dataclass, fields


DATACLASS_FIELDS = [(f"key{i}", str) for i in range(1, 26)]


BasicDataclass = make_dataclass(
    'BasicDataclass',
    DATACLASS_FIELDS
)

ImmutableDataclass = make_dataclass(
    'ImmutableDataclass',
    DATACLASS_FIELDS,
    frozen=True
)

SlottedDataclass = make_dataclass(
    'SlottedDataclass',
    DATACLASS_FIELDS,
    slots=True,
)

OptimisedDataclass = make_dataclass(
    'OptimisedDataclass',
    DATACLASS_FIELDS,
    slots=True,
    frozen=True,
)


def field_present(data_class: BasicDataclass | ImmutableDataclass, field_name: str) -> bool:
    return any(field.name == field_name for field in fields(data_class))


def access_dataclass_elements(data_struct: BasicDataclass | ImmutableDataclass) -> None:
    data_struct.key1
    data_struct.key15
    data_struct.key25

    field_present(data_struct, "key20")
    field_present(data_struct, "nonexistent_field")
