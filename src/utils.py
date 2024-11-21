from pympler.asizeof import asizeof
from typing import Callable
from time import perf_counter_ns
import matplotlib.pyplot as plt

from data_structures.dataclass_setup import ImmutableDataclass
from data_structures.dataclass_setup import SlottedDataclass
from data_structures.dataclass_setup import BasicDataclass
from data_structures.pydantic_setup import TestPydanticModel


FIELD_NAMES = [f"key{x}" for x in range(1, 26)]


def benchmark_namedtuple(iteration: int, struct_type, access_func: Callable) -> tuple:
    start = perf_counter_ns()
    struct_instance = struct_type(*[f"{field}__{iteration}" for field in FIELD_NAMES])
    access_func(struct_instance)
    end = perf_counter_ns()

    struct_size = asizeof(struct_instance)
    del struct_instance

    return struct_size, end - start


def benchmark_dict(iteration: int, access_func: Callable) -> tuple:
    start = perf_counter_ns()
    struct_instance = dict([(f"{field}", f"{field}__{iteration}") for field in FIELD_NAMES])
    access_func(struct_instance)
    end = perf_counter_ns()

    struct_size = asizeof(struct_instance)
    del struct_instance

    return struct_size, end - start


def benchmark_dataclasses(
        iteration: int, struct_type: BasicDataclass | ImmutableDataclass | SlottedDataclass, access_func: Callable
):
    start = perf_counter_ns()
    struct_instance = struct_type(*[f"{field}__{iteration}" for field in FIELD_NAMES])
    access_func(struct_instance)
    end = perf_counter_ns()

    struct_size = asizeof(struct_instance)
    del struct_instance

    return struct_size, end - start


def benchmark_pydantic(iteration: int, struct_type: TestPydanticModel, access_func: Callable):
    start = perf_counter_ns()
    struct_instance = struct_type(**{field: f"{field}__{iteration}" for field in FIELD_NAMES})
    access_func(struct_instance)
    end = perf_counter_ns()

    struct_size = asizeof(struct_instance)
    del struct_instance

    return struct_size, end - start


def calculate_averages(measurements: list[tuple]) -> tuple[float, float]:
    sizes = [x[0] for x in measurements]
    times = [x[1] for x in measurements]

    average_size = (sum(sizes) / len(sizes)) / 1024
    average_time = (sum(times) / len(times)) / int(1e6)

    return average_size, average_time


def generate_diagram(
        data: dict, labels: dict, file_name: str, plot_format: str | None = None
) -> None:
    fig, ax = plt.subplots()

    data_groups = data.keys()
    data_points = data.values()

    container = ax.bar(data_groups, data_points)
    if plot_format:
        ax.bar_label(container, fmt=plot_format)
    else:
        ax.bar_label(container)

    if labels.get("x"):
        ax.set_xlabel(labels["x"])
    if labels.get("y"):
        ax.set_ylabel(labels["y"])

    plt.savefig(file_name, transparent=True, bbox_inches="tight")
