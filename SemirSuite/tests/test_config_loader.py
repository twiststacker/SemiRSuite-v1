from subsystems.config_loader import load_config

def test_load_config():
    config = load_config("configs/config.toml")
    assert "framework" in config