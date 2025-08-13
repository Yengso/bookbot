from stats import get_word_count, get_letter_count, sort_dict, sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)
    


def main():

    text = str(get_book_text("./books/frankenstein.txt"))
    the_dict = get_letter_count(text)
    dict_list = sort_dict(the_dict)
    dict_list.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(get_word_count("./books/frankenstein.txt"))
    print("--------- Character Count -------")
    for char in dict_list:
        print(f"{char['char']}: {char['count']}")
    print(f"============= END ===============")

main()