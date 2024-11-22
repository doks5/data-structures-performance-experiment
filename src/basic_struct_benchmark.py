from data_structures.namedtuple_setup import BasicNamedTuple
from data_structures.namedtuple_setup import access_namedtuple_elements
from data_structures.dict_setup import access_dict_elements
from data_structures.dataclass_setup import BasicDataclass
from data_structures.dataclass_setup import access_dataclass_elements
from data_structures.pydantic_setup import TestPydanticModel
from data_structures.pydantic_setup import access_pydantic_elements

import utils as ut


def main():
    namedtuple_measurements = []
    dict_measurements = []
    basic_dataclass_measurements = []
    pydantic_measurements = []

    for i in range(1_000_000):
        namedtuple_measurements.append(ut.benchmark_namedtuple(i, BasicNamedTuple, access_namedtuple_elements))
        dict_measurements.append(ut.benchmark_dict(i, access_dict_elements))
        basic_dataclass_measurements.append(ut.benchmark_dataclasses(i, BasicDataclass, access_dataclass_elements))
        pydantic_measurements.append(ut.benchmark_pydantic(i, TestPydanticModel, access_pydantic_elements))

    namedtuple_avg_size, namedtuple_avg_time = ut.calculate_averages(namedtuple_measurements)
    dict_avg_size, dict_avg_time = ut.calculate_averages(dict_measurements)
    basic_dataclass_avg_size, basic_dataclass_avg_time = ut.calculate_averages(basic_dataclass_measurements)
    pydantic_avg_size, pydantic_avg_time = ut.calculate_averages(pydantic_measurements)

    average_sizes = {
        "namedtuple": namedtuple_avg_size,
        "dictionary": dict_avg_size,
        "dataclass": basic_dataclass_avg_size,
        "pydantic": pydantic_avg_size
    }
    average_times = {
        "namedtuple": namedtuple_avg_time,
        "dictionary": dict_avg_time,
        "dataclass": basic_dataclass_avg_time,
        "pydantic": pydantic_avg_time
    }

    ut.generate_diagram(
        average_sizes,
        {"y": "Average size (in KB)"},
        "results/basic_structures_avg_sizes.png",
        "{:,.2f}"
    )
    ut.generate_diagram(
        average_times,
        {"y": "Average creation and access time (in milliseconds)"},
        "results/basic_structures_avg_times.png",
        "{:,.3f}"
    )

if __name__ == "__main__":
    main()
