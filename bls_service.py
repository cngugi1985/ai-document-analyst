"""
CC AI Compensation Intelligence Service

Uses occupation mappings and real BLS wage data
to provide compensation intelligence.
"""

from occupation_mapping import get_bls_occupation
from real_bls_lookup import get_real_compensation


def get_compensation_intelligence(job_title, state):

    occupation = get_bls_occupation(job_title)

    if not occupation:
        return None

    result = get_real_compensation(
        occupation,
        state
    )

    if not result:
        return None

    return {
        "job_title": job_title,
        "occupation": occupation,
        "state": state,
        "state_compensation": int(
            result["median_wage"]
        ),
        "source": "BLS"
    }