def letterCount(text):
    count = 0
    text = text.lower()
    import string
    for char in text:
        if char in string.ascii_lowercase:
            count += 1
    return count

print(letterCount('my name is Sarah'))
