title = input()
article = input()
div = []

while True:
    comments = input()
    if comments == "end of comments":
        break
    div.append(comments)

print(f"<h1>\n    {title}\n</h1>")
print(f"<article>\n    {article}\n</article>")
for c in div:
    print(f"<div>\n    {c}\n</div>")