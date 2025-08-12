from stats import get_word_count, get_letter_count

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)
    


def main():
    text = str(get_book_text("./books/frankenstein.txt"))
    print(get_letter_count(text))

main()