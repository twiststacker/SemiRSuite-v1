import sys, os

# ✅ Ensure project root is in PYTHONPATH
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
print("🔍 PYTHONPATH:", sys.path)

# ✅ Optional: Load environment variables from .env
try:
    from dotenv import load_dotenv
    load_dotenv()
    print("✅ Environment variables loaded from .env")
except ImportError:
    print("⚠️ python-dotenv not installed. Skipping .env loading.")

# ✅ Import the agent
try:
    from agents.IdeaForge.ideaforge_agent import IdeaForgeAgent
except ModuleNotFoundError as e:
    print(f"❌ Import failed: {e}")
    sys.exit(1)

# ✅ Run the agent
def main():
    agent = IdeaForgeAgent()
    prompt = input("📝 Enter a prompt for IdeaForgeAgent: ")
    ideas = agent.generate_ideas(prompt)

    print("\n🔍 Prompt:")
    print(prompt)
    print("\n💡 Generated Ideas:")
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea}")

if __name__ == "__main__":
    main()