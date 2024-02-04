import re

def parse_includes(code: str):
    matches = re.findall(r"#include (.+)\n", code)

    for filename in set(matches):
        with open(filename, encoding="utf-8") as file:
            included_content = file.read()
            code = code.replace(f"#include {filename}\n", included_content)

    return "(" + code + ")"