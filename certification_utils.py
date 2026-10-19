CERTIFICATION_ALIASES = {
    "PMP": [
        "PMP",
        "Project Management Professional",
        "Project Management Professional (PMP)"
    ],

    "LEAN_SIX_SIGMA": [
        "Lean Six Sigma",
        "Lean Six Sigma Green Belt",
        "Lean Sigma"
    ]
}


def normalize_certification(certification):

    certification = certification.strip()

    for canonical, aliases in CERTIFICATION_ALIASES.items():

        for alias in aliases:

            if alias.lower() in certification.lower():

                return canonical

    return certification

def find_missing_certifications(
    existing_certifications,
    recommended_certifications
):

    missing = []

    normalized_existing = []

    for cert in existing_certifications:

        normalized_existing.append(
            normalize_certification(cert)
        )

    for cert in recommended_certifications:

        normalized_recommended = normalize_certification(cert)

        if normalized_recommended not in normalized_existing:

            missing.append(cert)

    return missing