from bls_sample_data import COMPENSATION_DATA


def get_market_insights(occupation):

    data = COMPENSATION_DATA.get(occupation)

    if not data:
        return None

    states = data["states"]

    highest_state = max(
        states,
        key=states.get
    )

    lowest_state = min(
        states,
        key=states.get
    )

    return {
        "highest_state": highest_state,
        "highest_salary": states[highest_state],
        "lowest_state": lowest_state,
        "lowest_salary": states[lowest_state]
    }