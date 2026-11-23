import grades
import pytest
from grades import gpa_points, subject_average, weighted_gpa


def test_ac1_average_of_two_grades():
    assert round(subject_average([90, 80]), 2) == 85.0


@pytest.mark.parametrize(
    "average, expected",
    [
        (90, 4.0),
        (89.99, 3.0),
        (80, 3.0),
        (79.99, 2.0),
        (70, 2.0),
        (69.99, 1.0),
        (60, 1.0),
        (59.99, 0.0),
    ],
)
def test_ac2_gpa_points_boundaries(average, expected):
    assert gpa_points(average) == expected


def test_ac3_weighted_gpa_math_and_physics():
    # Math: 3 credits, average 90 -> 4.0; Physics: 2 credits, average 70 -> 2.0
    entries = [(gpa_points(90), 3), (gpa_points(70), 2)]
    assert weighted_gpa(entries) == pytest.approx(3.2)

def test_subject_average_no_grades():
    assert subject_average([]) is None


def test_validate_subject_blank_name():
    assert grades.validate_subject("   ", 3) is not None


def test_validate_subject_credits_not_positive():
    assert grades.validate_subject("Math", 0) is not None
    assert grades.validate_subject("Math", -3) is not None


def test_validate_subject_valid():
    assert grades.validate_subject("Math", 3) is None


def test_validate_grade_out_of_range():
    assert grades.validate_grade(150) is not None
    assert grades.validate_grade(-5) is not None


def test_validate_grade_boundaries_ok():
    assert grades.validate_grade(0) is None
    assert grades.validate_grade(100) is None


def test_weighted_gpa_zero_total_credits_returns_none():
    assert grades.weighted_gpa([(4.0, 0)]) is None