import os
import pytest

@pytest.mark.parametrize("key_name", [
    "SEMIRSUITELATEST_API_KEY",
    "DEEPSEEK_R1_32B_API_KEY",
])
def test_env_key_presence(key_name):
    value = os.getenv(key_name)
    assert value is not None, f"{key_name} is missing."
    assert value.strip() != "", f"{key_name} is set but empty."