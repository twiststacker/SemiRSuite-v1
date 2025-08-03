import toml

def load_config(path: str) -> dict:
    with open(path, "r") as f:
        return toml.load(f)