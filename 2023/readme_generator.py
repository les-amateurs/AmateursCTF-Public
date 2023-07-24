import os
import yaml


for root, dirs, files in os.walk("."):
    for file in files:
        if file == "challenge.yml":
            path = os.path.join(root, file)
            folder_before = os.path.basename(os.path.dirname(path))
            print(f"Processing {path}...")
            with open(path, "r") as f:
                data = yaml.safe_load(f)
            with open(os.path.join(root, "README.md"), "w") as f:
                # write name to README.md
                f.write(f"# {data['name']}\n\n")
                # write author to README.md
                f.write(f"## Author: {data['author']}\n\n")
                f.write(f"**Solves:** \n\n")
                f.write(f"**Points:** \n\n")
                # write horizontal rule to README.md
                f.write("---\n\n")
                # write description to README.md, and templating all instances of {{nc}} and {{link}}
                description = data['description']
                if 'expose' in data and 'main' in data['expose'] and 'tcp' in data['expose']['main'][0]:
                    description = description.replace("{{nc}}", f"nc amt.rs {data['expose']['main'][0]['tcp']}")
                if 'expose' in data and 'main' in data['expose'] and 'http' in data['expose']['main'][0]:
                    description = description.replace("{{link}}", f"[{data['expose']['main'][0]['http']}.amt.rs](http://{data['expose']['main'][0]['http']}.amt.rs)")
                f.write(f"{description}\n\n")
                # write horizontal rule to README.md
                f.write("---\n\n")
                # add attachments to README.md
                if 'provide' in data:
                    f.write("**Provided Files:**\n\n")
                    for file in data['provide']:
                        # reduce file path to just the file name
                        filename = f"{file}".split("/")[-1]
                        f.write(f"- [{filename}]({file})\n")