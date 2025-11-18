import sys
from pathlib import Path
import inspect

# Add root to path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tc_api_sdk.resources import RESOURCE_CLASSES

total_methods = 0
for name, cls in RESOURCE_CLASSES.items():
    methods = [m for n, m in inspect.getmembers(cls) if not n.startswith('_') and n != 'metadata']
    total_methods += len(methods)

print(f"Total SDK methods: {total_methods}")
