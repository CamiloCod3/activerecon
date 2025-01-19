import yaml
import os

def load_config():
    """
    Loads the YAML configuration file and returns it as a dict.
    """
    # Hitta sökvägen till paketet
    base_path = os.path.dirname(__file__)
    # Relativ väg till config.yaml
    config_path = os.path.join(base_path, "config", "config.yaml")

    # Kontrollera om filen finns
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found at: {config_path}")

    # Läs in YAML-konfigurationen
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)