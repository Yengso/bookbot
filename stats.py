def get_word_count(filepath):
    counter = 0

    with open(filepath) as f:
        file_content = str(f.read())
        words = file_content.split()

        for word in words:
            counter += 1

    print(f"{counter} words found in the document")

def get_letter_count(text):
    char_counts = {}

    for letter in text:
        l = letter.lower()
        if l not in char_counts:
            char_counts[l] = 1
        else:
            char_counts[l] += 1
            
    return char_counts