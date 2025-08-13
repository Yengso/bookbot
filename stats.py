def get_word_count(filepath):
    counter = 0

    with open(filepath) as f:
        file_content = str(f.read())
        words = file_content.split()

        for word in words:
            counter += 1

    return(f"Found {counter} total words")

def get_letter_count(text):
    char_counts = {}

    for letter in text:
        l = letter.lower()
        if l not in char_counts:
            char_counts[l] = 1
        else:
            char_counts[l] += 1
            
    return char_counts

def sort_dict(char):
    dictionary = []
    for key in char:
        if key.isalpha():
            dictionary.append({"char": key, "count": char[key]})
    return dictionary

def sort_on(items):
    return items["count"]