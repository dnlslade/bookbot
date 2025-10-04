def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
        return contents



def word_count(filepath):
    contents = get_book_text(filepath)
    return len(contents.split())



def character_count(filepath):
    contents = get_book_text(filepath)

    char_counts = {}
    
    for char in contents.lower():
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts


def sort_on(items):
    return items["num"]

def sorted_chars(dict):

    char_list = list()

    for char in dict:
        char_count = {"char" : char , "num": dict[char]}
        char_list.append(char_count)
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list
