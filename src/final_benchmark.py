from data_structures.namedtuple_setup import TypedNamedTuple
from data_structures.namedtuple_setup import access_namedtuple_elements
from data_structures.dict_setup import BasicTypedDict
from data_structures.dict_setup import access_dict_elements
from data_structures.dataclass_setup import SlotsDataclass
from data_structures.dataclass_setup import access_dataclass_elements
from data_structures.pydantic_setup import CachelessPydanticModel
from data_structures.pydantic_setup import access_pydantic_elements

import utils as ut


def main():
    namedtuple_measurements = []
    typed_dict_measurements = []
    slots_dataclass_measurements = []
    cacheless_pydantic_measurements = []

    for i in range(1_000_000):
        namedtuple_measurements.append(ut.benchmark_namedtuple(i, TypedNamedTuple, access_namedtuple_elements))
        typed_dict_measurements.append(ut.benchmark_typeddict(i, BasicTypedDict, access_dict_elements))
        slots_dataclass_measurements.append(ut.benchmark_dataclasses(i, SlotsDataclass, access_dataclass_elements))
        cacheless_pydantic_measurements.append(ut.benchmark_pydantic(i, CachelessPydanticModel, access_pydantic_elements))

    namedtuple_avg_size, namedtuple_avg_time = ut.calculate_averages(namedtuple_measurements)
    typed_dict_avg_size, typed_dict_avg_time = ut.calculate_averages(typed_dict_measurements)
    slots_dataclass_avg_size, slots_dataclass_avg_time = ut.calculate_averages(slots_dataclass_measurements)
    cacheless_pydantic_avg_size, cacheless_pydantic_avg_time = ut.calculate_averages(cacheless_pydantic_measurements)

    average_sizes = {
        "NamedTuple": namedtuple_avg_size,
        "TypedDict": typed_dict_avg_size,
        "SlotsDataclass": slots_dataclass_avg_size,
        "CachelessPydantic": cacheless_pydantic_avg_size
    }
    average_times = {
        "NamedTuple": namedtuple_avg_time,
        "TypedDict": typed_dict_avg_time,
        "SlotsDataclass": slots_dataclass_avg_time,
        "CachelessPydantic": cacheless_pydantic_avg_time
    }

    ut.generate_diagram(
        average_sizes,
        {"y": "Average size (in KB)"},
        "results/final_avg_sizes.png",
        "{:,.2f}",
        (8.5, 3.5),
    )
    ut.generate_diagram(
        average_times,
        {"y": "Average creation/access time (in ms)"},
        "results/final_avg_times.png",
        "{:,.3f}",
        (8.5, 3.5),
    )

if __name__ == "__main__":
    main()
