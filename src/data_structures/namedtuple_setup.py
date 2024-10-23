from collections import namedtuple
from typing import NamedTuple


BasicNamedTuple = namedtuple("BasicNamedTuple", f"{' '.join([f'key{i}' for i in range(1, 26)])}")


def generate_and_call_basic_namedtuple(iteration: int):
    instance_i = BasicNamedTuple(*[f"val_{iteration}__{i}" for i in range(1, 26)])

    instance_i.key3
    instance_i.key8
    instance_i.key15
    instance_i.key19
    instance_i.key25


TypedNamedTuple = NamedTuple("TypedNamedTuple", [(f'key{field}', str) for field in range(1, 26)])


def generate_and_call_typed_namedtuple(iteration: int):
    instance_i = TypedNamedTuple(*[f"val_{iteration}__{i}" for i in range(1, 26)])

    instance_i.key5
    instance_i.key11
    instance_i.key18
    instance_i.key21
    instance_i.key25
