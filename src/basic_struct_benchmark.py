from data_structures.namedtuple_setup import BasicNamedTuple
from data_structures.namedtuple_setup import access_namedtuple_elements
from data_structures.dict_setup import access_dict_elements
from data_structures.dataclass_setup import BasicDataclass
from data_structures.dataclass_setup import access_dataclass_elements
from data_structures.pydantic_setup import BasicPydanticModel
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
        pydantic_measurements.append(ut.benchmark_pydantic(i, BasicPydanticModel, access_pydantic_elements))

    namedtuple_avg_size, namedtuple_avg_time = ut.calculate_averages(namedtuple_measurements)
    dict_avg_size, dict_avg_time = ut.calculate_averages(dict_measurements)
    basic_dataclass_avg_size, basic_dataclass_avg_time = ut.calculate_averages(basic_dataclass_measurements)
    pydantic_avg_size, pydantic_avg_time = ut.calculate_averages(pydantic_measurements)

    average_sizes = {
        "NamedTuple": namedtuple_avg_size,
        "Dictionary": dict_avg_size,
        "Dataclass": basic_dataclass_avg_size,
        "Pydantic": pydantic_avg_size
    }
    average_times = {
        "NamedTuple": namedtuple_avg_time,
        "Dictionary": dict_avg_time,
        "Dataclass": basic_dataclass_avg_time,
        "Pydantic": pydantic_avg_time
    }

    ut.generate_diagram(
        average_sizes,
        {"y": "Average size (in KB)"},
        "results/basic_structures_avg_sizes.png",
        "{:,.2f}",
        (4.5, 3.5),
    )
    ut.generate_diagram(
        average_times,
        {"y": "Average create/access time (in ms)"},
        "results/basic_structures_avg_times.png",
        "{:,.3f}",
        (4.5, 3.5),
    )

if __name__ == "__main__":
    main()
