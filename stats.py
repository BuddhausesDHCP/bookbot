def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    text = text.lower()
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_it(item):
    return item["num"]

def filter_dict(characters):
    result = []
    for char, num in characters.items():
        if char.isalpha():
            result.append({"char": char, "num": num})
    result.sort(reverse=True, key=sort_it)
    return result