from pathlib import Path
import json

path = Path('favorite_number.json')
if path.exists():
    contents = path.read_text()
    favorite_number = json.loads(contents)
    print(f"I know what your favorite number is! It's {favorite_number}.")