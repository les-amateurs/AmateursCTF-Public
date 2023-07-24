import os
import yaml
import datetime

start = datetime.datetime(2023, 7, 15, 3, 0, 0, tzinfo=datetime.timezone.utc) - datetime.timedelta(minutes=10)
waves = [start + datetime.timedelta(hours=12) * i for i in range(5)]

wave_zero = [
    "gcd-query-v1",
    "gcd-query-v2",
    "church",
    "compact-xors",
    "excuse-me",
    "lce-cream-generator",
    "minimalaestic",
    "non-quadratic-residues",
    "injection",
    "minceraft",
    "minisculer",
    "guessctf",
    "insanity-check",
    "discord-rules-sanity-check",
    "censorship-lite",
    "censorship",
    "q-warmup",
    "archived",
    "screenshot-guesser",
    "gitint-5e",
    "gitint-7d",
    "rntk",
    "frog-math",
    "permissions",
    "perfect-sandbox",
    "i-love-ffi",
    "csce221",
    "headache",
    "rusteze",
    "volcano",
    "emojicode-rev",
    "sanity",
    "waiting-an-eternity",
]
wave_one = [
    "owo-time-pad",
    "weak-primes",
    "you-get-extra-information-1",
    "you-get-extra-information-2",
    "lottery",
    "q-cheshires-game",
    "simple-heap-v1",
    "elfcrafting-v1",
    "jvm",
    "rusteze-2",
    "cps",
    "go-gopher",
    "lahoot",
    "legality",
]
wave_two = [
    "whiteboard",
    "flagchecker",
    "trick-question",
    "elfcrafting-v2",
    "zipper",
    "funny-factorials",
    "hex-converter",
    "gophers-hell",
]
wave_three = [
    "the-vault-2",
    "poly-fractions",
    "censorship-lite-plus-plus",
    "simple-os",
]
wave_four = [
    "latek",
    "painfullydeepflag",
    "uwuctf",
    "hex-converter-2",
    "latek",
    "rules-iceberg",
    "jsrev",
]
all_waves = [wave_zero, wave_one, wave_two, wave_three, wave_four]
active_ids = sum([all_waves[i] for i in range(5) if datetime.datetime.now(datetime.timezone.utc) > waves[i]], [])
print(f"Active ids: {active_ids}")

all_ids = []

unactive_ids = []
for root, dirs, files in os.walk("."):
    for file in files:
        if file == "challenge.yml" or file == "unchallenge.yml":
            path = os.path.join(root, file)
            folder_before = os.path.basename(os.path.dirname(path))
            print(f"Processing {path}...")
            with open(path, "r") as f:
                data = yaml.safe_load(f)

            # get the file id
            if "id" in data:
                id = data["id"]
            else:
                id = folder_before
            
            all_ids.append(id)

            if id in active_ids:
                pass
                # rename file to challenge.yml
                os.rename(path, os.path.join(root, "challenge.yml"))
            else:
                #  rename the file to unchallenge.yml
                os.rename(path, os.path.join(root, "unchallenge.yml"))
                unactive_ids.append(id)

all_ids = set(all_ids)
missing_ids = all_ids - set(sum(all_waves, []))
print(f"Missing ids: {missing_ids}")
print(f"Unactive ids: {unactive_ids}")
 
