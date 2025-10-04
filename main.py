import sys

from stats import word_count
from stats import character_count
from stats import sorted_chars



def main():
    #print(get_book_text("sys.argv"))
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")



    print("----------- Word Count ----------")

    num_words = word_count(f"{sys.argv[1]}")
    print(f"Found {num_words} total words")



    print("--------- Character Count -------")

    char_counts = character_count(f"{sys.argv[1]}")
    sorted_char_list = sorted_chars(char_counts)

    for dict in sorted_char_list:
        print(f"{dict["char"]}: {dict["num"]}")



    print("============= END ===============")

main()
