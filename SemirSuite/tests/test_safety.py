import pytest
from safety_protocols.safe_response_validator import validate_response

@pytest.mark.parametrize("text", [
    "This video promotes violence.",
    "Contains explicit scenes.",
    "Spreading hate speech.",
])
def test_unsafe_responses(text):
    assert not validate_response(text), f"Text '{text}' should be flagged as unsafe."

@pytest.mark.parametrize("text", [
    "This tutorial explains AI concepts.",
    "Learn how to build scalable systems.",
    "Creative storytelling in tech projects.",
])
def test_safe_responses(text):
    assert validate_response(text), f"Text '{text}' should be considered safe."

def test_empty_response():
    assert validate_response(""), "Empty response should be considered safe."

def test_case_insensitivity():
    assert not validate_response("This contains HATE."), "Ban list should be case-insensitive."

def test_partial_word_should_not_trigger():
    assert validate_response("This is a hateful situation."), "Partial matches should not trigger unless explicitly listed."