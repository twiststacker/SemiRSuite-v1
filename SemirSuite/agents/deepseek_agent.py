import subprocess

def query_deepseek(prompt: str) -> str:
    result = subprocess.run(
        ["ollama", "run", "deepseek-r1:32b"],
        input=prompt.encode(),
        capture_output=True
    )
    return result.stdout.decode()
