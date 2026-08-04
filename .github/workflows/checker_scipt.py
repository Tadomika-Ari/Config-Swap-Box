import json
import re
import sys
from pathlib import Path

required_keys = ["name", "author", "description", "path", "origin"]
required_files = ["settings.toml", "info.json", "preview.png", "wallpaper.png"]


def validate_config(config_dir: Path) -> bool:
    info_path = config_dir / "info.json"
    if not info_path.is_file():
        print(f"Missing file: {info_path}")
        return False

    for filename in required_files:
        file_path = config_dir / filename
        if not file_path.is_file():
            print(f"Missing file: {file_path}")
            return False

    try:
        with info_path.open() as file_handle:
            data = json.load(file_handle)
    except json.JSONDecodeError as error:
        print(f"Invalid JSON in {info_path}: {error}")
        return False

    for key in required_keys:
        if key not in data:
            print(f"Missing key: {key} in {info_path}")
            return False

    if not re.fullmatch(r"[A-Za-z0-9_-]+", str(data["name"])):
        print(f"Invalid name format in {info_path}")
        return False

    expected_path = config_dir.as_posix()
    if str(data["path"]) != expected_path:
        print(f"Invalid path value in {info_path}: expected {expected_path}, got {data['path']}")
        return False

    print(f"OK: {config_dir}")
    return True


config_root = Path("config")
config_dirs = [path for path in config_root.iterdir() if path.is_dir()]

if not config_dirs:
    print("No config directories found")
    sys.exit(1)

for config_dir in config_dirs:
    if not validate_config(config_dir):
        sys.exit(1)

print("All JSON checks passed")