from pathlib import Path

def query():
    challenges = []

    for file in Path(".").absolute().glob("*"):
        if not file.is_dir():
            continue

        if file.name.startswith("."):
            continue

        unchallenge = file / "unchallenge.toml"
        
        if unchallenge.exists():
            continue

        include = file / ".include"

        if not include.exists():
            continue

        challenges.append(file)
    
    return sorted(challenges)