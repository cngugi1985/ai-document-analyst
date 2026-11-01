
import ai_service
from market_data import BASE_SALARY
from market_adjustments import MARKET_ADJUSTMENTS




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
   









