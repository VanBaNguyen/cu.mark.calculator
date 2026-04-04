import csv
import sys
import os


GRADE_THRESHOLDS = {
    "A+": 90,
    "A":  85,
    "A-": 80,
    "B+": 77,
    "B":  73,
    "Pass": 50,
}


def parse_row(row):
    """Parse a CSV row into course name, exam weight, bonus, and list of marks.

    Format: [Name (optional)], Exam Weight, Bonus, Mark1, Mark2, ...
    If the first field is not a number, it is treated as the course name.
    """
    if not row or all(cell.strip() == "" for cell in row):
        return None

    idx = 0
    course_name = None

    # Check if first field is a course name (non-numeric)
    first = row[0].strip()
    try:
        float(first)
    except ValueError:
        # Not a number — treat as course name
        course_name = first if first else None
        idx = 1

    # Exam weight
    if idx >= len(row):
        return None
    exam_weight = float(row[idx].strip())
    idx += 1

    # Bonus (0 if empty)
    bonus = 0.0
    if idx < len(row):
        bonus_str = row[idx].strip()
        bonus = float(bonus_str) if bonus_str else 0.0
        idx += 1

    # Remaining fields are individual marks (course % earned)
    marks = []
    for cell in row[idx:]:
        val = cell.strip()
        if val:
            marks.append(float(val))

    return {
        "name": course_name,
        "exam_weight": exam_weight,
        "bonus": bonus,
        "marks": marks,
    }

