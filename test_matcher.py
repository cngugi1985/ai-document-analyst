from occupation_matcher import (
    find_matching_occupation
)

roles = [
    "Staff Engineer, QMS",
    "Quality Manager",
    "Supply Chain Manager",
    "Manufacturing Engineer",
    "Business Analyst"
]

for role in roles:

    print(role)

    print(
        find_matching_occupation(role)
    )

    print("-" * 40)