
from market_data import SALARY_DATA


def get_salary_com_data(role, location):

    data = SALARY_DATA.get(role, {}).get(location)

    if data:
        return {
            "source": "Salary.com",
            "status": "Connected",
            "salary_min": data["min"],
            "salary_max": data["max"]
        }

    return {
        "source": "Salary.com",
        "status": "Not Connected",
        "salary_min": None,
        "salary_max": None
    }

