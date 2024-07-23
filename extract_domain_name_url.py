import re

def domain_name(url):
    match = re.search(r'https?://(?:www\.)?([A-Za-z_0-9.-]+)\.[A-Za-z]{2,}', url).group(1)
    print(type(match))

# To test if the function works.
domain_name("https://www.adrienleveille.com")
