from pydantic import create_model, ConfigDict


fields: dict = {f"key{i}": (str, None) for i in range(1, 26)}


BasicPydanticModel = create_model('BasicPydanticModel', **fields)

CachelessPydanticModel = create_model(
'BasicPydanticModel', __config__=ConfigDict(cache_strings='none'), **fields
)


def access_pydantic_elements(data_struct: BasicPydanticModel):
    data_struct.key1
    data_struct.key15
    data_struct.key25

    "key12" in data_struct.__fields__
    "nonexistent_key" in data_struct.__fields__
