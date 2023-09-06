import random
import string

class URLShortener:
    def __init__(self):
        self.org_to_short = {}
        self.short_to_org = {}

    def shorten_url(self, org_url):
        if org_url in self.org_to_short:
            return self.org_to_short[org_url]
        short = self.generate_shortcode()
        self.org_to_short[org_url] = short
        self.short_to_org[short] = org_url
        return short

    def generate_shortcode(self):
        characters = string.ascii_letters + string.digits
        short_length = 6  
        short = ''.join(random.choice(characters) for _ in range(short_length))
        return short

    def expand_url(self, short):
        if short in self.short_to_org:
            return self.short_to_org[short]
        else:
            return "URL not found."

shortener = URLShortener()
org_url = input("Enter the url : ")
short_url = shortener.shorten_url(org_url)

print(f"Original URL: {org_url}")
print(f"Shortened URL: {short_url}")
expanded_url = shortener.expand_url(short_url)
print(f"Expanded URL: {expanded_url}")