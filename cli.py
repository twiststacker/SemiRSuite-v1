import argparse
from semirsuite.agents.IdeaForge.ideaforge_agent import IdeaForgeAgent
from semirsuite.models.handler import ModelHandler
from semirsuite.safety_protocols.safe_response_validator import validate_response

def run_agent(agent_name: str, prompt: str):
    if agent_name.lower() == "ideaforge":
        agent = IdeaForgeAgent()
        ideas = agent.generate_ideas(prompt)
        print("\n🔮 Generated Ideas:")
        for i, idea in enumerate(ideas, 1):
            status = "✅ Safe" if validate_response(idea) else "❌ Unsafe"
            print(f"{i}. {idea} [{status}]")
    else:
        print(f"⚠️ Agent '{agent_name}' not recognized.")

def inspect_model(model_name: str):
    handler = ModelHandler(model_name)
    if handler.model:
        print(f"✅ Model '{model_name}' loaded successfully.")
    else:
        print(f"❌ Failed to load model '{model_name}'.")

def main():
    parser = argparse.ArgumentParser(description="SemirSuite CLI")
    subparsers = parser.add_subparsers(dest="command")

    # Run Agent
    agent_parser = subparsers.add_parser("run-agent", help="Run an AI agent")
    agent_parser.add_argument("--agent", required=True, help="Agent name (e.g., IdeaForge)")
    agent_parser.add_argument("--prompt", required=True, help="Prompt for the agent")

    # Inspect Model
    model_parser = subparsers.add_parser("inspect-model", help="Inspect a model")
    model_parser.add_argument("--model", required=True, help="Model name (e.g., semirsuite_latest)")

    args = parser.parse_args()

    if args.command == "run-agent":
        run_agent(args.agent, args.prompt)
    elif args.command == "inspect-model":
        inspect_model(args.model)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()