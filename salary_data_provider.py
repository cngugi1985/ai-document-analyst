
from market_data import SALARY_DATA


def get_salary_com_data(role, location):

    role = role.lower()

    if "senior" in role and "analyst" in role:

        data = SALARY_DATA["Senior Analyst"].get(location)

    elif "analyst" in role:

        data = SALARY_DATA["Analyst"].get(location)

    else:
        data = None

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
    

def get_ziprecruiter_data(role, location):
    salary_info = SALARY_DATA.get(role, {}).get(location, {"min": None, "max": None})

    return {
        "source": "ZipRecruiter",
        "status": "Not Connected",
        "salary_min": salary_info["min"],
        "salary_max": salary_info["max"]
    }