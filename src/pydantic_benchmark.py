from data_structures.pydantic_setup import BasicPydanticModel
from data_structures.pydantic_setup import CachelessPydanticModel
from data_structures.pydantic_setup import access_pydantic_elements

import utils as ut


def main():
    basic_pydantic_measurements = []
    cacheless_pydantic_measurements = []

    for i in range(1_000_000):
        basic_pydantic_measurements.append(ut.benchmark_pydantic(i, BasicPydanticModel, access_pydantic_elements))
        cacheless_pydantic_measurements.append(ut.benchmark_pydantic(i, CachelessPydanticModel, access_pydantic_elements))

    basic_pydantic_avg_size, basic_pydantic_avg_time = ut.calculate_averages(basic_pydantic_measurements)
    cacheless_pydantic_avg_size, cacheless_pydantic_avg_time = ut.calculate_averages(cacheless_pydantic_measurements)

    average_sizes = {
        "BasicPydanticModel": basic_pydantic_avg_size,
        "CachelessPydanticModel": cacheless_pydantic_avg_size,
    }
    average_times = {
        "BasicPydanticModel": basic_pydantic_avg_time,
        "CachelessPydanticModel": cacheless_pydantic_avg_time,
    }

    ut.generate_diagram(
        average_sizes,
        {"y": "Average size (in KB)"},
        "results/pydantic_avg_sizes.png",
        "{:,.2f}",
        (4.5, 3.5),
    )
    ut.generate_diagram(
        average_times,
        {"y": "Average creation/access time (in ms)"},
        "results/pydantic_avg_times.png",
        "{:,.3f}",
        (4.5, 3.5),
    )

if __name__ == "__main__":
    main()
