import json

from pathlib import Path

data = Path("shakespeare.json", errors="ignore").read_text()

groups = json.loads(data)

print(groups)