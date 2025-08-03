import toml
from pathlib import Path

def check_toml(path: str = "configs/agent_registry.toml"):
    registry_path = Path(__file__).resolve().parent.parent / path
    try:
        toml.load(registry_path)
        print(f"✅ TOML syntax is valid: {registry_path}")
    except toml.TomlDecodeError as e:
        print(f"❌ TOML syntax error in {registry_path}")
        print(f"Line {e.lineno}, Column {e.colno}: {e.msg}")

if __name__ == "__main__":
    check_toml()