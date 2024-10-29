from pydantic import create_model


fields: dict = {f"key{i}": (str, None) for i in range(1, 26)}


TestPydanticModel = create_model('TestPydanticModel', **fields)


def access_pydantic_elements(data_struct: TestPydanticModel):
    data_struct.key1
    data_struct.key15
    data_struct.key25

    "key12" in data_struct.__fields__
    "nonexistent_key" in data_struct.__fields__
