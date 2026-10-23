
from zxcvbn import zxcvbn


def analyze_password(password):
    if not password:
        return None

    result = zxcvbn(password)

    score = result["score"]

    levels = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Good",
        4: "Strong"
    }

    feedback = result["feedback"]

    return {
        "score": score,
        "strength": levels[score],
        "guesses": result["guesses"],
        "warning": feedback.get("warning", ""),
        "suggestions": feedback.get("suggestions", [])
    }
