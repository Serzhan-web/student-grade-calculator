"""Grade calculations for the Student Grade Calculator (no Streamlit code here)."""


def subject_average(grades: list[float]) -> float:
    """Arithmetic mean of a subject's grades."""
    return sum(grades) / len(grades)


def gpa_points(average: float) -> float:
    """Convert a 0-100 average to GPA points on a 4.0 scale (boundaries inclusive)."""
    if average >= 90:
        return 4.0
    if average >= 80:
        return 3.0
    if average >= 70:
        return 2.0
    if average >= 60:
        return 1.0
    return 0.0


def weighted_gpa(entries: list[tuple[float, float]]) -> float:
    """Credit-weighted mean of GPA points. entries = [(points, credits), ...]."""
    total_credits = sum(credits for _, credits in entries)
    return sum(points * credits for points, credits in entries) / total_credits
