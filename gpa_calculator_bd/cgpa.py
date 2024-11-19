def calculate_cgpa(gpa_list, credit_list):
    """
    Calculate CGPA given a list of GPAs and credits.

    :param gpa_list: List of GPAs from each semester (e.g., [3.5, 3.7])
    :param credit_list: List of credits for each semester (e.g., [15, 18])
    :return: CGPA value
    """
    total_points = sum(gpa * credits for gpa, credits in zip(gpa_list, credit_list))
    total_credits = sum(credit_list)
    return round((total_points / total_credits),2) if total_credits != 0 else 0
