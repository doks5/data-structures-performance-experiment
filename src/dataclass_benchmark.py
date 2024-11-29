from data_structures.dataclass_setup import BasicDataclass
from data_structures.dataclass_setup import ImmutableDataclass
from data_structures.dataclass_setup import SlottedDataclass
from data_structures.dataclass_setup import OptimisedDataclass
from data_structures.dataclass_setup import access_dataclass_elements

import utils as ut


def main():
    basic_dataclass_measurements = []
    immutable_dataclass_measurements = []
    slotted_dataclass_measurements = []
    optimised_dataclass_measurements = []

    for i in range(1_000_000):
        basic_dataclass_measurements.append(ut.benchmark_dataclasses(i, BasicDataclass, access_dataclass_elements))
        immutable_dataclass_measurements.append(ut.benchmark_dataclasses(i, ImmutableDataclass, access_dataclass_elements))
        slotted_dataclass_measurements.append(ut.benchmark_dataclasses(i, SlottedDataclass, access_dataclass_elements))
        optimised_dataclass_measurements.append(ut.benchmark_dataclasses(i, OptimisedDataclass, access_dataclass_elements))

    basic_dataclass_avg_size, basic_dataclass_avg_time = ut.calculate_averages(basic_dataclass_measurements)
    immutable_dataclass_avg_size, immutable_dataclass_avg_time = ut.calculate_averages(immutable_dataclass_measurements)
    slotted_dataclass_avg_size, slotted_dataclass_avg_time = ut.calculate_averages(slotted_dataclass_measurements)
    optimised_dataclass_avg_size, optimised_dataclass_avg_time = ut.calculate_averages(optimised_dataclass_measurements)

    average_sizes = {
        "BasicDataclass": basic_dataclass_avg_size,
        "ImmutableDataclass": immutable_dataclass_avg_size,
        "SlottedDataclass": slotted_dataclass_avg_size,
        "OptimisedDataclass": optimised_dataclass_avg_size,
    }
    average_times = {
        "BasicDataclass": basic_dataclass_avg_time,
        "ImmutableDataclass": immutable_dataclass_avg_time,
        "SlottedDataclass": slotted_dataclass_avg_time,
        "OptimisedDataclass": optimised_dataclass_avg_time,
    }

    ut.generate_diagram(
        average_sizes,
        {"y": "Average size (in KB)"},
        "results/dataclass_avg_sizes.png",
        "{:,.2f}",
        (8.5, 4.0)
    )
    ut.generate_diagram(
        average_times,
        {"y": "Average creation/access time (in ms)"},
        "results/dataclass_avg_times.png",
        "{:,.3f}",
        (8.5, 4.0)
    )

if __name__ == "__main__":
    main()
