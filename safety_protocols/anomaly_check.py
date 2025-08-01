def validate(output: str) -> bool:
    banned_terms = ["execute", "system commands", "harmful", "malicious"]
    return not any(term in output.lower() for term in banned_terms)