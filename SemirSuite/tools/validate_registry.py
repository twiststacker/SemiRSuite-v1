import toml
import os
import sys

REGISTRY_PATH = os.path.join("semirsuite", "configs", "agent_registry.toml")

REQUIRED_FIELDS = [
    "capabilities",
    "status",
    "version",
    "author",
    "runtime",
    "dependencies",
    "description",
    "tags"
]

def load_registry():
    try:
        return toml.load(REGISTRY_PATH)
    except Exception as e:
        print(f"❌ Failed to load registry: {e}")
        sys.exit(1)

def validate_agent(name, config):
    errors = []

    for field in REQUIRED_FIELDS:
        if field not in config:
            errors.append(f"Missing field '{field}'")

    if not isinstance(config.get("capabilities", []), list):
        errors.append("Field 'capabilities' must be a list")
    if not isinstance(config.get("dependencies", []), list):
        errors.append("Field 'dependencies' must be a list")
    if not isinstance(config.get("tags", []), list):
        errors.append("Field 'tags' must be a list")
    if not isinstance(config.get("status", ""), str):
        errors.append("Field 'status' must be a string")
    if not isinstance(config.get("version", ""), str):
        errors.append("Field 'version' must be a string")
    if not isinstance(config.get("author", ""), str):
        errors.append("Field 'author' must be a string")
    if not isinstance(config.get("runtime", ""), str):
        errors.append("Field 'runtime' must be a string")
    if not isinstance(config.get("description", ""), str):
        errors.append("Field 'description' must be a string")

    return errors

def main():
    print("🔍 Validating agent registry...\n")
    agents = load_registry()
    total_errors = 0

    for name, config in agents.items():
        print(f"🧠 Validating agent: {name}")
        errors = validate_agent(name, config)
        if errors:
            total_errors += len(errors)
            for err in errors:
                print(f"   ❌ {err}")
        else:
            print("   ✅ Passed")

    if total_errors == 0:
        print("\n🎉 All agents validated successfully!")
    else:
        print(f"\n⚠️ Validation completed with {total_errors} issue(s).")

if __name__ == "__main__":
    main()