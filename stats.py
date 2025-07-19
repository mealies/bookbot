def count_words(book_text):
    # words = book_text.split()
    # num_words = 0
    # for word in words:
    #     num_words += 1
    # return num_words
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    chars = {}
    book_text = book_text.lower()
    for char in book_text:
        chars[char] = chars.get(char, 0) + 1
    return chars
    # chars = {}
    # for c in text:
    #     lowered = c.lower()
    #     if lowered in chars:
    #         chars[lowered] += 1
    #     else:
    #         chars[lowered] = 1
    # return chars

def sort_on(items):
    return items["num"]



def sort_characters(chars):
    ## instead of doing a for loop, use a list comprehension
    # for key in chars.keys():
    #     new_dict = {}
    #     new_dict["char"] = key
    #     new_dict["num"] = chars[key]
    #     list_of_chars.append(new_dict)
    list_of_chars = [{"char": key, "num": chars[key]} for key in chars.keys() if key.isalpha()]
    list_of_chars.sort(reverse=True, key=sort_on)
    return list_of_chars
