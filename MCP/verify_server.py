import sys
import os
from pathlib import Path

# Add root to path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

os.environ['TC_API_KEY'] = 'dummy_key'

try:
    from MCP.server import TOOL_REGISTRY
    print(f"Successfully imported TOOL_REGISTRY.")
except ImportError as e:
    print(f"Failed to import TOOL_REGISTRY: {e}")
    sys.exit(1)

print(f"Found {len(TOOL_REGISTRY)} tools.")

# Print first 10 tools
tools = list(TOOL_REGISTRY.keys())
for tool in tools[:10]:
    print(f"  - {tool}")

if len(tools) > 10:
    print(f"  ... and {len(tools) - 10} more.")

# Verify specific expected tools
expected = ['clients_list_all_clients', 'agents_list_all_agents']
for exp in expected:
    if exp in TOOL_REGISTRY:
        print(f"Verified tool present: {exp}")
    else:
        print(f"MISSING tool: {exp}")
