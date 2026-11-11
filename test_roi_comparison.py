from cost_of_living import get_cost_of_living
from adjusted_compensation import get_adjusted_salary

states = {
    "California": 124600,
    "New Jersey": 103840,
    "Utah": 103940
}

for state, salary in states.items():

    coli = get_cost_of_living(state)

    adjusted = get_adjusted_salary(
        salary,
        coli
    )

    print(state)
    print("Salary:", salary)
    print("COLI:", coli)
    print("Adjusted:", adjusted)
    print("-" * 20)