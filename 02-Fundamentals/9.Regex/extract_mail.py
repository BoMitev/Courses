import re
text = input()
pattern = r"\s[A-Za-z0-9]+[A-Za-z0-9\.\-\_]*\@[A-Za-z]+[A-Za-z\-]*(\.[A-Za-z\-]+)+\b"
results = re.finditer(pattern, text)
for result in results:
    print(result.group(0))