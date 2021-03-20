import re

def clean(source):
    pattern         = r"[^+-.,<>\[\]]"
    substitution    = ""
    content         = re.sub(pattern, substitution, source)

    return content
