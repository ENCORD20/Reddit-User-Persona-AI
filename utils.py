import re

def extract_username(url):
    match = re.search(r'reddit\.com/user/([^/]+)', url)
    return match.group(1) if match else None
