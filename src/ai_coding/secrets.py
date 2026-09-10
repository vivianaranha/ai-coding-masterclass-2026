import re
PATTERNS=[r"(?i)api[_-]?key\s*[:=]\s*['\"][^'\"]+",r"(?i)password\s*[:=]\s*['\"][^'\"]+",r"AKIA[0-9A-Z]{16}"]
def findings(text): return [p for p in PATTERNS if re.search(p,text)]
