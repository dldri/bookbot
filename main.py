import string

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_chars_dict(text)
    char_list_dict = convert_to_list_of_dictionaries(char_dict)
    char_list_dict.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for dict in char_list_dict:
        print(f"The '{dict["letter"]}' character was found {dict["count"]} times")

    print("\n--- End of Report")

def convert_to_list_of_dictionaries(dict):
    char_list_dict = []
    for char in dict:
        if char in string.ascii_lowercase:
            char_list_dict.append({"letter": char, "count": dict[char]})
    return char_list_dict


def sort_on(dict):
    return dict["count"]

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
    
main()