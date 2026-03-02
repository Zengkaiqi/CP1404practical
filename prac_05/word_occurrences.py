"""
Word Occurrences
Estimate: 15 minutes
Actual:   16 minutes
"""
text = input("Enter text: ")
words = text.split()
word_to_count = {}
wide = max([len(word) for word in words])

for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

for key in word_to_count:
    print(f"{key:{wide}} = {word_to_count[key]}")