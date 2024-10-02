from pathlib import Path
import toml
import challenges
import argparse

TEMPLATE = """
name = \"{}\"
author = \"{}\"
description = \"\"\"{}\"\"\"
flag.file = \"{}\"

provide = ["./dist.tar.xz"]

[containers.chal]
build = "./chal"
limits = {{ cpu = {}, mem = {} }}
ports = [5000]

[expose.chal]
target = 5000
tcp = {}
"""

parser = argparse.ArgumentParser("autogen.py")
parser.add_argument("--force", action=argparse.BooleanOptionalAction)
args = parser.parse_args()

PORT_BASE = 1337
defaults = {
    "name": "default",
    "author": "unvariant",
    "desc": "",
    "flag": Path("chal") / "flag.txt",
    "cpu": 1,
    "mem": 256,
    "tcp": 0
}

class Config:
    def __init__(self, name: str, author: str = None, desc: str = None, flag: Path = None, cpu: int = None, mem: int = None, tcp: int = None):
        self.name = name
        self.author = author or defaults["author"]
        self.desc = desc or defaults["desc"]
        self.flag = flag or defaults["flag"]
        self.cpu = cpu or defaults["cpu"]
        self.mem = mem or defaults["mem"]
        self.tcp = tcp or defaults["tcp"]

    def fmt(self):
        return TEMPLATE.format(self.name, self.author, self.desc, self.flag, self.cpu, self.mem, self.tcp)

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, desc: str):
        self._desc = desc.strip()

USED_PORTS = []
CONFIGS = {}

def get_unused_port():
    i = PORT_BASE
    while True:
        if i not in USED_PORTS:
            USED_PORTS.append(i)
            return i
        i += 1

def get_config_by_name(name: str):
    for _, config in CONFIGS.items():
        if config.name == name:
            return config
        
def gef_path_by_name(name: str):
    for path, _ in CONFIGS.items():
        if config.name == name:
            return path

for chal in challenges.query():
    config = chal / "challenge.toml"

    if config.exists() and not args.force:
        with open(config, "r") as fp:
            conf = toml.load(fp)
    else:
        conf = toml.loads(Config(chal.name).fmt())

    CONFIGS[config] = conf
    USED_PORTS.append(conf["expose"]["chal"]["tcp"])

for path, config in CONFIGS.items():
    if config["expose"]["chal"]["tcp"] < PORT_BASE:
        config["expose"]["chal"]["tcp"] = get_unused_port()

    desc = path.parent / "description.md"
    if desc.exists():
        with open(desc, "r") as fp:
            description = fp.read()
    else:
        description = "default description. contact an admin to write an actual description."
    config["description"] = description

for path, config in CONFIGS.items():
    with open(path, "w+") as fp:
        toml.dump(config, fp)