from cost_of_living import get_cost_of_living
from adjusted_compensation import get_adjusted_salary


def get_roi_salary(
    salary,
    state
):
    coli = get_cost_of_living(state)

    if not coli:
        return None

    return get_adjusted_salary(
        salary,
        coli
    )