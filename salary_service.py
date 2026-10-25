def get_salary_range(role, location):

    role = role.lower()

    if "vice president" in role or "vp" in role:
        return {
            "min": "180,000",
            "max": "280,000",
            "source": "Prototype",
            "source_2": "Coming Soon"
        }

    elif "director" in role:
        return {
            "min": "130,000",
            "max": "180,000",
            "source": "Prototype",
            "source_2": "Coming Soon"
        }

    else:
        return {
            "min": "80,000",
            "max": "120,000",
            "source": "Prototype",
            "source_2": "Coming Soon"
        }


def calculate_increase(current_salary, next_salary):

    current_min = int(current_salary["min"].replace(",", ""))
    current_max = int(current_salary["max"].replace(",", ""))

    next_min = int(next_salary["min"].replace(",", ""))
    next_max = int(next_salary["max"].replace(",", ""))

    return {
        "min": f"{next_min - current_min:,}",
        "max": f"{next_max - current_max:,}"
    }