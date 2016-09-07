sentence = input("Enter a sentence: ").lower().split()
wordcount_dict = {}
min_length = 0
print("Text: ", end="")
for word in sentence:
    if word in wordcount_dict:
        wordcount_dict[word] += 1
    else:
        wordcount_dict[word] = 1
    if len(word) > min_length:
        min_length = len(word)
min_length = max(len(word) for word in wordcount_dict)
for word in sentence[:-1]:
    print(word, end=" ")
print(sentence[-1])
for word in sorted(wordcount_dict):
    print("{:{}} : {}".format(word, min_length, wordcount_dict[word]))
