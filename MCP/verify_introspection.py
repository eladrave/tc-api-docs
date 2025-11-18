import sys
from pathlib import Path

# Add root to path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tc_api_sdk.resources import RESOURCE_CLASSES
from tc_api_sdk import models
import inspect

print(f"Found {len(RESOURCE_CLASSES)} resources.")

for resource_name, resource_cls in RESOURCE_CLASSES.items():
    print(f"Resource: {resource_name}")
    # Inspect methods
    for name, method in inspect.getmembers(resource_cls):
        if name.startswith('_') or name == 'metadata':
            continue
        print(f"  - Method: {name}")
        sig = inspect.signature(method)
        print(f"    Signature: {sig}")

# Check model lookup
print("\nModel Lookup Test:")
model_name = "ClientsClientObjectVersion2"
if hasattr(models, model_name):
    print(f"  Found model: {model_name}")
else:
    print(f"  Model {model_name} not found")
