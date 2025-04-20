from schemas import TestResultResponse


def interpret_phq9(score: int) -> TestResultResponse:
    if score <= 4:
        condition = "Minimal depression"
    elif score <= 9:
        condition = "Mild depression"
    elif score <= 14:
        condition = "Moderate depression"
    elif score <= 19:
        condition = "Moderately severe depression"
    else:
        condition = "Severe depression"

    return TestResultResponse(
        result=f"PHQ-9 score: {score}",
        condition=condition,
        stress_management_technique="Practice mindfulness, regular exercise, and maintain a healthy sleep schedule.",
        social_support="Reach out to friends or family for emotional support.",
        professional_help="Consider seeking help from a mental health professional."
    )

def interpret_gad7(score: int) -> TestResultResponse:
    if score <= 4:
        condition = "Minimal anxiety"
    elif score <= 9:
        condition = "Mild anxiety"
    elif score <= 14:
        condition = "Moderate anxiety"
    else:
        condition = "Severe anxiety"

    return TestResultResponse(
        result=f"GAD-7 score: {score}",
        condition=condition,
        stress_management_technique="Use deep breathing techniques, limit caffeine, and try relaxation exercises.",
        social_support="Talk about your worries with someone you trust.",
        professional_help="Therapy, medication, or counseling may be helpful."
    )

def interpret_pss(score: int) -> TestResultResponse:
    if score <= 13:
        condition = "Low stress"
    elif score <= 26:
        condition = "Moderate stress"
    else:
        condition = "High perceived stress"

    return TestResultResponse(
        result=f"PSS score: {score}",
        condition=condition,
        stress_management_technique="Organize tasks, get adequate rest, and practice stress-relief hobbies.",
        social_support="Connect with friends, family, or peer groups.",
        professional_help="Counseling or stress management programs can help reduce stress levels."
    )
