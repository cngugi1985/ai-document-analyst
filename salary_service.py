
import ai_service
from market_data import BASE_SALARY
from market_adjustments import MARKET_ADJUSTMENTS


def get_market_salary(role, location):

    role_level = ai_service.classify_role_level(role)

    print(f"{role} -> {role_level}")


    if role_level is None:
        return None

    sources = get_salary_sources(
    role_level,
    location
    )

    salary_com = sources["source_1"]

    if salary_com["status"] == "Available":

        return {
            "min": salary_com["salary_min"],
            "max": salary_com["salary_max"]
        }

    return None

def get_salary_range(role, location):

    role = role.lower()

    market_salary = get_market_salary(
        role,
        location
    )

    if market_salary:
        return {
            "min": f"{market_salary['min']:,}",
            "max": f"{market_salary['max']:,}",
            "source": "Internal Market Dataset",
            "source_2": "Compensation Model"
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
   

def get_market_advantage(location):

    baseline_multiplier = 1.00

    selected_multiplier = get_location_multiplier(
        location
    )

    percentage = (
        selected_multiplier - baseline_multiplier
    )

    return {
        "advantage": int(percentage * 100)
    }  







