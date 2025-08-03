import toml
import os

REGISTRY_PATH = os.path.join("semirsuite", "configs", "agent_registry.toml")
SUMMARY_PATH = os.path.join("semirsuite", "docs", "AGENT_SUMMARY.md")

def load_registry():
    return toml.load(REGISTRY_PATH)

def format_row(name, config):
    capabilities = ", ".join(config.get("capabilities", []))
    dependencies = ", ".join(config.get("dependencies", [])) or "—"
    tags = ", ".join(config.get("tags", [])) or "—"
    status = config.get("status", "unknown")
    version = config.get("version", "unknown")
    description = config.get("description", "—")
    return f"| {name} | {capabilities} | {dependencies} | {tags} | {status} | {version} | {description} |"

def generate_summary():
    agents = load_registry()
    lines = [
        "# 🧠 Agent Summary\n",
        "| Agent | Capabilities | Dependencies | Tags | Status | Version | Description |",
        "|-------|--------------|--------------|------|--------|---------|-------------|"
    ]
    for name, config in agents.items():
        lines.append(format_row(name, config))

    os.makedirs(os.path.dirname(SUMMARY_PATH), exist_ok=True)
    with open(SUMMARY_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"✅ Summary written to {SUMMARY_PATH}")

if __name__ == "__main__":
    generate_summary()