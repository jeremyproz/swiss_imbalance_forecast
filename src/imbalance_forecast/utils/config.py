from pathlib import Path
import yaml


def load_config(path: str | Path) -> dict:
    """Load a YAML configuration file."""
    path = Path(path)

    with path.open("r") as f:
        config = yaml.safe_load(f)

    return config