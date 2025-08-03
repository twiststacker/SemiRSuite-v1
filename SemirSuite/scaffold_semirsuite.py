import os

BASE_DIR = os.path.join(os.getcwd(), "semirsuite")
AGENTS_DIR = os.path.join(BASE_DIR, "agents")
SUBSYSTEMS_DIR = os.path.join(BASE_DIR, "subsystems")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# Create directories
ensure_dir(BASE_DIR)
ensure_dir(AGENTS_DIR)
ensure_dir(SUBSYSTEMS_DIR)

# __init__.py
write_file(os.path.join(BASE_DIR, "__init__.py"), "from .orchestrator import orchestrate\n")

# orchestrator.py
write_file(os.path.join(BASE_DIR, "orchestrator.py"), '''\
from semirsuite.agents.deepseek_agent import query_deepseek
from semirsuite.registry import get_registered_agents

def orchestrate(task: str) -> str:
    agents = get_registered_agents()
    response = query_deepseek(task)
    return response
''')

# deepseek_agent.py
write_file(os.path.join(AGENTS_DIR, "deepseek_agent.py"), '''\
import subprocess

def query_deepseek(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "deepseek-r1:32b"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()
''')

print("✅ semirsuite package scaffolded successfully.")