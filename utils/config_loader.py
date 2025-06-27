import yaml

def load_config(config_path: str = r"C:\Users\cprat\OneDrive\Desktop\Module(1-3)\PYTHON\Machine_Learning\GEN AI  COURSE\_AGENTIC_TRADING_BOT_\config\config.yaml") -> dict:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    return config