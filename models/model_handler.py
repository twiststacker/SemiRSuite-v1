import os
import tomli


def load_config(filename="config.toml"):
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", filename)
    with open(config_path, "rb") as f:
        return tomli.load(f)


class ModelHandler:
    def __init__(self, model_name: str, env: str = "dev"):
        self.model_name = model_name
        self.env = env

        path_map = {
            "semirsuite_latest": f"models/model_weights/semirsuite_latest/config.{env}.toml",
            "deepseek_r1_32b": f"models/model_weights/deepseek_r1_32b/config.{env}.toml"
        }

        if model_name not in path_map:
            raise ValueError(f"Unknown model: {model_name}")

        self.config = load_config(path_map[model_name])
        self._validate_config()

        self.model_path = self.config["model"]["path"]
        self.agent_name = self.config["agent"]["name"]

    def _validate_config(self):
        required_sections = ["agent", "model"]
        required_keys = {
            "agent": ["name"],
            "model": ["path"]
        }

        for section in required_sections:
            if section not in self.config:
                raise ValueError(f"Missing config section: [{section}]")

            for key in required_keys[section]:
                if key not in self.config[section]:
                    raise ValueError(f"Missing key '{key}' in section [{section}]")

    def get_model_info(self):
        return {
            "name": self.agent_name,
            "path": self.model_path,
            "config": self.config
        }