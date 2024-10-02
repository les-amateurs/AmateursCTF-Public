from pathlib import *
from subprocess import run
import shutil
import challenges

def rebuild(root: Path, parts: list[str]):
    for part in parts:
        root = root.joinpath(part)
    return root

cwd = Path(".").absolute()

for file in challenges.query():
    include = file / ".include"
    
    with open(include, "r") as f:
        includes = f.read().split("\n")
    
    includes = map(lambda s: s.strip(), includes)
    includes = filter(lambda s: len(s) > 0, includes)
    includes = map(lambda s: Path(s), includes)
    includes: list[Path] = list(includes)

    if not includes:
        continue

    dist = file / "_dist" / file.name
    if dist.exists():
        shutil.rmtree(dist)
    else:
        dist.mkdir(parents=True)
    dist_files: list[Path] = []

    for include in includes:
        real_parts = list(include.parts)
        dist_parts = []

        for i, part in enumerate(real_parts):
            if part.startswith("#"):
                real_parts[i] = part[1:]
            else:
                dist_parts.append(part)

        real_path = rebuild(file, real_parts)
        dist_path = rebuild(dist, dist_parts)

        if not real_path.exists():
            print(f"[-] warning: {real_path} does not exist")
            continue

        print(f"[+] {real_parts} => {dist_parts}")

        assert str(dist_path).startswith(str(file))
        dist_path.parent.mkdir(exist_ok=True)
        dist_path.symlink_to(real_path)
        dist_files.append(dist_path)

    fake = dist / "flag.txt"
    with open(fake, "w+") as f:
        f.write("amateursCTF{fake_flag}")

    package = file / "dist.tar.xz"
    dist_files.append(fake)
    for i, file in enumerate(dist_files):
        dist_files[i] = str(dist_files[i].relative_to(dist.parent))
    dist_files = " ".join(dist_files)

    run(f"tar cvfJh {package} {dist_files}", cwd=dist.parent, shell=True, check=True)
    shutil.rmtree(dist.parent)