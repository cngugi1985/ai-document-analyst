"""
CC AI Occupation Mapping

Maps resume occupations to BLS occupations.
"""

OCCUPATION_MAPPING = {

    "Quality Engineer": "Industrial Engineers",

    "Manufacturing Engineer": "Industrial Engineers",

    "Mechanical Engineer": "Mechanical Engineers",

    "Staff Engineer": "Industrial Engineers",

    "Project Manager": "Project Management Specialists",

    "Operations Manager": "General and Operations Managers",

    "Quality Manager": "Industrial Production Managers",

    "Business Analyst": "Management Analysts",

    "Supply Chain Manager": "Logisticians"
}



def get_bls_occupation(job_title):

    for title, occupation in OCCUPATION_MAPPING.items():

        if title.lower() in job_title.lower():
            return occupation

    return None

