from adjusted_compensation import (
    get_adjusted_salary
)

from cost_of_living import (
    get_cost_of_living
)

salary = 124600

coli = get_cost_of_living(
    "California"
)

print(coli)

print(
    get_adjusted_salary(
        salary,
        coli
    )
)