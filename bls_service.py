"""
CC AI Compensation Intelligence Service

Uses occupation mappings and compensation data
to provide compensation intelligence.
"""

from occupation_mapping import get_bls_occupation
from bls_sample_data import COMPENSATION_DATA


def get_compensation_intelligence(job_title, state):

    occupation = get_bls_occupation(job_title)

    if not occupation:
        return None

    data = COMPENSATION_DATA.get(occupation)

    if not data:
        return None

    state_compensation = data["states"].get(state)

    if state_compensation is None:
        return None

    difference = (
        state_compensation
        - data["national_median"]
    )

    return {
        "job_title": job_title,
        "occupation": occupation,
        "national_median": data["national_median"],
        "state": state,
        "state_compensation": state_compensation,
        "difference": difference,
        "source": "BLS"
    }