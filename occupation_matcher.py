from difflib import get_close_matches

from bls_occupations import get_all_occupations


def find_matching_occupation(role):

    occupations = get_all_occupations()

    matches = get_close_matches(
        role,
        occupations,
        n=1,
        cutoff=0.3
    )

    if matches:
        return matches[0]

    return None