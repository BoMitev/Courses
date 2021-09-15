import re
pattern = r"\bwww\.[A-Za-z0-9\-]+\.([a-z]+(\.[a-z]+)*)"
urls = []
while True:
    text = input()
    if text:
        results = re.finditer(pattern, text)
        for result in results:
            urls.append(result.group(0))
    else:
        break

print("\n".join(urls))