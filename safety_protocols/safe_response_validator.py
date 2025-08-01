def validate_output(output: str) -> bool:
    with open("safety_protocols/ban_list.txt", "r") as f:
        banned_words = [line.strip().lower() for line in f]

    if any(word in output.lower() for word in banned_words):
        raise ValueError("Unsafe content detected")
    return True