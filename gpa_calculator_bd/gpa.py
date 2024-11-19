def calculate_gpa(grades, credits):
    """
    Calculate GPA given the grades and credits for each subject.

    :param grades: List of grades (e.g., [4.0, 3.5, 3.0])
    :param credits: List of credits corresponding to each subject (e.g., [3, 4, 3])
    :return: GPA value
    """
    total_points = sum(grade * credit for grade, credit in zip(grades, credits))
    total_credits = sum(credits)
    return total_points / total_credits if total_credits != 0 else 0
