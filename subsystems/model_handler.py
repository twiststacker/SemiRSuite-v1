import toml

class ModelHandler:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.config = self._load_config()
        self.api_endpoint = self.config['model_settings']['api_endpoint']
        self.token = self.config['access']['token']

    def _load_config(self):
        path_map = {
            "semirsuite_latest": "models/model_weights/semirsuite_latest/config.toml",
            "deepseek_r1_32b": "models/model_weights/deepseek_r1_32b/config.toml"
        }
        with open(path_map[self.model_name], 'r') as f:
            return toml.load(f)