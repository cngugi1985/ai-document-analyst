
from market_data import SALARY_DATA
from market_data import BASE_SALARY
from market_adjustments import MARKET_ADJUSTMENTS



def get_salary_com_data(role, location):

    base_salary = BASE_SALARY.get(role)
    multiplier = MARKET_ADJUSTMENTS.get(location)

    if base_salary and multiplier:

        salary_min = round(
            base_salary["min"] * multiplier
        )

        salary_max = round(
            base_salary["max"] * multiplier
        )

        return {
            "source": "Career Intelligence Dataset",
            "status": "Available",
            "salary_min": salary_min,
            "salary_max": salary_max
        }

    return {
        "source": "Career Intelligence Dataset",
        "status": "Unavailable",
        "salary_min": None,
        "salary_max": None
    }

