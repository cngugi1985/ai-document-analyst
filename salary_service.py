def get_salary_range(role, location):

    role = role.lower()

    if "vice president" in role or "vp" in role:
        return {
            "min": "180,000",
            "max": "280,000",
            "source": "Prototype"
        }

    elif "director" in role:
        return {
            "min": "130,000",
            "max": "180,000",
            "source": "Prototype"
        }

    else:
        return {
            "min": "80,000",
            "max": "120,000",
            "source": "Prototype"
        }