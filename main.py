from stats import get_word_count, get_letter_count, sort_dict, sort_on
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return(file_contents)

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    if len(sys.argv) == 2:
        text = str(get_book_text(sys.argv[1]))
        the_dict = get_letter_count(text)
        dict_list = sort_dict(the_dict)
        dict_list.sort(reverse=True, key=sort_on)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(get_word_count(sys.argv[1]))
        print("--------- Character Count -------")
        for char in dict_list:
            print(f"{char['char']}: {char['count']}")
        print("============= END ===============")

main()