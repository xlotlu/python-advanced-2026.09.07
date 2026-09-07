# Considering the following function:
#
# call it multiple times:
#
# first, send both a URL and custom headers
# then, send a URL containing /de/ (like https://www.dw.com/de/themen/s-9077)
# and no headers
# then, send a URL containing a reference to another language
# (like https://www.dw.com/fr/) and no headers

# What do you notice? How can you fix this behavior?


def http_get(url, headers={}):
    if "/en/" in url:
        headers["Accept-Language"] = "en"
    elif "/de/" in url:
        headers["Accept-Language"] = "de"
    print(f"Making HTTP request to {url} with headers {headers}")


http_get("example.com", {"Accept": "html"})
http_get("example.com/de/")
http_get("example.com/fr/")


def http_get_fixed(url, headers=None):
    if headers is None:
        headers = {}
    if "/en/" in url:
        headers["Accept-Language"] = "en"
    elif "/de/" in url:
        headers["Accept-Language"] = "de"
    print(f"[fixed] Making HTTP request to {url} with headers {headers}")


http_get_fixed("example.com", {"Accept": "html"})
http_get_fixed("example.com/de/")
http_get_fixed("example.com/fr/")
