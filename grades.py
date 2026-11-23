"""Grade calculations for the Student Grade Calculator (no Streamlit code here)."""


def subject_average(grades: list[float]) -> float | None:
    """Arithmetic mean of a subject's grades, or None if there are no grades."""
    if not grades:
        return None
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


def weighted_gpa(entries: list[tuple[float, float]]) -> float | None:
    """Credit-weighted mean of GPA points, or None if total credits is not positive.

    entries = [(points, credits), ...]
    """
    total_credits = sum(credits for _, credits in entries)
    if total_credits <= 0:
        return None
    return sum(points * credits for points, credits in entries) / total_credits


def validate_subject(name: str, credits: float) -> str | None:
    """Return an error message for an invalid subject, or None if it is valid."""
    if not name.strip():
        return "Subject name must not be blank."
    if credits <= 0:
        return "Credits must be greater than 0."
    return None


def validate_grade(grade: float) -> str | None:
    """Return an error message if the grade is outside 0-100, else None."""
    if not 0 <= grade <= 100:
        return "Grade must be between 0 and 100."
    return None
