def calculate_average(marks):
    """
    Calculate the average mark.

    :param marks: List of marks (e.g., [85, 90, 78])
    :return: Average marks
    """
    return sum(marks) / len(marks) if marks else 0
