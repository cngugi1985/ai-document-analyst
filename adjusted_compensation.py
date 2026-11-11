def get_adjusted_salary(
    salary,
    cost_of_living
):
    return round(
        salary / (cost_of_living / 100)
    )