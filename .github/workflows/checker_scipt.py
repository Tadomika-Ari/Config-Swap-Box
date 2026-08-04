import json
import re
import sys
from pathlib import Path

for path in Path("config").glob("*/info.json"):
    with path.open() as f:
        data = json.load(f)

        required = ["name", "author", "description", "path", "origin"]
        for key in required:
            if key not in data:
                print(f"Missing key: {key} in {path}")
                sys.exit(1)

        if re.fullmatch(r"[/.]+", str(data["name"])):
            print(f"Invalid name format in {path}")
            sys.exit(1)

        print(f"OK: {path}")

print("All JSON checks passed")