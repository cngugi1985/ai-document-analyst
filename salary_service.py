def get_salary_range(role, location):

    role = role.lower()

    multiplier = get_location_multiplier(location)

    if "chief" in role or "ciso" in role:

        min_salary = int(220000 * multiplier)
        max_salary = int(350000 * multiplier)

    elif "vice president" in role or "vp" in role:

        min_salary = int(180000 * multiplier)
        max_salary = int(280000 * multiplier)

    elif "director" in role:

        min_salary = int(140000 * multiplier)
        max_salary = int(200000 * multiplier)

    elif "manager" in role:

        min_salary = int(110000 * multiplier)
        max_salary = int(160000 * multiplier)

    elif "architect" in role:

        min_salary = int(125000 * multiplier)
        max_salary = int(180000 * multiplier)

    elif "engineer" in role:

        min_salary = int(95000 * multiplier)
        max_salary = int(140000 * multiplier)

    elif "analyst" in role:

        min_salary = int(75000 * multiplier)
        max_salary = int(110000 * multiplier)

    elif "supervisor" in role:

        min_salary = int(85000 * multiplier)
        max_salary = int(125000 * multiplier)

    else:

        min_salary = int(80000 * multiplier)
        max_salary = int(120000 * multiplier)

    return {
        "min": f"{min_salary:,}",
        "max": f"{max_salary:,}",
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

def get_skill_roi(skills):

    if not skills:
        return {
            "skill": "Coming Soon",
            "impact": "0"
        }

    return {
        "skill": skills[0],
        "impact": "15,000 to 35,000"
    }
   

def get_location_multiplier(location):

    location = location.lower()

    if "san francisco" in location:
        return 1.40

    elif "seattle" in location:
        return 1.30

    elif "boston" in location:
        return 1.20

    elif "austin" in location:
        return 1.15

    elif "manchester" in location:
        return 1.00

    else:
        return 1.00

def get_location_insight(location):

    multiplier = get_location_multiplier(location)

    percentage = int((multiplier - 1) * 100)

    return {
        "market": location,
        "multiplier": multiplier,
        "percentage": percentage
    }       




