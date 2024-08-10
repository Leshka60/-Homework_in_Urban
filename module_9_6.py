def all_variants(text):
    for x in range(1, len(text) + 1):
        for y in range(len(text) - x + 1):
            yield text[y:y + x]


a = all_variants("abc")
for i in a:
    print(i)
    