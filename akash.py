import pyshorteners

# Initialize the shortener
shortener = pyshorteners.Shortener()

# Shorten a URL
short_url = shortener.tinyurl.short('https://infyspringboard.onwingspan.com/web/en/login?ref=%2Fpage%2Fhome')

print("Shortened URL:", short_url)
