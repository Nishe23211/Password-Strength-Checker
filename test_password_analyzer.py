
import pytest

from password_analyzer import analyze_password
from password_generator import generate_password


# Test 1: Empty password
def test_empty_password():
    assert analyze_password("") is None


# Test 2: Weak password
def test_weak_password():
    result = analyze_password("123456")

    assert result["score"] <= 1
    assert result["strength"] in [
        "Very Weak", "Weak"
    ]


# Test 3: Strength score is valid
def test_score_range():
    result = analyze_password("Example-Blue-47!")

    assert 0 <= result["score"] <= 4


# Test 4: Required analysis fields
def test_analysis_fields():
    result = analyze_password("Example-Blue-47!")

    required_fields = [
        "score",
        "strength",
        "guesses",
        "warning",
        "suggestions"
    ]

    for field in required_fields:
        assert field in result


# Test 5: Password length
@pytest.mark.parametrize(
    "length", [12, 16, 20, 32]
)
def test_generated_length(length):
    password = generate_password(length)

    assert len(password) == length


# Test 6: Character categories
def test_character_categories():
    password = generate_password(20)

    assert any(c.islower() for c in password)
    assert any(c.isupper() for c in password)
    assert any(c.isdigit() for c in password)
    assert any(not c.isalnum() for c in password)


# Test 7: Invalid password length
def test_invalid_length():
    with pytest.raises(ValueError):
        generate_password(8)


# Test 8: Generator returns a string
def test_generator_type():
    password = generate_password(16)

    assert isinstance(password, str)
