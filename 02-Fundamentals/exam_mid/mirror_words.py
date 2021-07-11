text = input().replace("@", "#")
text = text.split("#")
match = 0
match_list = []

for word in text:
    for word2 in text:
        if len(word) > 2 and word.isalpha():
            if text.index(word) + 2 == text.index(word2):
                word_lower = word.lower()
                word2_lower = word2.lower()
                if word == word2[::-1]:
                    match_list.append(f"{word} <=> {word2}")
                    match += 1
                elif sum(map(ord, word_lower)) == sum(map(ord, word2_lower)) or word:
                    match += 1
print(f"{match} word pairs found!\n"
      f"The mirror words are:")
print(", ".join(match_list))